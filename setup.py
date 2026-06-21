from setuptools import setup, find_packages

setup(
    name="pysimplecore",
    version="0.0.2",
    author="mreliseyyt",
    author_email="mail@mreliseyyt.ru",
    description="Легковесная утилитарная библиотека для Python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mreliseyyt/pysimplecore",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)