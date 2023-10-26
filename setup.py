from setuptools import setup, find_packages

VERSION = '0.0.5'
DESCRIPTION = 'A framework that makes discord bot programming easy'

with open("README.md", "r") as f:
    long_description = f.read()

# Setting up
setup(
    name="phonkd_bot",
    version=VERSION,
    author="Phonki",
    author_email="<phonkibusiness@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["aiohttp==3.8.6", "aiosignal==1.3.1", "async-timeout==4.0.3", "asyncio==3.4.3", "attrs==23.1.0", "charset-normalizer==3.3.0", "discord==2.3.2", "discord.py==2.3.2", "frozenlist==1.4.0", "idna==3.4", "multidict==6.0.4", "numpy==1.25.2", "pyperclip==1.8.2", "typing_extensions==4.7.1", "yarl==1.9.2"],
    keywords=['python', 'discord'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
    ]
)