from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
desc = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="cats.py",
    version="0.1.6",
    description="A synchronous, object oriented API wrapper for thecatapi",
    long_description=desc,
    long_description_content_type="text/markdown",
    url="https://github.com/MarzaElise/cats.py",
    author="Marcus",
    license="GNU AGPLv3",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=["aiohttp", "pydantic"],
    packages=find_packages(
        include=["cats", "cats.*"], exclude=["__pycache__"]
    ),
)
