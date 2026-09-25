# Changelog

## 1.0.25

- Unselected professions earn 50% skill XP; selected professions earn 100%. Keep normal maximum levels and unchanged character XP. Update profession guidance.

## 1.0.24

- Require Compatibility 1.0.16 to activate farming XP on the current game.

## 1.0.23

- Update BepInExPack_Valheim from 5.4.2350 to 5.4.2351.
- Update AzuCraftyBoxes from 1.8.22 to 1.8.23.
- Update FirstPersonMode from 1.4.0 to 1.4.3.
- Update WardIsLove from 4.0.4 to 4.0.5.
- Update MagicPlugin from 2.2.1 to 2.2.2.
- Update CraftyCartsRemake from 3.2.1 to 3.2.3.
- Update OdinsFoodBarrels from 1.3.1 to 1.3.3.
- Update OdinsKingdom from 1.6.1 to 1.6.2.
- Update OdinsUndercroft from 1.3.5 to 1.3.6.
- Update PotionPlus from 4.3.4 to 4.3.6.
- Update Afterdeath from 1.0.10 to 1.0.11.
- Update ZenRaids from 1.2.2 to 1.2.3.
- Update Zen_ModLib from 1.14.9 to 1.14.15.
- Update PlantEverything from 1.21.2 to 1.21.3.
- Update Max_Dungeon_Rooms from 2.0.39 to 2.0.40.
- Update EpicLoot from 0.14.12 to 0.14.13.
- Allow Frost Fir cones in seed bags alongside the existing vanilla and custom seeds.

- Update Compatibility to 1.0.15 for per-harvest and planting XP, including bulk actions, and safe farming previews.
- Preserve profession levels when unlearning; cap crop growth and yield at 1.5x each and retain normal cultivator stamina costs.

- Disable LazyVikings beehive automation so honey remains in hives for manual collection.

## 1.0.22

- Update Ragnavik Compatibility to 1.0.14 to restore hover prompts and interactions.

## 1.0.21

- Update Ragnavik Compatibility to 1.0.13 so assigned-bed interaction remains compatible with current Valheim startup.
- Update EpicLoot to 0.14.12, OdinsFoodBarrels to 1.3.1, Venture Location Reset to 1.1.0, and TargetPortal to 1.2.7.
- Keep FirstPersonMode at its current Hexium release 1.4.0 and FineWoodPieces at Hexium's available 1.6.6.

## 1.0.20

- Update Ragnavik Compatibility to 1.0.12 so ItemDrawers preserves cooked food, magic reagents, upgrades, and other custom item data during automatic storage and pickup.

## 1.0.19

- Disable the ZenRaids light perimeter visualization and its persistent hum while retaining lit fire spawn protection.
- Move the Explorer pin toggle from Alt+E to Alt+L so ItemDrawers keeps its contextual Alt+E action.
- Move AzuAutoStore Store All from Period to Alt+S and Pause Auto Store to Alt+Shift+S so storage no longer changes the minimap zoom.
- Reduce WardIsLove ward audio from 0.35 to 0.1.

## 1.0.18

- Update Ragnavik Compatibility to 1.0.11 so Afterdeath spirits can use permitted doors, resurrect at their assigned bed, and restore recovered AzuEPI items to their original quick slots.

## 1.0.17

- Allow players to carry ores, metals, and other normally restricted items through TargetPortal portals.

## 1.0.16

- Update Ragnavik Gameplay to 1.0.4 with its dedicated package icon.

## 1.0.15

- Update Ragnavik Gameplay to 1.0.3 so the starter chest cannot be damaged, targeted, or dismantled and is restored if its world object disappears.
- Update Ragnavik Compatibility to 1.0.9 so Take All coverage remains active across Epic Loot and MagicPlugin updates.

## 1.0.14

- Update WardIsLove to 4.0.4, Warfare to 1.9.4, Zen ModLib to 1.14.9, ZenRaids to 1.2.2, and Resurrection to 1.0.15.

## 1.0.13

- Correct StartupAccelerator to its available 1.0.3 release.

## 1.0.12

- Update Ragnavik Compatibility to 1.0.8 so Afterdeath uses a valid bed when it is closer to the death point than the nearest Skathi.

## 1.0.11

- Allow the shared Odin's Seed Bag to store supported seeds from Cooking Additions and Odin's Food Barrels.

## 1.0.10

- Update Ragnavik Gameplay to 1.0.2 to restore starter chest interaction and support the current Valheim APIs.

## 1.0.9

- Add Valheim Performance Profiler 0.1.0 for shared client and server diagnostics.


## 1.0.8

- Update Jotunn to 2.30.2 and EpicLoot to 0.14.11.
## 1.0.7

- Require Ragnavik Gameplay 1.0.1.
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
