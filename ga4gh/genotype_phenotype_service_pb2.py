# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/genotype_phenotype_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh import common_pb2 as ga4gh_dot_common__pb2
from ga4gh import metadata_pb2 as ga4gh_dot_metadata__pb2
from ga4gh import genotype_phenotype_pb2 as ga4gh_dot_genotype__phenotype__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/genotype_phenotype_service.proto',
  package='ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n&ga4gh/genotype_phenotype_service.proto\x12\x05ga4gh\x1a\x12ga4gh/common.proto\x1a\x14ga4gh/metadata.proto\x1a\x1ega4gh/genotype_phenotype.proto\"b\n%SearchPhenotypeAssociationSetsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"\x85\x01\n&SearchPhenotypeAssociationSetsResponse\x12\x42\n\x1aphenotype_association_sets\x18\x01 \x03(\x0b\x32\x1e.ga4gh.PhenotypeAssociationSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"7\n\x11OntologyTermQuery\x12\"\n\x05terms\x18\x01 \x03(\x0b\x32\x13.ga4gh.OntologyTerm\"A\n\x17\x45xternalIdentifierQuery\x12&\n\x03ids\x18\x01 \x03(\x0b\x32\x19.ga4gh.ExternalIdentifier\"\x88\x01\n\rEvidenceQuery\x12)\n\x0c\x65videnceType\x18\x01 \x01(\x0b\x32\x13.ga4gh.OntologyTerm\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x37\n\x14\x65xternal_identifiers\x18\x03 \x03(\x0b\x32\x19.ga4gh.ExternalIdentifier\"\xfe\x01\n\x17SearchPhenotypesRequest\x12$\n\x1cphenotype_association_set_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12!\n\x04type\x18\x04 \x01(\x0b\x32\x13.ga4gh.OntologyTerm\x12\'\n\nqualifiers\x18\x05 \x03(\x0b\x32\x13.ga4gh.OntologyTerm\x12)\n\x0c\x61ge_of_onset\x18\x06 \x01(\x0b\x32\x13.ga4gh.OntologyTerm\x12\x11\n\tpage_size\x18\x07 \x01(\x03\x12\x12\n\npage_token\x18\x08 \x01(\t\"a\n\x18SearchPhenotypesResponse\x12,\n\nphenotypes\x18\x01 \x03(\x0b\x32\x18.ga4gh.PhenotypeInstance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xc1\x01\n\x1eSearchGenotypePhenotypeRequest\x12$\n\x1cphenotype_association_set_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66\x65\x61ture_ids\x18\x02 \x03(\t\x12\x15\n\rphenotype_ids\x18\x03 \x03(\t\x12&\n\x08\x65vidence\x18\x04 \x03(\x0b\x32\x14.ga4gh.EvidenceQuery\x12\x11\n\tpage_size\x18\x05 \x01(\x03\x12\x12\n\npage_token\x18\x06 \x01(\t\"t\n\x1fSearchGenotypePhenotypeResponse\x12\x38\n\x0c\x61ssociations\x18\x01 \x03(\x0b\x32\".ga4gh.FeaturePhenotypeAssociation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd8\x02\n\x18GenotypePhenotypeService\x12}\n\x1eSearchPhenotypeAssociationSets\x12,.ga4gh.SearchPhenotypeAssociationSetsRequest\x1a-.ga4gh.SearchPhenotypeAssociationSetsResponse\x12R\n\x0fSearchPhenotype\x12\x1e.ga4gh.SearchPhenotypesRequest\x1a\x1f.ga4gh.SearchPhenotypesResponse\x12i\n\x18GetPhenotypeAssociations\x12%.ga4gh.SearchGenotypePhenotypeRequest\x1a&.ga4gh.SearchGenotypePhenotypeResponseb\x06proto3')
  ,
  dependencies=[ga4gh_dot_common__pb2.DESCRIPTOR,ga4gh_dot_metadata__pb2.DESCRIPTOR,ga4gh_dot_genotype__phenotype__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEARCHPHENOTYPEASSOCIATIONSETSREQUEST = _descriptor.Descriptor(
  name='SearchPhenotypeAssociationSetsRequest',
  full_name='ga4gh.SearchPhenotypeAssociationSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.SearchPhenotypeAssociationSetsRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchPhenotypeAssociationSetsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchPhenotypeAssociationSetsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=123,
  serialized_end=221,
)


_SEARCHPHENOTYPEASSOCIATIONSETSRESPONSE = _descriptor.Descriptor(
  name='SearchPhenotypeAssociationSetsResponse',
  full_name='ga4gh.SearchPhenotypeAssociationSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phenotype_association_sets', full_name='ga4gh.SearchPhenotypeAssociationSetsResponse.phenotype_association_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchPhenotypeAssociationSetsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=224,
  serialized_end=357,
)


_ONTOLOGYTERMQUERY = _descriptor.Descriptor(
  name='OntologyTermQuery',
  full_name='ga4gh.OntologyTermQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='terms', full_name='ga4gh.OntologyTermQuery.terms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=359,
  serialized_end=414,
)


_EXTERNALIDENTIFIERQUERY = _descriptor.Descriptor(
  name='ExternalIdentifierQuery',
  full_name='ga4gh.ExternalIdentifierQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='ga4gh.ExternalIdentifierQuery.ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=416,
  serialized_end=481,
)


_EVIDENCEQUERY = _descriptor.Descriptor(
  name='EvidenceQuery',
  full_name='ga4gh.EvidenceQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='evidenceType', full_name='ga4gh.EvidenceQuery.evidenceType', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ga4gh.EvidenceQuery.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_identifiers', full_name='ga4gh.EvidenceQuery.external_identifiers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=484,
  serialized_end=620,
)


_SEARCHPHENOTYPESREQUEST = _descriptor.Descriptor(
  name='SearchPhenotypesRequest',
  full_name='ga4gh.SearchPhenotypesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phenotype_association_set_id', full_name='ga4gh.SearchPhenotypesRequest.phenotype_association_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.SearchPhenotypesRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ga4gh.SearchPhenotypesRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='ga4gh.SearchPhenotypesRequest.type', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qualifiers', full_name='ga4gh.SearchPhenotypesRequest.qualifiers', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='age_of_onset', full_name='ga4gh.SearchPhenotypesRequest.age_of_onset', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchPhenotypesRequest.page_size', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchPhenotypesRequest.page_token', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=623,
  serialized_end=877,
)


_SEARCHPHENOTYPESRESPONSE = _descriptor.Descriptor(
  name='SearchPhenotypesResponse',
  full_name='ga4gh.SearchPhenotypesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phenotypes', full_name='ga4gh.SearchPhenotypesResponse.phenotypes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchPhenotypesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=879,
  serialized_end=976,
)


_SEARCHGENOTYPEPHENOTYPEREQUEST = _descriptor.Descriptor(
  name='SearchGenotypePhenotypeRequest',
  full_name='ga4gh.SearchGenotypePhenotypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phenotype_association_set_id', full_name='ga4gh.SearchGenotypePhenotypeRequest.phenotype_association_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_ids', full_name='ga4gh.SearchGenotypePhenotypeRequest.feature_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phenotype_ids', full_name='ga4gh.SearchGenotypePhenotypeRequest.phenotype_ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evidence', full_name='ga4gh.SearchGenotypePhenotypeRequest.evidence', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchGenotypePhenotypeRequest.page_size', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchGenotypePhenotypeRequest.page_token', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=979,
  serialized_end=1172,
)


_SEARCHGENOTYPEPHENOTYPERESPONSE = _descriptor.Descriptor(
  name='SearchGenotypePhenotypeResponse',
  full_name='ga4gh.SearchGenotypePhenotypeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='associations', full_name='ga4gh.SearchGenotypePhenotypeResponse.associations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchGenotypePhenotypeResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1174,
  serialized_end=1290,
)

_SEARCHPHENOTYPEASSOCIATIONSETSRESPONSE.fields_by_name['phenotype_association_sets'].message_type = ga4gh_dot_genotype__phenotype__pb2._PHENOTYPEASSOCIATIONSET
_ONTOLOGYTERMQUERY.fields_by_name['terms'].message_type = ga4gh_dot_metadata__pb2._ONTOLOGYTERM
_EXTERNALIDENTIFIERQUERY.fields_by_name['ids'].message_type = ga4gh_dot_common__pb2._EXTERNALIDENTIFIER
_EVIDENCEQUERY.fields_by_name['evidenceType'].message_type = ga4gh_dot_metadata__pb2._ONTOLOGYTERM
_EVIDENCEQUERY.fields_by_name['external_identifiers'].message_type = ga4gh_dot_common__pb2._EXTERNALIDENTIFIER
_SEARCHPHENOTYPESREQUEST.fields_by_name['type'].message_type = ga4gh_dot_metadata__pb2._ONTOLOGYTERM
_SEARCHPHENOTYPESREQUEST.fields_by_name['qualifiers'].message_type = ga4gh_dot_metadata__pb2._ONTOLOGYTERM
_SEARCHPHENOTYPESREQUEST.fields_by_name['age_of_onset'].message_type = ga4gh_dot_metadata__pb2._ONTOLOGYTERM
_SEARCHPHENOTYPESRESPONSE.fields_by_name['phenotypes'].message_type = ga4gh_dot_genotype__phenotype__pb2._PHENOTYPEINSTANCE
_SEARCHGENOTYPEPHENOTYPEREQUEST.fields_by_name['evidence'].message_type = _EVIDENCEQUERY
_SEARCHGENOTYPEPHENOTYPERESPONSE.fields_by_name['associations'].message_type = ga4gh_dot_genotype__phenotype__pb2._FEATUREPHENOTYPEASSOCIATION
DESCRIPTOR.message_types_by_name['SearchPhenotypeAssociationSetsRequest'] = _SEARCHPHENOTYPEASSOCIATIONSETSREQUEST
DESCRIPTOR.message_types_by_name['SearchPhenotypeAssociationSetsResponse'] = _SEARCHPHENOTYPEASSOCIATIONSETSRESPONSE
DESCRIPTOR.message_types_by_name['OntologyTermQuery'] = _ONTOLOGYTERMQUERY
DESCRIPTOR.message_types_by_name['ExternalIdentifierQuery'] = _EXTERNALIDENTIFIERQUERY
DESCRIPTOR.message_types_by_name['EvidenceQuery'] = _EVIDENCEQUERY
DESCRIPTOR.message_types_by_name['SearchPhenotypesRequest'] = _SEARCHPHENOTYPESREQUEST
DESCRIPTOR.message_types_by_name['SearchPhenotypesResponse'] = _SEARCHPHENOTYPESRESPONSE
DESCRIPTOR.message_types_by_name['SearchGenotypePhenotypeRequest'] = _SEARCHGENOTYPEPHENOTYPEREQUEST
DESCRIPTOR.message_types_by_name['SearchGenotypePhenotypeResponse'] = _SEARCHGENOTYPEPHENOTYPERESPONSE

SearchPhenotypeAssociationSetsRequest = _reflection.GeneratedProtocolMessageType('SearchPhenotypeAssociationSetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHPHENOTYPEASSOCIATIONSETSREQUEST,
  __module__ = 'ga4gh.genotype_phenotype_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchPhenotypeAssociationSetsRequest)
  ))
