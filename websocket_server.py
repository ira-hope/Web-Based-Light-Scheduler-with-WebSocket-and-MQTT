import asyncio
import websockets
import json
import subprocess

async def handler(websocket):
    async for message in websocket:
        schedule = json.loads(message)
        print(f"Received schedule: {schedule}")

        # Publish the schedule to MQTT broker
        payload = json.dumps(schedule)
        subprocess.run(['mosquitto_pub', '-h', 'localhost', '-t', 'lights/schedule', '-m', payload])

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server started at ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
