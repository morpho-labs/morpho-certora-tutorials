// SPDX-License-Identifier: MIT
// Taken from https://github.com/clesaege/HackSmartContract

pragma solidity ^0.8.0;

// You can buy some object.
// Further purchases are discounted.
// You need to pay basePrice / (1 + objectBought), where objectBought is the number of object you previously bought.
contract DiscountedBuy {
    uint256 public basePrice = 1 ether;
    mapping(address => uint256) public objectBought;

    /// @dev Buy an object.
    function buy() public payable {
        require(msg.value * (1 + objectBought[msg.sender]) == basePrice);
        objectBought[msg.sender] += 1;
    }

    /** @dev Return the price you'll need to pay.
     *  @return price The amount you need to pay in wei.
     */
    function price() public view returns (uint256) {
        return basePrice / (1 + objectBought[msg.sender]);
    }
}