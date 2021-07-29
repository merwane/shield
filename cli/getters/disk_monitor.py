from cli.api import ShieldApi

api = ShieldApi()

def get():
    disk_data = api.get("disk")

    return disk_data
