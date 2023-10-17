import os
from evdev import ecodes
from utils import move_workspace_forward, move_workspace_backward,mute_microphone,unmute_microphone

def handle_key_event(event_code):
    """Handles key events and performs the associated action."""
    events = {
        ecodes.KEY_A: ("Key A - Mute Microphone", 'amixer set Capture nocap'),
        ecodes.KEY_B: ("Key B - Unmute Microphone", 'amixer set Capture cap'),
        ecodes.KEY_C: ("Key C", move_workspace_backward()),
        ecodes.KEY_D: ("Key D", move_workspace_forward()),
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

    action = events.get(event_code, ("No Action Mapped: " + str(event_code), None))
    print(action[0])

    if action[1]:
        os.popen(action[1]).read()
        ##action[1];