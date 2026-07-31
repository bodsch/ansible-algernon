from __future__ import annotations, unicode_literals

import os

import pytest
import testinfra.utils.ansible_runner
from helper.molecule import get_vars, infra_hosts, local_facts

testinfra_hosts = infra_hosts(host_name="instance")

# --- tests -----------------------------------------------------------------


def test_files(host):
    files = ["/usr/bin/algernon"]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_user(host):
    assert host.group("algernon").exists
    assert "algernon" in host.user("algernon").groups
    assert host.user("algernon").shell == "/usr/sbin/nologin"
    assert host.user("algernon").home == "/nonexistent"


def test_service(host):
    s = host.service("algernon")
    assert s.is_enabled
    assert s.is_running


@pytest.mark.parametrize(
    "ports",
    [
        "127.0.0.1:8090",
    ],
)
def test_open_port(host, ports):

    for i in host.socket.get_listening_sockets():
        print(i)

    s = host.socket("tcp://{}".format(ports))
    assert s.is_listening
