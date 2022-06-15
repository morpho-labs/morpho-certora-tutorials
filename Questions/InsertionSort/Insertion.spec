methods {
    insert(uint) envfree;
    array(uint) returns (uint) envfree;
    length() returns (uint) envfree;
    sorted() returns (bool) envfree;
}

// function arraySorted() returns(bool) {
//     return (forall uint i.  i + 1 < array.length => array[i] < array[i+1]);
// }

function arrayS(uint i) returns bool {
    return (i + 1 < length() => array(i) < array(i+1));
}

invariant alwaysSorted(uint256 i)
    arrayS(i)
    // forall uint i. i + 1 < to_uint256(length()) => array(i) < array(i+1)

invariant isSorted()
    sorted()