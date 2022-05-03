methods {
    // does not depend on msg, tx, block
    balanceOf(address) returns (uint256) envfree;
}


rule transferIncreasesRecipientBalance {
    env e;
    uint amount;

    address recipient;
    address sender;
    require sender == e.msg.sender;

    address any_other;
    require any_other != sender;
    require any_other != recipient;

    mathint balance_recipient_before = balanceOf(recipient);
    mathint balance_sender_before = balanceOf(sender);
    mathint balance_any_other_before = balanceOf(any_other);

    transfer(e, recipient, amount);

    mathint balance_recipient_after = balanceOf(recipient);
    mathint balance_sender_after = balanceOf(sender);
    mathint balance_any_other_after = balanceOf(any_other);

    bool same = recipient == sender;

    if (same) {
           assert balance_recipient_after == balance_recipient_before,
           "transfer from same address shouldn't change recipient's balance";
           assert balance_sender_after == balance_sender_before,
           "transfer from same address shouldn't change sender's balance";
           assert balance_any_other_after == balance_any_other_before,
           "transfer from same address shouldn't change any other balance";
    } else {
           assert balance_recipient_after == balance_recipient_before + amount,
           "transfer should increase recipient's balance by amount";
           assert balance_sender_after == balance_sender_before - amount,
           "transfer should reduce sender's balance by amount";
           assert balance_any_other_after == balance_any_other_before,
           "transfer shouldn't change any other balance";
    }
}

rule revertTransfer {
    env e;
    uint amount;

    address recipient;
    address sender;
    require sender == e.msg.sender;

    mathint balance_recipient_before = balanceOf(recipient);
    mathint balance_sender_before = balanceOf(sender);

    /* transfer(e, recipient, amount); */
    transfer@withrevert(e, recipient, amount);
    bool reverted = lastReverted;

    mathint balance_recipient_after = balanceOf(recipient);
    mathint balance_sender_after = balanceOf(sender);

    assert reverted <=> (
           e.msg.value != 0 ||
           balance_sender_before < amount ||
           recipient == 0 ||
           (sender != recipient && balance_recipient_before + amount > max_uint256)
                         ),
        "revert cases";

}

rule nonRevertAssumptions {
    address receiver; address sender; uint amount; env e;
    require sender == e.msg.sender;
    uint balance_sender_before = balanceOf(sender);

    transfer(e, receiver, amount);

    assert receiver != 0;
    assert amount <= balance_sender_before;
}

rule nonRevertIncoherence {
    address receiver; address sender; uint amount; env e;
    require sender == e.msg.sender;
    uint balance_sender_before = balanceOf(sender);

    require amount > 100;
    require balance_sender_before < 10;

    transfer(e, receiver, amount);

    assert false;
}

rule balanceInvariantNoTransfer {
    address anyone;
    mathint balance_anyone_before = balanceOf(anyone);

    env e;
    method f; calldataarg args;
    require f.selector != transfer(address, uint256).selector;
    require f.selector != transferFrom(address, address, uint256).selector;
    f(e, args);

    mathint balance_anyone_after = balanceOf(anyone);

    assert balance_anyone_before == balance_anyone_after,
        "no balance changes except for transfer";
}
