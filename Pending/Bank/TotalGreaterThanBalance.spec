methods {
	getFunds(address) returns (uint256) envfree
	getTotalFunds() returns (uint256) envfree
	initialized() returns (bool) envfree
}

rule weakRequireDepositSender(uint256 amount) {
	env e; 
	
	uint256 userFundsBefore = getFunds(e.msg.sender);
	uint256 totalBefore = getTotalFunds();
    
    require totalBefore >= userFundsBefore; 

	deposit(e, amount);
	
	uint256 userFundsAfter = getFunds(e.msg.sender);
	uint256 totalAfter = getTotalFunds();
	
	assert ( totalAfter >=  userFundsAfter, "Total funds are less than a user's funds " );
}

rule strongRequireDepositSender(uint256 amount) {
	env e; 
	
	uint256 userFundsBefore = getFunds(e.msg.sender);
	uint256 totalBefore = getTotalFunds();
    
	require forall address a. getFunds(a) <= getTotalFunds();

	deposit(e, amount);
	
	uint256 userFundsAfter = getFunds(e.msg.sender);
	uint256 totalAfter = getTotalFunds();
	
	assert ( totalAfter >=  userFundsAfter, "Total funds are less than a user's funds " );
}


// invariant TotalGreaterThanSumOfTwoUsers(address user1, address user2)
// 	getTotalFunds() >= getFunds(user1) + getFunds(user2)

// invariant TotalGreaterThanUser(address user) // preserved with deposit but not withdraw, why ?
// 	getTotalFunds() >= getFunds(user)
// { preserved { requireInvariant TotalGreaterThanUser(user); } }

ghost ghostTotalFunds() returns uint256
{ init_state axiom  ghostTotalFunds() == 0; }

invariant totalFundsAtStart() 
	! initialized() => getTotalFunds() == 0

invariant UserFundsAtStart(address user) 
	! initialized() => getFunds(user) == 0

hook Sstore funds[KEY address user] uint256 fundsUser (uint256 oldFundsUser) STORAGE {
	havoc ghostTotalFunds assuming
		ghostTotalFunds@new() == ghostTotalFunds@old() + fundsUser - oldFundsUser;
}

invariant HookTotalGreaterThanUser(address user) // preserved with deposit but not withdraw, why ?
	ghostTotalFunds() >= getFunds(user)
{ preserved with (env e) { require forall address user. user != e.msg.sender => ghostTotalFunds() >= getFunds(user) + getFunds(e.msg.sender); } }

invariant HookTotalEqualTotal()
	ghostTotalFunds() == getTotalFunds()

