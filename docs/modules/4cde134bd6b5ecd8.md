# scripts/core_common/dialog_shared.csc

Project-added notes. See the [code](../../src/scripts/core_common/dialog_shared.csc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `49e4092e517304c80a9f2386fccf70d5c4761e34cdfbb5afabc16f534682b9aa`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/4cde134bd6b5ecd8.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-deps7:003` (original lines 187-187, 187-206, 227-227, 5-5, 194-194, 5-5, 227-227, 187-187, 187-206, 227-227, 5-5, 198-198, 5-5, 227-227, 227-249, 187-206, 187-206, 229-232, 234-239, 241-248, 227-249, 187-206, 187-206): Accept dialogbundle and dialogkey. If either is undefined, explicitly return undefined. Otherwise read dynamic field dialogbundle.(dialogkey) into dialogalias. If that result is undefined, use a bare return. Read voiceprefix only after a defined alias; if the prefix is defined, replace alias with voiceprefix+dialogalias. Return the resulting alias. A defined empty or false value is not rejected by a truthiness test. No external state is written; dynamic field and concatenation type semantics remain VM-dependent.

  unknowns: &#91;"actual dialog bundle/key/voiceprefix contents", "VM dynamic field access and concatenation for malformed types", "whether bare return and explicit undefined are bytecode-equivalent; preserved as distinct source forms"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/4cde134bd6b5ecd8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4cde134bd6b5ecd8.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00445` at JSON pointer `/units/2`; file SHA-256 `a7bb2e5aea8ad75c41ab65ff86c473160dd796a9f767c1cb89e03414cd2434a5`; selected record SHA-256 `0f7611ed4649e898d2315b0a98ec0a1a87421017703ed15ffd3410e958bb3908`.

- `hmh07-deps7:004` (original lines 187-187, 187-206, 167-167, 5-5, 196-196, 5-5, 167-167, 187-187, 187-206, 167-167, 5-5, 196-196, 5-5, 167-167, 167-181, 187-206, 187-206, 169-169, 171-177, 180-180, 169-169, 5-5, 5-5, 255-255, 180-180, 167-181, 187-206, 187-206): Accept chancekey. Synchronously call same-namespace mpdialog_value(chancekey) once and store dialogchance. Undefined or <=0 returns false. Otherwise >=100 returns true without randomint. For the remaining comparison path, return randomint(100)<dialogchance. This records a threshold comparison, not a measured probability or a verified distribution of the engine RNG. No clamping, numeric/type conversion or retries occur locally.

  unknowns: &#91;"mpdialog_value result and effective session/dialog data", "native randomint range/distribution and VM comparisons for malformed values", "actual invocation and RNG state"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/4cde134bd6b5ecd8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4cde134bd6b5ecd8.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00445` at JSON pointer `/units/3`; file SHA-256 `a7bb2e5aea8ad75c41ab65ff86c473160dd796a9f767c1cb89e03414cd2434a5`; selected record SHA-256 `523fedaa4895cf76af2baeec2a02ef406f8208b0fa95ae7ed2d508d3c7862180`.
