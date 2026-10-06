import hashlib
import os
import tempfile

import yaml


def hash_password(password):
    """Generate a SHA-256 hash for testing."""
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