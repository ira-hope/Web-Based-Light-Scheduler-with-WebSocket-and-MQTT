import paho.mqtt.client as mqtt
import json
import serial
import time
import sys

# === CONFIGURATION ===
SERIAL_PORT = 'COM5'  # Make sure this matches your Arduino's COM port
BAUD_RATE = 9600
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "lights/schedule"

# === INITIAL SETUP ===
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Give Arduino time to reset
    print(f"[INFO] Connected to Arduino on {SERIAL_PORT}")
except serial.SerialException as e:
    print(f"[ERROR] Could not open serial port {SERIAL_PORT}: {e}")
    sys.exit(1)

schedule = {'on': None, 'off': None}

# === MQTT CALLBACKS ===
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[INFO] Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"[ERROR] Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    global schedule
    print(f"[INFO] Message received: {msg.payload.decode()}")
    try:
        schedule = json.loads(msg.payload.decode())
        print(f"[INFO] Updated schedule: {schedule}")
    except json.JSONDecodeError:
        print("[ERROR] Failed to decode JSON from MQTT message")

# === LIGHT CONTROL LOOP ===
def control_light():
    while True:
        now = time.strftime("%H:%M")
        if schedule['on'] == now:
            print("[ACTION] Turning light ON")
            ser.write(b'1')
            time.sleep(60)  # Prevent retrigger
        elif schedule['off'] == now:
            print("[ACTION] Turning light OFF")
            ser.write(b'0')
            time.sleep(60)
        time.sleep(1)

# === MAIN ===
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"[ERROR] Failed to connect to MQTT broker: {e}")
    sys.exit(1)

client.loop_start()

try:
    control_light()
except KeyboardInterrupt:
    print("\n[INFO] Shutting down...")
    client.loop_stop()
    ser.close()
    sys.exit(0)
