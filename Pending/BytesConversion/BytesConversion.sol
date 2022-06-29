// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract BytesConversion {

    function isValidSignature(bytes4 sig) public pure returns(bool) {
        return sig == bytes4("ffff"); // something random here
    }

}