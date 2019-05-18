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
    direction_label = ttk.Label(frame, text="Choose a direction: ")
    forwards_button = ttk.Button(frame, text="Forwards")
    backwards_button = ttk.Button(frame, text="Backwards")
    speed_label = ttk.Label(frame, text='Enter speed')
    distance_label = ttk.Label(frame, text='Enter distance')
    speed_box = ttk.Entry(frame, width=8)
    distance_box = ttk.Entry(frame, width=8)
    function_label = ttk.Label(frame, text='Executes the move_until function.')
    function_button = ttk.Button(frame, text='Execute')
    frame_label.grid()
    direction_label.grid()
    forwards_button.grid(row=2, column=0)
    backwards_button.grid(row=2, column=1)
    speed_label.grid()
    speed_box.grid()
    distance_label.grid()
    distance_box.grid()
    function_label.grid()
    function_button.grid()


    forwards_button["command"] = lambda: move_forward(speed_box, distance_box, mqtt_sender)
    backwards_button["command"] = lambda: move_backward(speed_box, distance_box, mqtt_sender)
    function_button["command"] = lambda: move_until(speed_box, distance_box, mqtt_sender)
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

def move_forward(speed_box, distance_box, mqtt_sender):
    speed = speed_box.get()
    distance = distance_box.get()
    mqtt_sender.send_message("move_forward", [speed, distance])

def move_backward(speed_box, distance_box, mqtt_sender):
    speed = speed_box.get()
    distance = distance_box.get()
    mqtt_sender.send_message("move_backward", [speed, distance])

def move_until(speed_box, distance_box, mqtt_sender):
    speed = speed_box.get()
    distance = distance_box.get()
    mqtt_sender.send_message("move_until", [speed, distance])


