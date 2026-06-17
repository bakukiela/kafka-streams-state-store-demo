# Kafka Orders Producer & Consumer (Python)

Simple learning project built with Python and Confluent Kafka client.  
It demonstrates how to send and receive JSON messages using Apache Kafka.

## 🚀 What this project does

- Produces order messages to a Kafka topic (`orders`)
- Consumes messages from the same topic in real-time
- Serializes/deserializes data using JSON
- Simulates a simple order tracking system

## 🧰 Tech stack

- Python 3
- confluent-kafka
- Apache Kafka (local broker)
- JSON

## 📦 Producer

The producer sends an order event to Kafka:

- Generates a unique `order_id`
- Encodes order as JSON
- Sends message to topic `orders`
- Prints delivery confirmation (topic, partition, offset)

Example message:

```json
{
  "order_id": "uuid",
  "user": "El",
  "order_type": "LIMIT",
  "item": "hot dog",
  "quantity": 10
}
