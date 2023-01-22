import copy

import clip
import numpy as np
import torch
from PIL import Image
from clip.model import CLIP
from torchvision import transforms

from img2vec.util import getLogger

logger = getLogger('clip')


class ClipVectorizer:

    @staticmethod
    def load(model: str, cuda: bool) -> None:
        device = "cuda" if cuda and torch.cuda.is_available() else "cpu"
        clip.load(model, device=device)

    def __init__(self, model: str, cuda: bool):
        self.__device = "cuda" if cuda and torch.cuda.is_available() else "cpu"
        logger.info(f'Using device: {self.__device}')
        model, preprocess = clip.load(model, device=self.__device)
        model: CLIP = model
        self.__model = model.visual
        self.__dtype = model.dtype
        model.cpu()
        self.__preprocess: transforms.Compose = preprocess

    @torch.cuda.amp.autocast()
    @torch.no_grad()
    @torch.inference_mode()
    def vectorize(self, image: Image.Image) -> np.ndarray:
        image: torch.Tensor = self.__preprocess(image).unsqueeze(0).to(self.__device)
        vector = self.__model(image.type(self.__dtype))
        return vector.cpu().numpy().flatten()
