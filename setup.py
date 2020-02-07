from setuptools import setup, find_packages

setup(
    name='candles',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Team 22 Analyse Sprint',
    long_description=open('README.md').read(),
    install_requires=["numpy", "pandas"],
    url='https://github.com/Mikentosh/Eskom_Team_22',
    author='EDSA Team 22',
    author_email='<Your Email>'
)