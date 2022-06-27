from threading import local
from brownie import accounts,network,config, MockV3Aggregator
from web3 import Web3
LOCAL_FORK_DELPOY =["mainnet-fork", "mainnet-fork-dev"]
LOCAL_DEPLOY_CONTRACT =['development', 'ganache-locall','ganach']
def getaccount():
    if(network.show_active() in LOCAL_DEPLOY_CONTRACT or network.show_active() in LOCAL_FORK_DELPOY):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from"])

def deploy_mock(ac):
    print("the active network is ", network.show_active())
    print("deploy mocks")
    MockV3Aggregator.deploy(18,Web3.toWei("200","ether")  ,{"from":ac})