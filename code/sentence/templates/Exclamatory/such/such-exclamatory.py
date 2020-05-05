# Using ElementTree
import xml.etree.ElementTree as Et
import random


def such():
    doc = Et.parse("/Users/navkar14/Desktop/smart-learning/code/sentence/templates/exclamatory/such/such-exclamatory.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)
            if phrase.tag == "EXPRESSION":
                arr1.append(phrase.text)
            if phrase.tag == "ARTICLE":
                arr1.append("a")
            if phrase.tag=="ADJECTIVE":
                class0=phrase.attrib
                temp=[]
                adj_dict = open(
                    "/Users/navkar14/Desktop/smart-learning/code/sentence/adjective_dict"
                    "/adjective-exclamatory.txt")
                f1 = adj_dict.readlines()
                for i in f1:
                    if i.find(class0["class"]+":",0) ==0:
                        t1=i.split(":")
                        temp.append(t1[1])
                for i in f1:
                    if i.find(class0["class"]+":",0) ==0:
                        arr0.append(random.choice(temp))
                        if i.find(arr0[0]+":",0)>=0:
                            temp=i.split(":")
                            temp.remove("\n")
                            arr1.append(random.choice(temp[2:]))
                            break

            if phrase.tag=="SNOUN":
                class0 = phrase.attrib
                temp = []
                noun_dict = open(
                    "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                    "/common_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:

                    if i.find(class0["class"] + ":", 0) >= 0:
                        if i.find(arr0[0]+":",0)>=0:
                            temp=i.split(":")
                            temp.remove("\n")
                            arr1.append(random.choice(temp[3:]))
                            arr1.append("\b!")
                            break

        listToStr = ' '.join(map(str, arr1))

    return listToStr
such()