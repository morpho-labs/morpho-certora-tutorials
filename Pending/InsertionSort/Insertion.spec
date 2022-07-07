methods {
    insert(uint) envfree;
    array(uint) returns (uint) envfree;
    length() returns (uint) envfree;
    sorted() returns (bool) envfree;
}

function sortedAt(uint i) returns bool {
    return (i + 1 < length() => array(i) <= array(i+1));
}

invariant sortedEverywhere(uint256 i)
    sortedAt(i)
{ preserved { requireInvariant sortedEverywhere(to_uint256(i-1)); } }