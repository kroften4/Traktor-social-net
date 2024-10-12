import secrets
import string
import json
from traktor_sn import settings

# DEPLOYMENT: Change the path to, for example, '/etc/traktor-config.json'
# Do not put the config file inside the project dir

with open(settings.CONFIG_PATH) as config_file:
    config = json.load(config_file)

alphabet = string.ascii_letters + string.digits
length = 42


def gen_flag():
    flag = ''.join(secrets.choice(alphabet) for _ in range(length))
    config["FLAG"] = flag
    config_file = open(settings.CONFIG_PATH, "w")
    json.dump(config, config_file, indent=4)


def get_flag():
    flag = config["FLAG"]
    return flag


if __name__ == "__main__":
    gen_flag()
