"""Project-authored ordered data-path model of PS4 RVA 0xf224a0.

Purpose: explain the shared scalar getter reached by a saved Blackout binding.
Inputs: width-aware read/write callbacks and an explicitly opaque-call callback.
Output: old top register value; writes carry a separate tag/payload record.
See docs/native/scalar-append.md. New executable model awaits independent review.
This models the ordered data accesses, not the complete native ABI/stack frame.
"""


class NativeTrap(RuntimeError):
    """The modeled UD2 is reached only if the error callee returns."""


def run(read, write, opaque):
    """Propagate faults/nonreturns; preserve earlier writes and opaque effects.

    read(bits, address) and write(bits, address, value) may alias or raise.
    opaque(rva, edi, rbx) supplies post-call RBX when that value is needed.
    No callee behavior, register preservation, units or live globals are assumed.
    """
    mask = (1 << 64) - 1
    scalar = read(32, 0x1CF8458) & 0xFFFFFFFF
    rbx = scalar - (1 << 32) if scalar & 0x80000000 else scalar
    if read(32, 0x3BFF850) & 0xFFFFFFFF:
        rbx = opaque(0xAACA70, 0, rbx)
    old_top = read(64, 0x3BF7038) & mask
    limit = read(64, 0x3BF7028) & mask
    if old_top == limit:
        opaque(0x14F2DD0, 0xB413C4F5, rbx)
        raise NativeTrap("modeled UD2 after returning error callee")
    # The original checks equality only. Do not add a greater-than guard.
    write(64, 0x3BF7038, (old_top + 16) & mask)
    count = read(32, 0x3BFF84C)
    write(32, 0x3BFF84C, (count + 1) & 0xFFFFFFFF)
    write(32, (old_top + 24) & mask, 6)
    write(64, (old_top + 16) & mask, rbx & mask)
    return old_top
