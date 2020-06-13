# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TableService.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import Players_pb2 as Players__pb2
from . import Betting_pb2 as Betting__pb2
from . import Table_pb2 as Table__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TableService.proto',
  package='poker.proto',
  syntax='proto3',
  serialized_options=b'\n\013poker.protoP\001',
  serialized_pb=b'\n\x12TableService.proto\x12\x0bpoker.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\rPlayers.proto\x1a\rBetting.proto\x1a\x0bTable.proto\"Y\n\x16\x41\x64\x64PlayerRequestStatus\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x1a.poker.proto.RequestStatus\x12\x13\n\x0bplayerToken\x18\x02 \x01(\t\"*\n\x13SubscriptionRequest\x12\x13\n\x0bplayerToken\x18\x01 \x01(\t\"G\n\rRequestStatus\x12%\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x17.poker.proto.StatusCode\x12\x0f\n\x07message\x18\x02 \x01(\t\"`\n\nGameUpdate\x12!\n\x05table\x18\x01 \x01(\x0b\x32\x12.poker.proto.Table\x12/\n\nnextAction\x18\x02 \x01(\x0b\x32\x1b.poker.proto.NextActionData\"%\n\rTableSettings\x12\x14\n\x0cjsonSettings\x18\x01 \x01(\t\"!\n\rSimpleMessage\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t\"~\n\x0eNextActionData\x12)\n\x08noAction\x18\x01 \x01(\x0b\x32\x15.poker.proto.NoActionH\x00\x12\x37\n\x0f\x61vailableAction\x18\x02 \x01(\x0b\x32\x1c.poker.proto.AvailableActionH\x00\x42\x08\n\x06\x61\x63tion\"\n\n\x08NoAction\"_\n\x0f\x41vailableAction\x12\x37\n\ractionOptions\x18\x02 \x03(\x0b\x32 .poker.proto.BettingActionOption\x12\x13\n\x0b\x61\x63tionToken\x18\x03 \x01(\t* \n\nStatusCode\x12\x06\n\x02OK\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x32\x88\x04\n\x14\x43\x61shGameTableService\x12@\n\x06\x63reate\x12\x1a.poker.proto.TableSettings\x1a\x1a.poker.proto.RequestStatus\x12H\n\tsubscribe\x12 .poker.proto.SubscriptionRequest\x1a\x17.poker.proto.GameUpdate0\x01\x12;\n\x05start\x12\x16.google.protobuf.Empty\x1a\x1a.poker.proto.RequestStatus\x12:\n\x04stop\x12\x16.google.protobuf.Empty\x1a\x1a.poker.proto.RequestStatus\x12P\n\taddPlayer\x12\x1e.poker.proto.PlayerJoinRequest\x1a#.poker.proto.AddPlayerRequestStatus\x12L\n\x0cremovePlayer\x12 .poker.proto.PlayerRemoveRequest\x1a\x1a.poker.proto.RequestStatus\x12K\n\ntakeAction\x12!.poker.proto.BettingActionRequest\x1a\x1a.poker.proto.RequestStatusB\x0f\n\x0bpoker.protoP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,Players__pb2.DESCRIPTOR,Betting__pb2.DESCRIPTOR,Table__pb2.DESCRIPTOR,])

_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='poker.proto.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=757,
  serialized_end=789,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
OK = 0
FAILED = 1



_ADDPLAYERREQUESTSTATUS = _descriptor.Descriptor(
  name='AddPlayerRequestStatus',
  full_name='poker.proto.AddPlayerRequestStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='poker.proto.AddPlayerRequestStatus.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playerToken', full_name='poker.proto.AddPlayerRequestStatus.playerToken', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=140,
  serialized_end=229,
)


_SUBSCRIPTIONREQUEST = _descriptor.Descriptor(
  name='SubscriptionRequest',
  full_name='poker.proto.SubscriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerToken', full_name='poker.proto.SubscriptionRequest.playerToken', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=231,
  serialized_end=273,
)


