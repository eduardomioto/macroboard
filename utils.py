import os
from constants import LINUX_OS

def reduce_volume():
    """Reduces the volume by 5%."""
    if os.name == LINUX_OS:
        os.system('amixer set Master 5%-')
    else:
        print("Unsupported OS")
