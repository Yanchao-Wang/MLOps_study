"""Iris classifier with Typer CLI - Complete version with nested subcommands."""

import typer
import pickle
from typing import Annotated
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

app = typer.Typer(help="Iris classifier CLI with nested subcommands")
train_app = typer.Typer(help="Train a model")
app.add_typer(train_app, name="train")


@train_app.command("svm")
def train_svm(
    kernel: Annotated[str, typer.Option(help="Kernel type for SVM")] = "linear",
    output: Annotated[
        str, typer.Option("--output", "-o", help="Output path for the trained model")
    ] = "model_svm.ckpt",
) -> None:
    """Train a Support Vector Machine (SVM) model."""
    # Load the dataset
    data = load_iris()
    x = data.data
    y = data.target

    # Split the dataset
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Standardize the features
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    # Train SVM model
    print(f"Training SVM with kernel='{kernel}'...")
    model = SVC(kernel=kernel, random_state=42)
    model.fit(x_train, y_train)

    # Evaluate
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)

    # Save the model
    with open(output, "wb") as f:
        pickle.dump({"model": model, "scaler": scaler, "type": "svm", "kernel": kernel}, f)
    print(f"✅ SVM model saved to {output}")


@train_app.command("knn")
def train_knn(
    n_neighbors: Annotated[int, typer.Option(help="Number of neighbors for KNN")] = 5,
    output: Annotated[
        str, typer.Option("--output", "-o", help="Output path for the trained model")
    ] = "model_knn.ckpt",
) -> None:
    """Train a K-Nearest Neighbors (KNN) model."""
    # Load the dataset
    data = load_iris()
    x = data.data
    y = data.target

    # Split the dataset
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Standardize the features
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    # Train KNN model
    print(f"Training KNN with n_neighbors={n_neighbors}...")
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(x_train, y_train)

    # Evaluate
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)

    # Save the model
    with open(output, "wb") as f:
        pickle.dump(
            {"model": model, "scaler": scaler, "type": "knn", "n_neighbors": n_neighbors}, f
        )
    print(f"✅ KNN model saved to {output}")


@app.command()
def evaluate(
    checkpoint: Annotated[str, typer.Argument(help="Path to the model checkpoint")],
) -> None:
    """Evaluate a saved model on the test set."""
    # Load the model
    try:
        with open(checkpoint, "rb") as f:
            saved_data = pickle.load(f)
        model = saved_data["model"]
        scaler = saved_data["scaler"]
        model_type = saved_data.get("type", "unknown")
        print(f"📊 Loaded {model_type.upper()} model from {checkpoint}")
    except FileNotFoundError:
        print(f"❌ Model file not found: {checkpoint}")
        raise typer.Exit(code=1)

    # Load the dataset
    data = load_iris()
    x = data.data
    y = data.target

    # Split to get test set
    _, x_test, _, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Standardize
    x_test = scaler.transform(x_test)

    # Predict and evaluate
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)


if __name__ == "__main__":
    app()
