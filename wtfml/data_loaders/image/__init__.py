from .classification import ClassificationDataLoader
import pytorch_lightning as pl


class FaceDataModule(pl.LightningDataModule):
    def __init__(self, train_data_loader, valid_data_loader) -> None:
        super().__init__()
        self.train_data_loader = train_data_loader
        self.valid_data_loader = valid_data_loader

    def train_dataloader(self):
        return self.train_data_loader

    def val_dataloader(self):
        return self.valid_data_loader
