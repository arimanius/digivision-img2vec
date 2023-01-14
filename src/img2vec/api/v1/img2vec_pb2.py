# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: img2vec/api/v1/img2vec.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='img2vec/api/v1/img2vec.proto',
  package='img2vec',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cimg2vec/api/v1/img2vec.proto\x12\x07img2vec\"\x16\n\x05Image\x12\r\n\x05image\x18\x01 \x01(\x0c\"\x18\n\x06Vector\x12\x0e\n\x06vector\x18\x01 \x03(\x02\x32\x39\n\x07Img2Vec\x12.\n\tVectorize\x12\x0e.img2vec.Image\x1a\x0f.img2vec.Vector\"\x00\x62\x06proto3'
)




_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='img2vec.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='img2vec.Image.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=63,
)


_VECTOR = _descriptor.Descriptor(
  name='Vector',
  full_name='img2vec.Vector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vector', full_name='img2vec.Vector.vector', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['Vector'] = _VECTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'img2vec.api.v1.img2vec_pb2'
  # @@protoc_insertion_point(class_scope:img2vec.Image)
  })
_sym_db.RegisterMessage(Image)

Vector = _reflection.GeneratedProtocolMessageType('Vector', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR,
  '__module__' : 'img2vec.api.v1.img2vec_pb2'
  # @@protoc_insertion_point(class_scope:img2vec.Vector)
  })
_sym_db.RegisterMessage(Vector)



_IMG2VEC = _descriptor.ServiceDescriptor(
  name='Img2Vec',
  full_name='img2vec.Img2Vec',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=91,
  serialized_end=148,
  methods=[
  _descriptor.MethodDescriptor(
    name='Vectorize',
    full_name='img2vec.Img2Vec.Vectorize',
    index=0,
    containing_service=None,
    input_type=_IMAGE,
    output_type=_VECTOR,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMG2VEC)

DESCRIPTOR.services_by_name['Img2Vec'] = _IMG2VEC

# @@protoc_insertion_point(module_scope)