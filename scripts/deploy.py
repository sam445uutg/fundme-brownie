
from brownie import Fundme , network, config, MockV3Aggregator, accounts
from scripts.help_full import getaccount, deploy_mock, LOCAL_DEPLOY_CONTRACT

def fundme_deploy():
    account = getaccount()
    if (network.show_active() not in LOCAL_DEPLOY_CONTRACT ):
        price_feed_add = config["Network"][network.show_active()][
            "eth_usd_price_feed"
            ]
    else:
        deploy_mock(account)
        price_feed_add = MockV3Aggregator[-1].address
    
   # print(price_feed_add)
    fundme_add = Fundme.deploy(price_feed_add,{"from":account},publish_source =config["Network"][network.show_active()]["Publish"])
    return fundme_add
def main():
    fundme_deploy()


