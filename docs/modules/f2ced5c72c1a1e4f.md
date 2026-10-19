# hashed/4f16fa4b2242d6cf.lua

Project-added notes. See the [code](../../src/lua/hashed/4f16fa4b2242d6cf.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `7a4265ccd1b8fbb35ae2f189c170b06e0618fb14be5adab4f40c114887c926bb`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/f2ced5c72c1a1e4f.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua:041` (original lines 11-239): Builds the WZ back HUD children including team/player/ammo/inventory/compass/collapse/reinsertion/death notifications. Spawn selection hides deployable notifications; dead+not hacked+not spawn-select gates DeathCamContainer. KilledBy is locally always hidden; killer identity is hidden outside killcam, binds Attacker and updates emblem/name/rank views only for nonnil data. Overall caster-profile/spawn-select hides are separate predicates. The constructor wires child source contracts; it does not reconstruct every child, event producer or server state.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used.", "Source-ready close body exists outside frozen allowed companion range; exact locator is retained in new_dependencies. Other class clip bodies not frozen were not authored.", "Additional same-class reset/clip/close body ranges are available but outside the frozen author scope; exact locators are in unfrozen_same_class_body_locators and source-frontier.json. No body authoring or completion credit for them."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/f2ced5c72c1a1e4f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f2ced5c72c1a1e4f.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00334` at JSON pointer ``; file SHA-256 `d7b01efaff174a0a14ed475e48e08a33c016b6923722ae27d3d1cba3b746a1d0`.

- `hmh07-lua-follow2:140` (original lines 20-20, 20-20): Builds style and damage-contribution obituary children and forwards the parent model to both. State depends on style==0, style==4, and PC; style changes trigger validation. The exact state predicates do not establish effective squad-wipe settings.

  unknowns: &#91;"Original PS4/source exact-version and original Lua/VM binding remain unverified.", "Effective enum/mode/platform/settings and asset/model/storage data are unavailable.", "Native/LUI event/subscription/timer dispatch, cleanup guarantees and errors not shown in selected source remain open.", "Unavailable service/server code is not reconstructed or counted."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f2ced5c72c1a1e4f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f2ced5c72c1a1e4f.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00028` at JSON pointer `/units/139`; file SHA-256 `2f4ecc3aabb5072135e148ef5782181882bd3b940908913a20bf258d3754185e`; selected record SHA-256 `3db0db27c9aba96f03d73a4fc836e4f538aa29d7caf8571b4683f3cdc8d0d121`.

- `hmh07-lua-follow1:170` (original lines 11-239, 11-239, 11-239, 11-11, 21-23, 21-21, 28-30, 28-28, 35-37, 35-35, 44-46, 44-44, 50-58, 50-50, 64-72, 64-64, 76-84, 76-76, 88-96, 88-88, 100-108, 100-100, 112-120, 112-112, 124-132, 124-124, 136-144, 136-136, 148-156, 148-148, 160-168, 160-160, 172-180, 172-172, 184-192, 184-184, 196-204, 196-196, 208-216, 208-208, 220-228, 220-220, 11-239, 11-239, 44-46, 50-58, 12-12, 20-20, 27-27, 34-34, 45-45, 52-52, 230-230, 237-237, 53-53, 75-75, 233-233, 52-52, 63-63, 87-87, 99-99, 111-111, 123-123, 135-135, 147-147, 159-159, 171-171, 183-183, 195-195, 207-207, 219-219, 11-239): Builds player-name, expanded-callout and squad-killed children and binds each to the parent model. HiddenPreference checks kill-identity hiding; Visible uses the full recorded demo/caster/HUD/death/killcam/UI/training gate. Settings and visibility subscriptions only validate state. Existing close and optional PostLoadFunc precede InitObituaryCallout and return self. Kill-event generation and callback delivery remain separate gaps.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f2ced5c72c1a1e4f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f2ced5c72c1a1e4f.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00053` at JSON pointer ``; file SHA-256 `95b1966a3ebcd1a74e047061b8abba465113ecb187d4d140ab9e1cbd7f91647e`; selected record SHA-256 `a7d3c27b04960f5482f9bd2e3c3b71c4f5d9327212778a8daf1cf9d255e290fd`.
