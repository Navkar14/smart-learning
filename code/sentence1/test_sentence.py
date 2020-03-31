import xml.dom.minidom
from xml.dom.minidom import Node
import random
import xlrd

class Simple:
    doc = xml.dom.minidom.parse("C:\\Users\\payal\\Desktop\\Navkar\\MAC\\Smart Learning\\simple0.xml")

    def sentence_no1(self0):
        for node in Simple.doc.getElementsByTagName("SENTENCE"):
            for