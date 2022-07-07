# How to reproduce

`make` does not go through.
Counter-example shows newMask = mask + 2, which should not be possible.

Solution: use the flag `-settings -useBitVectorTheory` to have sound computation on bitvectors.
