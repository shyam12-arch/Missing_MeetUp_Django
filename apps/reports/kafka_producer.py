from confluent_kafka import Producer
import json,time

KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092",
}

producer = Producer(KAFKA_CONFIG)

def publish_missing_person_event(data):
    """Publish missing person report event to Kafka."""
    # topic = "missing_persons"
    print(data)
    producer.produce(topic, json.dumps(data).encode("utf-8"))
    time.sleep(10)
    producer.flush()