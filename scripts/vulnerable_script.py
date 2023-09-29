"""This script has intentional vulnerabilities for testing purposes."""

import argparse
import logging
import os
import random
import string
import sys

import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

# Set up argument parser
parser = argparse.ArgumentParser(
    description="This script has intentional vulnerabilities for testing purposes."
)
parser.add_argument("--debug", action="store_true", help="Enable debug logging")
parser.add_argument("--log-file", help="Log file path")

# Parse arguments
args = parser.parse_args()

# Set up logging
if args.debug:
    logging.getLogger().setLevel(logging.DEBUG)

if args.log_file:
    logging.getLogger().addHandler(logging.FileHandler(args.log_file))

# Set up variables
script_dir = os.path.dirname(os.path.realpath(__file__))
script_name = os.path.basename(__file__)
script_name_no_ext = os.path.splitext(script_name)[0]
script_path = os.path.realpath(__file__)
script_path_no_ext = os.path.splitext(script_path)[0]
script_user = os.getlogin()
script_hostname = os.uname()[1]
script_pid = os.getpid()
script_ppid = os.getppid()
script_uid = os.getuid()
script_gid = os.getgid()
script_euid = os.geteuid()
script_egid = os.getegid()


# Set up functions
def get_random_string(length):
    """Returns a random string of the specified length."""
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def get_random_number(length):
    """Returns a random number of the specified length."""
    return random.randint(10 ** (length - 1), (10**length) - 1)


def get_random_ip():
    """Returns a random IP address."""
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
