"""Tests for Hello World."""

from SemanticCommitDemo import HelloWorld


def test_say_hello() -> None:
    """Test that standard works."""
    world = HelloWorld()
    world.say_hello()


def test_say_bye() -> None:
    """Test that standard works."""
    world = HelloWorld()
    world.say_bye()
