import socket
import pytest
from urllib.parse import urlparse


def host_port(url: str):
    parsed_url = urlparse(url)
    host = parsed_url.hostname
    port = parsed_url.port or 80
    return host, port


@pytest.mark.parametrize('link', ['frontend_url', 'gateway_url', 'auth_url'])
def test_resource_availability(link, request):
    host, port = host_port(request.getfixturevalue(link))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((host, port))
        available = True
    except (socket.timeout, ConnectionRefusedError):
        available = False
    finally:
        sock.close()
    assert available, f"Resource at {host}:{port} is not available"


@pytest.mark.parametrize('link', ['frontend_url', 'gateway_url', 'auth_url'])
def test_port_is_open(link, request):
    host, port = host_port(request.getfixturevalue(link))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    assert result == 0, f"Port {port} on host {host} is not open"
