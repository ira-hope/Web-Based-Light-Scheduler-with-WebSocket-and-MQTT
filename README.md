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

## How to Run

1. **Start Mosquitto Broker**  
```bash
sudo systemctl start mosquitto
