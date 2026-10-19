# Shared scalar append wrapper

The new [executable model](../../src/native/scalar_append_model.py) describes the
ordered data path in the saved PS4 window at RVA `0xf224a0`. Names such as
`old_top`, `limit` and `scalar` are project labels. They are not recovered symbols.

The original ELF fingerprint is
`63d7dacdccc09772ffb366eeb3a82da33bf1bf6b261db2c02358befe40e118f2`.
The 96-byte window has 24 reachable instructions covering 92 bytes. The saved
Blackout laststand binding reaches this destination; actual circle invocation
was not captured. The initialized scalar is 50. Its live value and units remain
unknown. The current exact source-contract and review fingerprints are recorded
in the [model provenance](../../provenance/native-model.json).

The wrapper reads a signed 32-bit scalar, checks a guard, and may call an opaque
callee. It then reads the candidate top and limit. Unequal values select an
ordered top-pointer write, wrapping count increment, tag-6 write and 64-bit
payload write. The returned native register contains the old top; it is distinct
from the written payload. Equal values call an opaque error path; a returning
callee reaches UD2. A top beyond the limit still takes the unequal branch.

Callbacks expose each memory access in order so aliasing, faults and callee
changes remain observable. Exceptions propagate after any earlier writes.
Post-call RBX is supplied explicitly instead of assuming ABI preservation.
Stack-frame effects, flags and complete native calling conventions are outside
this data-path model. It is newly authored and awaits independent review; the
old bounded contract review does not approve this implementation.

The saved circle expression is grouped as
`scalesec / (float(function_60d95f53()) / 1000)` under the recorded decoder
stack interpretation. The printed recovered source omits the right-hand
division brackets. This is a known formatter limitation, not a reason to patch
game logic or claim source-to-VM equivalence.
