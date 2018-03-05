from dns import resolver
import consul

def resolve_service(service):
    consul_resolver = resolver.Resolver()
    consul_resolver_port = 8600 # consul agent port
    consul_full_name = '%s.service.consul' % service
    consul_resolver.nameservers = ['127.0.0.1']
    print('DNS resolving %s' % consul_full_name)
    dns_answer = consul_resolver.query(consul_full_name, 'A')
    ip = str(dns_answer[0])
    dns_answer_server = resolver.query(consul_full_name, 'SRV')
    port = int(str(dns_answer_server[0]).split()[2])
    print('Service %s resolved to ip: %s and port %d' % (consul_full_name, ip, port))


def main():
    resolve_service(service='my_service')


if __name__ == '__main__':
    main()