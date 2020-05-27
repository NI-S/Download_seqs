from download_seq import Uniprot
import re

#eerste_seq = open("accessie_opdr1.txt", "r")
vierde_seq = open("accessie_opdr4.txt", "r")
accessies = []
for line in vierde_seq:
    #print(line)
    line = line.strip("\n")
    line = re.sub(r"^(...)", "", line)
    line = line.replace("|", " ")
    #print(line)
    accessies.append(line)

#uniprot = Uniprot("sequentie_opdr1.txt")
uniprot = Uniprot("sequentie_opdr4.txt")
for accessie in accessies:
    uniprot.__zoek_sequentie__(accessie)