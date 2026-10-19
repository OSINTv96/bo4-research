# Source, credits and sharing audit

Checked October 18, 2026. **35 source/version references; 34 pinned revisions and one unresolved historical identity.**

This audit checked exact root notices and READMEs, plus saved complete path indexes where available. It did not review every source file or dependency. The audit was made before source imports. The current candidate includes 1,582 recovered files; original notice observations are unchanged. A declared tool license does not establish permission for recovered output.

## Results

| Observation | Records |
| --- | ---: |
| Ambiguous sharing notice | 1 |
| Conflicting license notices | 1 |
| Apache 2.0 and NOTICE | 1 |
| GPL v3 or MIT; dependency conditions | 1 |
| GPL v3 declared | 10 |
| MIT declared | 12 |
| Unresolved repository/revision | 1 |
| No explicit grant found in checked materials | 8 |

## Decisions that affect the first release

- **BO4 script and Lua dumps:** no explicit sharing grant was found in the checked `ate47/bo4-source` and `ate47/bo4-source-lua` materials. Original game-code redistribution permission remains unresolved.
- **Atian Tools:** the root notice offers GPL v3 or MIT, with separate dependency conditions. This does not license its recovered game output.
- **Cerberus:** the exact revision has both GPL v3 text and a restrictive EULA. The applicable terms are unresolved.
- **Other missing or ambiguous grants:** retain reference links and credits; do not treat an absent notice or informal wording as an unlimited license.
- **Original project files:** their license is not selected yet. No blanket license is applied to future imported material.

