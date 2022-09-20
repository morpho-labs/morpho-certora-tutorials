methods {
    evens(uint) returns (uint256) envfree
    odds(uint) returns (uint256) envfree
    nextIndexEven() returns (uint256) envfree
    nextIndexOdd() returns (uint256) envfree
    addNew() envfree
    len() returns (uint256) envfree
}

invariant evensContainsEvenNumbers()
    evens(len() - 1) % 2 == 0

invariant evensPreservedAddNew(uint256 i)
    evens(i) % 2 == 0
