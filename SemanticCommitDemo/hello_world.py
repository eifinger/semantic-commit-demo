"""Hello World Program."""


class HelloWorld:
    """A Hello World Class."""

    def __init__(
        self,
        name: str = "World",
    ) -> None:
        """Initialize connection data."""
        self.name = name

    def say_hello(self):
        """Say hello to the world."""
        print(f"Hello {self.name}")
