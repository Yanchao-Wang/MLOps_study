"""Simple greeting script using Typer."""

import typer


def main(count: int = 1) -> None:
    """Print 'Hello World!' a specified number of times.

    Args:
        count: Number of times to print the greeting (default: 1)
    """
    for _ in range(count):
        print("Hello World!")


if __name__ == "__main__":
    typer.run(main)
