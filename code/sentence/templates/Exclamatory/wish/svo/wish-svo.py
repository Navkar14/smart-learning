# import xml.dom.minidom
# Using ElementTree
import xml.etree.ElementTree as Et
import random


def wish_svo():
    doc = Et.parse("/Users/navkar14/Desktop/smart-learning/code/sentence/templates/exclamatory/wish-exclamatory.xml")
    root = doc.getroot()
    for sentence in root:
        arr0 = []
        arr1 = []
        gender_list = ["male", "female"]
        for phrase in sentence:
            if phrase.tag == "SUBJECTPHRASE":
                class0 = phrase.attrib
                noun_dict = open(
                    "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                    "/abstract.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) == 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        arr0.append(random.choice(temp[1:]))
                        arr0.append("\b,")
                        arr1.append(temp[0])
            if phrase.tag == "SNOUN":
                class0 = phrase.attrib
                if  class0["class"] == "name":
                    class0 = phrase.attrib
                    noun_dict = open(
                        "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                        "/proper_nouns.txt")

                    f1 = noun_dict.readlines()
                    for i in f1:
                        if i.find(class0["class"] + ":", 0) == 0:
                            if i.find(random.choice(gender_list), 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                arr0.append(random.choice(temp[3:]))
                                arr0.append("\b!")
                                t=random.choice(temp[3:])
                                arr1.append(temp[1])
                                listToStr0 = ' '.join(map(str, arr0))
                                print(listToStr0)
                                break
