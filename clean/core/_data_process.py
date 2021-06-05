import torch
import numpy as np
import torch.utils.data as tud
from PIL import Image


class CellsDataset(tud.Dataset):
    def __init__(self, images):
        self.images = images

    def __len__(self): return len(self.images)

    def __getitem__(self, index): return self.images[index, :, :, :]


class CellsDataBuilder:
    def __init__(self, data_path):
        self.data_path = data_path

    def forward(self):
        input_data_clean, \
        input_data_reshaped = self.prepare()
        loader = self.get_loaders(input_data_reshaped)

        return input_data_clean, loader

    def prepare(self):
        data = Image.open(self.data_path)
        data_clean = torch.from_numpy(np.asarray(data).copy())
        data = torch.stack(torch.chunk(data_clean, 4, 0))
        data = torch.stack(torch.chunk(data, 4, 2))

        return data_clean, torch.reshape(data, (16, 480, 640, 3))

    @staticmethod
    def get_loaders(images,
                    batch_size: int = 1,
                    num_workers: int = 1,
                    pin_memory: bool = True):
        train_ds = CellsDataset(images=images)

        data_loader = tud.DataLoader(train_ds,
                                     batch_size=batch_size,
                                     shuffle=False,
                                     num_workers=num_workers,
                                     pin_memory=pin_memory)

        return data_loader
