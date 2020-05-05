# Using ElementTree
import xml.etree.ElementTree as Et
import random


def how():
    doc = Et.parse("/Users/navkar14/Desktop/smart-learning/code/sentence/templates/exclamatory/how/how-literary.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for child in sentence:
            if child.tag=="PREFIX":
                arr1.append(child.text)
            if child.tag=="ADVERB":
                class0=child.attrib
                adverb_dict = open(
                    "/Users/navkar14/Desktop/smart-learning/code/sentence/adverb_dict"
                    "/adverb.txt")
                f1 = adverb_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))
            if child.tag == "PRONOUN":
                class0=child.attrib
                noun_dict = open(
                    "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                    "/pronouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))

                # arr1.append("your")
            if child.tag == "SNOUN":
                class0=child.attrib
                noun_dict = open(
                    "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                    "/proper_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[3:]))

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
                        break
                arr1.append(random.choice(temp[1:]))
            if child.tag == "ARTICLE":
                arr1.append("the")
            if child.tag=="CNOUN":
                class0 = child.attrib
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
            if child.tag=="CNOUN1":
                class0 = child.attrib
                noun_dict = open(
                    "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                    "/common_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")

                        break
                arr1.append(random.choice(temp[3:]))
        listToStr = ' '.join(map(str, arr1))
        if listToStr.find("!")==-1:
            listToStr+="!"
    return print(listToStr)

how()