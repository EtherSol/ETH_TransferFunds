from brownie import transaction,accounts,config,network
from scripts.helpful_scripts import get_account
from web3 import Web3

# def ganache():
#     sender = accounts[0]
#     rec = accounts[1]

#     print(sender)
#     print(rec)
#     transfer = transaction.deploy({"from":sender})
#     print(transfer.contract_balance())
#     contract_transfer = int(input("How much money you want to send?: "))
#     transfer.mint(sender,contract_transfer)
#     print(transfer.contract_balance())
#     print(sender.balance())
#     print(f"Current balance from contract is: {transfer.balances(sender)}")
#     print(f"Current balance from receiver is: {transfer.balances(rec)}")


#     transfer.sent(rec,contract_transfer,{"from":sender})
#     print(f"Processing transaction transfer of: {contract_transfer}...")
#     print(f"Current balance from receiver is: {transfer.balances(rec)}")
#     exit(0)


def deploy_transfer():
    account = get_account()
    account1 = "0x493f521f0362362F867f3Af936e02e776327bC7b"
    transfer = transaction.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from":account},)
    
    balance = transfer.getPrice()
    eth_amount = Web3.fromWei(balance,'ether')
    

    # print(f"{balance} Wei or {eth_amount} Ether")
    balance_of_contract = transfer.mint(account,balance)
    balance_of_contract.wait(1)
    send = transfer.transfer_eth(account1,balance,"sent")
    send.wait(1)

    # deposit = transfer.deposit(account,balance)
    # deposit.wait(1)
    # transfer.contract_balance()

    # trans = transfer.transfer_eth(account1,20000000000000000)
    # trans.wait(1)
    exit(0)
    

def main():
    deploy_transfer()

main()