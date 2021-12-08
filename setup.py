
from setuptools import setup

setup(
    name='awesome',
    version='0.1.0',
    author='An Awesome Coder',
    author_email='aac@example.com',
    packages=['awesome'],
    url='http://github.com/bonartm/awesome-project',
    license='LICENSE',
    description='An awesome package that does something',
    long_description=open('README.md').read(),

    install_requires=[
        "pandas", "seaborn", "scikit-learn",
    ],
)
