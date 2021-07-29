from cli.api import ShieldApi

api = ShieldApi()

def get():
    device_data = api.get("device")

    return device_data
