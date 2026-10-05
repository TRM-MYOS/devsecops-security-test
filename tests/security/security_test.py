import subprocess
import hashlib
import tempfile
import yaml


# TEST CASE 1: Bandit B602
# shell=True with untrusted input
def run_command(user_input):
    subprocess.call(user_input, shell=True)


# TEST CASE 2: Bandit B324
# Weak cryptographic hash
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# TEST CASE 3: Bandit B506
# Unsafe YAML loading
def load_config(data):
    return yaml.load(data, Loader=yaml.Loader)


# TEST CASE 4: Bandit B108
# Hardcoded temporary directory
def save_temp_file(data):
    path = "/tmp/security_test.txt"

    with open(path, "w") as f:
        f.write(data)

    return path


# TEST CASE 5: Bandit B404 / subprocess usage
def execute_program(command):
    return subprocess.Popen(command)