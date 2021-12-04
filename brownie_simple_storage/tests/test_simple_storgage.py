from brownie import accounts, SimpleStorage


def test_deploy():
    # arrange
    account = accounts[0]

    # act ,i.e, deploy
    simple_storage = SimpleStorage.deploy({"from": account})
    intial_value = simple_storage.show()
    expected = 0

    # assert
    assert intial_value == expected


def test_updating_storage():
    # arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy(
        {"from": account}
    )  # present here because we need to deploy the contract first in order to check the updated value later

    # act
    expected = 69
    simple_storage.store(69, {"from": account})

    # assert
    assert expected == simple_storage.show()
