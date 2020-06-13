# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Betting.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Betting.proto',
  package='poker.proto',
  syntax='proto3',
  serialized_options=b'\n\013poker.protoP\001',
  serialized_pb=b'\n\rBetting.proto\x12\x0bpoker.proto\"\xd1\x02\n\x10\x42\x65ttingActionLog\x12,\n\x08noAction\x18\x01 \x01(\x0b\x32\x18.poker.proto.NoActionLogH\x00\x12*\n\npostAction\x18\x02 \x01(\x0b\x32\x14.poker.proto.PostLogH\x00\x12*\n\nfoldAction\x18\x03 \x01(\x0b\x32\x14.poker.proto.FoldLogH\x00\x12,\n\x0b\x63heckAction\x18\x04 \x01(\x0b\x32\x15.poker.proto.CheckLogH\x00\x12*\n\ncallAction\x18\x05 \x01(\x0b\x32\x14.poker.proto.CallLogH\x00\x12(\n\tbetAction\x18\x06 \x01(\x0b\x32\x13.poker.proto.BetLogH\x00\x12,\n\x0braiseAction\x18\x07 \x01(\x0b\x32\x15.poker.proto.RaiseLogH\x00\x42\x05\n\x03log\"\r\n\x0bNoActionLog\"\t\n\x07PostLog\"\t\n\x07\x46oldLog\"\n\n\x08\x43heckLog\"\t\n\x07\x43\x61llLog\"\x08\n\x06\x42\x65tLog\"\n\n\x08RaiseLog\"\xa8\x02\n\x14\x42\x65ttingActionRequest\x12\x13\n\x0b\x61\x63tionToken\x18\x01 \x01(\t\x12.\n\nfoldAction\x18\x02 \x01(\x0b\x32\x18.poker.proto.FoldRequestH\x00\x12\x30\n\x0b\x63heckAction\x18\x03 \x01(\x0b\x32\x19.poker.proto.CheckRequestH\x00\x12.\n\ncallAction\x18\x04 \x01(\x0b\x32\x18.poker.proto.CallRequestH\x00\x12,\n\tbetAction\x18\x05 \x01(\x0b\x32\x17.poker.proto.BetRequestH\x00\x12\x30\n\x0braiseAction\x18\x06 \x01(\x0b\x32\x19.poker.proto.RaiseRequestH\x00\x42\t\n\x07request\"\r\n\x0b\x46oldRequest\"\x0e\n\x0c\x43heckRequest\"\r\n\x0b\x43\x61llRequest\"\x1b\n\nBetRequest\x12\r\n\x05\x63hips\x18\x02 \x01(\x05\"\x1d\n\x0cRaiseRequest\x12\r\n\x05\x63hips\x18\x02 \x01(\x05\"\x8c\x02\n\x13\x42\x65ttingActionOption\x12-\n\nfoldOption\x18\x01 \x01(\x0b\x32\x17.poker.proto.FoldOptionH\x00\x12/\n\x0b\x63heckOption\x18\x02 \x01(\x0b\x32\x18.poker.proto.CheckOptionH\x00\x12-\n\ncallOption\x18\x03 \x01(\x0b\x32\x17.poker.proto.CallOptionH\x00\x12+\n\tbetOption\x18\x04 \x01(\x0b\x32\x16.poker.proto.BetOptionH\x00\x12/\n\x0braiseOption\x18\x05 \x01(\x0b\x32\x18.poker.proto.RaiseOptionH\x00\x42\x08\n\x06option\"\x0c\n\nFoldOption\"\r\n\x0b\x43heckOption\"\x0c\n\nCallOption\"\x1b\n\tBetOption\x12\x0e\n\x06minBet\x18\x01 \x01(\x05\"\x1f\n\x0bRaiseOption\x12\x10\n\x08minRaise\x18\x01 \x01(\x05\x42\x0f\n\x0bpoker.protoP\x01\x62\x06proto3'
)




_BETTINGACTIONLOG = _descriptor.Descriptor(
  name='BettingActionLog',
  full_name='poker.proto.BettingActionLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='noAction', full_name='poker.proto.BettingActionLog.noAction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postAction', full_name='poker.proto.BettingActionLog.postAction', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='foldAction', full_name='poker.proto.BettingActionLog.foldAction', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkAction', full_name='poker.proto.BettingActionLog.checkAction', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callAction', full_name='poker.proto.BettingActionLog.callAction', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='betAction', full_name='poker.proto.BettingActionLog.betAction', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raiseAction', full_name='poker.proto.BettingActionLog.raiseAction', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
      name='log', full_name='poker.proto.BettingActionLog.log',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=31,
  serialized_end=368,
)