_sym_db.RegisterMessage(SearchPhenotypeAssociationSetsRequest)

SearchPhenotypeAssociationSetsResponse = _reflection.GeneratedProtocolMessageType('SearchPhenotypeAssociationSetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHPHENOTYPEASSOCIATIONSETSRESPONSE,
  __module__ = 'ga4gh.genotype_phenotype_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchPhenotypeAssociationSetsResponse)
  ))
_sym_db.RegisterMessage(SearchPhenotypeAssociationSetsResponse)

OntologyTermQuery = _reflection.GeneratedProtocolMessageType('OntologyTermQuery', (_message.Message,), dict(
  DESCRIPTOR = _ONTOLOGYTERMQUERY,
  __module__ = 'ga4gh.genotype_phenotype_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.OntologyTermQuery)
  ))
_sym_db.RegisterMessage(OntologyTermQuery)

ExternalIdentifierQuery = _reflection.GeneratedProtocolMessageType('ExternalIdentifierQuery', (_message.Message,), dict(
  DESCRIPTOR = _EXTERNALIDENTIFIERQUERY,
  __module__ = 'ga4gh.genotype_phenotype_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.ExternalIdentifierQuery)
  ))
_sym_db.RegisterMessage(ExternalIdentifierQuery)

EvidenceQuery = _reflection.GeneratedProtocolMessageType('EvidenceQuery', (_message.Message,), dict(
  DESCRIPTOR = _EVIDENCEQUERY,
  __module__ = 'ga4gh.genotype_phenotype_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.EvidenceQuery)
  ))
