import os
from evdev import InputDevice, ecodes

# Constants for device path and OS type
DEVICE_PATH = '/dev/input/by-id/usb-1189_USB_Composite_Device_8560134250313334-if01-event-kbd'
LINUX_OS = 'posix'

# Initialize the device and grab it
dev = InputDevice(DEVICE_PATH)
dev.grab()


def reduce_volume():
    """Reduces the volume by 5%."""
    if os.name == LINUX_OS:
        os.system('amixer set Master 5%-')
    else:
        print("Unsupported OS")

#google-chrome --profile-directory=Default

def handle_key_event(event_code):
    """Handles key events and performs the associated action."""
    actions = {
        ecodes.KEY_A: ("Key A - Mute Microphone", 'amixer set Capture nocap'),
        ecodes.KEY_B: ("Key B - Unmute Microphone", 'amixer set Capture cap'),
        ecodes.KEY_C: ("Key C", None),
        ecodes.KEY_D: ("Key D", None),
        ecodes.KEY_E: ("Key E", None),
        ecodes.KEY_F: ("Key F", None),
        ecodes.KEY_G: ("Key G", None),
        ecodes.KEY_H: ("Key H", None),
        ecodes.KEY_I: ("Key I", None),
        ecodes.KEY_J: ("Key J", None),
        ecodes.KEY_K: ("Key K", None),
        ecodes.KEY_L: ("Key L", None),
        ecodes.KEY_1: ("Key 1 - Volume Down", 'amixer sset Master 5%-'),
        ecodes.KEY_3: ("Key 3 - Volume Up", 'amixer sset Master 5%+'),
        ecodes.KEY_4: ("Key 4", None),
        ecodes.KEY_6: ("Key 6", None)
    }

    action = actions.get(event_code, ("No Action Mapped: " + str(event_code), None))
    print(action[0])

    if action[1]:
        os.popen(action[1]).read()


# Main loop to read events
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY and event.value == 1:
        handle_key_event(event.code)
