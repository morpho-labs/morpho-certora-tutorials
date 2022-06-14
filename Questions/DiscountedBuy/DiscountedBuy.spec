methods {
    nbOjbectBought(address) returns(uint) envfree
}

rule successiveBuysAreDiscounted() {
    env e;

    uint paidPrice1 = e.msg.value;
    buy(e);
    uint paidPrice2 = e.msg.value;
    buy(e);

    assert(paidPrice2 < paidPrice1);
}

rule sanity() {
    env e;
    require(nbOjbectBought(e.msg.sender) == 2);
    buy(e);
    assert(false);
}