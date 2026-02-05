"""Re-export data utilities from data_solution."""

from data_solution import corrupt_mnist, MyDataset, normalize, preprocess_data

__all__ = ["corrupt_mnist", "MyDataset", "normalize", "preprocess_data"]
