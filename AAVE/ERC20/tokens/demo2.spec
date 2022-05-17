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
    require sender == e.msg.sender;
    mathint supplyBefore = totalSupply();
    address u1; address u2;
    require forall address a1. forall address a2. balanceOf(a1) + balanceOf(a2) <= totalSupply();


    transfer(e, receiver, amount);

    mathint supplyAfter = totalSupply();
    mathint balanceAfterUser1 = balanceOf(u1);
    mathint balanceAfterUser2 = balanceOf(u2);

    assert(supplyBefore == supplyAfter);
    assert(balanceAfterUser1 + balanceAfterUser2 <= supplyAfter);
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
