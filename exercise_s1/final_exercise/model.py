from torch import nn
import torch.nn.functional as F

class MyAwesomeModel(nn.Module):
    """My awesome model."""

    def __init__(self) -> None:
        super().__init__()
        # Convolutional layers to capture spatial features
        # Input channels: 1 (grayscale), Output: 32, Kernel: 3x3
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        
        # Max pooling to reduce dimensions
        self.pool = nn.MaxPool2d(2, 2)
        
        # Fully connected layers
        # Image is 28x28. After two poolings (div by 2 twice): 7x7.
        # 64 channels * 7 * 7 = 3136
        self.fc1 = nn.Linear(64 * 7 * 7, 256)
        self.fc2 = nn.Linear(256, 10) # 10 output classes
        
        self.dropout = nn.Dropout(0.25)

    def forward(self, x):
        # Layer 1: Conv -> ReLU -> Pool
        x = self.pool(F.relu(self.conv1(x)))
        # Layer 2: Conv -> ReLU -> Pool
        x = self.pool(F.relu(self.conv2(x)))
        
        # Flatten for fully connected layer
        x = x.view(-1, 64 * 7 * 7)
        
        # FC layers with dropout
        x = self.dropout(F.relu(self.fc1(x)))
        x = self.fc2(x)
        
        return x