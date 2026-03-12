import dictionary as d
import richWord as rw

import resources as r


class MultiDictionary:

    def __init__(self):
       self.italiano = d.Dictionary().loadDictionary(r"Italian.txt")
       self.english = d.Dictionary().loadDictionary(r"English.txt")
       self.spanish = d.Dictionary().loadDictionary(r"Spanish.txt")

    def printDic(self, language):
        if language.lower() == "italian":
            for parola in self.italiano:
                print(f"{parola}")
        elif language.lower() == "english":
            for parola in self.english:
                print(f"{parola}")
        elif language.lower() == "spanish":
            for parola in self.spanish:
                print(f"{parola}")
        else:
            print("Lingua non trovata")

    def searchWord(self, words, language):
        listaRich = []
        if language.lower() == "italian":
            for parola in words:
                if parola in self.italiano:
                    parolaRicca = rw.RichWord(parola)
                    parolaRicca.corretta = True
                    listaRich.append(parolaRicca)
                else:
                    parolaRicca = rw.RichWord(parola)
                    parolaRicca.corretta = False
                    listaRich.append(parolaRicca)
        elif language.lower() == "english":
            for parola in words:
                if parola in self.english:
                    parolaRicca = rw.RichWord(parola)
                    parolaRicca.corretta=True
                    listaRich.append(parolaRicca)
                else:
                    parolaRicca = rw.RichWord(parola)
                    parolaRicca.corretta=False
                    listaRich.append(parolaRicca)
        elif language.lower() == "spanish":
            for parola in words:
                if parola in self.spanish:
                    parolaRicca = rw.RichWord(parola)
                    parolaRicca.corretta = True
                    listaRich.append(parolaRicca)
                else:
                    parolaRicca = rw.RichWord(parola)
                    parolaRicca.corretta = False
                    listaRich.append(parolaRicca)
        else:
            print("Lingua non trovata")
        return listaRich



