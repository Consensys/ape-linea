import pytest
from ape_ethereum.transactions import TransactionType
from ethpm_types import MethodABI


def test_gas_limit(linea):
    assert linea.config.local.gas_limit == "max"


@pytest.mark.parametrize("tx_type", (0, "0x0"))
def test_create_transaction(linea, tx_type, eth_tester_provider):
    tx = linea.create_transaction(type=tx_type)
    assert tx.type == TransactionType.STATIC.value
    assert tx.gas_limit == eth_tester_provider.max_gas


@pytest.mark.parametrize(
    "tx_type",
    (TransactionType.STATIC.value, TransactionType.DYNAMIC.value),
)
def test_encode_transaction(tx_type, linea, eth_tester_provider):
    abi = MethodABI.model_validate(
        {
            "type": "function",
            "name": "fooAndBar",
            "stateMutability": "nonpayable",
            "inputs": [],
            "outputs": [],
        }
    )
    address = "0x274b028b03A250cA03644E6c578D81f019eE1323"
    actual = linea.encode_transaction(address, abi, sender=address, type=tx_type)
    assert actual.gas_limit == eth_tester_provider.max_gas
