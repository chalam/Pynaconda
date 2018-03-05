import consul

def register_service(service, service_id, port):
    c = consul.Consul()
    check = consul.Check.tcp('127.0.0.1', port, '30s')
    c.agent.service.register(service,
                             service_id=service_id,
                             port=port,
                             check=check,
                             tags=['t1'])
    print(c.agent.services())
    for s in c.agent.services():
        print(s)
    print('Service %s registered' % service)


def deregister_service(service_id):
    c = consul.Consul()
    c.agent.service.deregister(service_id=service_id)
    print(c.agent.services())
    for s in c.agent.services():
        print(s)
    print('Service %s deregistered' % service_id)


def main():
    register_service(service='my_service', service_id='server_id101', port=1010)
    deregister_service('server_id101')


if __name__ == '__main__':
    main()