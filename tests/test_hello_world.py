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


def test_say_hello_multiple_times() -> None:
    """Test that say_hello_multiple_times works."""
    world = HelloWorld()
    world.say_hello_multiple_times()


def test_say_hello_five_times() -> None:
    """Test that say_hello_five_times works."""
    world = HelloWorld()
    world.say_hello_five_times()
