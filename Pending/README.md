Things to fix (search for the FAILS keyword to see the examples):

- Bank
  - foralls make verification fail, even when used in a stronger require
  - foralls make verification fail, even when used in a stronger preserved block
  - ghost variables make verification fail, even though it is passing when replaced by a function with no argument
- DollarSign
  - not accepted as part of the syntax, even though they can be used for variables in solidity
- BytesConversion
  - no conversion between bytes32 and uint256, not practical for functions expecting a selector as a bytes32
