# scripts/mp_common/rat.gsc

Project-added notes. See the [code](../../src/scripts/mp_common/rat.gsc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `17df319a53bb4510e195e716b45681bee0f5148f9d53b3ad55fb36f5fc496f55`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/3474fbec0cbfdd43.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `scripts/mp_common/rat.gsc::function_50634409` (original lines 11-50, 40-50): MP RAT automation command that force-adds a test bot: resolves a player via util::gethostplayerforbots() (a different util from unit 13 gethostplayer), sets five bot dvars to 0 (bot_allowmovement, bot_pressattackbtn, bot_pressmeleebtn, scr_botsallowkillstreaks, bot_allowgrenades), computes team with bot::devgui_relative_team(player, marker x53) and runs level bot::add_bot(team). HMH-path limit: wholly dev-delimited file (one dev block lines 11-122); registration addratscriptcmd(x43, &function_50634409) at mp rat __init__ line 32; delivery only via native rat_scriptcommand -> rat_shared::codecallback_ratscriptcommand -> rat.script_command_list lookup; the pinned recovered mp_common/gametypes/globallogic.gsc81 imports scripts\mp_common\rat. This establishes that source import link; actual original-build VM loading, dev inclusion, HMH configuration and native delivery remain unverified.

  unknowns: &#91;"Which VM in the original PS4 build actually loads/includes this dev-delimited RAT code remains unverified. The recovered source importer at mp_common/gametypes/globallogic.gsc81 is identified and must not be described as missing.", "Native rat_scriptcommand emitter in the original build", "Plaintext command name for x43", "gethostplayerforbots and devgui_relative_team x53 marker semantics"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/3474fbec0cbfdd43-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/3474fbec0cbfdd43.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00076` at JSON pointer ``; file SHA-256 `7a419a62c7d54671fbe0b6dee16eedbe6a28d81a883777b24ce1d63b05591c6e`.

- `scripts/mp_common/rat.gsc::__init__system__` (original lines 17-20): No standalone body contract is available in this selected summary. Available classification: autoexec_registration_inventory; native invocation/load order unverified.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/3474fbec0cbfdd43-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/3474fbec0cbfdd43.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/632`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `00ffb318bde94eac651a084a50379779cfe11635b7f5393853239408876c21ba`.

- `scripts/mp_common/gametypes/dev.gsc::getormakebot` (original lines 56-88): Dev bot-finder/creator helper: scans level.players for a player on the requested team with isbot() true and returns it; otherwise bot::add_bot(team); if defined, plays sound marker x617 on players and waits 1; returns the bot entity. HMH-path limit: the function body and all recorded callers are dev-delimited. Pointer store level.devongetormakebot=&getormakebot happens only inside the dev block of the NON-dev dev.gsc __init__ (51-53); dev system registration itself is dev-delimited (autoexec 35-38). Inbound edges: four in-file dev callers (updatehardpoints 191, addenemyheli 1755, addtestcarepackage 1845, force_grenade_throw 2832), mp rat rscaddenemy:66 dev::getormakebot(team), and two dev dvar-poll field-dispatch consumers (killstreak_hacking::killstreak_switch_team 232-234 gated on isdefined(level.devongetormakebot), weaponobjects::switch_team 3787-3789 same pattern). The observed pointer store and both field-dispatch consumers are developer-delimited. If a consumer is included and reached, its defined-pointer guard/fallback applies. Original-build inclusion, effective pointer writers/values, VM loading and invocation remain unknown; omitted consumer code does not execute a fallback.

  unknowns: &#91;"Whether dev-delimited dev.gsc content exists in the original PS4 script VMs for any VM that HMH loads (exact original-build evidence still needed)", "Recovered source importer is globallogic.gsc81 #using scripts/mp_common/rat, reached in the Warzone source closure through warzone.gsc30. Actual original VM loading/execution remains unproved.", "on_start_gametype / on_connect native dispatch timing", "bot::add_bot contract (m1 scope) and sound marker x617"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/3474fbec0cbfdd43-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/3474fbec0cbfdd43.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00338` at JSON pointer ``; file SHA-256 `474625b951fa3b88b32fa3ec8a7056643601efa164f08f040683a71e2c2d5f87`.

- `scripts/mp_common/rat.gsc::__init__` (original lines 26-34): No standalone body contract is available in this selected summary. Available classification: dev_delimited_candidate_runtime_inclusion_unverified.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/3474fbec0cbfdd43-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/3474fbec0cbfdd43.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/1001`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `98e68657ad410b5933754162779933d44a82958942bb3260bf671faba9280569`.

- `scripts/mp_common/rat.gsc::__init__system__` (original lines 17-20): No standalone body contract is available in this selected summary. Available classification: dev_delimited_candidate_runtime_inclusion_unverified.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/3474fbec0cbfdd43-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/3474fbec0cbfdd43.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/1000`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `e3d8df70a9a76b410dd6a36c153b6f811958cd190e8b7551d0e4172632c43d84`.

- `scripts/mp_common/rat.gsc::rscaddenemy` (original lines 11-88, 94-120, 56-88): MP RAT automation command adding and placing an enemy bot: dispatches level.rat.common.gethostplayer (unit 13 function via pointer stored at mp rat init line 29), team defaults #axis else util::getotherteam(host.pers&#91;team&#93;); calls dev::getormakebot(team) (unit 10; cross-file namespace call, mp rat imports dev at line 6); when undefined bot prints x5b, reports failure to native ratreportcommandresult and returns; else threads rat::testenemy(team) (94-109: waits pers team, notifies menuresponse with menu_team when level.teambased) and rat::deathcounter() (115-120: on death increments level.rat.deathcount and sets dvar rat_death_count), waits 2, sets bot origin from float(params.x,y,z), optional angles params.ax/ay/az via setplayerangles, then reports success. HMH-path limit: wholly dev-delimited file; registration addratscriptcmd(x38, &rscaddenemy) at line 31; delivery only via native rat_scriptcommand chain; recovered mp_common/gametypes/globallogic.gsc81 imports scripts\mp_common\rat. Actual original-build VM loading, dev inclusion and native command delivery remain unverified.

  unknowns: &#91;"Original PS4 VM loading and dev inclusion remain unverified. Recovered source explicitly imports mp rat from globallogic81, and mp rat imports dev at6; these source links do not establish actual build/VM loading.", "Native rat_scriptcommand emitter in the original build; whether any HMH/HMH-Research flow issues this command", "Plaintext command/arg names (x38, x5b, menu_team markers)", "menu menuresponse routing for bots (ui/menu scope outside script dump)", "outcome when gethostplayer pointer yields undefined host"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/3474fbec0cbfdd43-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/3474fbec0cbfdd43.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00339` at JSON pointer ``; file SHA-256 `027d3a4c838f0e67744efa3aa8034f19ea8274516c9ee072b9676396e3c180fa`.

- `scripts/mp_common/rat.gsc::__init__` (original lines 26-34): No standalone body contract is available in this selected summary. Available classification: registered_system_pre_or_post_initializer.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/3474fbec0cbfdd43-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/3474fbec0cbfdd43.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/631`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `de919bcb102244cf838331178c03f0ce671e285292e1b044ffefafe716927b5b`.
