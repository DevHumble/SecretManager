# SecretManager
Python client for AWS Secret keys management. This can be used easily to manage AWS secrets as well as implement them in your code without hardcoding anything!
#Quickstart

from secretkeeper import SecretKeeper
sk = SecretKeeper.SecretKeeper()
sk.get_secret('your_secret')

Test

# Run command in project root on cmd line
python -m unittest test.integration.test_SecretKeeper
