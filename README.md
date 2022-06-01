# SecretManager
Python client for AWS Secret keys management. This can be used easily to manage AWS secrets as well as implement them in your code without hardcoding anything!

# Installation
pip install git+https://github.com/DevHumble/SecretManager.git

# Quickstart
<pre>
from secretmanager import SecretManager
sk = SecretManager.SecretManager()
sk.get_secret('your_secret')
<pre>

# TEST
<per>
# Run command in project root on cmd line
python -m unittest test.integration.test_SecretManager
<pre>
