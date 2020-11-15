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

        self.predmety = {
            0: {},
            1: {},
            2: {"kámen", "láhev"},
        }

        s = "sever"
        j = "jih"
        v = "východ"
        z = "západ"

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
            "s": "sever",
            "j": "jih",
            "v": "východ",
            "z": "západ"
        }

        while True:
            print(self.lokace[self.aktivni_lokace])

            if self.aktivni_lokace == 0:
                break

            moznosti = self.vychody[self.aktivni_lokace]
            dostupne_vychody = ", ".join(moznosti.keys())
            dostupne_predmety = ", ".join(self.predmety[self.aktivni_lokace])

            predmety_na_zemi = ("Na zemi vidíš " + dostupne_predmety)
            print(predmety_na_zemi)

            smer = input("Můžeš jít na " + dostupne_vychody + " ").lower()
            slova = smer.split()
            print("-"*40)

            if smer.startswith("jdi"):
                for slovo in slova:
                    # Zkontroluje, zda input obsahuje směr
                    if slovo in moznosti:
                        self.aktivni_lokace = moznosti[slovo]
                        break

                    # Přeloží 1 písmeno na směr
                    elif len(slovo) == 1:
                        for pismeno in slovnik:
                            if smer == pismeno:
                                self.aktivni_lokace = moznosti[slovnik[pismeno]]
                                break
                        break

                    elif smer == "exit":
                        print("S pláčem jsi utekl z lesního bludiště. Třeba se ti příště povede lépe!")
                        break
                else:
                    print("!!! Tudy se nedá jít !!!")
                    print("-" * 40)

            elif smer.startswith("polož"):
                predmet = input("Co chceš položit? ")
                self.predmety[self.aktivni_lokace].remove(predmet)

            else:
                print("Nerozuměl jsem. Zkus to znovu.")

