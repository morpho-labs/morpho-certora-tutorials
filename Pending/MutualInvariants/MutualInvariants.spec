methods {
    evens(uint) returns (uint256) envfree
    odds(uint) returns (uint256) envfree
    nextIndexEven() returns (uint256) envfree
    nextIndexOdd() returns (uint256) envfree
    addNew() envfree
}

invariant evensContainsEvenNumbers(uint256 i)
    evens(i) % 2 == 0
