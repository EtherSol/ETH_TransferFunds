from brownie import accounts, Transact

def deploy_transact():
    sen = accounts[0]
    rec = accounts[1]

    print("Sender: ")
    print(sen)
    print("Receiver: ")
    print(rec)
    print()

    transaction = Transact.deploy({'from': sen})
    transaction.giveMoney(sen, 20)
    print("-----Transact deployed-----")
    print()

    print("Sender: ")
    print(sen)
    print(transaction.balances(sen))
    print("Receiver: ")
    print(rec)
    print(transaction.balances(rec))
    print()

    print("-----Transaction sending-----")
    print()
    transaction.send(rec, 2, {'from': sen})
    print("-----Transaction completed-----")
    print()

    print("Sender: ")
    print(sen)
    print(transaction.balances(sen))
    print("Receiver: ")
    print(rec)
    print(transaction.balances(rec))
    print()

def main(): 
    deploy_transact()