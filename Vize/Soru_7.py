class Device:
    def __init__(self, device_name, **kwargs):
        self.device_name = device_name
        print(f"Device: {self.device_name}")
        super().__init__(**kwargs)

class NetworkEnabled:
    def __init__(self, ip_address, **kwargs):
        self.ip_address = ip_address
        print(f"IP: {self.ip_address}")
        super().__init__(**kwargs)

class BatteryPowered:
    def __init__(self, battery_level, **kwargs):
        self.battery_level = battery_level
        print(f"Battery: %{self.battery_level}")
        super().__init__(**kwargs)

class SmartPhone(Device, NetworkEnabled, BatteryPowered):
    def __init__(self, device_name, ip_address, battery_level):
        print("SmartPhone oluşturuluyor")
        super().__init__(
            device_name=device_name,
            ip_address=ip_address,
            battery_level=battery_level
        )
    def show_info(self):
        print(f"{self.device_name} - {self.ip_address} - %{self.battery_level}")
phone = SmartPhone("Galaxy", "192.168.1.10", 85)
phone.show_info()
print(SmartPhone.mro())
