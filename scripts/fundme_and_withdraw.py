from brownie import Fundme
from scripts.help_full import getaccount
from scripts.deploy import fundme_deploy
from  web3 import Web3
def fundme_and_withdraw():
    account = getaccount()
    # fundme_add= fundme_deploy()
    fundme_add = Fundme[-1]
    enterance = fundme_add.enetrance()
    print(enterance)
    # fundme_add.fundme({"from":account,"value":enterance })
    # fundme.fundme({"from":account, "value":enterance})
    tx=fundme_add.withdraw({"from":account})
    tx.wait(1)

def main():
    fundme_and_withdraw()
