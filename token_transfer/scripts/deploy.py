from brownie import transaction,accounts
from scripts.helpful_scripts import get_account

def ganache():
    sender = accounts[0]
    rec = accounts[1]

    print(sender)
    print(rec)
    transfer = transaction.deploy({"from":sender})
    transfer.mint(sender,4 eth)

    print(f"Current balance from minter is: {transfer.balances(sender)}")
    print(f"Current balance from receiver is: {transfer.balances(rec)}")

    money_transfer = int(input("How much money you want to send?: "))
    transfer.sent(rec,money_transfer,{"from":sender})
    print(f"Processing transaction transfer of: {money_transfer}...")
    print(f"Minter balance is {transfer.balances(sender)}")
    print(f"Current balance from receiver is: {transfer.balances(rec)}")
    exit(0)





def deploy_transfer():
    account = get_account()
    transfer = transaction.deploy({"from":account})
    
    

    transfer.sent()
    # print(account.address)
    # print(transfer.address)

    print("Hello World")

    # print(price_feed_address)

    # print(get_account(),get_account().balance())

    # transfer = transaction.deploy({"from": get_account()})
    # print(transfer.balances(get_account()))

def main():
    ganache()

main()