import subprocess


def run_command():
    command = "echo security-test"

    result = subprocess.call(
        command,
        shell=True,
    )

    return result