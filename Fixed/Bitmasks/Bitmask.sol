// SPDX-License-Identifier: MIT

pragma solidity 0.8.13;

contract Bitmask {
    function addRoleMask(uint8 role, uint256 mask) public pure returns(uint256) {
        return mask | (1 << role);
    }
}