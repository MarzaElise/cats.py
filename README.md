# cats.py

A synchronous, object oriented API wrapper for [thecatapi](https://thecatapi.com)

## Table Of Content

- [cats.py](#catspy)
  - [Table Of Content](#table-of-content)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [FAQ](#faq)
  - [What's new](#whats-new)
  - [License](#license)

## Installation

- Install it from [pypi](https://pypi.org/project/cats.py)

   ```shell
   pip install cats.py
   ```

- To install the development version,
clone this repository and install it. You need [git](https://git-scm.com) installed for this

   ```shell
   pip install git+https://github.com/MarzaElise/cats.py.git
   ```

## Usage

If you don't already have an API key, get one [here](https://thecatapi.com/)

```py
from cats import Client

client = Client(api_key="YOUR API KEY HERE")

breed = client.search_breed("beng")

print(breed)
```

The above code should print something similar to this

[![screenshot](https://media.discordapp.net/attachments/887217168276656191/896471930557853736/unknown.png?width=1024&height=131)](https://media.discordapp.net/attachments/887217168276656191/896471930557853736/unknown.png?width=1024&height=131)

For async support, import `Client` from `async_cats` instead of `cats`.

More usage examples can be found [here](./examples)

## Contributing

This module/repository is new and might break at any moment. Which is why all pull requests that bring
good changes are welcome.

If you are new to github and wondering how to contribute, click [here](https://github.com/firstcontributions/first-contributions)

If you are confused on what would be a good contribution, take a look at the open [issues](https://github.com/MarzaElise/cats.py/issues)

## FAQ

1. Are all endpoints supported?

   - All of the endpoints except for images/upload works perfectly as I tested them locally before publishing
   - All `breeds/` endpoints might break since the API is constantly adding new properties

2. Why is `utils/_dataclasses.py` such a code-gore?

   - Data returned by the API is inconsistent. For example, some properties are sometimes given and
    sometimes not. To manage that I set them all to None by default

3. How is this wrapper object oriented?

   - All values returned by each method has its own class (Breed, Vote, Favourite etc)
   - This entire wrapper revolves around dataclasses and subclassing

4. I found a bug, how do I report?

   - You can contact me on discord at [Marcus | Bot Dev#4438](https://discord.com/users/754557382708822137)
   - If you are not on discord, open a new [issue](https://github.com/MarzaElise/cats.py/issues)
   - If you also have a fix for it, create a new pull request and I'll merge it if its good. (See [Contributing](#contributing))

5. Will there be an async version of this?

   - I currently have no plans to do it in the near future. If you really want an asynchronous wrapper,
   take a look at [catapi.py](https://github.com/ephreal/catapi.py)

6. Is this wrapper consistent?

   - I tried my best to keep this wrapper consistent with the API itself. By returning lists when API
     returns an array etc.

7. Where is the documentation?

   - Currently, there is no documentation for this wrapper. Alternatively, you can take a look at the
     [API documentation](https://docs.thecatapi.com) and the source to figure out some stuff.

8. Who asked?

   - [I](https://discord.com/users/754557382708822137) did

Note: all changes were tested on python 3.10.0 64-bit before being published

## What's new

- Support for asynchronous environment
- New `async_cats` package

## License

GNU AGPLv3
