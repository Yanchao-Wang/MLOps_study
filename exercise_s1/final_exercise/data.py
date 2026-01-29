import torch
import os
import glob

def corrupt_mnist():
    """Return train and test datasets for corrupt MNIST."""
    
    data_path = "data/corruptmnist"
    
    if os.path.exists(data_path) and glob.glob(os.path.join(data_path, "train_*.pt")):
        # Load training data (split across multiple .pt files)
        train_images = []
        train_targets = []
        
        # Find all train files (e.g., train_0.pt, train_1.pt...)
        train_files = glob.glob(os.path.join(data_path, "train_*.pt"))
        
        for f in train_files:
            content = torch.load(f)
            train_images.append(content['images'])
            train_targets.append(content['labels'])
            
        # Concatenate all parts
        train_images = torch.cat(train_images)
        train_targets = torch.cat(train_targets)
        
        # Load test data
        test_content = torch.load(os.path.join(data_path, "test.pt"))
        test_images = test_content['images']
        test_targets = test_content['labels']
        
        # Add channel dimension: [N, H, W] -> [N, 1, H, W]
        train_images = train_images.unsqueeze(1).float()
        test_images = test_images.unsqueeze(1).float()

        # Create TensorDatasets
        train_set = torch.utils.data.TensorDataset(train_images, train_targets)
        test_set = torch.utils.data.TensorDataset(test_images, test_targets)
    else:
        print("!! Data not found. Using FAKE data for local debugging !!")
        train_images = torch.randn(100, 1, 28, 28) 
        train_targets = torch.randint(0, 10, (100,))
        
        test_images = torch.randn(10, 1, 28, 28)
        test_targets = torch.randint(0, 10, (10,))
        
        train_set = torch.utils.data.TensorDataset(train_images, train_targets)
        test_set = torch.utils.data.TensorDataset(test_images, test_targets)
    
    return train_set, test_set