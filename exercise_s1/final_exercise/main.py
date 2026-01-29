import torch
import typer
from data import corrupt_mnist
from model import MyAwesomeModel

app = typer.Typer()

@app.command()
def train(lr: float = 1e-3, epochs: int = 5) -> None:
    """Train a model on MNIST."""
    print("Training day and night")
    print(f"Learning rate: {lr}")

    # Initialize model, loss, and optimizer
    model = MyAwesomeModel()
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    
    # Load data
    train_set, _ = corrupt_mnist()
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=64, shuffle=True)

    # Training loop
    for epoch in range(epochs):
        running_loss = 0.0
        for images, labels in train_loader:
            # Zero gradients
            optimizer.zero_grad()
            
            # Forward pass
            output = model(images)
            loss = criterion(output, labels)
            
            # Backward pass
            loss.backward()
            
            # Update weights
            optimizer.step()
            
            running_loss += loss.item()
            
        print(f"Epoch {epoch+1}, Loss: {running_loss/len(train_loader)}")

    # Save the trained model
    torch.save(model.state_dict(), "model.pt")
    print("Training complete. Model saved to model.pt")


@app.command()
def evaluate(model_checkpoint: str) -> None:
    """Evaluate a trained model."""
    print("Evaluating like my life depends on it")
    print(model_checkpoint)

    # Load model structure and weights
    model = MyAwesomeModel()
    model.load_state_dict(torch.load(model_checkpoint))
    model.eval() # Set to evaluation mode
    
    # Load test data
    _, test_set = corrupt_mnist()
    test_loader = torch.utils.data.DataLoader(test_set, batch_size=64, shuffle=False)
    
    correct = 0
    total = 0
    
    # Evaluation loop (no gradients needed)
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    print(f"Accuracy on test set: {accuracy:.2f}%")

if __name__ == "__main__":
    app()