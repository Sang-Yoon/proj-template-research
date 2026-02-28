"""Tests for my_package.main module."""

from __future__ import annotations

import pytest

from my_package.main import add, greet


class TestGreet:
    """Tests for the greet function."""

    def test_greet_simple(self) -> None:
        """Test basic greeting."""
        assert greet("World") == "Hello, World!"

    def test_greet_name(self) -> None:
        """Test greeting with a custom name."""
        assert greet("Python") == "Hello, Python!"

    def test_greet_empty_raises(self) -> None:
        """Test that empty name raises ValueError."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("")

    @pytest.mark.parametrize(
        ("name", "expected"),
        [
            ("Alice", "Hello, Alice!"),
            ("Bob", "Hello, Bob!"),
            ("Claude", "Hello, Claude!"),
        ],
    )
    def test_greet_parametrized(self, name: str, expected: str) -> None:
        """Test greeting with multiple names."""
        assert greet(name) == expected


class TestAdd:
    """Tests for the add function."""

    def test_add_integers(self) -> None:
        """Test adding two integers."""
        assert add(1, 2) == 3

    def test_add_floats(self) -> None:
        """Test adding two floats."""
        assert add(1.5, 2.5) == 4.0

    def test_add_mixed(self) -> None:
        """Test adding int and float."""
        assert add(1, 2.5) == 3.5

    def test_add_negative(self) -> None:
        """Test adding negative numbers."""
        assert add(-1, -2) == -3

    def test_add_zero(self) -> None:
        """Test adding zero."""
        assert add(0, 5) == 5

    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (1, 2, 3),
            (0, 0, 0),
            (-1, 1, 0),
            (100, 200, 300),
        ],
    )
    def test_add_parametrized(self, a: int, b: int, expected: int) -> None:
        """Test add with multiple inputs."""
        assert add(a, b) == expected
