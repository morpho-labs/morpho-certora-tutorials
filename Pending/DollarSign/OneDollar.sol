// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract OneDollar {
    uint public $one;
    function setToOne() public {
        $one = 1;
    }
}