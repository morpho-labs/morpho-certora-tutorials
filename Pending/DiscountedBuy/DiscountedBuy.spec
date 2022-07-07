methods {
    objectBought(address) returns (uint) envfree
    basePrice() returns (uint256) envfree
}

definition oneEth() returns uint256 =
    1000000000000000000;

invariant basePriceIsOne()
    basePrice() == oneEth()

rule successiveBuysAreDiscounted() {
    requireInvariant basePriceIsOne();
    env e1; env e2;
    require (e1.msg.sender == e2.msg.sender);

    require (basePrice() == 1000000000000000000);

    uint paidPrice1 = e1.msg.value;
    buy(e1);
    uint paidPrice2 = e2.msg.value;
    buy(e2);

    assert(paidPrice2 < paidPrice1);
}

rule invariantTakenIntoAccount() {
    requireInvariant basePriceIsOne();
    env e;
    assert (basePrice() == 1000000000000000000);
}

rule alwaysPossibleToBuyBeforeOneThousand() {
    requireInvariant basePriceIsOne();
    env e;
    uint256 objectsBought = objectBought(e.msg.sender);
    uint256 priceCalculated = price(e);

    require (objectsBought < 1000);
    require (e.msg.value == priceCalculated);

    buy@withrevert(e);

    assert (!lastReverted);
}