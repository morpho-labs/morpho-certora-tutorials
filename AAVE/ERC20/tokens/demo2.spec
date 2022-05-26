methods {
    balanceOf(address) returns (uint256) envfree;
    totalSupply()      returns (uint256) envfree;
}

// totalSupply is sum of balanceOf(user) for all users
ghost mathint sum_of_balances {
    init_state axiom sum_of_balances == 0;
}

hook Sstore balances[KEY address user] uint256 newValue (uint256 oldValue) STORAGE {
    sum_of_balances = sum_of_balances + newValue - oldValue;
}

invariant totalSupplyIsSumOfBalances()
    totalSupply() == sum_of_balances

rule transferPreserveSupply {
    address sender; address receiver;
    uint amount; env e;
    require (sender == e.msg.sender);
    address user;
    require (sender != receiver);
    require (user != receiver);
    require (user != sender);

    mathint balanceBeforeUser = to_mathint(balanceOf(user));
    mathint balanceBeforeSender = to_mathint(balanceOf(sender));
    mathint balanceBeforeReceiver = to_mathint(balanceOf(receiver));

    transfer(e, receiver, amount);

    mathint balanceAfterUser = to_mathint(balanceOf(user));
    mathint balanceAfterSender = to_mathint(balanceOf(sender));
    mathint balanceAfterReceiver = to_mathint(balanceOf(receiver));

    assert (balanceAfterUser + balanceAfterSender + balanceAfterReceiver ==
            balanceBeforeUser + balanceBeforeSender + balanceBeforeReceiver);
}

ghost address[] addresses {
    init_state axiom addresses.length == 0;
}

ghost mapping(address => bool) addressBook {
    init_state axiom forall address a. addressBook[a] = 0;
}

hook Sstore balances[KEY address user] uint256 newValue (uint256 oldValue) STORAGE {
    if (!addressBook[user]) {
        addresses.push(user);
        addressBook[user] = true;
    }
}

function sum(address[] addresses, mapping(address => bool) addressBook) returns (uint totalSum) {
    uint totalSum;
    for(uint i = 0; i < addresses.length; i++)
        totalSum += balances[addresses[i]];
    }

invariant totalSupplyIsSum()
    totalSupply() == sum(balances, addresses)



invariant userBalanceBounded(address user)
    balanceOf(user) <= totalSupply()
