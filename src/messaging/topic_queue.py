import pika
import requests
from requests.exceptions import ReadTimeout, ConnectionError

FLASK_ENDPOINT = 'http://localhost:5000/event'

# standalone Python application that consumes messages on behalf of your Flask microservice and performs synchronous HTTP calls

def on_message(channel, method_frame, header_frame, body):
    message = {'delivery_tag': method_frame.delivery_tag,
               'message': body}
    try:
        res = requests.post(FLASK_ENDPOINT, json=message,
                            timeout=1.)
    except (ReadTimeout, ConnectionError):
        print('Failed to connect to %s.' % FLASK_ENDPOINT)
        # need to implement a retry here
        return

    if res.status_code == 200:
        print('Message forwarded to Flask')
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)


connection = pika.BlockingConnection()
channel = connection.channel()
channel.basic_consume(on_message, queue='race')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()