#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/commands.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from pyspark.sql.connect.proto import common_pb2 as spark_dot_connect_dot_common__pb2
from pyspark.sql.connect.proto import expressions_pb2 as spark_dot_connect_dot_expressions__pb2
from pyspark.sql.connect.proto import relations_pb2 as spark_dot_connect_dot_relations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cspark/connect/commands.proto\x12\rspark.connect\x1a\x19google/protobuf/any.proto\x1a\x1aspark/connect/common.proto\x1a\x1fspark/connect/expressions.proto\x1a\x1dspark/connect/relations.proto"\xf5\x07\n\x07\x43ommand\x12]\n\x11register_function\x18\x01 \x01(\x0b\x32..spark.connect.CommonInlineUserDefinedFunctionH\x00R\x10registerFunction\x12H\n\x0fwrite_operation\x18\x02 \x01(\x0b\x32\x1d.spark.connect.WriteOperationH\x00R\x0ewriteOperation\x12_\n\x15\x63reate_dataframe_view\x18\x03 \x01(\x0b\x32).spark.connect.CreateDataFrameViewCommandH\x00R\x13\x63reateDataframeView\x12O\n\x12write_operation_v2\x18\x04 \x01(\x0b\x32\x1f.spark.connect.WriteOperationV2H\x00R\x10writeOperationV2\x12<\n\x0bsql_command\x18\x05 \x01(\x0b\x32\x19.spark.connect.SqlCommandH\x00R\nsqlCommand\x12k\n\x1cwrite_stream_operation_start\x18\x06 \x01(\x0b\x32(.spark.connect.WriteStreamOperationStartH\x00R\x19writeStreamOperationStart\x12^\n\x17streaming_query_command\x18\x07 \x01(\x0b\x32$.spark.connect.StreamingQueryCommandH\x00R\x15streamingQueryCommand\x12X\n\x15get_resources_command\x18\x08 \x01(\x0b\x32".spark.connect.GetResourcesCommandH\x00R\x13getResourcesCommand\x12t\n\x1fstreaming_query_manager_command\x18\t \x01(\x0b\x32+.spark.connect.StreamingQueryManagerCommandH\x00R\x1cstreamingQueryManagerCommand\x12m\n\x17register_table_function\x18\n \x01(\x0b\x32\x33.spark.connect.CommonInlineUserDefinedTableFunctionH\x00R\x15registerTableFunction\x12\x35\n\textension\x18\xe7\x07 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00R\textensionB\x0e\n\x0c\x63ommand_type"\xef\x03\n\nSqlCommand\x12\x10\n\x03sql\x18\x01 \x01(\tR\x03sql\x12;\n\x04\x61rgs\x18\x02 \x03(\x0b\x32#.spark.connect.SqlCommand.ArgsEntryB\x02\x18\x01R\x04\x61rgs\x12@\n\x08pos_args\x18\x03 \x03(\x0b\x32!.spark.connect.Expression.LiteralB\x02\x18\x01R\x07posArgs\x12V\n\x0fnamed_arguments\x18\x04 \x03(\x0b\x32-.spark.connect.SqlCommand.NamedArgumentsEntryR\x0enamedArguments\x12>\n\rpos_arguments\x18\x05 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x0cposArguments\x1aZ\n\tArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x05value:\x02\x38\x01\x1a\\\n\x13NamedArgumentsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12/\n\x05value\x18\x02 \x01(\x0b\x32\x19.spark.connect.ExpressionR\x05value:\x02\x38\x01"\x96\x01\n\x1a\x43reateDataFrameViewCommand\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1b\n\tis_global\x18\x03 \x01(\x08R\x08isGlobal\x12\x18\n\x07replace\x18\x04 \x01(\x08R\x07replace"\x9b\x08\n\x0eWriteOperation\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x1b\n\x06source\x18\x02 \x01(\tH\x01R\x06source\x88\x01\x01\x12\x14\n\x04path\x18\x03 \x01(\tH\x00R\x04path\x12?\n\x05table\x18\x04 \x01(\x0b\x32\'.spark.connect.WriteOperation.SaveTableH\x00R\x05table\x12:\n\x04mode\x18\x05 \x01(\x0e\x32&.spark.connect.WriteOperation.SaveModeR\x04mode\x12*\n\x11sort_column_names\x18\x06 \x03(\tR\x0fsortColumnNames\x12\x31\n\x14partitioning_columns\x18\x07 \x03(\tR\x13partitioningColumns\x12\x43\n\tbucket_by\x18\x08 \x01(\x0b\x32&.spark.connect.WriteOperation.BucketByR\x08\x62ucketBy\x12\x44\n\x07options\x18\t \x03(\x0b\x32*.spark.connect.WriteOperation.OptionsEntryR\x07options\x1a:\n\x0cOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x82\x02\n\tSaveTable\x12\x1d\n\ntable_name\x18\x01 \x01(\tR\ttableName\x12X\n\x0bsave_method\x18\x02 \x01(\x0e\x32\x37.spark.connect.WriteOperation.SaveTable.TableSaveMethodR\nsaveMethod"|\n\x0fTableSaveMethod\x12!\n\x1dTABLE_SAVE_METHOD_UNSPECIFIED\x10\x00\x12#\n\x1fTABLE_SAVE_METHOD_SAVE_AS_TABLE\x10\x01\x12!\n\x1dTABLE_SAVE_METHOD_INSERT_INTO\x10\x02\x1a[\n\x08\x42ucketBy\x12.\n\x13\x62ucket_column_names\x18\x01 \x03(\tR\x11\x62ucketColumnNames\x12\x1f\n\x0bnum_buckets\x18\x02 \x01(\x05R\nnumBuckets"\x89\x01\n\x08SaveMode\x12\x19\n\x15SAVE_MODE_UNSPECIFIED\x10\x00\x12\x14\n\x10SAVE_MODE_APPEND\x10\x01\x12\x17\n\x13SAVE_MODE_OVERWRITE\x10\x02\x12\x1d\n\x19SAVE_MODE_ERROR_IF_EXISTS\x10\x03\x12\x14\n\x10SAVE_MODE_IGNORE\x10\x04\x42\x0b\n\tsave_typeB\t\n\x07_source"\xad\x06\n\x10WriteOperationV2\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x1d\n\ntable_name\x18\x02 \x01(\tR\ttableName\x12\x1f\n\x08provider\x18\x03 \x01(\tH\x00R\x08provider\x88\x01\x01\x12L\n\x14partitioning_columns\x18\x04 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x13partitioningColumns\x12\x46\n\x07options\x18\x05 \x03(\x0b\x32,.spark.connect.WriteOperationV2.OptionsEntryR\x07options\x12_\n\x10table_properties\x18\x06 \x03(\x0b\x32\x34.spark.connect.WriteOperationV2.TablePropertiesEntryR\x0ftableProperties\x12\x38\n\x04mode\x18\x07 \x01(\x0e\x32$.spark.connect.WriteOperationV2.ModeR\x04mode\x12J\n\x13overwrite_condition\x18\x08 \x01(\x0b\x32\x19.spark.connect.ExpressionR\x12overwriteCondition\x1a:\n\x0cOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x42\n\x14TablePropertiesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"\x9f\x01\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMODE_CREATE\x10\x01\x12\x12\n\x0eMODE_OVERWRITE\x10\x02\x12\x1d\n\x19MODE_OVERWRITE_PARTITIONS\x10\x03\x12\x0f\n\x0bMODE_APPEND\x10\x04\x12\x10\n\x0cMODE_REPLACE\x10\x05\x12\x1a\n\x16MODE_CREATE_OR_REPLACE\x10\x06\x42\x0b\n\t_provider"\xa0\x06\n\x19WriteStreamOperationStart\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x16\n\x06\x66ormat\x18\x02 \x01(\tR\x06\x66ormat\x12O\n\x07options\x18\x03 \x03(\x0b\x32\x35.spark.connect.WriteStreamOperationStart.OptionsEntryR\x07options\x12:\n\x19partitioning_column_names\x18\x04 \x03(\tR\x17partitioningColumnNames\x12:\n\x18processing_time_interval\x18\x05 \x01(\tH\x00R\x16processingTimeInterval\x12%\n\ravailable_now\x18\x06 \x01(\x08H\x00R\x0c\x61vailableNow\x12\x14\n\x04once\x18\x07 \x01(\x08H\x00R\x04once\x12\x46\n\x1e\x63ontinuous_checkpoint_interval\x18\x08 \x01(\tH\x00R\x1c\x63ontinuousCheckpointInterval\x12\x1f\n\x0boutput_mode\x18\t \x01(\tR\noutputMode\x12\x1d\n\nquery_name\x18\n \x01(\tR\tqueryName\x12\x14\n\x04path\x18\x0b \x01(\tH\x01R\x04path\x12\x1f\n\ntable_name\x18\x0c \x01(\tH\x01R\ttableName\x12N\n\x0e\x66oreach_writer\x18\r \x01(\x0b\x32\'.spark.connect.StreamingForeachFunctionR\rforeachWriter\x12L\n\rforeach_batch\x18\x0e \x01(\x0b\x32\'.spark.connect.StreamingForeachFunctionR\x0c\x66oreachBatch\x1a:\n\x0cOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\t\n\x07triggerB\x12\n\x10sink_destination"\xb3\x01\n\x18StreamingForeachFunction\x12\x43\n\x0fpython_function\x18\x01 \x01(\x0b\x32\x18.spark.connect.PythonUDFH\x00R\x0epythonFunction\x12\x46\n\x0escala_function\x18\x02 \x01(\x0b\x32\x1d.spark.connect.ScalarScalaUDFH\x00R\rscalaFunctionB\n\n\x08\x66unction"y\n\x1fWriteStreamOperationStartResult\x12\x42\n\x08query_id\x18\x01 \x01(\x0b\x32\'.spark.connect.StreamingQueryInstanceIdR\x07queryId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name"A\n\x18StreamingQueryInstanceId\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06run_id\x18\x02 \x01(\tR\x05runId"\xf8\x04\n\x15StreamingQueryCommand\x12\x42\n\x08query_id\x18\x01 \x01(\x0b\x32\'.spark.connect.StreamingQueryInstanceIdR\x07queryId\x12\x18\n\x06status\x18\x02 \x01(\x08H\x00R\x06status\x12%\n\rlast_progress\x18\x03 \x01(\x08H\x00R\x0clastProgress\x12)\n\x0frecent_progress\x18\x04 \x01(\x08H\x00R\x0erecentProgress\x12\x14\n\x04stop\x18\x05 \x01(\x08H\x00R\x04stop\x12\x34\n\x15process_all_available\x18\x06 \x01(\x08H\x00R\x13processAllAvailable\x12O\n\x07\x65xplain\x18\x07 \x01(\x0b\x32\x33.spark.connect.StreamingQueryCommand.ExplainCommandH\x00R\x07\x65xplain\x12\x1e\n\texception\x18\x08 \x01(\x08H\x00R\texception\x12k\n\x11\x61wait_termination\x18\t \x01(\x0b\x32<.spark.connect.StreamingQueryCommand.AwaitTerminationCommandH\x00R\x10\x61waitTermination\x1a,\n\x0e\x45xplainCommand\x12\x1a\n\x08\x65xtended\x18\x01 \x01(\x08R\x08\x65xtended\x1aL\n\x17\x41waitTerminationCommand\x12"\n\ntimeout_ms\x18\x02 \x01(\x03H\x00R\ttimeoutMs\x88\x01\x01\x42\r\n\x0b_timeout_msB\t\n\x07\x63ommand"\xf5\x08\n\x1bStreamingQueryCommandResult\x12\x42\n\x08query_id\x18\x01 \x01(\x0b\x32\'.spark.connect.StreamingQueryInstanceIdR\x07queryId\x12Q\n\x06status\x18\x02 \x01(\x0b\x32\x37.spark.connect.StreamingQueryCommandResult.StatusResultH\x00R\x06status\x12j\n\x0frecent_progress\x18\x03 \x01(\x0b\x32?.spark.connect.StreamingQueryCommandResult.RecentProgressResultH\x00R\x0erecentProgress\x12T\n\x07\x65xplain\x18\x04 \x01(\x0b\x32\x38.spark.connect.StreamingQueryCommandResult.ExplainResultH\x00R\x07\x65xplain\x12Z\n\texception\x18\x05 \x01(\x0b\x32:.spark.connect.StreamingQueryCommandResult.ExceptionResultH\x00R\texception\x12p\n\x11\x61wait_termination\x18\x06 \x01(\x0b\x32\x41.spark.connect.StreamingQueryCommandResult.AwaitTerminationResultH\x00R\x10\x61waitTermination\x1a\xaa\x01\n\x0cStatusResult\x12%\n\x0estatus_message\x18\x01 \x01(\tR\rstatusMessage\x12*\n\x11is_data_available\x18\x02 \x01(\x08R\x0fisDataAvailable\x12*\n\x11is_trigger_active\x18\x03 \x01(\x08R\x0fisTriggerActive\x12\x1b\n\tis_active\x18\x04 \x01(\x08R\x08isActive\x1aH\n\x14RecentProgressResult\x12\x30\n\x14recent_progress_json\x18\x05 \x03(\tR\x12recentProgressJson\x1a\'\n\rExplainResult\x12\x16\n\x06result\x18\x01 \x01(\tR\x06result\x1a\xc5\x01\n\x0f\x45xceptionResult\x12\x30\n\x11\x65xception_message\x18\x01 \x01(\tH\x00R\x10\x65xceptionMessage\x88\x01\x01\x12$\n\x0b\x65rror_class\x18\x02 \x01(\tH\x01R\nerrorClass\x88\x01\x01\x12$\n\x0bstack_trace\x18\x03 \x01(\tH\x02R\nstackTrace\x88\x01\x01\x42\x14\n\x12_exception_messageB\x0e\n\x0c_error_classB\x0e\n\x0c_stack_trace\x1a\x38\n\x16\x41waitTerminationResult\x12\x1e\n\nterminated\x18\x01 \x01(\x08R\nterminatedB\r\n\x0bresult_type"\xbd\x06\n\x1cStreamingQueryManagerCommand\x12\x18\n\x06\x61\x63tive\x18\x01 \x01(\x08H\x00R\x06\x61\x63tive\x12\x1d\n\tget_query\x18\x02 \x01(\tH\x00R\x08getQuery\x12|\n\x15\x61wait_any_termination\x18\x03 \x01(\x0b\x32\x46.spark.connect.StreamingQueryManagerCommand.AwaitAnyTerminationCommandH\x00R\x13\x61waitAnyTermination\x12+\n\x10reset_terminated\x18\x04 \x01(\x08H\x00R\x0fresetTerminated\x12n\n\x0c\x61\x64\x64_listener\x18\x05 \x01(\x0b\x32I.spark.connect.StreamingQueryManagerCommand.StreamingQueryListenerCommandH\x00R\x0b\x61\x64\x64Listener\x12t\n\x0fremove_listener\x18\x06 \x01(\x0b\x32I.spark.connect.StreamingQueryManagerCommand.StreamingQueryListenerCommandH\x00R\x0eremoveListener\x12\'\n\x0elist_listeners\x18\x07 \x01(\x08H\x00R\rlistListeners\x1aO\n\x1a\x41waitAnyTerminationCommand\x12"\n\ntimeout_ms\x18\x01 \x01(\x03H\x00R\ttimeoutMs\x88\x01\x01\x42\r\n\x0b_timeout_ms\x1a\xcd\x01\n\x1dStreamingQueryListenerCommand\x12)\n\x10listener_payload\x18\x01 \x01(\x0cR\x0flistenerPayload\x12U\n\x17python_listener_payload\x18\x02 \x01(\x0b\x32\x18.spark.connect.PythonUDFH\x00R\x15pythonListenerPayload\x88\x01\x01\x12\x0e\n\x02id\x18\x03 \x01(\tR\x02idB\x1a\n\x18_python_listener_payloadB\t\n\x07\x63ommand"\xb4\x08\n"StreamingQueryManagerCommandResult\x12X\n\x06\x61\x63tive\x18\x01 \x01(\x0b\x32>.spark.connect.StreamingQueryManagerCommandResult.ActiveResultH\x00R\x06\x61\x63tive\x12`\n\x05query\x18\x02 \x01(\x0b\x32H.spark.connect.StreamingQueryManagerCommandResult.StreamingQueryInstanceH\x00R\x05query\x12\x81\x01\n\x15\x61wait_any_termination\x18\x03 \x01(\x0b\x32K.spark.connect.StreamingQueryManagerCommandResult.AwaitAnyTerminationResultH\x00R\x13\x61waitAnyTermination\x12+\n\x10reset_terminated\x18\x04 \x01(\x08H\x00R\x0fresetTerminated\x12#\n\x0c\x61\x64\x64_listener\x18\x05 \x01(\x08H\x00R\x0b\x61\x64\x64Listener\x12)\n\x0fremove_listener\x18\x06 \x01(\x08H\x00R\x0eremoveListener\x12{\n\x0elist_listeners\x18\x07 \x01(\x0b\x32R.spark.connect.StreamingQueryManagerCommandResult.ListStreamingQueryListenerResultH\x00R\rlistListeners\x1a\x7f\n\x0c\x41\x63tiveResult\x12o\n\x0e\x61\x63tive_queries\x18\x01 \x03(\x0b\x32H.spark.connect.StreamingQueryManagerCommandResult.StreamingQueryInstanceR\ractiveQueries\x1as\n\x16StreamingQueryInstance\x12\x37\n\x02id\x18\x01 \x01(\x0b\x32\'.spark.connect.StreamingQueryInstanceIdR\x02id\x12\x17\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x88\x01\x01\x42\x07\n\x05_name\x1a;\n\x19\x41waitAnyTerminationResult\x12\x1e\n\nterminated\x18\x01 \x01(\x08R\nterminated\x1aK\n\x1eStreamingQueryListenerInstance\x12)\n\x10listener_payload\x18\x01 \x01(\x0cR\x0flistenerPayload\x1a\x45\n ListStreamingQueryListenerResult\x12!\n\x0clistener_ids\x18\x01 \x03(\tR\x0blistenerIdsB\r\n\x0bresult_type"\x15\n\x13GetResourcesCommand"\xd4\x01\n\x19GetResourcesCommandResult\x12U\n\tresources\x18\x01 \x03(\x0b\x32\x37.spark.connect.GetResourcesCommandResult.ResourcesEntryR\tresources\x1a`\n\x0eResourcesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32".spark.connect.ResourceInformationR\x05value:\x02\x38\x01\x42\x36\n\x1eorg.apache.spark.connect.protoP\x01Z\x12internal/generatedb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "spark.connect.commands_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\n\036org.apache.spark.connect.protoP\001Z\022internal/generated"
    )
    _SQLCOMMAND_ARGSENTRY._options = None
    _SQLCOMMAND_ARGSENTRY._serialized_options = b"8\001"
    _SQLCOMMAND_NAMEDARGUMENTSENTRY._options = None
    _SQLCOMMAND_NAMEDARGUMENTSENTRY._serialized_options = b"8\001"
    _SQLCOMMAND.fields_by_name["args"]._options = None
    _SQLCOMMAND.fields_by_name["args"]._serialized_options = b"\030\001"
    _SQLCOMMAND.fields_by_name["pos_args"]._options = None
    _SQLCOMMAND.fields_by_name["pos_args"]._serialized_options = b"\030\001"
    _WRITEOPERATION_OPTIONSENTRY._options = None
    _WRITEOPERATION_OPTIONSENTRY._serialized_options = b"8\001"
    _WRITEOPERATIONV2_OPTIONSENTRY._options = None
    _WRITEOPERATIONV2_OPTIONSENTRY._serialized_options = b"8\001"
    _WRITEOPERATIONV2_TABLEPROPERTIESENTRY._options = None
    _WRITEOPERATIONV2_TABLEPROPERTIESENTRY._serialized_options = b"8\001"
    _WRITESTREAMOPERATIONSTART_OPTIONSENTRY._options = None
    _WRITESTREAMOPERATIONSTART_OPTIONSENTRY._serialized_options = b"8\001"
    _GETRESOURCESCOMMANDRESULT_RESOURCESENTRY._options = None
    _GETRESOURCESCOMMANDRESULT_RESOURCESENTRY._serialized_options = b"8\001"
    _COMMAND._serialized_start = 167
    _COMMAND._serialized_end = 1180
    _SQLCOMMAND._serialized_start = 1183
    _SQLCOMMAND._serialized_end = 1678
    _SQLCOMMAND_ARGSENTRY._serialized_start = 1494
    _SQLCOMMAND_ARGSENTRY._serialized_end = 1584
    _SQLCOMMAND_NAMEDARGUMENTSENTRY._serialized_start = 1586
    _SQLCOMMAND_NAMEDARGUMENTSENTRY._serialized_end = 1678
    _CREATEDATAFRAMEVIEWCOMMAND._serialized_start = 1681
    _CREATEDATAFRAMEVIEWCOMMAND._serialized_end = 1831
    _WRITEOPERATION._serialized_start = 1834
    _WRITEOPERATION._serialized_end = 2885
    _WRITEOPERATION_OPTIONSENTRY._serialized_start = 2309
    _WRITEOPERATION_OPTIONSENTRY._serialized_end = 2367
    _WRITEOPERATION_SAVETABLE._serialized_start = 2370
    _WRITEOPERATION_SAVETABLE._serialized_end = 2628
    _WRITEOPERATION_SAVETABLE_TABLESAVEMETHOD._serialized_start = 2504
    _WRITEOPERATION_SAVETABLE_TABLESAVEMETHOD._serialized_end = 2628
    _WRITEOPERATION_BUCKETBY._serialized_start = 2630
    _WRITEOPERATION_BUCKETBY._serialized_end = 2721
    _WRITEOPERATION_SAVEMODE._serialized_start = 2724
    _WRITEOPERATION_SAVEMODE._serialized_end = 2861
    _WRITEOPERATIONV2._serialized_start = 2888
    _WRITEOPERATIONV2._serialized_end = 3701
    _WRITEOPERATIONV2_OPTIONSENTRY._serialized_start = 2309
    _WRITEOPERATIONV2_OPTIONSENTRY._serialized_end = 2367
    _WRITEOPERATIONV2_TABLEPROPERTIESENTRY._serialized_start = 3460
    _WRITEOPERATIONV2_TABLEPROPERTIESENTRY._serialized_end = 3526
    _WRITEOPERATIONV2_MODE._serialized_start = 3529
    _WRITEOPERATIONV2_MODE._serialized_end = 3688
    _WRITESTREAMOPERATIONSTART._serialized_start = 3704
    _WRITESTREAMOPERATIONSTART._serialized_end = 4504
    _WRITESTREAMOPERATIONSTART_OPTIONSENTRY._serialized_start = 2309
    _WRITESTREAMOPERATIONSTART_OPTIONSENTRY._serialized_end = 2367
    _STREAMINGFOREACHFUNCTION._serialized_start = 4507
    _STREAMINGFOREACHFUNCTION._serialized_end = 4686
    _WRITESTREAMOPERATIONSTARTRESULT._serialized_start = 4688
    _WRITESTREAMOPERATIONSTARTRESULT._serialized_end = 4809
    _STREAMINGQUERYINSTANCEID._serialized_start = 4811
    _STREAMINGQUERYINSTANCEID._serialized_end = 4876
    _STREAMINGQUERYCOMMAND._serialized_start = 4879
    _STREAMINGQUERYCOMMAND._serialized_end = 5511
    _STREAMINGQUERYCOMMAND_EXPLAINCOMMAND._serialized_start = 5378
    _STREAMINGQUERYCOMMAND_EXPLAINCOMMAND._serialized_end = 5422
    _STREAMINGQUERYCOMMAND_AWAITTERMINATIONCOMMAND._serialized_start = 5424
    _STREAMINGQUERYCOMMAND_AWAITTERMINATIONCOMMAND._serialized_end = 5500
    _STREAMINGQUERYCOMMANDRESULT._serialized_start = 5514
    _STREAMINGQUERYCOMMANDRESULT._serialized_end = 6655
    _STREAMINGQUERYCOMMANDRESULT_STATUSRESULT._serialized_start = 6097
    _STREAMINGQUERYCOMMANDRESULT_STATUSRESULT._serialized_end = 6267
    _STREAMINGQUERYCOMMANDRESULT_RECENTPROGRESSRESULT._serialized_start = 6269
    _STREAMINGQUERYCOMMANDRESULT_RECENTPROGRESSRESULT._serialized_end = 6341
    _STREAMINGQUERYCOMMANDRESULT_EXPLAINRESULT._serialized_start = 6343
    _STREAMINGQUERYCOMMANDRESULT_EXPLAINRESULT._serialized_end = 6382
    _STREAMINGQUERYCOMMANDRESULT_EXCEPTIONRESULT._serialized_start = 6385
    _STREAMINGQUERYCOMMANDRESULT_EXCEPTIONRESULT._serialized_end = 6582
    _STREAMINGQUERYCOMMANDRESULT_AWAITTERMINATIONRESULT._serialized_start = 6584
    _STREAMINGQUERYCOMMANDRESULT_AWAITTERMINATIONRESULT._serialized_end = 6640
    _STREAMINGQUERYMANAGERCOMMAND._serialized_start = 6658
    _STREAMINGQUERYMANAGERCOMMAND._serialized_end = 7487
    _STREAMINGQUERYMANAGERCOMMAND_AWAITANYTERMINATIONCOMMAND._serialized_start = 7189
    _STREAMINGQUERYMANAGERCOMMAND_AWAITANYTERMINATIONCOMMAND._serialized_end = 7268
    _STREAMINGQUERYMANAGERCOMMAND_STREAMINGQUERYLISTENERCOMMAND._serialized_start = 7271
    _STREAMINGQUERYMANAGERCOMMAND_STREAMINGQUERYLISTENERCOMMAND._serialized_end = 7476
    _STREAMINGQUERYMANAGERCOMMANDRESULT._serialized_start = 7490
    _STREAMINGQUERYMANAGERCOMMANDRESULT._serialized_end = 8566
    _STREAMINGQUERYMANAGERCOMMANDRESULT_ACTIVERESULT._serialized_start = 8098
    _STREAMINGQUERYMANAGERCOMMANDRESULT_ACTIVERESULT._serialized_end = 8225
    _STREAMINGQUERYMANAGERCOMMANDRESULT_STREAMINGQUERYINSTANCE._serialized_start = 8227
    _STREAMINGQUERYMANAGERCOMMANDRESULT_STREAMINGQUERYINSTANCE._serialized_end = 8342
    _STREAMINGQUERYMANAGERCOMMANDRESULT_AWAITANYTERMINATIONRESULT._serialized_start = 8344
    _STREAMINGQUERYMANAGERCOMMANDRESULT_AWAITANYTERMINATIONRESULT._serialized_end = 8403
    _STREAMINGQUERYMANAGERCOMMANDRESULT_STREAMINGQUERYLISTENERINSTANCE._serialized_start = 8405
    _STREAMINGQUERYMANAGERCOMMANDRESULT_STREAMINGQUERYLISTENERINSTANCE._serialized_end = 8480
    _STREAMINGQUERYMANAGERCOMMANDRESULT_LISTSTREAMINGQUERYLISTENERRESULT._serialized_start = 8482
    _STREAMINGQUERYMANAGERCOMMANDRESULT_LISTSTREAMINGQUERYLISTENERRESULT._serialized_end = 8551
    _GETRESOURCESCOMMAND._serialized_start = 8568
    _GETRESOURCESCOMMAND._serialized_end = 8589
    _GETRESOURCESCOMMANDRESULT._serialized_start = 8592
    _GETRESOURCESCOMMANDRESULT._serialized_end = 8804
    _GETRESOURCESCOMMANDRESULT_RESOURCESENTRY._serialized_start = 8708
    _GETRESOURCESCOMMANDRESULT_RESOURCESENTRY._serialized_end = 8804
# @@protoc_insertion_point(module_scope)
