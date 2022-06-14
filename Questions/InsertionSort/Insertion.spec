methods {
    insert(uint) envfree;
    array(uint) returns (uint) envfree;
    length() returns (uint) envfree;
}

// function sorted() {
//     assert(forall uint i.  i + 1 < array.length => array[i] < array[i+1]);
// }

invariant alwaysSorted()
    forall uint i.  i + 1 < length() => array(i) < array(i+1)