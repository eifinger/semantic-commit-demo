"""Hello World Program."""


class HelloWorld:
    """A Hello World Class."""

    def __init__(
        self,
        name: str = "World!",
    ) -> None:
        """Initialize connection data."""
        self.name = name

    def say_hello(self) -> None:
        """Say hello to the world."""
        print(f"Hello {self.name}")

    def say_hello_multiple_times(self) -> None:
        """Say hello to the world five times."""
        print(f"Hello {self.name}")
        print(f"Hello {self.name}")
        print(f"Hello {self.name}")
        print(f"Hello {self.name}")
        print(f"Hello {self.name}")

    def say_hello_five_times(self) -> None:
        """Say hello to the world five times."""
        print(f"Hello {self.name}")
        print(f"Hello {self.name}")
        print(f"Hello {self.name}")
        print(f"Hello {self.name}")
        print(f"Hello {self.name}")

    def say_bye(self) -> None:
        """Say hello to the world!!!!!!"""
        print(f"Goodbye {self.name}")
