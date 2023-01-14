import io

import PIL
from PIL import Image as pi
import grpc

from img2vec.api.v1.img2vec_pb2_grpc import Img2VecServicer
from img2vec.api.v1.img2vec_pb2 import Vector, Image
from img2vec.vectorizer import ClipVectorizer


class Img2VecService(Img2VecServicer):

    def __init__(self, vectorizer: ClipVectorizer):
        self.__vectorizer = vectorizer

    def Vectorize(self, request: Image, context: grpc.ServicerContext) -> Vector:
        try:
            image = pi.open(io.BytesIO(request.image))
            v = self.__vectorizer.vectorize(image)
            return Vector(vector=v)
        except PIL.UnidentifiedImageError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, f'invalid image type: {e}')
        except Exception as e:
            context.abort(grpc.StatusCode.UNKNOWN, f'unknown error: {e}')
