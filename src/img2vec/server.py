from concurrent import futures
from threading import Event

import grpc
import signal

from img2vec.config.config import Config
from img2vec.vectorizer import ClipVectorizer
from img2vec.util import getLogger
from img2vec.api.v1 import img2vec_pb2_grpc as pb2_grpc
from img2vec.servicer.v1.img2vec import Img2VecService

logger = getLogger(__name__)


class GracefulKiller:
    kill_now = False

    def __init__(self):
        self.__event = Event()
        signal.signal(signal.SIGINT, self.__exit_gracefully)
        signal.signal(signal.SIGTERM, self.__exit_gracefully)

    def __exit_gracefully(self, signum, frame):
        self.__event.set()

    def wait(self):
        self.__event.wait()


def serve(config: Config):
    logger.info('starting server')

    killer = GracefulKiller()

    logger.info(f'loading the model: {config.vectorizer.model}')
    ClipVectorizer.load(config.vectorizer.model, config.vectorizer.cuda)
    logger.info('model loaded')

    vectorizer = ClipVectorizer(config.vectorizer.model, config.vectorizer.cuda)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=config.grpc.num_workers),
                         options=[
                             ('grpc.max_receive_message_length', 1024 ** 3),
                             ('grpc.max_send_message_length', 1024 ** 3),
                         ])
    pb2_grpc.add_Img2VecServicer_to_server(Img2VecService(vectorizer), server)

    listen_addr = f'[::]:{config.grpc.listen_port}'
    server.add_insecure_port(listen_addr)
    server.start()

    logger.info(f'started server on {listen_addr}')

    killer.wait()
    logger.info('stopping server')
    server.stop(0)
