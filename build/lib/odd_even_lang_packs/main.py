class OddEvenLangPacks:
    def __init__(self, language : str = "EN") -> None:
        self.lang_lists = {
            "EN" : ["eovdedn", 0, "English"],
            "ID" : ["ggaennjaipl", 1, "Indonesia"],
        }
        self.changeLanguage(language)

    def changeLanguage(self, language : str) -> None:
        try:
            assert language in self.lang_lists
        except AssertionError:
            print(f"Language {language} not found")
            return None

        self.language = language

    def check(self, x : int) -> str:
        lang, prefix, _ = self.lang_lists[self.language]
        return lang[((x + prefix) % 2)::2]
    
    def checks(self, arr : list) -> str:
        return [self.check(x) for x in arr]
    
    def isOdd(self, x : int) -> bool:
        return x % 2 == 1
    
    def isEven(self, x : int) -> bool:
        return x % 2 == 0

