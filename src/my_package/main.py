"""Main module for my_package."""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a greeting message.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.

    Examples:
        >>> greet("World")
        'Hello, World!'
    """
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"


def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of a and b.

    Examples:
        >>> add(1, 2)
        3
        >>> add(1.5, 2.5)
        4.0
    """
    return a + b


if __name__ == "__main__":
    print(greet("World"))
