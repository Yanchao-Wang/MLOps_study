"""Entry point for evaluation with Click CLI."""

import click
from evaluate_solution import evaluate


@click.command()
@click.option(
    "--checkpoint",
    "-c",
    type=str,
    default="models/model.pth",
    help="Path to the trained model checkpoint",
)
def main(checkpoint):
    """Evaluate a trained neural network model on the test dataset.

    Example:
        python evaluate.py
        python evaluate.py --checkpoint models/best_model.pth
        python evaluate.py -c /path/to/model.pth
    """
    print(f"📊 Evaluating model: {checkpoint}")
    try:
        evaluate(checkpoint)
        print("✅ Evaluation completed successfully!")
    except Exception as e:
        print(f"❌ Evaluation failed: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
