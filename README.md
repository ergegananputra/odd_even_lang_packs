# Odd Even Language Packs

This repository contains language packs for the Odd Even application. These language packs provide translations for various languages to enhance the user experience.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install a language pack, follow these steps:
- Install the package using pip:
    ```sh
    pip install odd_even_lang_packs
    ```

## Example Usage

To use the `odd_even_lang_packs` package in your Python application, follow these steps:

1. Import the package in your Python code:
    ```python
    from odd_even_lang_packs import OddEvenLangPacks
    ```

2. Use the odd even language packs:
    ```python
    # Create the OddEvenLangPacks Object
    lang_pack = OddEvenLangPacks()

    # Change the language to Indonesia
    lang_pack.changeLanguage("ID")

    # Check odd or even and print the output in string text
    oddEvenText = lang_pack.check(4)

    print(oddEvenText)
    ```

## Contributing

We welcome contributions to improve and add new language packs. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature/new-language-pack
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Add new language pack for [Language]"
    ```
4. Push to the branch:
    ```sh
    git push origin feature/new-language-pack
    ```
5. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.