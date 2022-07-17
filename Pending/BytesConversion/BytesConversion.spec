// FAILS because the selector is not of the right type
rule checkSomethingForSignature() {
    env e; method f;
    require (isValidSignature(e, f.selector));
    assert (true);
}