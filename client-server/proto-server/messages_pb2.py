# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\"\x14\n\x12GetMessagesRequest\"1\n\x13GetMessagesResponse\x12\x1a\n\x08messages\x18\x01 \x03(\x0b\x32\x08.Message\"#\n\x07Message\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t2F\n\x08Messages\x12:\n\x0bGetMessages\x12\x13.GetMessagesRequest\x1a\x14.GetMessagesResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETMESSAGESREQUEST']._serialized_start=18
  _globals['_GETMESSAGESREQUEST']._serialized_end=38
  _globals['_GETMESSAGESRESPONSE']._serialized_start=40
  _globals['_GETMESSAGESRESPONSE']._serialized_end=89
  _globals['_MESSAGE']._serialized_start=91
  _globals['_MESSAGE']._serialized_end=126
  _globals['_MESSAGES']._serialized_start=128
  _globals['_MESSAGES']._serialized_end=198
# @@protoc_insertion_point(module_scope)
