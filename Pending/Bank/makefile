all:
	certoraRun Bank.sol --verify Bank:TotalGreaterThanBalance.spec \
    --settings -optimisticFallback=true \
    --msg "Bank" \
    --send_only