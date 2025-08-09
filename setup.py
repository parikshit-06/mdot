from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    name="dd",  # This will be the pip install name
    version="0.1.0",
    author="ParikshitSonwane",
    author_email="parik.sonwane06@gmail.com",
    description="A simple CLI Morse Code encoder/decoder",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dd=dot-dash.main:main"
        ]
    },
    python_requires=">=3.6",
)
