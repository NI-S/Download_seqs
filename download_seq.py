from selenium.webdriver.common.keys import Keys     #hierdoor kan je tekst plaatsen op site
from selenium import webdriver  #hierdoor kan je zoeken op sites automatiseren
import os

"""chromedriver is nu voor chrome versie 83 (windows)
"""

class Uniprot:
    def __init__(self, bestand):
        print(os.path.abspath("chromedriver.exe").replace("\\", "/"))
        self.site = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe").replace("\\", "/"))
        self.bestand = open(bestand, "w")

    def __zoek_sequentie__(self, accessie):
        self.site.get("https://www.uniprot.org/")
        self.site.find_element_by_name("query").send_keys(accessie)
        self.site.find_element_by_id("search-button").click()
        try:
            print(self.site.find_element_by_class_name("entryID").text)
            self.site.find_element_by_partial_link_text(self.site.find_element_by_class_name("entryID").text).send_keys("\n")
            self.site.find_element_by_xpath('//*[@title="Sequence data in FASTA format"]').send_keys('\n')
            print(self.site.find_element_by_tag_name("body").text)
            self.bestand.writelines(self.site.find_element_by_tag_name("body").text + "\n")
        except:
            print("kon niet gevonden worden")


