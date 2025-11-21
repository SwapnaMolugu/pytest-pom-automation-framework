import os
import yaml

def load_config(env="credentials"):
    """
    Loads a YAML config file from utils/config/ based on the given environment name.
    Example: load_config("credentials") loads utils/config/credentials.yaml
    """
    # Get the directory where config_loader.py lives
    base_dir = os.path.dirname(__file__)

    # Build path to ../config/{env}.yaml
    config_path = os.path.join(base_dir, "..", "config", f"{env}.yaml")
    config_path = os.path.abspath(config_path)

    # Load and return the configuration data
    with open(config_path, "r") as f:
        return yaml.safe_load(f)