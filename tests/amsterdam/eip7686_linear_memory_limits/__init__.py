"""
Tests for EIP-7686: Linear EVM Memory Limits.

Parking note: tests elsewhere whose subject is the quadratic memory
cost, the pre-EIP 63/64-only call grant rule, or an exact-gas boundary
those rules produce are parked with
``pytest.mark.valid_before("EIP7686")``; grepping that marker
enumerates the worklist. Each park carries a ``TODO(EIP-7686)``
stating how to re-derive it: recompute budgets with
``fork.memory_expansion_gas_calculator()`` (linear from this EIP),
``fork.memory_grant_floor()`` (a frame needs one gas per byte of
memory it touches), and the call grant rule
``gas - max(gas // 64, memory_byte_size)``.
"""
