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

    #ESERCIZIO 2
    def searchWordLinear(self, words, language):
        target_dict = self._get_target_dict(language)
        listaRich = []
        for parola in words:
            pw = rw.RichWord(parola.lower())
            found = False
            for d_word in target_dict:  # Ricerca lineare: uno per uno [cite: 134, 135]
                if d_word == pw._parola:
                    found = True
                    break
            pw.corretta = found
            listaRich.append(pw)
        return listaRich

    def searchWordDichotomic(self, words, language):
        target_dict = self._get_target_dict(language)
        listaRich = []
        for parola in words:
            pw = rw.RichWord(parola.lower())
            found = False
            low, high = 0, len(target_dict) - 1
            while low <= high:  # Ricerca dicotomica: divide a metà [cite: 137, 138]
                mid = (low + high) // 2
                if target_dict[mid] == pw._parola:
                    found = True
                    break
                elif target_dict[mid] < pw._parola:
                    low = mid + 1
                else:
                    high = mid - 1
            pw.corretta = found
            listaRich.append(pw)
        return listaRich

    def _get_target_dict(self, language):
        if language.lower() == "italian": return self.italiano
        if language.lower() == "english": return self.english
        return self.spanish



