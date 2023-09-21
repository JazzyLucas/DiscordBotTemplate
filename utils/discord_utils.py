import random
import time


def connect_to_discord(client, token):
    while True:
        try:
            client.run(token)
            break
        except Exception as e:
            print(f"Failed to connect to Discord: {e}")
            retry_seconds = random.randint(30, 90)  # Generates a random integer between 30 and 90
            print(f"Retrying in {retry_seconds} seconds...")
            time.sleep(retry_seconds)