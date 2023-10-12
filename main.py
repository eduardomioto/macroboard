from evdev import InputDevice, ecodes
from constants import DEVICE_PATH
from actions import handle_key_event

# Initialize the device and grab it
dev = InputDevice(DEVICE_PATH)
dev.grab()

# Main loop to read events
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY and event.value == 1:
        handle_key_event(event.code)
