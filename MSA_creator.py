from selenium import webdriver  #hierdoor kan je zoeken op sites automatiseren
import os


class MSA:
    def __init__(self, bestand):
        print(os.path.abspath("chromedriver.exe").replace("\\", "/"))
        self.site = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe").replace("\\", "/"))
        self.bestand = open(bestand, "w")

    def __maak_MSA__(self, site, sequenties):
        if site.__eq__("ClustalO"):
            self.site.get("https://www.ebi.ac.uk/Tools/msa/clustalo/")
            self.site.find_element_by_id("sequence").send_keys(sequenties)
            self.site.find_element_by_xpath("//input[@type='submit' and @value='Submit']").send_keys('\n')
            self.site.implicitly_wait(50)
            self.site.find_element_by_id("alnFile").send_keys("\n")
            print(self.site.find_element_by_tag_name("body").text)
            self.bestand.writelines(self.site.find_element_by_tag_name("body").text + "\n")