#!/bin/bash
mkdir /backend/protos/server/
mkdir /backend/protos/server/grpc_out/
cp /backend/protos/* /backend/protos/server/grpc_out/
python -m grpc_tools.protoc --proto_path=/backend/protos/ --python_out=/backend --grpc_python_out=/backend /backend/protos/server/grpc_out/banpick.proto
# rm backend/protos/server -rf
