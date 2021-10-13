"""Tests for Hello World."""

from SemanticCommitDemo import HelloWorld


def test_say_hello():
    """Test that standard works."""
    world = HelloWorld()
    world.say_hello()
