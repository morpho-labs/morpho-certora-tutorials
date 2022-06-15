methods {
    objectBought(address) returns(uint) envfree
}

rule successiveBuysAreDiscounted() {
    env e;

    // require (e.msg.value > 0);
    uint paidPrice1 = e.msg.value;
    buy(e);
    uint paidPrice2 = e.msg.value;
    buy(e);

    assert(paidPrice2 < paidPrice1);
}

rule sanity() {
    env e;
    require(objectBought(e.msg.sender) == 2);
    buy(e);
    assert(false);
}

rule checksomething() {
    env e;
    wrong(e);
    assert(basePrice(e) == 2);
}