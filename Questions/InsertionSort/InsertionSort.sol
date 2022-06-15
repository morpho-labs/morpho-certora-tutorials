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

    function sorted() public view returns(bool) {
        if (array.length <= 1) return true;
        for(uint i; i < array.length - 1; i++) {
            if(array[i] > array[i+1]) return false;
        }
        return true;
    }
}