_REQUESTSTATUS = _descriptor.Descriptor(
  name='RequestStatus',
  full_name='poker.proto.RequestStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='poker.proto.RequestStatus.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='poker.proto.RequestStatus.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=275,
  serialized_end=346,
)


_GAMEUPDATE = _descriptor.Descriptor(
  name='GameUpdate',
  full_name='poker.proto.GameUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='poker.proto.GameUpdate.table', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nextAction', full_name='poker.proto.GameUpdate.nextAction', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=348,
  serialized_end=444,
)


_TABLESETTINGS = _descriptor.Descriptor(
  name='TableSettings',
  full_name='poker.proto.TableSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jsonSettings', full_name='poker.proto.TableSettings.jsonSettings', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=446,
  serialized_end=483,
)


_SIMPLEMESSAGE = _descriptor.Descriptor(
  name='SimpleMessage',
  full_name='poker.proto.SimpleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents', full_name='poker.proto.SimpleMessage.contents', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=485,
  serialized_end=518,
)


_NEXTACTIONDATA = _descriptor.Descriptor(
  name='NextActionData',
  full_name='poker.proto.NextActionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='noAction', full_name='poker.proto.NextActionData.noAction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='availableAction', full_name='poker.proto.NextActionData.availableAction', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='action', full_name='poker.proto.NextActionData.action',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=520,
  serialized_end=646,
)


_NOACTION = _descriptor.Descriptor(
  name='NoAction',
  full_name='poker.proto.NoAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=648,
  serialized_end=658,
)


_AVAILABLEACTION = _descriptor.Descriptor(
  name='AvailableAction',
  full_name='poker.proto.AvailableAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionOptions', full_name='poker.proto.AvailableAction.actionOptions', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actionToken', full_name='poker.proto.AvailableAction.actionToken', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=660,
  serialized_end=755,
)

_ADDPLAYERREQUESTSTATUS.fields_by_name['status'].message_type = _REQUESTSTATUS
_REQUESTSTATUS.fields_by_name['code'].enum_type = _STATUSCODE
_GAMEUPDATE.fields_by_name['table'].message_type = Table__pb2._TABLE
_GAMEUPDATE.fields_by_name['nextAction'].message_type = _NEXTACTIONDATA
_NEXTACTIONDATA.fields_by_name['noAction'].message_type = _NOACTION
_NEXTACTIONDATA.fields_by_name['availableAction'].message_type = _AVAILABLEACTION
_NEXTACTIONDATA.oneofs_by_name['action'].fields.append(
  _NEXTACTIONDATA.fields_by_name['noAction'])
_NEXTACTIONDATA.fields_by_name['noAction'].containing_oneof = _NEXTACTIONDATA.oneofs_by_name['action']
_NEXTACTIONDATA.oneofs_by_name['action'].fields.append(
  _NEXTACTIONDATA.fields_by_name['availableAction'])
_NEXTACTIONDATA.fields_by_name['availableAction'].containing_oneof = _NEXTACTIONDATA.oneofs_by_name['action']
_AVAILABLEACTION.fields_by_name['actionOptions'].message_type = Betting__pb2._BETTINGACTIONOPTION
DESCRIPTOR.message_types_by_name['AddPlayerRequestStatus'] = _ADDPLAYERREQUESTSTATUS
DESCRIPTOR.message_types_by_name['SubscriptionRequest'] = _SUBSCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['RequestStatus'] = _REQUESTSTATUS
DESCRIPTOR.message_types_by_name['GameUpdate'] = _GAMEUPDATE
DESCRIPTOR.message_types_by_name['TableSettings'] = _TABLESETTINGS
DESCRIPTOR.message_types_by_name['SimpleMessage'] = _SIMPLEMESSAGE
DESCRIPTOR.message_types_by_name['NextActionData'] = _NEXTACTIONDATA
DESCRIPTOR.message_types_by_name['NoAction'] = _NOACTION
DESCRIPTOR.message_types_by_name['AvailableAction'] = _AVAILABLEACTION
DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddPlayerRequestStatus = _reflection.GeneratedProtocolMessageType('AddPlayerRequestStatus', (_message.Message,), {
  'DESCRIPTOR' : _ADDPLAYERREQUESTSTATUS,
  '__module__' : 'TableService_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.AddPlayerRequestStatus)
  })
