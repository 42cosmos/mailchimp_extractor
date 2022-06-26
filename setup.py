from setuptools import setup, find_packages

NAME = "extract-mailchimp-data"
VERSION = "0.0.1"

REQUIRES = [
    "python-dotenv==0.20.0",
    "mailchimp-marketing"
]

setup(
    name=NAME,
    version=VERSION,
    description="Extract MailChimp data only by folder ID",
    long_description=open("README.md").read(),
    author="Eunbin Park",
    author_email="parkeb417@gmail.com",
    install_requires=REQUIRES,
    packages=find_packages(),
    keywords=["data", "inflab", "api", "mailchimp"],
    python_requires=">=3.6",
    include_package_data=True
)