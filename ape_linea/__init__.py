from ape import plugins
from ape.api import NetworkAPI, create_network_type
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_geth import GethProvider
from ape_test import LocalProvider

from .ecosystem import NETWORKS, Linea, LineaConfig


@plugins.register(plugins.Config)
def config_class():
    return LineaConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    yield Linea


@plugins.register(plugins.NetworkPlugin)
def networks():
    for network_name, network_params in NETWORKS.items():
        yield "linea", network_name, create_network_type(*network_params)
        yield "linea", f"{network_name}-fork", NetworkAPI

    # NOTE: This works for development providers, as they get chain_id from themselves
    yield "linea", LOCAL_NETWORK_NAME, NetworkAPI


@plugins.register(plugins.ProviderPlugin)
def providers():
    for network_name in NETWORKS:
        yield "linea", network_name, GethProvider

    yield "linea", LOCAL_NETWORK_NAME, LocalProvider
