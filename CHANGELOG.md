# Changelog

## 1.0.7

- Require Ragnavik Gameplay 1.0.1 with Jotunn 2.30.2.
- Update OdinBanners to 1.1.14, OdinHorse to 1.7.3, and KillMeForMyPower to 2.5.0.

## 1.0.6

- Add Ragnavik Gameplay 1.0.0 for the shared personalized starter chest at the StartTemple.

## 1.0.5

- Update Ragnavik Compatibility to 1.0.7 so Afterdeath wisps can cross dungeon transitions and use existing portals during corpse recovery.

## 1.0.4

- Remove GhostBuild after isolated testing identified it as a major client frame-rate regression.
- Remove HearthBelow after isolated testing confirmed terrain rendering defects and additional frame-rate loss.

## 1.0.3

- Remove DedicatedServer 1.0.3 to restore normal simulation ownership and reduce performance issues.

## 1.0.2

- Update Ragnavik Compatibility to 1.0.6 for the current MagicPlugin and EpicMMO versions and custom creature progression.

## 1.0.1

- Update the package icon with a matching `SHARED PACK` label.

## 1.0.0

- Establish the shared dependency layer used by both Ragnavik clients and servers.
- Add DedicatedServer 1.0.3 for controlled testing of server-owned world simulation with the existing Epic Loot stack.
- Move synchronized gameplay configuration out of the side-specific packs.
- Keep Network and Server Bridge out of the client dependency graph.
