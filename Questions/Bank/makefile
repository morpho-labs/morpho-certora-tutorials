%:
	certoraRun Bank.sol --verify "Bank:TotalGreaterThanUser$*.spec" \
    --optimistic_loop \
    --msg "Bank${*}"\
    --send_only