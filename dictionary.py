class Dictionary:

    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split()
                    self._dict.append(parts)
            return self._dict
        except FileNotFoundError:
            print(f"File {dict} non trovato.")
            return []

    def printAll(self):
        for parola in self._dict:
            print(f"{parola}")

    @property
    def dict(self):
        return self._dict