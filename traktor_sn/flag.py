import secrets
import string
import os

alphabet = string.ascii_letters + string.digits
length = 42
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flag.txt")


def gen_flag():
    flag = ''.join(secrets.choice(alphabet) for _ in range(length))
    open(file_path, "w").write(flag)
    print(file_path)


def get_flag():
    flag = open(file_path).readline().strip()
    return flag


if __name__ == "__main__":
    gen_flag()
