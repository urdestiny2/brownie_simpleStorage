from brownie import accounts, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]
    # print(account)
    simple_storage = SimpleStorage.deploy(
        {"from": account}
    )  # this is a transaction and hence it changes the state of the blockchain thats why we need to provide it an account to use
    # print(simple_storage)
    stored_value = simple_storage.show()
    print(stored_value)
    updating_value = simple_storage.store(69, {"from": account})
    updating_value.wait(1)
    updated_value = simple_storage.show()
    print(updated_value)


def main():
    deploy_simple_storage()
