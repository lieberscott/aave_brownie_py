from brownie import network, config, accounts

# FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local", "mainnet-fork"]

def get_account(index=None, id=None):
  if index:
    return accounts[index]
  if id:
    return accounts.load(id)
  if (
    network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
    # or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
  ):
    return accounts[0]
  if network.show_active() in config["networks"]:
    return accounts.add(config["wallets"]["from_key"])
  return None