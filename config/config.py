import yaml

class Config:
    def __init__(self, data):
        self.base_url = data["base_url"]

def load_config(env="dev"):
    with open(f"config/{env}.yaml") as f:
        data = yaml.safe_load(f)
    return Config(data)