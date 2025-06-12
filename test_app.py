"""Test app module"""

import app


def test_hello():
    """Test Hello"""
    assert "Hello ABC" == app.hello("ABC")
