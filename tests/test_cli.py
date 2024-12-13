import subprocess
import sys

from sim_hive_controller import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "sim_hive_controller", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
