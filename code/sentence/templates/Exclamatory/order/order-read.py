# Using ElementTree
import xml.etree.ElementTree as Et
import random


def order():
    doc = Et.parse("/Users/navkar14/Desktop/smart-learning/code/sentence/templates/exclamatory/order/order-read.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for phrase in sentence:
            if phrase.tag=="ORDERPHRASE":
                for child in phrase:
                    if child.tag=="EXPRESSION":
                        arr1.append(child.text)
                    if child.tag == "PERSONALPRONOUN":
                        arr1.append("your")

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "/Users/navkar14/Desktop/smart-learning/code/sentence/verb_dict"
                            "/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[1:]))
                                break
                    if child.tag == "ARTICLE":
                        arr1.append("the")
                    if child.tag=="CNOUN":
                        class0 = child.attrib
                        temp = []
                        noun_dict = open(
                            "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                            "/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp=i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[3:]))
                                arr1.append("\b!")
                                break

        listToStr = ' '.join(map(str, arr1))
        return listToStr