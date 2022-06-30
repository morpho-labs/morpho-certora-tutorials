methods {
    objectBought(address) returns (uint) envfree
    basePrice() returns (uint256) envfree
}

invariant basePriceIsOne()
    basePrice() == 1000000000000000000

rule successiveBuysAreDiscounted() { // fails
    env e1; env e2;
    require (e1.msg.sender == e2.msg.sender);

    require (basePrice() == 1000000000000000000);

    uint paidPrice1 = e1.msg.value;
    buy(e1);
    uint paidPrice2 = e2.msg.value;
    buy(e2);

    assert(paidPrice2 < paidPrice1);
}

rule invariantTakenIntoAccount() { // also fails
    env e;
    assert (basePrice() == 1000000000000000000);
}