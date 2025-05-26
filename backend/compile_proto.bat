@echo off

echo [1/3] Copying files...
mkdir protos\server\grpc_out
copy protos\banpick.proto protos\server\grpc_out

echo [2/3] Generating proto...
python -m grpc_tools.protoc --proto_path=./protos/ --python_out=. --grpc_python_out=. server/grpc_out/banpick.proto

echo [3/3] Removing files...
rmdir protos\server /s /q

echo Competed!