python -m grpc.tools.protoc -I..\protos --python_out=..\gen\ --grpc_python_out=..\gen\ ..\protos\search.proto
rem python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/route_guide.proto