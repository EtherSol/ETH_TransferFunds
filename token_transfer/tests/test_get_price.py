from brownie import accounts, config, network, transaction
from web3 import Web3

# 0.01 
# 10000000000000000


def test_get_price():
    account = accounts[0]
    eth_price = transaction.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from":account},
    )
    assert eth_price.getPrice() >= Web3.toWei(0.01, "ether")
    assert eth_price.getPrice() < Web3.toWei(0.015, "ether")


