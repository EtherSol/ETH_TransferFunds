from brownie import config,accounts,network

def get_account():
    return accounts.add(config["wallets"]["from_key"])