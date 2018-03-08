import grpc
import sys
import logging
# from dns import resolver

from src.grpc_io.gen import search_pb2 as search_pb2
from src.grpc_io.gen import search_pb2_grpc as search_pb2_grpc

log = logging.getLogger()
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)


# def resolve_service():
#     global ip, port
#     consul_resolver = resolver.Resolver()
#     consul_resolver.port = 8600
#     consul_resolver.nameservers = ["127.0.0.1"]
#     dnsanswer = consul_resolver.query("search-service.service.consul", 'A')
#     ip = str(dnsanswer[0])
#     dnsanswer_srv = consul_resolver.query("search-service.service.consul", 'SRV')
#     port = int(str(dnsanswer_srv[0]).split()[2])
#     return ip, port


# ip, port = resolve_service()
ip, port = 'localhost', 50051

log.info("creating grpc client based on consul data: ip=%s port=%d" % (ip, port))
channel = grpc.insecure_channel('%s:%d' % (ip, port))
stub = search_pb2_grpc.SearchStub(channel)

if len(sys.argv) == 2 and sys.argv[1] == "--monitor":
    monitresp = stub.monitor(search_pb2.google_dot_protobuf_dot_empty__pb2.Empty())
    log.debug("monitor response: {}".format(monitresp))
else:
    req = search_pb2.SearchRequest(
        query="thing1",
        lat=float(sys.argv[1]),
        lng=float(sys.argv[2]),
        result_per_page=10)
    log.debug("sending request: {}".format(req))
    resp = stub.search(req)
    log.debug("received response: {}".format(resp))