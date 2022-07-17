// FAILS with a syntax error
rule easy() {
    env e;
    setToOne(e);
    assert ($one(e) == 1);
}