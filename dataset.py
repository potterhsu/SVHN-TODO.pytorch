from enum import Enum
from typing import Tuple

import PIL
import torch.utils.data
from PIL import Image
from torch import Tensor


class Dataset(torch.utils.data.Dataset):

    class Mode(Enum):
        TRAIN = 'train'
        TEST = 'test'

    def __init__(self, path_to_data_dir: str, mode: Mode):
        super().__init__()
        is_train = mode == Dataset.Mode.TRAIN

        # TODO: CODE BEGIN
        raise NotImplementedError
        # TODO: CODE END

    def __len__(self) -> int:
        # TODO: CODE BEGIN
        raise NotImplementedError
        # TODO: CODE END

    def __getitem__(self, index) -> Tuple[Tensor, Tensor]:
        # TODO: CODE BEGIN
        raise NotImplementedError
        # TODO: CODE END

    @staticmethod
    def preprocess(image: PIL.Image.Image) -> Tensor:
        # TODO: CODE BEGIN
        raise NotImplementedError
        # TODO: CODE END
