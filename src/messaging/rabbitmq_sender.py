from pika import BlockingConnection, BasicProperties

# assuming there's a working local RabbitMQ server with a working
# guest / guest
# account

# sender -> exchange -> queue -> receiver

# $ rabbitmqadmin declare exchange name=incoming type=topic
# exchange declared
#
# $ rabbitmqadmin declare queue name=race
# queue declared
#
# $ rabbitmqadmin declare queue name=training
# queue declared
#
# $ rabbitmqadmin declare binding source="incoming" destination_type="queue" destination="race" routing_key="race.*"
# binding declared
#
# $ rabbitmqadmin declare binding source="incoming" destination_type="queue" destination="training" routing_key="training.*"
# binding declared

def message(topic, message):
    connection = BlockingConnection()
    try:
        channel = connection.channel()
        props = BasicProperties(content_type='text/plain',
                                delivery_mode=1)
        channel.basic_publish('incoming', topic, message, props)
    finally:
        connection.close()

    # sending a message about race 34
    message('race.34', 'We have some results!')

    # training 12
    message('training.12', "It's time to do your long run")