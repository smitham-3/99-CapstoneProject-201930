"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Alex Smith.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m2_laptop_code as m2
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Alex Smith")
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # DONE: Put your GUI onto your frame (using sub-frames if you wish).
    execute_label = ttk.Label(frame, text='Click this when ready')
    direction_label = ttk.Label(frame, text='Enter direction')
    speed_label = ttk.Label(frame, text='Enter speed')
    distance_label = ttk.Label(frame, text='Enter distance')
    execute_button = ttk.Button(frame, text="Execute")
    direction_box = ttk.Entry(frame, width=18)
    speed_box = ttk.Entry(frame, width=8)
    distance_box = ttk.Entry(frame, width=8)
    frame_label.grid()
    execute_label.grid()
    execute_button.grid()
    direction_label.grid()
    direction_box.grid()
    speed_label.grid()
    speed_box.grid()
    distance_label.grid()
    distance_box.grid()


    # Return your frame:
    return frame


class MyLaptopDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from the ROBOT via MQTT.
    """
    def __init__(self, root):
        self.root = root  # type: tkinter.Tk
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # TODO: Add methods here as needed.


# DONE: Add functions here as needed.



