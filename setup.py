from setuptools import setup
import os
try:
    import fabrice
except:
    os.system("pip install fabrice")
    import fabrice
setup(
   name='SecretManager',
   version='1.0',
   description='AWS Secret Manager Client',
   author='DevHumble',
   author_email='sohrabkhandae@gmail.com',
   packages=['SecretManager'],
   install_requires=['boto3'], #external packages as dependencies
)
