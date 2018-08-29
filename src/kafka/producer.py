from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_server='localhost:9092')
for i in range(10):
    print(i)
    producer.send('topic-one', b'some_message_bytes')