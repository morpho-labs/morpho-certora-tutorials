## Questions

- How to make the `discountedBuy` go through ?
- Is it possible to write 1 ether easily ?
- How to take into account the invariant for rules (like requireInvariant) ?
- Why does `alwaysPossibleToBuyBeforeOneThousand` go through ?
- Why do we get the `objectsBought` = 1 counterexample

## Solution

- the tool does not assume that the value of `basePrice` is set, use an invariant for that
- use a definition, or a solidity function
- just use `requireInvariant` in the rule itself
- don't use the same environment, otherwise the price paid is required to be 0 (because the `price` function is non payable), such that the rule becomes trivial
