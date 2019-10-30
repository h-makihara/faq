# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: faq.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='faq.proto',
  package='faq',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tfaq.proto\x12\x03\x66\x61q\"p\n\x0c\x46\x61qComponent\x12\x0b\n\x03qid\x18\x01 \x01(\r\x12\r\n\x05share\x18\x02 \x01(\r\x12\x14\n\x0cservice_name\x18\x03 \x01(\t\x12\x0c\n\x04lang\x18\x04 \x01(\t\x12\x10\n\x08question\x18\x05 \x01(\t\x12\x0e\n\x06\x61nswer\x18\x06 \x01(\t\">\n\x17ServerResponseComponent\x12\x12\n\nis_success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"I\n\x10\x46\x61qCreateRequest\x12\"\n\x07\x66\x61qData\x18\x01 \x03(\x0b\x32\x11.faq.FaqComponent\x12\x11\n\ttimestamp\x18\x02 \x01(\t\"V\n\x11\x46\x61qCreateResponse\x12.\n\x08response\x18\x01 \x01(\x0b\x32\x1c.faq.ServerResponseComponent\x12\x11\n\ttimestamp\x18\x02 \x01(\t\"#\n\x0e\x46\x61qShowRequest\x12\x11\n\ttimestamp\x18\x01 \x01(\t\"1\n\x0f\x46\x61qShowResponse\x12\x1e\n\x03\x66\x61q\x18\x01 \x03(\x0b\x32\x11.faq.FaqComponent\"E\n\x10\x46\x61qUpdateRequest\x12\x1e\n\x03\x66\x61q\x18\x01 \x01(\x0b\x32\x11.faq.FaqComponent\x12\x11\n\ttimestamp\x18\x02 \x01(\t\"V\n\x11\x46\x61qUpdateResponse\x12.\n\x08response\x18\x01 \x01(\x0b\x32\x1c.faq.ServerResponseComponent\x12\x11\n\ttimestamp\x18\x02 \x01(\t2\xc0\x01\n\nFaqGateway\x12<\n\tFaqCreate\x12\x15.faq.FaqCreateRequest\x1a\x16.faq.FaqCreateResponse\"\x00\x12\x36\n\x07\x46\x61qShow\x12\x13.faq.FaqShowRequest\x1a\x14.faq.FaqShowResponse\"\x00\x12<\n\tFaqUpdate\x12\x15.faq.FaqUpdateRequest\x1a\x16.faq.FaqUpdateResponse\"\x00\x62\x06proto3')
)




_FAQCOMPONENT = _descriptor.Descriptor(
  name='FaqComponent',
  full_name='faq.FaqComponent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='qid', full_name='faq.FaqComponent.qid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='share', full_name='faq.FaqComponent.share', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='faq.FaqComponent.service_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lang', full_name='faq.FaqComponent.lang', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='question', full_name='faq.FaqComponent.question', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='answer', full_name='faq.FaqComponent.answer', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=18,
  serialized_end=130,
)


_SERVERRESPONSECOMPONENT = _descriptor.Descriptor(
  name='ServerResponseComponent',
  full_name='faq.ServerResponseComponent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_success', full_name='faq.ServerResponseComponent.is_success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='faq.ServerResponseComponent.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=132,
  serialized_end=194,
)


_FAQCREATEREQUEST = _descriptor.Descriptor(
  name='FaqCreateRequest',
  full_name='faq.FaqCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faqData', full_name='faq.FaqCreateRequest.faqData', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='faq.FaqCreateRequest.timestamp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=196,
  serialized_end=269,
)


_FAQCREATERESPONSE = _descriptor.Descriptor(
  name='FaqCreateResponse',
  full_name='faq.FaqCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='faq.FaqCreateResponse.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='faq.FaqCreateResponse.timestamp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=271,
  serialized_end=357,
)


_FAQSHOWREQUEST = _descriptor.Descriptor(
  name='FaqShowRequest',
  full_name='faq.FaqShowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='faq.FaqShowRequest.timestamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=359,
  serialized_end=394,
)


_FAQSHOWRESPONSE = _descriptor.Descriptor(
  name='FaqShowResponse',
  full_name='faq.FaqShowResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faq', full_name='faq.FaqShowResponse.faq', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=396,
  serialized_end=445,
)


_FAQUPDATEREQUEST = _descriptor.Descriptor(
  name='FaqUpdateRequest',
  full_name='faq.FaqUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faq', full_name='faq.FaqUpdateRequest.faq', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='faq.FaqUpdateRequest.timestamp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=447,
  serialized_end=516,
)


_FAQUPDATERESPONSE = _descriptor.Descriptor(
  name='FaqUpdateResponse',
  full_name='faq.FaqUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='faq.FaqUpdateResponse.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='faq.FaqUpdateResponse.timestamp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=518,
  serialized_end=604,
)

