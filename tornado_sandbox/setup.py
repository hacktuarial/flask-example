from setuptools import setup, find_packages

requires = [
    'tornado',
]

setup(
    name='tornado_sandbox',
    version='0',
    description='kicking the tires of Tornado',
    author='Tim Sweetser',
    keywords='web tornado data-science',
    packages=find_packages(),
    install_requires=requires,
)
