# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from img2vec.api.v1 import img2vec_pb2 as img2vec_dot_api_dot_v1_dot_img2vec__pb2


class Img2VecStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Vectorize = channel.unary_unary(
                '/img2vec.Img2Vec/Vectorize',
                request_serializer=img2vec_dot_api_dot_v1_dot_img2vec__pb2.Image.SerializeToString,
                response_deserializer=img2vec_dot_api_dot_v1_dot_img2vec__pb2.Vector.FromString,
                )


class Img2VecServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Vectorize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Img2VecServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Vectorize': grpc.unary_unary_rpc_method_handler(
                    servicer.Vectorize,
                    request_deserializer=img2vec_dot_api_dot_v1_dot_img2vec__pb2.Image.FromString,
                    response_serializer=img2vec_dot_api_dot_v1_dot_img2vec__pb2.Vector.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'img2vec.Img2Vec', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Img2Vec(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Vectorize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/img2vec.Img2Vec/Vectorize',
            img2vec_dot_api_dot_v1_dot_img2vec__pb2.Image.SerializeToString,
            img2vec_dot_api_dot_v1_dot_img2vec__pb2.Vector.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