_FAQCREATEREQUEST.fields_by_name['faqData'].message_type = _FAQCOMPONENT
_FAQCREATERESPONSE.fields_by_name['response'].message_type = _SERVERRESPONSECOMPONENT
_FAQSHOWRESPONSE.fields_by_name['faq'].message_type = _FAQCOMPONENT
_FAQUPDATEREQUEST.fields_by_name['faq'].message_type = _FAQCOMPONENT
_FAQUPDATERESPONSE.fields_by_name['response'].message_type = _SERVERRESPONSECOMPONENT
DESCRIPTOR.message_types_by_name['FaqComponent'] = _FAQCOMPONENT
DESCRIPTOR.message_types_by_name['ServerResponseComponent'] = _SERVERRESPONSECOMPONENT
DESCRIPTOR.message_types_by_name['FaqCreateRequest'] = _FAQCREATEREQUEST
DESCRIPTOR.message_types_by_name['FaqCreateResponse'] = _FAQCREATERESPONSE
DESCRIPTOR.message_types_by_name['FaqShowRequest'] = _FAQSHOWREQUEST
DESCRIPTOR.message_types_by_name['FaqShowResponse'] = _FAQSHOWRESPONSE
DESCRIPTOR.message_types_by_name['FaqUpdateRequest'] = _FAQUPDATEREQUEST
DESCRIPTOR.message_types_by_name['FaqUpdateResponse'] = _FAQUPDATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FaqComponent = _reflection.GeneratedProtocolMessageType('FaqComponent', (_message.Message,), {
  'DESCRIPTOR' : _FAQCOMPONENT,
  '__module__' : 'faq_pb2'
  # @@protoc_insertion_point(class_scope:faq.FaqComponent)
  })
_sym_db.RegisterMessage(FaqComponent)

ServerResponseComponent = _reflection.GeneratedProtocolMessageType('ServerResponseComponent', (_message.Message,), {
  'DESCRIPTOR' : _SERVERRESPONSECOMPONENT,
  '__module__' : 'faq_pb2'
  # @@protoc_insertion_point(class_scope:faq.ServerResponseComponent)
  })
_sym_db.RegisterMessage(ServerResponseComponent)

FaqCreateRequest = _reflection.GeneratedProtocolMessageType('FaqCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _FAQCREATEREQUEST,
  '__module__' : 'faq_pb2'
  # @@protoc_insertion_point(class_scope:faq.FaqCreateRequest)
  })
_sym_db.RegisterMessage(FaqCreateRequest)

FaqCreateResponse = _reflection.GeneratedProtocolMessageType('FaqCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _FAQCREATERESPONSE,
  '__module__' : 'faq_pb2'
  # @@protoc_insertion_point(class_scope:faq.FaqCreateResponse)
  })
_sym_db.RegisterMessage(FaqCreateResponse)

FaqShowRequest = _reflection.GeneratedProtocolMessageType('FaqShowRequest', (_message.Message,), {
  'DESCRIPTOR' : _FAQSHOWREQUEST,
  '__module__' : 'faq_pb2'
  # @@protoc_insertion_point(class_scope:faq.FaqShowRequest)
  })
_sym_db.RegisterMessage(FaqShowRequest)

FaqShowResponse = _reflection.GeneratedProtocolMessageType('FaqShowResponse', (_message.Message,), {
  'DESCRIPTOR' : _FAQSHOWRESPONSE,
  '__module__' : 'faq_pb2'
  # @@protoc_insertion_point(class_scope:faq.FaqShowResponse)
  })
_sym_db.RegisterMessage(FaqShowResponse)

FaqUpdateRequest = _reflection.GeneratedProtocolMessageType('FaqUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _FAQUPDATEREQUEST,
  '__module__' : 'faq_pb2'
  # @@protoc_insertion_point(class_scope:faq.FaqUpdateRequest)
  })
_sym_db.RegisterMessage(FaqUpdateRequest)

FaqUpdateResponse = _reflection.GeneratedProtocolMessageType('FaqUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _FAQUPDATERESPONSE,
  '__module__' : 'faq_pb2'
  # @@protoc_insertion_point(class_scope:faq.FaqUpdateResponse)
  })
_sym_db.RegisterMessage(FaqUpdateResponse)



_FAQGATEWAY = _descriptor.ServiceDescriptor(
  name='FaqGateway',
  full_name='faq.FaqGateway',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=607,
  serialized_end=799,
  methods=[
  _descriptor.MethodDescriptor(
    name='FaqCreate',
    full_name='faq.FaqGateway.FaqCreate',
    index=0,
    containing_service=None,
    input_type=_FAQCREATEREQUEST,
    output_type=_FAQCREATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FaqShow',
    full_name='faq.FaqGateway.FaqShow',
    index=1,
    containing_service=None,
    input_type=_FAQSHOWREQUEST,
    output_type=_FAQSHOWRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FaqUpdate',
    full_name='faq.FaqGateway.FaqUpdate',
    index=2,
    containing_service=None,
    input_type=_FAQUPDATEREQUEST,
    output_type=_FAQUPDATERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FAQGATEWAY)

DESCRIPTOR.services_by_name['FaqGateway'] = _FAQGATEWAY

# @@protoc_insertion_point(module_scope)
