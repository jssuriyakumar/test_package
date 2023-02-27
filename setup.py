import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='test-package',
    version='0.0.1',
    author='Mike Huls',
    author_email='jssuriyakumar@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jssuriyakumar/test_package',
    project_urls = {
        "Bug Tracker": "https://github.com/jssuriyakumar/test_package/issues"
    },
    license='MIT',
    packages=['test_package'],
    install_requires=['pandas','python_dateutil','tqdm' ,'requests','beautifulsoup4'],
)
