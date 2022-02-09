from os import path
import os
from pathlib import Path

print("""
     -----------------------------------------------------------
    |   Tervetuloa tekstitiedostojen puhdistus ohjelmaan!       |
    |               Toimintaperiaate on helppo!                 |
    | Sinä annat minulle tekstitiedoston ja teksti mitä haluat  |
    |   kyseisestä tiedostosta poistaa, minä teen loput.        |
     -----------------------------------------------------------                                                
""")

#kysytään tiedostopolut 

def alkufile():
    "Kysyy tiedostoa, josta haluaa poistaa."
    vaarin=True

    while vaarin:
        infile = input("Kerro tekstitiedoston polku, josta haluat poistaa: ")
        #tarkistetaan onko nämä olemassa
        if path.exists(infile) and infile.endswith(".txt"):
            vaarin=False       
        else:
            print("Muistathan, että tekstitiedoston pitää olla .txt muotoinen sekä tiedostopolun pitää olla oikea.")
    return infile

def outfile(infile):
    vaarin=True

    while vaarin:
        outfile =input("Anna puhtaan tekstitiedoston polku, johon voin kirjoittaa: ")
        #tarkistetaan, että tämä tiedosto on olemassa, eikä ole annettu kaksi samanlaista tiedostoa
        if path.exists(outfile) and outfile.endswith(".txt") and path.samefile(infile,outfile) ==False:
            vaarin=False
        else:
            print("Muistathan, että tekstitiedoston pitää olla .txt muotoinen sekä tiedostopolun pitää olla oikea, eikä saa olla sama tiedosto kuin jo antamasi tiedosto.")
    return outfile

#kysytään poistettava tieto ja tallennetaan listalle 
def anna_poistettava_tieto():
    "Kysyy poistettavia tietoja"
    jatka =True
    delete_list = []
    #Voi kokeilla kommenteissa alla olevalla listalla
    #delete_list = ["<st>", "<s>", "<t>", "<tn>", "</tn>", "</t>", "</st>", "</av>", "<av>", "<t taivutus=\"harvinainen\">", "<av astevaihtelu=\"valinnainen\">", "<t taivutus=\"mahdollinen\">", "<t taivutus=\"yksikössä\">", "<t taivutus=\"monikossa\">","</s>", "<hn>", "</hn>","A", "B", "C", "D", "E","F","G","H","I", "J","K","L","M"]
    #kysytään loopissa mitä haluaa poistaa tekstitiedostosta, annetaan myös mahdollisuus muokata poistettava lista
    while jatka:
        poistettava=input("Kirjoita mitä haluat poistaa tekstitiedostosta. Jos haluat poistua niin paina X. ")
        if poistettava.upper()=="X":
            while jatka:
                print("Poistettava tieto on "+ str(delete_list))
                korjaa=input("Haluatko muuttaa listaa Kyllä/k, Ei/e ")
                #muutetaan isoihin kirjaimiin, jotta isot ja pienet kirjaimet toimisi yhtä hyvin
                if korjaa.upper() =="KYLLÄ" or korjaa.upper()=="K":
                    poista=input("Mitä haluat poistaa: ")
                    #jos ei poistettava ei ole listalla niin otetaan kiinni exceptissa
                    try:
                        delete_list.remove(poista)
                        continue
                    except:
                        print("Jotain meni pieleen listasta poistossa... Tarkista oikeinkirjoitus ja yritä uudelleen.")

                elif korjaa.upper() =="EI" or korjaa.upper()=="E":
                    jatka=False
                    print("Eli jatkataan. Odota hetki...")
        #jos on kirjoitettu monta sanaa välilyönnillä erotettuna, lisätään nämäkin listalle
        try:
            poista=poistettava.split(" ")
            for x in poista:
                if x !="":
                    delete_list.append(x)
            
        except:
            print("Kirjoitathan kirjaimen tai numeron.")
    return delete_list

#avataan tiedostot ja käydään ne läpi
def poisto(infile, outfile, delete_list):

    with open(infile) as fin, open(outfile, "w+") as fout:
        #käydään tekstitiedoston rivi riviltä ja poistetaan delete_listalla esiintyviä sanoja
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "")
            fout.write(line)
    #suljetaan tiedosto
    fout.close()
    fin.close()
    print("Tehtävä suoritettu")

#tulostetaan tarvittaessa myös tiedoston nimi
def tulosta(outfile):
    tulosta=input("Haluatko katsoa miltä uusi tiedosto näyttää? K/E ")
    #jos haluaa avata niin avataan tiedosto ja luetaan se rivi riviltä
    if tulosta.upper()=="K":
        tiedosto_koko=os.path.getsize(outfile)
        kilobytes=tiedosto_koko*0.001
        print("Tiedoston koko on " + "{:.0f}".format(kilobytes)+" kilotavua." )
        if tiedosto_koko < 1000000:
            with open(outfile, 'r') as fin:
                for line in fin:
                    print(line)
                fin.close()
        else:
            print("Tiedosto on liian iso avattavaksi täällä. Suosittelen avaamaan tämän Notepadissa.")
    elif tulosta.upper()=="E":
        jatketaan=input("Lopetetaan. Jos haluatkin katsoa puhdistaa toisen tiedoston niin kirjoita K, enterilla lopetan")
        jatkuu=True
        while jatkuu:
            #jos halutaan aloittaa ohjelman alusta niin palautetaan main() metodille True, jolloin loop alkaa alusta
            if jatketaan.upper()=="K":
                return True
                break
            elif jatketaan=="":
                print("""
         -----------------------------------------------------------
        |                                                           |
        |                    Nähdään myöhemmmin!                    |
        |                                                           |
         -----------------------------------------------------------                                                 
    """)
                return False
                break
            else:
                print("En ymmärtänyt. Toistaisitko..")

def main():
    #Loopissa jotta pystyisi halutessaa aloittaa ohjelma alusta lopussa
    while True:
        infilex=alkufile()
        outfilex=outfile(infilex)
        poistettava=anna_poistettava_tieto()
        poisto(infilex, outfilex, poistettava)
        tulosta(outfilex)
        #jos halutaan aloittaa ohjelman alusta niin palautettu main() metodille True, jolloin loop alkaa alusta, jos False niin ohjelma hyppää loopista pois ja lopettaa ohjelman
        if tulosta(outfilex)==False:
            break

if __name__ == "__main__":
    main()
    