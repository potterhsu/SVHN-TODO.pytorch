import os
import time
from typing import Tuple

import torch
import torch.nn.functional
from torch import nn, Tensor


class Model(nn.Module):

    def __init__(self):
        super().__init__()
        # TODO: CODE BEGIN
        raise NotImplementedError
        # TODO: CODE END

    def forward(self, images: Tensor) -> Tuple[Tensor, Tensor]:
        # TODO: CODE BEGIN
        raise NotImplementedError
        # TODO: CODE END

    def loss(self, logits: Tensor, labels: Tensor) -> Tensor:
        # TODO: CODE BEGIN
        raise NotImplementedError
        # TODO: CODE END

    def save(self, path_to_checkpoints_dir: str, step: int) -> str:
        path_to_checkpoint = os.path.join(path_to_checkpoints_dir,
                                          'model-{:s}-{:d}.pth'.format(time.strftime('%Y%m%d%H%M'), step))
        torch.save(self.state_dict(), path_to_checkpoint)
        return path_to_checkpoint

    def load(self, path_to_checkpoint: str) -> 'Model':
        self.load_state_dict(torch.load(path_to_checkpoint))
        return self
