methods {
    evens(uint) returns (uint256) envfree
    odds(uint) returns (uint256) envfree
    nextIndexEven() returns (uint256) envfree
    nextIndexOdd() returns (uint256) envfree
    lengthEvens() returns (uint256) envfree
    lengthOdds() returns (uint256) envfree
    addNew() envfree
}

invariant evensIsEvenAt(uint256 i)
    evens(i) % 2 == 0

invariant evensIsEvenLast()
    evens(lengthEvens() - 1) % 2 == 0
    { preserved { requireInvariant oddsIsOddAt(nextIndexOdd()); } }

invariant oddsIsOddAt(uint256 i)
    odds(i) % 2 == 1

invariant oddsIsOddLast()
    odds(lengthOdds() - 1) % 2 == 1
    { preserved { requireInvariant evensIsEvenAt(nextIndexEven()); } }
