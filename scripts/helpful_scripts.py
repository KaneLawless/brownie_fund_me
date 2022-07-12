from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8  # 8 decimals because v3aggregator returns a value with 8 decimals
STARTING_PRICE = 200000000000  # 2000 with 8 decimals


FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f'the active network is {network.show_active()}')
    print("Deploying Mocks...")

    # Check if a Mock is already deployed
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {"from": get_account()})

    print("Mocks deployed")
