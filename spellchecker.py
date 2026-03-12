import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiD = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn)
        words = txtIn.split()
        start_time = time.perf_counter()
        lista = self.multiD.searchWord(words, language)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print("Using contains")
        errori = 0
        for w in lista:
            if not w.corretta:
                print(w)
                errori += 1
        print(f"Numero di errori: {errori}")
        print(f"Time elapsed: {elapsed_time}")

        # --- AGGIUNTA ESERCIZIO 2: LINEAR SEARCH ---
        # Recupero il dizionario corretto dal MultiDictionary
        if language.lower() == "italian":
            target_dict = self.multiD.italiano
        elif language.lower() == "english":
            target_dict = self.multiD.english
        else:
            target_dict = self.multiD.spanish

        start_time_lin = time.perf_counter()
        errori_lin = []
        for parola in words:
            found = False
            # Iterare su tutti gli elementi del vocabolario
            for d_word in target_dict:
                if d_word == parola:
                    found = True
                    break
            if not found:
                errori_lin.append(parola)
        end_time_lin = time.perf_counter()

        print(f"------------------------------")
        print("Using Linear search")
        for err in errori_lin:
            print(err)
        print(f"Numero di errori: {len(errori_lin)}")
        print(f"Time elapsed: {end_time_lin - start_time_lin}")

        # --- AGGIUNTA ESERCIZIO 2: DICHOTOMIC SEARCH ---
        start_time_dic = time.perf_counter()
        errori_dic = []
        for parola in words:
            found = False
            low = 0
            high = len(target_dict) - 1
            # La ricerca viene ripetuta iterativamente fino a trovare l'elemento o scartarli tutti
            while low <= high:
                mid = (low + high) // 2  # Inizia dall'elemento centrale
                if target_dict[mid] == parola:
                    found = True
                    break
                elif target_dict[mid] < parola:  # Se inferiore, cerca nella metà successiva
                    low = mid + 1
                else:  # Se superiore, cerca nella metà precedente
                    high = mid - 1
            if not found:
                errori_dic.append(parola)
        end_time_dic = time.perf_counter()

        print(f"------------------------------")
        print("Using Dichotomic search")
        for err in errori_dic:
            print(err)
        print(f"Numero di errori: {len(errori_dic)}")
        print(f"Time elapsed: {end_time_dic - start_time_dic}")
        print(f"------------------------------")

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