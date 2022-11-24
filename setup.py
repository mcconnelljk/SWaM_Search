import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='swam_search',
                 packages=['src'],
                 install_requires=install_requires)