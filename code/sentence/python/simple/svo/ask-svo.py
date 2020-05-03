import xml.etree.ElementTree as Et
import random


class AskSvo:
    doc = Et.parse("C:/Users/lenova/Desktop/FYP/smart-learning-master/code/sentence/templates/simple/svo/Ask.xml")
    root = doc.getroot()
    def asksvo(self):
        for sentence in AskSvo.root:
            arr0 = []  # for storing class and tags
            arr1 = []  # for storing sentence

            for phrase in sentence:
                if phrase.tag == "SUBJECTPHRASE":
                    for child in phrase:
                        if child.tag == "SNOUN":
                            class0 = child.attrib
                            if class0["class"] == "name":
                                noun_dict = open(
                                    "C:/Users/lenova/Desktop/FYP/smart-learning-master/code/sentence/noun_dict"
                                    "/proper_nouns.txt")

                                f1 = noun_dict.readlines()
                                for i in f1:
                                    if i.find(class0["class"] + ":", 0) == 0:
                                        temp = i.split(":")
                                        arr0.extend(temp[3:-1])
                                arr1.append(random.choice(arr0))

                if phrase.tag == "VERBPHRASE":
                    for child in phrase:
                        if child.tag == "VERB":
                            class0 = child.attrib
                            verb_dict = open(
                                "C:/Users/lenova/Desktop/FYP/smart-learning-master/code/sentence/verb_dict"
                                "/verbs.txt")
                            f1 = verb_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    break
                            arr0=[]
                            arr1.append(random.choice(temp[1:-1]))

                        if child.tag == "CNOUN":
                            class0 = child.attrib
                            noun_dict = open(
                                "C:/Users/lenova/Desktop/FYP/smart-learning-master/code/sentence/noun_dict"
                                "/common_nouns.txt")
                            f1 = noun_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    arr1.append(random.choice(temp[1:-1]))

                        if child.tag == "PREPOSITION":
                            class0 = child.attrib
                            arr1.append("in")

                        if child.tag == "ARTICLE1":
                            class0 = child.attrib
                            arr1.append("the")

                        if child.tag == "CNOUN1":
                            class0 = child.attrib
                            noun_dict = open(
                                "C:/Users/lenova/Desktop/FYP/smart-learning-master/code/sentence/noun_dict"
                                "/common_nouns.txt")
                            f1 = noun_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) >= 0:
                                    temp = i.split(":")
                                    arr1.append(random.choice(temp[1:-1]))

                            listToStr = ' '.join(map(str, arr1))
                            return listToStr
    asksvo()