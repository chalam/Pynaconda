import jaeger_client import Config
import time

def main():
    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 101,
            },
            'logging': True
        },
        service_name='app_name',
    )
    tracer = config.initialize_tracer()

    with tracer.start_span('span_one') as span:
        span.log_event('test_message', payload={'life': 42})
        # some logic
        with tracer.start_span('child_span_one') as child_span:
            child_span.log_event('down below')

    time.sleep(2) # yield to IOLoop to flush the spans
    tracer.close()  # flush any buffered spans

if __name__ == '__main__':
    main()