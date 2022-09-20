// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract MutualInvariants {
    uint256[] public evens;
    uint256[] public odds;
    uint256 public nextIndexEven;
    uint256 public nextIndexOdd;

    constructor() {
        evens.push(0);
        odds.push(1);
        nextIndexEven = 42;
    }

    function addNew() public {
        uint256 even = evens[nextIndexEven % evens.length];
        nextIndexEven = (nextIndexEven * 2) % 42;
        uint256 odd = odds[nextIndexOdd % odds.length];
        nextIndexOdd = (nextIndexOdd * 3) % 87;
        evens.push(odd + 1);
        odds.push(even + 1);
    }

    function len() public view returns (uint256) {
        return evens.length;
    }
}
