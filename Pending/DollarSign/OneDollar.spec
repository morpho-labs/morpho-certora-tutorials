rule easy() {
    env e;
    setToOne(e);
    assert ($one(e) == 1);
}