_NOACTIONLOG = _descriptor.Descriptor(
  name='NoActionLog',
  full_name='poker.proto.NoActionLog',
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
  serialized_start=370,
  serialized_end=383,
)


_POSTLOG = _descriptor.Descriptor(
  name='PostLog',
  full_name='poker.proto.PostLog',
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
  serialized_start=385,
  serialized_end=394,
)


_FOLDLOG = _descriptor.Descriptor(
  name='FoldLog',
  full_name='poker.proto.FoldLog',
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
  serialized_start=396,
  serialized_end=405,
)


_CHECKLOG = _descriptor.Descriptor(
  name='CheckLog',
  full_name='poker.proto.CheckLog',
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
  serialized_start=407,
  serialized_end=417,
)


_CALLLOG = _descriptor.Descriptor(
  name='CallLog',
  full_name='poker.proto.CallLog',
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
  serialized_start=419,
  serialized_end=428,
)


_BETLOG = _descriptor.Descriptor(
  name='BetLog',
  full_name='poker.proto.BetLog',
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
  serialized_start=430,
  serialized_end=438,
)


_RAISELOG = _descriptor.Descriptor(
  name='RaiseLog',
  full_name='poker.proto.RaiseLog',
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
  serialized_start=440,
  serialized_end=450,
)


_BETTINGACTIONREQUEST = _descriptor.Descriptor(
  name='BettingActionRequest',
  full_name='poker.proto.BettingActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionToken', full_name='poker.proto.BettingActionRequest.actionToken', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='foldAction', full_name='poker.proto.BettingActionRequest.foldAction', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkAction', full_name='poker.proto.BettingActionRequest.checkAction', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callAction', full_name='poker.proto.BettingActionRequest.callAction', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='betAction', full_name='poker.proto.BettingActionRequest.betAction', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raiseAction', full_name='poker.proto.BettingActionRequest.raiseAction', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
      name='request', full_name='poker.proto.BettingActionRequest.request',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=453,
  serialized_end=749,
)


_FOLDREQUEST = _descriptor.Descriptor(
  name='FoldRequest',
  full_name='poker.proto.FoldRequest',
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
  serialized_start=751,
  serialized_end=764,
)


_CHECKREQUEST = _descriptor.Descriptor(
  name='CheckRequest',
  full_name='poker.proto.CheckRequest',
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
  serialized_start=766,
  serialized_end=780,
)


_CALLREQUEST = _descriptor.Descriptor(
  name='CallRequest',
  full_name='poker.proto.CallRequest',
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
  serialized_start=782,
  serialized_end=795,
)


_BETREQUEST = _descriptor.Descriptor(
  name='BetRequest',
  full_name='poker.proto.BetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chips', full_name='poker.proto.BetRequest.chips', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=797,
  serialized_end=824,
)


_RAISEREQUEST = _descriptor.Descriptor(
  name='RaiseRequest',
  full_name='poker.proto.RaiseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chips', full_name='poker.proto.RaiseRequest.chips', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=826,
  serialized_end=855,
)


_BETTINGACTIONOPTION = _descriptor.Descriptor(
  name='BettingActionOption',
  full_name='poker.proto.BettingActionOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='foldOption', full_name='poker.proto.BettingActionOption.foldOption', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkOption', full_name='poker.proto.BettingActionOption.checkOption', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callOption', full_name='poker.proto.BettingActionOption.callOption', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='betOption', full_name='poker.proto.BettingActionOption.betOption', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raiseOption', full_name='poker.proto.BettingActionOption.raiseOption', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
      name='option', full_name='poker.proto.BettingActionOption.option',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=858,
  serialized_end=1126,
)


_FOLDOPTION = _descriptor.Descriptor(
  name='FoldOption',
  full_name='poker.proto.FoldOption',
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
  serialized_start=1128,
  serialized_end=1140,
)


_CHECKOPTION = _descriptor.Descriptor(
  name='CheckOption',
  full_name='poker.proto.CheckOption',
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
  serialized_start=1142,
  serialized_end=1155,
)


_CALLOPTION = _descriptor.Descriptor(
  name='CallOption',
  full_name='poker.proto.CallOption',
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
  serialized_start=1157,
  serialized_end=1169,
)


_BETOPTION = _descriptor.Descriptor(
  name='BetOption',
  full_name='poker.proto.BetOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minBet', full_name='poker.proto.BetOption.minBet', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1171,
  serialized_end=1198,
)


_RAISEOPTION = _descriptor.Descriptor(
  name='RaiseOption',
  full_name='poker.proto.RaiseOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minRaise', full_name='poker.proto.RaiseOption.minRaise', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1200,
  serialized_end=1231,
)

