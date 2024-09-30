from setuptools import setup, find_packages

setup(
    name='eastTesterScpi',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pyserial'],
    entry_points='''
        [console_scripts]
        configure-load=eastTester.cli:main
    ''',
)
