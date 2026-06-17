import json
import uuid

from confluent_kafka import Producer

producer_config = {
    'bootstrap.servers': 'localhost:9092',
}

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print('Delivery failed'.format(err))
    else:
        print(f"Delivered: {msg.value().decode('utf-8')}")
        print(f"Delivered to: {msg.topic()}: partition: {msg.partition()} at offset: {msg.offset()}")

order = {
    "order_id": str(uuid.uuid4()),
    "user": 'Nara',
    "order_type": 'LIMIT',
    "item": "beer",
    "quantity": 10
}

value = json.dumps(order).encode("utf-8") # Make sure order is readable for producer (kafka)

producer.produce(topic="orders", value=value, callback=delivery_report, key=str(uuid.uuid4()))

producer.flush()  # Make sure that all buffered events are sent before the program exits, even if it crashes.

