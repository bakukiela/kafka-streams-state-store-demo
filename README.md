# Kafka Orders Tracker (v1.0.0)

Simple event-driven system built with Apache Kafka and Python.

This project demonstrates a full pipeline:

**Producer → Kafka (KRaft mode via Docker) → Consumer (tracker)**

---

## 🧠 What this project does

This system simulates a basic order processing flow:

- Producer creates an order (JSON)
- Sends it to Kafka topic `orders`
- Kafka stores and distributes the message
- Consumer (tracker) reads and processes orders in real-time

---

## ⚙️ Architecture

```
Producer (Python)
      ↓
Kafka Topic: orders
      ↓
Consumer (Python tracker)
```

---

## 🐳 Kafka setup (Docker - KRaft mode)

Kafka runs in a single-node KRaft configuration (no Zookeeper).

### Key configuration explained:

- KAFKA_PROCESS_ROLES=broker,controller  
  → Kafka runs both broker and controller in one node

- KAFKA_CONTROLLER_QUORUM_VOTERS=1@kafka:9093  
  → defines internal controller communication

- KAFKA_LISTENERS  
  → exposes:
  - PLAINTEXT://0.0.0.0:9092 (client access)
  - CONTROLLER://0.0.0.0:9093 (internal Kafka coordination)

- KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092  
  → how Kafka is reachable from your machine

- KAFKA_LOG_DIRS  
  → where Kafka stores logs and data

---

## 🚀 How to run the project

### 1. Start Kafka

```bash
docker compose up -d
```

Check logs:

```bash
docker logs -f kafka
```

---

### 2. Start the consumer (tracker first)

```bash
python tracker.py
```

Expected output:

```
Consumer is running and subscribed to: orders
```

---

### 3. Run producer

In another terminal:

```bash
python producer.py
```

---

## 📦 Producer (producer.py)

- Creates an order with UUID
- Serializes it to JSON
- Sends it to Kafka topic `orders`
- Prints delivery confirmation (partition + offset)

Example message:

```json
{
  "order_id": "uuid",
  "user": "Nara",
  "order_type": "LIMIT",
  "item": "beer",
  "quantity": 10
}
```

---

## 📥 Consumer (tracker.py)

- Subscribes to topic `orders`
- Polls Kafka continuously
- Decodes JSON messages
- Prints readable output

Example:

```
Received order: 10 x beer from Nara
```

---

## 🔁 End-to-end flow

1. Docker starts Kafka (broker + controller)
2. Producer sends JSON message to topic `orders`
3. Kafka stores message in partition
4. Consumer polls topic continuously
5. Message is deserialized and printed

---

## 📁 Project structure

```
.
├── docker-compose.yml
├── producer.py
├── tracker.py
└── README.md
```

---

## 🏷️ Version

v1.0.0 — Basic Kafka Producer/Consumer system

---

## 📚 What I learned

- Kafka topics, partitions, and offsets
- Producer / consumer model
- KRaft mode (Kafka without Zookeeper)
- Dockerized Kafka setup
- Event-driven architecture basics
- JSON serialization in distributed systems
