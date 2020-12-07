import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = '/usr/local/bin/terraforming'


def test_terraforming_binary_exists(host):
    """
    Tests if terraforming binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_terraforming_binary_file(host):
    """
    Tests if terraforming binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_terraforming_binary_which(host):
    """
    Tests the output to confirm terraforming's binary location.
    """
    assert host.check_output('which terraforming') == PACKAGE_BINARY
