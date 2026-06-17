import json

from confluent_kafka import Consumer


consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest",
}

consumer = Consumer(consumer_config)

consumer.subscribe(['orders'])


print("Consumer is running and subscribed to: orders")



#Ask the broker for any new messages on the subscribed topics and returns them to the customer of processing
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error:".format(msg.error()))
            continue

        value = msg.value().decode("utf-8")
        order = json.loads(value)

        print(f"Received order: {order['quantity']} x {order['item']} from {order['user']}")
except KeyboardInterrupt:
    print("\nShutting down...")

finally:
    consumer.close()