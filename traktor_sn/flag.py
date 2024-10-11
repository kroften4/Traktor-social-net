import secrets
import string
import json
from traktor_sn import settings

# DEPLOYMENT: Change the path to, for example, '/etc/traktor-config.json'
# Do not put the config file inside the project dir
# (see 'prod' branch on https://github.com/kroften4/Traktor-social-net/tree/prod for an example)
PATH_TO_CONFIG = settings.BASE_DIR / "config-example.json"

with open(PATH_TO_CONFIG) as config_file:
    config = json.load(config_file)

alphabet = string.ascii_letters + string.digits
length = 42


def gen_flag():
    flag = ''.join(secrets.choice(alphabet) for _ in range(length))
    config["FLAG"] = flag
    config_file = open(PATH_TO_CONFIG, "w")
    json.dump(config, config_file, indent=4)


def get_flag():
    flag = config["FLAG"]
    return flag


if __name__ == "__main__":
    gen_flag()
