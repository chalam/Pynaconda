import time
import sys
# import consul
import logging
import statsd
import random
import os
from concurrent import futures
import grpc

from src.grpc_io.gen import search_pb2 as search_pb2
from src.grpc_io.gen import search_pb2_grpc as search_pb2_grpc
from src.grpc_io.src.search_models import session, Thing, func

log = logging.getLogger()
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

port = random.randint(50000, 59000)
# stat = statsd.StatsClient('localhost', 8125)

class SearchServicer(search_pb2_grpc.SearchServicer):
    # @stat.timer("search")
    def search(self, request, context):
        # stat.incr("search_count")
        log.info("search request: " + str(request))
        query = session.query(Thing).filter(Thing.name == request.query)
                # func.ST_Contains(Thing.geom, 'POINT({} {})'.format(request.lat, request.lng))

        responses = [search_pb2.SearchResponse(response=rec.name) for rec in query]
        log.info("search responses: " + str(responses))
        return search_pb2.SearchResponses(responses=responses)

    # @stat.timer("monitor")
    def monitor(self, request, context):
        # stat.incr("monitor_count")
        n_things = session.query(Thing).count()
        return search_pb2.MonitorResponse(n_things=n_things)

# def register():
#     log.info("register started")
#     c = consul.Consul()
#     check = consul.Check.tcp("127.0.0.1", port, "30s")
#     c.agent.service.register("search-service", "search-service-%d" % port, address="127.0.0.1", port=port, check=check)
#     log.info("services: " + str(c.agent.services()))

# def unregister():
#     log.info("unregister started")
#     c = consul.Consul()
#     c.agent.service.deregister("search-service-%d" % port)
#     log.info("services: " + str(c.agent.services()))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    search_pb2_grpc.add_SearchServicer_to_server(
        SearchServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    # register()
    serve()
    # unregister()