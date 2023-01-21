import clip
import numpy as np
import torch
from PIL import Image

from img2vec.util import getLogger

logger = getLogger('clip')


class ClipVectorizer:

    @staticmethod
    def load(model: str) -> None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        clip.load(model, device=device)

    def __init__(self, model: str):
        self.__device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f'Using device: {self.__device}')
        self.__model, self.__preprocess = clip.load(model, device=self.__device)

    @torch.cuda.amp.autocast()
    @torch.no_grad()
    @torch.inference_mode()
    def vectorize(self, image: Image.Image) -> np.ndarray:
        image = self.__preprocess(image).unsqueeze(0).to(self.__device)
        vector = self.__model.encode_image(image)
        return vector.cpu().numpy().flatten()
