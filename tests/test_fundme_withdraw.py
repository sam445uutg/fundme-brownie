import pytest
from brownie import Fundme, network,exceptions, accounts
from scripts.deploy import fundme_deploy
from scripts.help_full import getaccount, LOCAL_DEPLOY_CONTRACT
import pytest

def test_fundme_withdraw():
    account= getaccount()
    fundme_add= fundme_deploy()
    enterance = fundme_add.enetrance()
    tx1 = fundme_add.fundme({"from":account, "value":enterance})
    tx1.wait(1)
    assert fundme_add.addresstouint256(account.address) == enterance
    # tx2 = fundme_add.withdraw({"from":account})
    # tx2.wait(1)
    # assert fundme_add.addresstouint256(account.address) == 0

def test_only_withdraw_owner():
    if network.show_active()  not in  LOCAL_DEPLOY_CONTRACT:
        pytest.skip("only for loacal")
    fundme = fundme_deploy()
    bad_actor= accounts.add()
    # with pytest.raises(exceptions.VirtualMachineError):
    fundme.withdraw({"from":bad_actor})