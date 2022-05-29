import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pip-test",
    version="0.0.1",
    author="Monukushwaha",
    author_email="monu17@navgurukul.org",
    description="It's pip... with git.",
    long_description=long_description,
    url="https://github.com/Monukushwaha/pip-test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
