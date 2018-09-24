# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='search.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0csearch.proto\x1a\x1bgoogle/protobuf/empty.proto\"f\n\rSearchRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x0b\n\x03lat\x18\x04 \x01(\x02\x12\x0b\n\x03lng\x18\x05 \x01(\x02\x12\x13\n\x0bpage_number\x18\x02 \x01(\x05\x12\x17\n\x0fresult_per_page\x18\x03 \x01(\x05\"5\n\x0fSearchResponses\x12\"\n\tresponses\x18\x01 \x03(\x0b\x32\x0f.SearchResponse\"\"\n\x0eSearchResponse\x12\x10\n\x08response\x18\x01 \x01(\t\"#\n\x0fMonitorResponse\x12\x10\n\x08n_things\x18\x01 \x01(\x05\x32m\n\x06Search\x12\x35\n\x07monitor\x12\x16.google.protobuf.Empty\x1a\x10.MonitorResponse\"\x00\x12,\n\x06search\x12\x0e.SearchRequest\x1a\x10.SearchResponses\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='SearchRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat', full_name='SearchRequest.lat', index=1,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lng', full_name='SearchRequest.lng', index=2,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_number', full_name='SearchRequest.page_number', index=3,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_per_page', full_name='SearchRequest.result_per_page', index=4,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=147,
)


_SEARCHRESPONSES = _descriptor.Descriptor(
  name='SearchResponses',
  full_name='SearchResponses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responses', full_name='SearchResponses.responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=202,
)


_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='SearchResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=238,
)


_MONITORRESPONSE = _descriptor.Descriptor(
  name='MonitorResponse',
  full_name='MonitorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n_things', full_name='MonitorResponse.n_things', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=275,
)

_SEARCHRESPONSES.fields_by_name['responses'].message_type = _SEARCHRESPONSE
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchResponses'] = _SEARCHRESPONSES
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
DESCRIPTOR.message_types_by_name['MonitorResponse'] = _MONITORRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREQUEST,
  __module__ = 'search_pb2'
  # @@protoc_insertion_point(class_scope:SearchRequest)
  ))
_sym_db.RegisterMessage(SearchRequest)

SearchResponses = _reflection.GeneratedProtocolMessageType('SearchResponses', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHRESPONSES,
  __module__ = 'search_pb2'
  # @@protoc_insertion_point(class_scope:SearchResponses)
  ))
_sym_db.RegisterMessage(SearchResponses)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHRESPONSE,
  __module__ = 'search_pb2'
  # @@protoc_insertion_point(class_scope:SearchResponse)
  ))
_sym_db.RegisterMessage(SearchResponse)

MonitorResponse = _reflection.GeneratedProtocolMessageType('MonitorResponse', (_message.Message,), dict(
  DESCRIPTOR = _MONITORRESPONSE,
  __module__ = 'search_pb2'
  # @@protoc_insertion_point(class_scope:MonitorResponse)
  ))
_sym_db.RegisterMessage(MonitorResponse)



_SEARCH = _descriptor.ServiceDescriptor(
  name='Search',
  full_name='Search',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=277,
  serialized_end=386,
  methods=[
  _descriptor.MethodDescriptor(
    name='monitor',
    full_name='Search.monitor',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_MONITORRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='search',
    full_name='Search.search',
    index=1,
    containing_service=None,
    input_type=_SEARCHREQUEST,
    output_type=_SEARCHRESPONSES,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEARCH)

DESCRIPTOR.services_by_name['Search'] = _SEARCH

# @@protoc_insertion_point(module_scope)