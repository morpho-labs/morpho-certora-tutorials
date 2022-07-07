rule addOneSometimes() {
    env e; uint256 mask; uint8 role = 3;
    require (mask < 10000);
    uint256 newMask = addRoleMask(e, role, mask);
    assert (newMask == mask || newMask == mask + 8);
}