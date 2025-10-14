def handle_pairing_request(self, request_type, device, uuid=None, passkey=None):
    """Handle various incoming Bluetooth pairing requests and user interactions.

    Args:
        request_type: The type of pairing request.
        device: The D-Bus object path of the Bluetooth device requesting pairing.
        uuid: The UUID of the Bluetooth service being authorized or PIN to display.
        passkey: The passkey value for confirmation or display.

    Returns:
        pin, passkey, True or None depending on request.

    """
    self.log.info(f"Handling pairing request: {request_type} for {device}")
    device_address = device.split("dev_")[-1].replace("_", ":")
    if self.selected_capability == "NoInputNoOutput" and self.bluetooth_device_manager.is_device_paired(device_address):
        self.add_paired_device_to_list(device_address)
        self.log.info(f"Pairing successful with {device_address}")
    else:
        self.log.info(f"Pairing failed with {device_address}")
        return
    handler = constants.pairing_request_handlers.get(request_type)
    if handler:
        return handler(self, device_address, uuid, passkey)
    else:
        self.log.warning(f"Unknown pairing request type: {request_type}")

def perform_device_action(self, action, device_address, load_profiles):
        device_action =constants.device_action_map.get(action)
        if not device_action:
            self.log.error("Unknown action: %s", action)
            return
        method_name = device_action["method"]
        method = getattr(self.bluetooth_device_manager, method_name)
        result = method(device_address)
        self.log.info("Performing %s on %s", method_name, device_address)
        message = device_action["success"] if result else device_action["failure"]
        message_popup = QMessageBox.information if result else QMessageBox.warning
        message_popup(self, action.capitalize(), f"{device_address}: {message}")
        post_method = getattr(self, device_action["post_action"])
        if action == "connect" and load_profiles:
            post_method(device_address)
        elif action!="connect":
            post_method(device_address)


'''def handle_pairing_request(self, request_type, device, uuid=None, passkey=None):
    """Handle various incoming Bluetooth pairing requests and user interactions.

    Args:
        request_type: The type of pairing request.
        device: The D-Bus object path of the Bluetooth device requesting pairing.
        uuid: The UUID of the Bluetooth service being authorized or PIN to display.
        passkey: The passkey value for confirmation or display.

    Returns:
        pin, passkey or True.

    """
    self.log.info(f"Handling pairing request: {request_type} for {device}")
    device_address = device.split("dev_")[-1].replace("_", ":")
    if self.selected_capability == "NoInputNoOutput":
        pairing_status = self.bluetooth_device_manager.is_device_paired(device_address)
        if pairing_status:
            QMessageBox.information(self, "Pairing Successful", f"{device_address} was paired.")
            self.add_paired_device_to_list(device_address)
            self.log.info("Pairing successful with %s", device_address)
        else:
            self.log.info("Pairing failed with %s", device_address)
    elif request_type == "pin":
        pin, accept = QInputDialog.getText(self, "Pairing Request", f"Enter PIN for device {device_address}:")
        if accept and pin:
            return pin
        else:
            self.log.info("User cancelled or provided no PIN for device %s", device_address)
    elif request_type == "passkey":
        passkey, accept = QInputDialog.getInt(self, "Pairing Request",
                                              f"Enter passkey for device {device_address}:")
        if accept:
            QMessageBox.information(self, "Pairing Successful", f"{device_address} was paired.")
            self.add_paired_device_to_list(device_address)
            return passkey
        else:
            self.log.info("User cancelled passkey input for device %s", device_address)
            return False
    elif request_type == "confirm":
        reply = QMessageBox.question(self, "Confirm Pairing",
                                     f"Device {device_address} requests to pair with passkey: {uuid}\nAccept?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self, "Pairing Successful", f"{device_address} was paired.")
            self.add_paired_device_to_list(device_address)
            return True
        elif reply == QMessageBox.StandardButton.No:
            QMessageBox.information(self, "Pairing Failed", f"Pairing with {device_address} failed.")
            self.log.info("User rejected pairing confirmation request")
            return False
    elif request_type == "authorize":
        reply = QMessageBox.question(self, "Authorize Service",
                                     f"Device {device_address} wants to use service {uuid}\nAllow?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self, "Connection Successful", f"{device_address} was connected.")
            return True
        elif reply == QMessageBox.StandardButton.No:
            self.log.warning("User denied service authorization for device %s", device_address)
            self.bluetooth_device_manager.disconnect(device_address)
    elif request_type == "display_pin":
        if uuid is not None:
            QMessageBox.information(self, "Display PIN", f"Enter this PIN on {device_address}: {uuid}")
            QTimer.singleShot(5000, lambda: (self.add_paired_device_to_list(device_address)
                                             if self.bluetooth_device_manager.is_device_paired(device_address)
                                             else QMessageBox.warning(self, "Pairing Failed",
                                                                      f"Pairing with {device_address} did not complete.")))
        else:
            self.log.warning("DisplayPinCode called, but no PIN provided.")
    elif request_type == "display_passkey":
        if passkey is not None:
            QMessageBox.information(self, "Display Passkey", f"Enter this passkey on {device_address}: {passkey}")
            QTimer.singleShot(5000, lambda: (self.add_paired_device_to_list(device_address)
                                             if self.bluetooth_device_manager.is_device_paired(device_address)
                                             else QMessageBox.warning(self, "Pairing Failed",
                                                                      f"Pairing with {device_address} did not complete.")))
    elif request_type == "cancel":
        QMessageBox.warning(self, "Pairing Cancelled", f"Pairing with {device_address} was cancelled.")'''