Public access and attribution alone do not supply a redistribution license. [GitHub explains the distinction](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository). The archived audit also recorded [Activision software terms](https://www.activision.com/legal/software-terms-of-use) as restricting copying/distribution and reverse engineering subject to stated exceptions. Those recorded terms are not established as the exact historical PS4 agreement, and this audit does not decide jurisdiction-specific exceptions.

## Exact source records

Each link below opens the pinned revision where available. Exact notice links, hashes, credit chains and limits are in [sources.json](sources.json). GPL v3 text alone does not settle an 'only' versus 'or later' version option for every file.

| ID | Source / version | Notice observation |
| --- | --- | --- |
| SRC-001 | [ahrimd0n/t8-mod @ 8a79fdd62c07](https://github.com/ahrimd0n/t8-mod/tree/8a79fdd62c07e579e491d00023a3e5a8e0dfd6a8) | GPL v3 declared |
| SRC-002 | [Ahrimdon/t8-mod @ unresolved](https://github.com/Ahrimdon/t8-mod) | Unresolved repository/revision |
| SRC-003 | [astrelsky/GhidraOrbis @ 2d6e3fac23ae](https://github.com/astrelsky/GhidraOrbis/tree/2d6e3fac23ae9830e941c32826e97100ed603311) | GPL v3 declared |
| SRC-004 | [ate47/atian-cod-tools @ 5d4d1ee6f767](https://github.com/ate47/atian-cod-tools/tree/5d4d1ee6f7676f4529b99fc89c2382dde8b856b7) | GPL v3 or MIT; dependency conditions |
| SRC-005 | [ate47/bo4-source @ f4b9a51f8b7f](https://github.com/ate47/bo4-source/tree/f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac) | No explicit grant found in checked materials |
| SRC-006 | [ate47/bo4-source-lua @ 1a46c72b710c](https://github.com/ate47/bo4-source-lua/tree/1a46c72b710c1820b63f72d22654f570286eee0b) | No explicit grant found in checked materials |
| SRC-007 | [ate47/CoDLuaDecompiler @ dd3e263ca508](https://github.com/ate47/CoDLuaDecompiler/tree/dd3e263ca50851bd1ad3401cb99dbb93bbe279b4) | MIT declared |
| SRC-008 | [ate47/HashIndex @ 40bdb5f7a34a](https://github.com/ate47/HashIndex/tree/40bdb5f7a34ad361d34db30beaee1346e5d7a22d) | MIT declared |
| SRC-009 | [ate47/hksc @ 16c58805b9b8](https://github.com/ate47/hksc/tree/16c58805b9b8fd9038a366601f290ba95ae51e9d) | MIT declared |
| SRC-010 | [ate47/shield-development @ 6b8f7ce6cfc8](https://github.com/ate47/shield-development/tree/6b8f7ce6cfc8734d60a2f014cb245ebe7e8fe8f4) | GPL v3 declared |
| SRC-011 | [ate47/t7-compiler-custom @ c7f83d69e1bc](https://github.com/ate47/t7-compiler-custom/tree/c7f83d69e1bcd9f46d65f2ef10b60e384ba1395f) | No explicit grant found in checked materials |
| SRC-012 | [ate47/t8-atian-menu @ f78bff6fac3e](https://github.com/ate47/t8-atian-menu/tree/f78bff6fac3e36a31e3d17503def2822f6dfdb9a) | MIT declared |
| SRC-013 | [bodnjenie14/shield-docs @ 5dc571257b16](https://github.com/bodnjenie14/shield-docs/tree/5dc571257b16e75ead25ce07a9a95b4824128e68) | No explicit grant found in checked materials |
| SRC-014 | [EthanC/Jekyll @ 7f5a771e83cc](https://github.com/EthanC/Jekyll/tree/7f5a771e83cc3cb697f7a5a4ffa0b81fcfc62314) | MIT declared |
| SRC-015 | [Ezz-lol/project-bo4 @ 95a051a369fd](https://github.com/Ezz-lol/project-bo4/tree/95a051a369fd948bd665067e14879c992cccad02) | GPL v3 declared |
| SRC-016 | [GoldHEN/ps4debug @ de38906c4b36](https://github.com/GoldHEN/ps4debug/tree/de38906c4b365e3006c91130a2299a8610af36cf) | No explicit grant found in checked materials |
| SRC-017 | [hosseinpourziyaie/demonware-companion @ d7f2a539ddd0](https://github.com/hosseinpourziyaie/demonware-companion/tree/d7f2a539ddd0039c924dee69cb949a728d7088c2) | No explicit grant found in checked materials |
| SRC-018 | [JariKCoding/CoDLuaDecompiler @ dd3e263ca508](https://github.com/JariKCoding/CoDLuaDecompiler/tree/dd3e263ca50851bd1ad3401cb99dbb93bbe279b4) | MIT declared |
| SRC-019 | [jordam/demonbugger @ 9888435fca4d](https://github.com/jordam/demonbugger/tree/9888435fca4d49e0e202d7c15aeb679803b77e49) | Ambiguous sharing notice |
| SRC-020 | [monocolotion/shield-development @ 6b8f7ce6cfc8](https://github.com/monocolotion/shield-development/tree/6b8f7ce6cfc8734d60a2f014cb245ebe7e8fe8f4) | GPL v3 declared |
| SRC-021 | [NationalSecurityAgency/ghidra @ 77f213795d97](https://github.com/NationalSecurityAgency/ghidra/tree/77f213795d97abaae7da8ac9097794acb7438c59) | Apache 2.0 and NOTICE |
| SRC-022 | [NotNierPea/shield-launcher @ 3e782a1eb436](https://github.com/NotNierPea/shield-launcher/tree/3e782a1eb4365e7d56dd3a34a74a5343a54103dd) | MIT declared |
| SRC-023 | [NotNierPea/T8-EnhancementMod @ 040ac1ab7a95](https://github.com/NotNierPea/T8-EnhancementMod/tree/040ac1ab7a95520d664796c7b984b1e036f6a2d6) | No explicit grant found in checked materials |
| SRC-024 | [project-bo4/shield-development @ 6b8f7ce6cfc8](https://github.com/project-bo4/shield-development/tree/6b8f7ce6cfc8734d60a2f014cb245ebe7e8fe8f4) | GPL v3 declared |
| SRC-025 | [Scobalula/Cerberus-Repo @ 4a3f352bd716](https://github.com/Scobalula/Cerberus-Repo/tree/4a3f352bd7162fdf02b3264b9de71de3ccadab4a) | Conflicting license notices |
| SRC-026 | [Scobalula/Greyhound @ 22c3d17f7428](https://github.com/Scobalula/Greyhound/tree/22c3d17f7428573042b56f43af0ed2585989bebd) | GPL v3 declared |
| SRC-027 | [Scroptss/shield-development @ 42b651bbfedd](https://github.com/Scroptss/shield-development/tree/42b651bbfedd22c0c0498ae7f15a0fc41562d042) | GPL v3 declared |
| SRC-028 | [shiversoftdev/t7-compiler @ 8b012bd08e5f](https://github.com/shiversoftdev/t7-compiler/tree/8b012bd08e5f2afcd145efd37281a3da93bc80c7) | No explicit grant found in checked materials |
| SRC-029 | [Snickers-Projects/shield-development @ 6b8f7ce6cfc8](https://github.com/Snickers-Projects/shield-development/tree/6b8f7ce6cfc8734d60a2f014cb245ebe7e8fe8f4) | GPL v3 declared |
| SRC-030 | [xensik/gsc-tool @ 05d212f5059f](https://github.com/xensik/gsc-tool/tree/05d212f5059f7e2b08d95be3e083eb1d6bb83ffc) | GPL v3 declared |
| SRC-031 | [fstirlitz/luaparse @ fa4ba476841b](https://github.com/fstirlitz/luaparse/tree/fa4ba476841b9ca4891848dfe96e42336f54f932) | MIT declared |
| SRC-032 | [morluto/rea @ 74cf9e1401fc](https://github.com/morluto/rea/tree/74cf9e1401fcd89482fe39c27cc898f5858e9b72) | MIT declared |
| SRC-033 | [ate47/hksc @ b1cee842d1df](https://github.com/ate47/hksc/tree/b1cee842d1df516320610d709218d992bdb74b72) | MIT declared |
| SRC-034 | [actions/checkout @ 3d3c42e5aac5](https://github.com/actions/checkout/tree/3d3c42e5aac5ba805825da76410c181273ba90b1) | MIT declared |
| SRC-035 | [actions/setup-python @ 5fda3b95a4ea](https://github.com/actions/setup-python/tree/5fda3b95a4ea91299a34e894583c3862153e4b97) | MIT declared |

See [credits](../CREDITS.md) for attribution and [license scope](../LICENSE-SCOPE.md) for the remaining publication decisions. No upstream author or publisher was contacted; this task checks recorded terms rather than obtaining new permission.