_sym_db.RegisterMessage(AddPlayerRequestStatus)

SubscriptionRequest = _reflection.GeneratedProtocolMessageType('SubscriptionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONREQUEST,
  '__module__' : 'TableService_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.SubscriptionRequest)
  })
_sym_db.RegisterMessage(SubscriptionRequest)

RequestStatus = _reflection.GeneratedProtocolMessageType('RequestStatus', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSTATUS,
  '__module__' : 'TableService_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.RequestStatus)
  })
_sym_db.RegisterMessage(RequestStatus)

GameUpdate = _reflection.GeneratedProtocolMessageType('GameUpdate', (_message.Message,), {
  'DESCRIPTOR' : _GAMEUPDATE,
  '__module__' : 'TableService_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.GameUpdate)
  })
_sym_db.RegisterMessage(GameUpdate)

TableSettings = _reflection.GeneratedProtocolMessageType('TableSettings', (_message.Message,), {
  'DESCRIPTOR' : _TABLESETTINGS,
  '__module__' : 'TableService_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.TableSettings)
  })
_sym_db.RegisterMessage(TableSettings)

SimpleMessage = _reflection.GeneratedProtocolMessageType('SimpleMessage', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLEMESSAGE,
  '__module__' : 'TableService_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.SimpleMessage)
  })
_sym_db.RegisterMessage(SimpleMessage)

NextActionData = _reflection.GeneratedProtocolMessageType('NextActionData', (_message.Message,), {
  'DESCRIPTOR' : _NEXTACTIONDATA,
  '__module__' : 'TableService_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.NextActionData)
  })
_sym_db.RegisterMessage(NextActionData)

NoAction = _reflection.GeneratedProtocolMessageType('NoAction', (_message.Message,), {
  'DESCRIPTOR' : _NOACTION,
  '__module__' : 'TableService_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.NoAction)
  })
_sym_db.RegisterMessage(NoAction)

AvailableAction = _reflection.GeneratedProtocolMessageType('AvailableAction', (_message.Message,), {
  'DESCRIPTOR' : _AVAILABLEACTION,
  '__module__' : 'TableService_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.AvailableAction)
  })
_sym_db.RegisterMessage(AvailableAction)


DESCRIPTOR._options = None

_CASHGAMETABLESERVICE = _descriptor.ServiceDescriptor(
  name='CashGameTableService',
  full_name='poker.proto.CashGameTableService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=792,
  serialized_end=1312,
  methods=[
  _descriptor.MethodDescriptor(
    name='create',
    full_name='poker.proto.CashGameTableService.create',
    index=0,
    containing_service=None,
    input_type=_TABLESETTINGS,
    output_type=_REQUESTSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='subscribe',
    full_name='poker.proto.CashGameTableService.subscribe',
    index=1,
    containing_service=None,
    input_type=_SUBSCRIPTIONREQUEST,
    output_type=_GAMEUPDATE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='start',
    full_name='poker.proto.CashGameTableService.start',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_REQUESTSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='stop',
    full_name='poker.proto.CashGameTableService.stop',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_REQUESTSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='addPlayer',
    full_name='poker.proto.CashGameTableService.addPlayer',
    index=4,
    containing_service=None,
    input_type=Players__pb2._PLAYERJOINREQUEST,
    output_type=_ADDPLAYERREQUESTSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='removePlayer',
    full_name='poker.proto.CashGameTableService.removePlayer',
    index=5,
    containing_service=None,
    input_type=Players__pb2._PLAYERREMOVEREQUEST,
    output_type=_REQUESTSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='takeAction',
    full_name='poker.proto.CashGameTableService.takeAction',
    index=6,
    containing_service=None,
    input_type=Betting__pb2._BETTINGACTIONREQUEST,
    output_type=_REQUESTSTATUS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CASHGAMETABLESERVICE)

DESCRIPTOR.services_by_name['CashGameTableService'] = _CASHGAMETABLESERVICE

# @@protoc_insertion_point(module_scope)
