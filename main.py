from download_seq import Uniprot
from MSA_creator import MSA
import re

def main():
    #accessies = set_accessie("accessie_opdr11.txt")
    #set_seq("sequentie_opdr1.txt", accessies)
    #accessies4 = set_accessie("accessie_opdr4.txt")
    #set_seq("sequentie_opdr4.txt", accessies4)
    maak_MSA("sequentie_opdr1.txt", "msa_clustalo.txt", "ClustalO")

def set_accessie(bestand):
    seq = open(bestand, "r")
    accessies = []
    for line in seq:
        line = line.strip("\n")
        line = re.sub(r"^(...)", "", line)
        line = line.replace("|", " ")
        accessies.append(line)
    return seq


def set_seq(bestand, accessies):
    uniprot = Uniprot(bestand)
    for accessie in accessies:
        uniprot.__zoek_sequentie__(accessie)

def maak_MSA(bestand, msa_bestand, site):
    seq = open(bestand, 'r')
    sequenties = seq.read()
    print(sequenties)
    msa = MSA(msa_bestand)
    msa.__maak_MSA__(site, sequenties)


main()