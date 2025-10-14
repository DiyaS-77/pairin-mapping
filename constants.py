from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMessageBox, QInputDialog

adapter_interface = 'org.bluez.Adapter1'
agent_path = '/test/agent'
agent="org.bluez.Agent1"
agent_interface = 'org.bluez.AgentManager1'
bluez_service = 'org.bluez'
bluez_path = '/org/bluez'
device_interface = "org.bluez.Device1"
properties_interface = "org.freedesktop.DBus.Properties"
pulseaudio_command = '/usr/local/bluez/pulseaudio-13.0_for_bluez-5.65/bin/pulseaudio -vvv'
media_control_interface = "org.bluez.MediaControl1"
obex_client = "org.bluez.obex.Client1"
obex_path = "/org/bluez/obex"
obex_service = "org.bluez.obex"
obex_object_push = "org.bluez.obex.ObjectPush1"
obex_object_transfer = "org.bluez.obex.Transfer1"
object_manager_interface = "org.freedesktop.DBus.ObjectManager"
device_action_map = {
    "pair" : {
        "method" : "pair",
        "success" : "Device paired successfully.",
        "failure" : "Failed to pair device.",
        "post_action" : "add_paired_device_to_list"
    },
    "connect" :{
        "method" : "connect",
        "success" : "Device connected successfully.",
        "failure" : "Failed to connect device.",
        "post_action" : "load_device_profile_tabs"
    },
    "disconnect" : {
        "method" : "disconnect",
        "success" : "Device disconnected successfully.",
        "failure" : "Failed to disconnect device.",
        "post_action" : "load_device_profile_tabs"
    },
    "unpair" : {
        "method" : "unpair_device",
        "success" : "Device unpaired successfully.",
        "failure" : "Failed to unpair device.",
        "post_action" : "remove_device_from_list"
    }
}

pairing_request_handlers = {
    "pin": "handle_pin_request",
    "passkey": "handle_passkey_request",
    "confirm": "handle_confirm_request",
    "authorize": "handle_authorize_request",
    "display_pin": "handle_display_pin_request",
    "display_passkey": "handle_display_passkey_request",
    "cancel": "handle_cancel_request",
}


