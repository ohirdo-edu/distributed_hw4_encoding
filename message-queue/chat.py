import redis
import threading
import sys
import json


redis_connection = redis.Redis(host='localhost', port=6379, decode_responses=True)

user_name = sys.argv[1]
group = sys.argv[2]


def listen():
    ps = redis_connection.pubsub()
    ps.subscribe(group)
    for msg in ps.listen():
        if msg['type'] == 'message':
            obj = json.loads(msg['data'])
            if obj['from'] != user_name:
                print(f"{obj['from']}: {obj['text']}")


def send_text(text: str):
    redis_connection.publish(group, json.dumps({
        'from': user_name,
        'text': text,
    }))


listener = threading.Thread(target=listen, daemon=True)
listener.start()

send_text('entered the chat')

try:
    while True:
        send_text(input())
except KeyboardInterrupt:
    send_text('left the chat')
