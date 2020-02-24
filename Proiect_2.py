#Un pachet de carti are 52 de carti!!!!!!

import random


class Carte:
    def __init__(self):
        self.tip_carte = ''
        self.valoare = 0
        #Fiecare carte are o valoare si un tip.
    def creare_carte(self, tip, valoare):
        self.tip_carte = tip
        self.valoare = valoare





class Pachet(Carte):
    def __init__(self):
        super().__init__()
        self.pachet=[]
        self.pachet_1=[]
        self.pachet_2=[]
        #pachet_1 si pachet_2 reprezinta pachetele ce vor fi date celor 2 jucatori

    def construieste_pachet(self):
        tip_carte = ['romb', 'trefla', 'inima rosie', 'inima neagra']
        #tip_carte = lista cu tipurile de carti existente in pachet
        carte = Carte()
        l = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
        #l = lista cu valorile ce le poate lua o carte

        for j in tip_carte:
            for i in l:
                carte.creare_carte(j, i)
                c = []
                #c = cartea ce este definita ca o lista ce contine tipul cartii si valoarea acesteia
                c.append(carte.tip_carte)
                c.append(carte.valoare)
                self.pachet.append(c)
                #Adaugam fiecare carte in pachetul initial de 52 de carti.
        return self.pachet




    def amesteca_pachet(self):
        random.shuffle(self.pachet)
        print("Pachetul initial a fost amestecat: \n", self.pachet)




    def trage_carte(self):
        print(self.pachet.pop(0))
        #cu ajutorul functiei trage_carte() scoatem cate o carte din pachetul de 52 de carti



    def formeaza_pachet(self, nr):
        for i in range(0,len(self.pachet)):
            if i%2 == 0:
                self.pachet_1.append(self.pachet.pop(0))
            else:
                self.pachet_2.append(self.pachet.pop(0))
            #impartirea cartilor se face dand cate o carte pe ran fiecarui jucator
        if nr == 1:
            return self.pachet_1
            #pachet_1 este pachetul pe care il primeste primul jucator dupa impartirea tuturor cartilor
        else:
            return self.pachet_2
            #pachet_2 este pachetul pe care il primeste cel de-al doilea jucator dupa impartirea tuturor cartilor




class Jucator(Pachet):
    def __init__(self, p , nume):
        self.pachet_jucator = p
        self.nume = nume


    def trage_carte(self):
        return self.pachet_jucator.pop(0)
        #cu ajutorul functiei trage_carte() scoatem cate o carte din pachetul jucatorului


    def joaca_carte(self, jucator_2):
        lista_runda = []
        #lista_runda = lista in care vom pune toate cartile care se joaca in acea runda
        print("\n\n\n\nSA INCEAPA JOCUL!\n\n\n")
        while (len(self.pachet_jucator) > 0 and len(jucator_2.pachet_jucator) > 0):
            c1 = self.trage_carte()
            c2 = jucator_2.trage_carte()
            #fiecare jucator va trage cate o carte
            lista_runda.append(c1)
            lista_runda.append(c2)
            #adaugam cartile trase in lista de carti jucate in acea runda
            if c1[1] == c2[1]:
                val = c1[1]
                #folosim variabila val, deoarece valoarea lui c1 se modifica de fiecare data cand tragem alta carte
                print("\n#####################################################################################################################################################################################")
                print("\nEGALITATE! Acum incepe jocul de RAZBOI!")
                print("Cartile pentru care se joaca RAZBOI sunt:")
                print(c1)
                print(c2)
                print("Fiecare jucator va pune pe masa", val, "carti!")
                contor = 0
                #folosim contorul pentru a pune jos un numar de carti egal cu valoarea cartii pentru care se joaca razboi
                for i in range(val):
                    contor = contor + 1
                    if self.pachet_jucator != [] and contor < val:
                        c1 = self.trage_carte()
                        lista_runda.append(c1)
                    if jucator_2.pachet_jucator != [] and contor < val:
                        c2 = jucator_2.trage_carte()
                        lista_runda.append(c2)
                for i in range(val):
                    if i == 0:
                        print("Se pune jos prima carte.")
                    else:
                        print("Se pune jos a ", i+1 , "-a carte.")
                print("\nSfarsitul razboiului!")
                print("\n#####################################################################################################################################################################################\n")
            else:
                print("\n#####################################################################################################################################################################################")
                print("\nLUPTA SIMPLA\nSe joaca urmatoarele carti:")
                print(c1)
                print(c2)


            if c1[1] > c2[1]:
                self.pachet_jucator = self.pachet_jucator + lista_runda
                print("Cartile jucate in aceasta runda sunt: ", lista_runda)
                print("Jucatorul", self.nume.upper(), "a castigat runda!")
                print("\n#####################################################################################################################################################################################")

            else:
                jucator_2.pachet_jucator = jucator_2.pachet_jucator + lista_runda
                print("Cartile jucate in aceasta runda sunt: \n", lista_runda)
                print("Jucatorul", jucator_2.nume.upper(), "a castigat runda!")
                print("\n#####################################################################################################################################################################################")
            lista_runda.clear()
            #La sfarsitul rundei golim lista de carti jucate.
            #In continuare, vom afisa pachetul de carti al fiecarui jucator si numarul de carti din pachet.
            print("\n\nJucatorul ",self.nume, "are urmatoarele carti:")
            print(self.pachet_jucator)
            print("Total carti: ", len(self.pachet_jucator))
            print("\nJucatorul ",jucator_2.nume, "are urmatoarele carti:")
            print(jucator_2.pachet_jucator)
            print("Total carti: ",len(jucator_2.pachet_jucator))
            print("\n")


        print("\n\n\n#####################################################################################################################################################################################")
        print("\n                                                                                 FINAL JOC!")
        if len(self.pachet_jucator) != 0:
            print("                                                                        Castigatorul jocului este: ", self.nume)
        else:
            print("                                                                        Castigatorul jocului este: ", jucator_2.nume)
        print("\n#####################################################################################################################################################################################")





#Construirea pachetului cu cele 52 de carti:
pachet = Pachet()
p = pachet.construieste_pachet()
print("Pachetul initial este:\n",pachet.pachet)
#Amestecarea pachetului:
pachet.amesteca_pachet()
pachet1 = pachet.formeaza_pachet(1)
pachet2  = pachet.formeaza_pachet(2)

#Numele celor 2 jucatori vor fi introduse de la tastatura.
nume1 = input("\nIntroduceti numele primului jucator: ")
nume2 = input("Introduceti numele celui de-al doilea jucator: ")
jucator1 = Jucator(pachet1, nume1)
jucator2 = Jucator(pachet2, nume2)
print("\nJucatorul", jucator1.nume, "are urmatorul pachet:\n",jucator1.pachet_jucator)
print("\nJucatorul", jucator2.nume, "are urmatorul pachet:\n",jucator2.pachet_jucator)
jucator1.joaca_carte(jucator2)

