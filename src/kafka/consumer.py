from kafka import KafkaConsumer

consumer = KafkaConsumer('topic-one')
for msg in consumer:
    print(msg)