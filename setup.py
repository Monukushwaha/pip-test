import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pip-test',
    version='0.0.3',
    author='Monukushwaha',
    author_email='monu17@navgurukul.org',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Monukushwaha/pip-test',
    project_urls = {
        "Bug Tracker": "https://github.com/Monukushwaha/pip-test/issues"
    },
    license='MIT',
    packages=['pip-test'],
    install_requires=['requests'],
)