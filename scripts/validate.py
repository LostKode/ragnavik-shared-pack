#!/usr/bin/env python3
"""Validate package metadata, policy generation, contents, and reproducibility."""

from __future__ import annotations

import json
import re
import struct
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

from build_package import build, package_files

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SHARED_CONFIGS = {
    "config/blacks7ar.LazyVikings.cfg",
    "config/Azumatt.AzuAutoStore.cfg",
    "config/Azumatt.WardIsLove.cfg",
    "config/ZenDragon.ZenRaids.cfg",
    "config/blacks7ar.Explorer.cfg",
    "config/Azumatt.MaxPlayerCount.cfg",
    "config/Azumatt.SleepSkip.cfg",
    "config/Azumatt_and_ValheimPlusDevs.PerfectPlacement.cfg",
    "config/blacks7ar.LootParticlePlus.cfg",
    "config/gravebear.odinsfoodbarrels.cfg",
    "config/neobotics.valheim_mod.seidrchest.cfg",
    "config/org.bepinex.plugins.farming.cfg",
    "config/org.bepinex.plugins.passivepowers.cfg",
    "config/org.bepinex.plugins.professions.cfg",
    "config/org.bepinex.plugins.targetportal.cfg",
    "config/randyknapp.mods.epicloot.cfg",
    "config/xyz.alcan.comfortcalc.cfg",
}

FORBIDDEN_PARTS = {"node_modules", "bin", "obj", "__pycache__", ".git"}


def fail(message: str) -> None:
    raise RuntimeError(message)


def main() -> int:
    try:
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        if manifest.get("name") != "Ragnavik_Shared":
            fail("manifest name must be Ragnavik_Shared")
        if not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version_number", "")):
            fail("manifest version_number must be semantic version x.y.z")
        dependencies = manifest.get("dependencies", [])
        if not dependencies or len(dependencies) != len(set(dependencies)):
            fail("manifest dependencies must be nonempty and unique")
        dependency_pattern = re.compile(r"^[A-Za-z0-9_]+-[A-Za-z0-9_]+-\d+\.\d+\.\d+$")
        invalid_dependencies = [item for item in dependencies if not dependency_pattern.fullmatch(item)]
        if invalid_dependencies:
            fail(f"invalid dependency strings: {invalid_dependencies}")
        forbidden_dependencies = {
            "LostKode-Ragnavik_UI",
            "LostKode-Ragnavik_Server_Bridge",
            "Smoothbrain-Network",
        }
        dependency_keys = {item.rsplit("-", 1)[0] for item in dependencies}
        overlap = sorted(dependency_keys & forbidden_dependencies)
        if overlap:
            fail(f"side-specific dependencies are forbidden in Shared: {overlap}")
        required = [ROOT / name for name in ("README.md", "CHANGELOG.md", "icon.png")]
        if any(not path.is_file() for path in required):
            fail("README.md, CHANGELOG.md, and icon.png are required")
        png = (ROOT / "icon.png").read_bytes()
        shared_configs = {
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "config").rglob("*")
            if path.is_file()
        }
        if shared_configs != REQUIRED_SHARED_CONFIGS:
            fail(f"Shared config ownership mismatch: {sorted(shared_configs ^ REQUIRED_SHARED_CONFIGS)}")
        if png[:8] != b"\x89PNG\r\n\x1a\n" or struct.unpack(">II", png[16:24]) != (256, 256):
            fail("icon.png must be a 256 by 256 PNG")
        for path in ROOT.rglob("*"):
            relative = path.relative_to(ROOT)
            if set(relative.parts) & FORBIDDEN_PARTS and ".git" not in relative.parts:
                fail(f"forbidden generated path: {relative}")
            if path.is_file() and path.suffix.lower() == ".zip":
                fail(f"release ZIP must not be committed: {relative}")
        dlls = [path for path in package_files() if path.suffix.lower() == ".dll"]
        dll_names = [path.name.lower() for path in dlls]
        if len(dll_names) != len(set(dll_names)):
            fail("package contains duplicate DLL basenames")
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.zip"
            second = Path(directory) / "second.zip"
            first_hash = build(first)
            second_hash = build(second)
            if first_hash != second_hash or first.read_bytes() != second.read_bytes():
                fail("package build is not reproducible")
        print(f"validated {manifest['name']} {manifest['version_number']}")
        print(f"package files: {len(package_files())}")
        print(f"reproducible sha256: {first_hash}")
        return 0
    except (OSError, ValueError, KeyError, RuntimeError, json.JSONDecodeError) as error:
        print(f"validation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
