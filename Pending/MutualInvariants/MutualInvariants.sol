// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract MutualInvariants {
    uint256[] public evens;
    uint256[] public odds;
    uint256 public nextIndexEven;
    uint256 public nextIndexOdd;

    constructor () {
        evens.push(0);
        odds.push(1);
        nextIndexEven = 42;
    }

    function addNew() public {
        uint even = evens[nextIndexEven % evens.length];
        nextIndexEven = uint256(keccak256(abi.encode(nextIndexEven)));
        uint odd = odds[nextIndexOdd % odds.length];
        nextIndexOdd = uint256(keccak256(abi.encode(nextIndexOdd)));
        evens.push(odd + 1);
        odds.push(even + 1);
    }
}
