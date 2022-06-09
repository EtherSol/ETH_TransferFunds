from brownie import accounts, transaction

def main():
    sender = accounts[0]
    rec = accounts[1]
    transfer = transaction.deploy({"from":sender})
    transfer.mint(sender,4)

    print(f"Current balance from minter is: {transfer.balances(sender)}")
    print(f"Current balance from receiver is: {transfer.balances(rec)}")

    money_transfer = int(input("How much money you want to send?: "))
    transfer.sent(rec,money_transfer,{"from":sender})
    print(f"Processing transaction transfer of: {money_transfer}...")
    print(f"Minter balance is {transfer.balances(sender)}")
    print(f"Current balance from receiver is: {transfer.balances(rec)}")
    
main()