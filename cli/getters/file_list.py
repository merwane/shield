from cli.api import ShieldApi

api = ShieldApi()

def get():
    all_files = api.get("files")

    return all_files
