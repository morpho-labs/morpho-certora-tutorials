// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract InsertionSort {

    uint[] public array;

    function insert(uint e) public {
        uint i = array.length;
        array.push(e);
        while (i > 0 && e < array[i-1]) {
            array[i] = array[i-1];
            i--;
        }
        array[i] = e;
    }

    function length() public view returns(uint) {
        return array.length;
    }
}