"""Entry point for training with Click CLI."""

import click
from train_solution import train


@click.command()
@click.option("--lr", type=float, default=0.001, help="Learning rate for the optimizer")
@click.option("--batch-size", type=int, default=32, help="Batch size for training")
@click.option("--epochs", type=int, default=10, help="Number of training epochs")
def main(lr, batch_size, epochs):
    """Train a neural network model on the MNIST dataset.

    Example:
        python train.py --lr 0.01 --epochs 20
        python train.py --batch-size 64 --epochs 5
    """
    print(f"🚀 Starting training with lr={lr}, batch_size={batch_size}, epochs={epochs}")
    try:
        train(lr=lr, batch_size=batch_size, epochs=epochs)
        print("✅ Training completed successfully!")
    except Exception as e:
        print(f"❌ Training failed: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