_BETTINGACTIONLOG.fields_by_name['noAction'].message_type = _NOACTIONLOG
_BETTINGACTIONLOG.fields_by_name['postAction'].message_type = _POSTLOG
_BETTINGACTIONLOG.fields_by_name['foldAction'].message_type = _FOLDLOG
_BETTINGACTIONLOG.fields_by_name['checkAction'].message_type = _CHECKLOG
_BETTINGACTIONLOG.fields_by_name['callAction'].message_type = _CALLLOG
_BETTINGACTIONLOG.fields_by_name['betAction'].message_type = _BETLOG
_BETTINGACTIONLOG.fields_by_name['raiseAction'].message_type = _RAISELOG
_BETTINGACTIONLOG.oneofs_by_name['log'].fields.append(
  _BETTINGACTIONLOG.fields_by_name['noAction'])
_BETTINGACTIONLOG.fields_by_name['noAction'].containing_oneof = _BETTINGACTIONLOG.oneofs_by_name['log']
_BETTINGACTIONLOG.oneofs_by_name['log'].fields.append(
  _BETTINGACTIONLOG.fields_by_name['postAction'])
_BETTINGACTIONLOG.fields_by_name['postAction'].containing_oneof = _BETTINGACTIONLOG.oneofs_by_name['log']
_BETTINGACTIONLOG.oneofs_by_name['log'].fields.append(
  _BETTINGACTIONLOG.fields_by_name['foldAction'])
_BETTINGACTIONLOG.fields_by_name['foldAction'].containing_oneof = _BETTINGACTIONLOG.oneofs_by_name['log']
_BETTINGACTIONLOG.oneofs_by_name['log'].fields.append(
  _BETTINGACTIONLOG.fields_by_name['checkAction'])
_BETTINGACTIONLOG.fields_by_name['checkAction'].containing_oneof = _BETTINGACTIONLOG.oneofs_by_name['log']
_BETTINGACTIONLOG.oneofs_by_name['log'].fields.append(
  _BETTINGACTIONLOG.fields_by_name['callAction'])
_BETTINGACTIONLOG.fields_by_name['callAction'].containing_oneof = _BETTINGACTIONLOG.oneofs_by_name['log']
_BETTINGACTIONLOG.oneofs_by_name['log'].fields.append(
  _BETTINGACTIONLOG.fields_by_name['betAction'])
_BETTINGACTIONLOG.fields_by_name['betAction'].containing_oneof = _BETTINGACTIONLOG.oneofs_by_name['log']
_BETTINGACTIONLOG.oneofs_by_name['log'].fields.append(
  _BETTINGACTIONLOG.fields_by_name['raiseAction'])
_BETTINGACTIONLOG.fields_by_name['raiseAction'].containing_oneof = _BETTINGACTIONLOG.oneofs_by_name['log']
_BETTINGACTIONREQUEST.fields_by_name['foldAction'].message_type = _FOLDREQUEST
_BETTINGACTIONREQUEST.fields_by_name['checkAction'].message_type = _CHECKREQUEST
_BETTINGACTIONREQUEST.fields_by_name['callAction'].message_type = _CALLREQUEST
_BETTINGACTIONREQUEST.fields_by_name['betAction'].message_type = _BETREQUEST
_BETTINGACTIONREQUEST.fields_by_name['raiseAction'].message_type = _RAISEREQUEST
_BETTINGACTIONREQUEST.oneofs_by_name['request'].fields.append(
  _BETTINGACTIONREQUEST.fields_by_name['foldAction'])
_BETTINGACTIONREQUEST.fields_by_name['foldAction'].containing_oneof = _BETTINGACTIONREQUEST.oneofs_by_name['request']
_BETTINGACTIONREQUEST.oneofs_by_name['request'].fields.append(
  _BETTINGACTIONREQUEST.fields_by_name['checkAction'])
_BETTINGACTIONREQUEST.fields_by_name['checkAction'].containing_oneof = _BETTINGACTIONREQUEST.oneofs_by_name['request']
_BETTINGACTIONREQUEST.oneofs_by_name['request'].fields.append(
  _BETTINGACTIONREQUEST.fields_by_name['callAction'])
_BETTINGACTIONREQUEST.fields_by_name['callAction'].containing_oneof = _BETTINGACTIONREQUEST.oneofs_by_name['request']
_BETTINGACTIONREQUEST.oneofs_by_name['request'].fields.append(
  _BETTINGACTIONREQUEST.fields_by_name['betAction'])
