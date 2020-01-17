import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_files(host):
    files = [
        "/etc/systemd/system/algernon.service",
        "/usr/local/bin/algernon"
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_user(host):
    assert host.group("algernon").exists
    assert "algernon" in host.user("algernon").groups
    assert host.user("algernon").shell == "/usr/sbin/nologin"
    assert host.user("algernon").home == "/"


def test_service(host):
    s = host.service("algernon")
#    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    sockets = [
        "tcp://127.0.0.1:8090"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening
