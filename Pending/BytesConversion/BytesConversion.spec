rule checkSomethingForSignature() {
    env e; method f;
    require (isValidSignature(e, f.selector));
    assert (true);
}