_sym_db.RegisterMessage(EvidenceQuery)

SearchPhenotypesRequest = _reflection.GeneratedProtocolMessageType('SearchPhenotypesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHPHENOTYPESREQUEST,
  __module__ = 'ga4gh.genotype_phenotype_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchPhenotypesRequest)
  ))
_sym_db.RegisterMessage(SearchPhenotypesRequest)

SearchPhenotypesResponse = _reflection.GeneratedProtocolMessageType('SearchPhenotypesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHPHENOTYPESRESPONSE,
  __module__ = 'ga4gh.genotype_phenotype_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchPhenotypesResponse)
  ))
_sym_db.RegisterMessage(SearchPhenotypesResponse)

SearchGenotypePhenotypeRequest = _reflection.GeneratedProtocolMessageType('SearchGenotypePhenotypeRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHGENOTYPEPHENOTYPEREQUEST,
  __module__ = 'ga4gh.genotype_phenotype_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchGenotypePhenotypeRequest)
  ))
_sym_db.RegisterMessage(SearchGenotypePhenotypeRequest)

SearchGenotypePhenotypeResponse = _reflection.GeneratedProtocolMessageType('SearchGenotypePhenotypeResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHGENOTYPEPHENOTYPERESPONSE,
  __module__ = 'ga4gh.genotype_phenotype_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchGenotypePhenotypeResponse)
  ))
_sym_db.RegisterMessage(SearchGenotypePhenotypeResponse)


# @@protoc_insertion_point(module_scope)