_BETTINGACTIONREQUEST.fields_by_name['betAction'].containing_oneof = _BETTINGACTIONREQUEST.oneofs_by_name['request']
_BETTINGACTIONREQUEST.oneofs_by_name['request'].fields.append(
  _BETTINGACTIONREQUEST.fields_by_name['raiseAction'])
_BETTINGACTIONREQUEST.fields_by_name['raiseAction'].containing_oneof = _BETTINGACTIONREQUEST.oneofs_by_name['request']
_BETTINGACTIONOPTION.fields_by_name['foldOption'].message_type = _FOLDOPTION
_BETTINGACTIONOPTION.fields_by_name['checkOption'].message_type = _CHECKOPTION
_BETTINGACTIONOPTION.fields_by_name['callOption'].message_type = _CALLOPTION
_BETTINGACTIONOPTION.fields_by_name['betOption'].message_type = _BETOPTION
_BETTINGACTIONOPTION.fields_by_name['raiseOption'].message_type = _RAISEOPTION
_BETTINGACTIONOPTION.oneofs_by_name['option'].fields.append(
  _BETTINGACTIONOPTION.fields_by_name['foldOption'])
_BETTINGACTIONOPTION.fields_by_name['foldOption'].containing_oneof = _BETTINGACTIONOPTION.oneofs_by_name['option']
_BETTINGACTIONOPTION.oneofs_by_name['option'].fields.append(
  _BETTINGACTIONOPTION.fields_by_name['checkOption'])
_BETTINGACTIONOPTION.fields_by_name['checkOption'].containing_oneof = _BETTINGACTIONOPTION.oneofs_by_name['option']
_BETTINGACTIONOPTION.oneofs_by_name['option'].fields.append(
  _BETTINGACTIONOPTION.fields_by_name['callOption'])
_BETTINGACTIONOPTION.fields_by_name['callOption'].containing_oneof = _BETTINGACTIONOPTION.oneofs_by_name['option']
_BETTINGACTIONOPTION.oneofs_by_name['option'].fields.append(
  _BETTINGACTIONOPTION.fields_by_name['betOption'])
_BETTINGACTIONOPTION.fields_by_name['betOption'].containing_oneof = _BETTINGACTIONOPTION.oneofs_by_name['option']
_BETTINGACTIONOPTION.oneofs_by_name['option'].fields.append(
  _BETTINGACTIONOPTION.fields_by_name['raiseOption'])
_BETTINGACTIONOPTION.fields_by_name['raiseOption'].containing_oneof = _BETTINGACTIONOPTION.oneofs_by_name['option']
DESCRIPTOR.message_types_by_name['BettingActionLog'] = _BETTINGACTIONLOG
DESCRIPTOR.message_types_by_name['NoActionLog'] = _NOACTIONLOG
DESCRIPTOR.message_types_by_name['PostLog'] = _POSTLOG
DESCRIPTOR.message_types_by_name['FoldLog'] = _FOLDLOG
DESCRIPTOR.message_types_by_name['CheckLog'] = _CHECKLOG
DESCRIPTOR.message_types_by_name['CallLog'] = _CALLLOG
DESCRIPTOR.message_types_by_name['BetLog'] = _BETLOG
DESCRIPTOR.message_types_by_name['RaiseLog'] = _RAISELOG
DESCRIPTOR.message_types_by_name['BettingActionRequest'] = _BETTINGACTIONREQUEST
DESCRIPTOR.message_types_by_name['FoldRequest'] = _FOLDREQUEST
DESCRIPTOR.message_types_by_name['CheckRequest'] = _CHECKREQUEST
DESCRIPTOR.message_types_by_name['CallRequest'] = _CALLREQUEST
DESCRIPTOR.message_types_by_name['BetRequest'] = _BETREQUEST
DESCRIPTOR.message_types_by_name['RaiseRequest'] = _RAISEREQUEST
DESCRIPTOR.message_types_by_name['BettingActionOption'] = _BETTINGACTIONOPTION
DESCRIPTOR.message_types_by_name['FoldOption'] = _FOLDOPTION
DESCRIPTOR.message_types_by_name['CheckOption'] = _CHECKOPTION
DESCRIPTOR.message_types_by_name['CallOption'] = _CALLOPTION
DESCRIPTOR.message_types_by_name['BetOption'] = _BETOPTION
DESCRIPTOR.message_types_by_name['RaiseOption'] = _RAISEOPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BettingActionLog = _reflection.GeneratedProtocolMessageType('BettingActionLog', (_message.Message,), {
  'DESCRIPTOR' : _BETTINGACTIONLOG,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.BettingActionLog)
  })
_sym_db.RegisterMessage(BettingActionLog)

