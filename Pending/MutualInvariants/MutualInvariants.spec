methods {
    evens(uint) returns (uint256) envfree
    odds(uint) returns (uint256) envfree
    nextIndex() returns (uint256) envfree
    addNew() envfree
}

invariant evensContainsEvenNumbers(uint256 i)
    evens(i) % 2 == 0

invariant oddsContainsOddNumbers(uint256 i)
    odds(i) % 2 == 1
