import hashlib
import os
import subprocess
import tempfile

import yaml


def run_command(program, args=None):
    """Run a command without invoking a shell."""
    command = [program]

    if args:
        command.extend(args)

    return subprocess.run(
        command,
        shell=False,
        check=True,
        capture_output=True,
        text=True,
    )


def hash_password(password):
    """Example stronger hash for this security test."""
    return hashlib.sha256(password.encode()).hexdigest()


def load_config(data):
    """Safely load YAML data."""
    return yaml.safe_load(data)


def save_temp_file(data):
    """Create a temporary file safely."""
    fd, path = tempfile.mkstemp(
        prefix="security_test_",
        suffix=".txt",
    )

    with os.fdopen(fd, "w", encoding="utf-8") as file:
        file.write(data)

    return path


def execute_program(program, args=None):
    """Execute a program without shell=True."""
    command = [program]

    if args:
        command.extend(args)

    return subprocess.run(
        command,
        shell=False,
        check=True,
        capture_output=True,
        text=True,
    )