NoActionLog = _reflection.GeneratedProtocolMessageType('NoActionLog', (_message.Message,), {
  'DESCRIPTOR' : _NOACTIONLOG,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.NoActionLog)
  })
_sym_db.RegisterMessage(NoActionLog)

PostLog = _reflection.GeneratedProtocolMessageType('PostLog', (_message.Message,), {
  'DESCRIPTOR' : _POSTLOG,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.PostLog)
  })
_sym_db.RegisterMessage(PostLog)

FoldLog = _reflection.GeneratedProtocolMessageType('FoldLog', (_message.Message,), {
  'DESCRIPTOR' : _FOLDLOG,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.FoldLog)
  })
_sym_db.RegisterMessage(FoldLog)

CheckLog = _reflection.GeneratedProtocolMessageType('CheckLog', (_message.Message,), {
  'DESCRIPTOR' : _CHECKLOG,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.CheckLog)
  })
_sym_db.RegisterMessage(CheckLog)

CallLog = _reflection.GeneratedProtocolMessageType('CallLog', (_message.Message,), {
  'DESCRIPTOR' : _CALLLOG,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.CallLog)
  })
_sym_db.RegisterMessage(CallLog)

BetLog = _reflection.GeneratedProtocolMessageType('BetLog', (_message.Message,), {
  'DESCRIPTOR' : _BETLOG,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.BetLog)
  })
_sym_db.RegisterMessage(BetLog)

RaiseLog = _reflection.GeneratedProtocolMessageType('RaiseLog', (_message.Message,), {
  'DESCRIPTOR' : _RAISELOG,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.RaiseLog)
  })
_sym_db.RegisterMessage(RaiseLog)

BettingActionRequest = _reflection.GeneratedProtocolMessageType('BettingActionRequest', (_message.Message,), {
  'DESCRIPTOR' : _BETTINGACTIONREQUEST,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.BettingActionRequest)
  })
_sym_db.RegisterMessage(BettingActionRequest)

FoldRequest = _reflection.GeneratedProtocolMessageType('FoldRequest', (_message.Message,), {
  'DESCRIPTOR' : _FOLDREQUEST,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.FoldRequest)
  })
_sym_db.RegisterMessage(FoldRequest)

CheckRequest = _reflection.GeneratedProtocolMessageType('CheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKREQUEST,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.CheckRequest)
  })
_sym_db.RegisterMessage(CheckRequest)

CallRequest = _reflection.GeneratedProtocolMessageType('CallRequest', (_message.Message,), {
  'DESCRIPTOR' : _CALLREQUEST,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.CallRequest)
  })
_sym_db.RegisterMessage(CallRequest)

BetRequest = _reflection.GeneratedProtocolMessageType('BetRequest', (_message.Message,), {
  'DESCRIPTOR' : _BETREQUEST,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.BetRequest)
  })
_sym_db.RegisterMessage(BetRequest)

RaiseRequest = _reflection.GeneratedProtocolMessageType('RaiseRequest', (_message.Message,), {
  'DESCRIPTOR' : _RAISEREQUEST,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.RaiseRequest)
  })
_sym_db.RegisterMessage(RaiseRequest)

BettingActionOption = _reflection.GeneratedProtocolMessageType('BettingActionOption', (_message.Message,), {
  'DESCRIPTOR' : _BETTINGACTIONOPTION,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.BettingActionOption)
  })
_sym_db.RegisterMessage(BettingActionOption)

FoldOption = _reflection.GeneratedProtocolMessageType('FoldOption', (_message.Message,), {
  'DESCRIPTOR' : _FOLDOPTION,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.FoldOption)
  })
_sym_db.RegisterMessage(FoldOption)

CheckOption = _reflection.GeneratedProtocolMessageType('CheckOption', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOPTION,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.CheckOption)
  })
_sym_db.RegisterMessage(CheckOption)

CallOption = _reflection.GeneratedProtocolMessageType('CallOption', (_message.Message,), {
  'DESCRIPTOR' : _CALLOPTION,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.CallOption)
  })
_sym_db.RegisterMessage(CallOption)

BetOption = _reflection.GeneratedProtocolMessageType('BetOption', (_message.Message,), {
  'DESCRIPTOR' : _BETOPTION,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.BetOption)
  })
_sym_db.RegisterMessage(BetOption)

RaiseOption = _reflection.GeneratedProtocolMessageType('RaiseOption', (_message.Message,), {
  'DESCRIPTOR' : _RAISEOPTION,
  '__module__' : 'Betting_pb2'
  # @@protoc_insertion_point(class_scope:poker.proto.RaiseOption)
  })
_sym_db.RegisterMessage(RaiseOption)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
