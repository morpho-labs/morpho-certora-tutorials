// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract MutualInvariants {
    uint256[] public evens;
    uint256[] public odds;
    uint256 public nextIndex;

    constructor () {
        evens.push(0);
        odds.push(1);
    }

    function addNew() public {
        uint even = evens[nextIndex % evens.length];
        uint odd = odds[nextIndex % odds.length];
        evens.push(odd + 1);
        odds.push(even + 1);
        nextIndex = uint256(keccak256(abi.encode(nextIndex)));
    }
}
