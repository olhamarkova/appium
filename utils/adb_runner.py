import subprocess


def run_adb_command(command: str) -> str:
    result = subprocess.run(
        ["adb"] + command.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"ADB Error: {result.stderr}")
    return result.stdout.strip()
