from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
desc = (here / 'README.md').read_text(encoding='utf-8')


setup(
    name="cats",
    version="0.0.1",
    description="A synchronous, object oritented API wrapper for thecatapi",
    long_description=desc,
    long_description_content_type='text/markdown',
    url="https://github.com/MarzaElise/cats.py",
    author='M-a-r-c-u-s',
    license='GNU AGPLv3',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=["requests"],
    packages=find_packages(include=['cats', 'cats.*'], exclude=["__pycache__"]),
)