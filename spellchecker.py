import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiD = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn)
        words = txtIn.split()
        start_time = time.time()
        lista = self.multiD.searchWord(words, language)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Using contains")
        errori = 0
        for w in lista:
            if not w.corretta:
                print(w)
                errori += 1
        print(f"Numero di errori: {errori}")
        print(f"Time elapsed: {elapsed_time}")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text