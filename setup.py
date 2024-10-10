from setuptools import setup, find_packages

setup(
    name='pocwatchdog',
    version='1.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "schedule>=1.1.0",
    ],
)
