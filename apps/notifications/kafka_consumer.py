from confluent_kafka import Consumer
import json,time

KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "missing_persons_group",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(KAFKA_CONFIG)
consumer.subscribe(["missing_persons"])

def consume_missing_person_events():
    """Consume missing person report events from Kafka."""
    while True:
        print("consumer...........")
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        event_data = json.loads(msg.value().decode("utf-8"))
        print(f"📢 New Missing Person Alert: {event_data['name']} last seen at {event_data['last_seen_location']}")



if __name__=="__main__":
    consume_missing_person_events()
    time.sleep(10)