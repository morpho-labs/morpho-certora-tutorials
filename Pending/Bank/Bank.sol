// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {

  bool public initialized;

  constructor() { initialized = true;}

  mapping(address => uint256) private funds;
  uint256 private totalFunds;

  function deposit(uint256 amount) public payable {
    require(msg.sender != address(0));

    funds[msg.sender] += amount;
    totalFunds += amount;
  }

  function transfer(address to, uint256 amount) public {
    require(to != address(0));

    funds[msg.sender] -= amount;
    funds[to] += amount;
  }

  function withdraw() public returns (bool success) {
    uint256 amount = getFunds(msg.sender);
    funds[msg.sender] = 0;
    success = payable(msg.sender).send(amount);
    require(success);
    totalFunds -= amount;
  }

  function getFunds(address account) public view returns (uint256) {
    return funds[account];
  }

  function getTotalFunds() public view returns (uint256) {
    return totalFunds;
  }
}
