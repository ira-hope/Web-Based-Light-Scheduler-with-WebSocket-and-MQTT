# IoT Light Scheduler 🌟

This project simulates a real-world IoT dashboard that schedules a light ON/OFF using a browser interface, WebSocket server, MQTT, and Arduino.

## Features
- Browser UI for setting ON and OFF times
- WebSocket server receives schedule and forwards it to MQTT
- MQTT subscriber script controls Arduino via serial connection
- Arduino triggers a relay to control light

## Tech Stack
- HTML/CSS/JavaScript
- Python (websockets, paho-mqtt, pyserial)
- mosquitto_pub / mosquitto_sub
- Arduino UNO

System Workflow
User inputs ON/OFF time on the browser UI and clicks submit.

Data is sent via WebSocket to a Python server.

The server relays the data to MQTT broker using mosquitto_pub.

A Python MQTT subscriber listens, processes the schedule, and sends '1' (ON) or '0' (OFF) via serial to Arduino.

The Arduino receives the signal and triggers the relay accordingly.


