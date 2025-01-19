class OddEvenLangPacks:
    """Class to check if a number is odd or even in multiple languages

    Args:
        language (str, optional): language code. Defaults to "EN".

    Methods:
        changeLanguage: Change the language of the language pack
        check: Check if a number is odd or even and return the corresponding word
        checks: Check a list of numbers if they are odd or even
        isOdd: Check if a number is odd
        isEven: Check if a number is
        getLanguage: Get the current language
        getLanguageCodes: Get the list of available language codes
        getLanguageCodesAndFullNames: Get the list of available language codes and full names
    """
    def __init__(self, language : str = "EN") -> None:
        self.__lang_lists = {
            "EN" : ["eovdedn", 0, "English"],
            "ID" : ["ggaennjaipl", 1, "Indonesia"],
            "DK" : ["ulliiggee", 1, "Danish"],
        }
        self.changeLanguage(language)

    def changeLanguage(self, language : str) -> None:
        """Change the language of the language pack

        Args:
            language (str): language code
        """
        try:
            assert language in self.__lang_lists
        except AssertionError:
            print(f"Language {language} not found")
            return None

        self.__language = language

    def check(self, x : int) -> str:
        """Check if a number is odd or even and return the corresponding word

        Args:
            x (int): number to be checked

        Returns:
            str: odd or even in the selected language
        """
        lang, prefix, _ = self.__lang_lists[self.__language]
        return lang[((x + prefix) % 2)::2]
    
    def checks(self, arr : list) -> list[str]:
        """Check a list of numbers if they are odd or even

        Args:
            arr (list): list of numbers

        Returns:
            list[str]: list of odd or even in the selected language
        """
        return [self.check(x) for x in arr]
    
    def isOdd(self, x : int) -> bool:
        """Check if a number is odd

        Args:
            x (int): number to be checked

        Returns:
            bool: True if the number is odd, False otherwise
        """
        return x % 2 == 1
    
    def isEven(self, x : int) -> bool:
        """Check if a number is even

        Args:
            x (int): number to be checked

        Returns:
            bool: True if the number is even, False otherwise
        """
        return x % 2 == 0

    def getLanguage(self) -> str:
        """Get the current language

        Returns:
            str: language code
        """
        return self.__language
    
    def getLanguageCodes(self) -> list[str]:
        """Get the list of available language codes

        Returns:
            list[str]: list of language codes
        """
        return list(self.__lang_lists.keys())
    
    def getLanguageCodesAndFullNames(self) -> dict[str, str]:
        """Get the list of available language codes and full names

        Returns:
            dict[str, str]: dictionary of language codes and full names
        """
        return {code : self.__lang_lists[code][2] for code in self.__lang_lists}
