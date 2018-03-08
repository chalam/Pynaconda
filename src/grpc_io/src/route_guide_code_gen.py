from grpc_tools import protoc

protoc.main((
    '',
    '-I..\\protos',
    '--python_out=..\\gen\\',
    '--grpc_python_out=..\\gen\\',
    '..\\protos\\route_guide.proto',
))

print('fix the import path to src')