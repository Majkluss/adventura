class Hra:
    def __init__(self):
        self.lokace = {
            0: "Propast\n\nVe tmě sis nevšiml propasti před sebou a spadl do ní. Smůla.",
            1: "Lesní křižovatka\n\nStojíš na lesní křižovatce, která se rozděluje do všech stran.",
            2: "Dům\n\nStojíš před domem, který jsi našel hluboko v lese. Okenice jsou rozlámané a barva z dřevěné fasády je již dávno oprýskaná.",
            3: "Les\n\nStojíš po kotníky v lesním porostu a spadaném listí. Brzký podzim se podepsal na barvách okolního světa.",
            4: "Jeskyně\n\nStojíš v prostorné jeskyni. U začouzené stěny je vidět pozůstatek ohniště. Konec jeskyně se ztrácí ve tmě.",
            5: "Zničený most\n\nStojíš před zničeným mostem. Tady nic nenaděláš, leda bys chtěl přeskočit řeku."
        }

        s = "SEVER"
        j = "JIH"
        v = "VÝCHOD"
        z = "ZÁPAD"

        self.vychody = {
            0: {},
            1: {z: 2, v: 3, s: 5, j: 4},
            2: {s: 5, j: 4, v: 1},
            3: {z: 1},
            4: {s: 1, z: 2, j: 0},
            5: {z: 2, j: 1}
        }
        self.aktivni_lokace = 1

    def hra(self):
        """ Vypíše dostupné směry pro aktivní lokaci """

        slovnik = {
            "S": "SEVER",
            "J": "JIH",
            "V": "VÝCHOD",
            "Z": "ZÁPAD"
        }

        while True:
            moznosti = self.vychody[self.aktivni_lokace]
            dostupne_vychody = ", ".join(moznosti.keys())

            print(self.lokace[self.aktivni_lokace])

            if self.aktivni_lokace == 0:
                break

            smer = input("Můžeš jít na " + dostupne_vychody + " ").upper()
            slova = smer.split()
            print("-"*40)

            for slovo in slova:
                if slovo in moznosti:
                    self.aktivni_lokace = moznosti[slovo]
                    break

                elif len(slovo) == 1:
                    for pismeno in slovnik:
                        if smer == pismeno:
                            self.aktivni_lokace = moznosti[slovnik[pismeno]]
                            break
                    break

                elif smer == "EXIT":
                    print("S pláčem jsi utekl z lesního bludiště. Třeba se ti příště povede lépe!")
                    break
            else:
                print("!!! Tudy se nedá jít !!!")
                print("-" * 40)


