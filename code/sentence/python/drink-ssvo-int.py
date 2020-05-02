# import xml.dom.minidom
# Using ElementTree
import xml.etree.ElementTree as Et
import random


class DrinkSsvoInt:
    doc = Et.parse("/Users/navkar14/Desktop/smart-learning/code/sentence/templates/interrogative/What/ssvo/drink.xml")
    # doc = Et.parse("C:\\Users\\payal\\Desktop\\Navkar\\Smart_Learning\\code\\sentence\\templates\\simple0.xml")
    root = doc.getroot()

    # print(root.tag)
    # print(root.attrib)
    # print(et.tostring(root, encoding='utf8').decode('utf8'))
    # print([elem.tag for elem in root.iter()])
    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]
        # print(sentence.tag)
        # print(sentence.attrib)
        # print()
        for phrase in sentence:
            # print(phrase.tag)
            # print(phrase.attrib)
            # print()
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text) #adding "what"
                print(arr1)
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0=child.attrib
                        verb_dict = open(
                            "/Users/navkar14/Desktop/smart-learning/code/sentence/verb_dict"
                            "/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                # print(temp)
                                break

                        arr1.append(random.choice(temp[1:]))
                        print(arr1)
                    if child.tag == "SNOUN":
                        class0 = child.attrib

                        noun_dict = open(
                            "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                            "/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                                # print(arr0)
                        # print(arr0)
                        arr1.append(random.choice(arr0))
                        arr1.append("and")
                        print(arr1)
                        arr0.remove(arr1[2])
                        arr1.append(random.choice(arr0))
                        print(arr1)

            if phrase.tag == "VERBPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0=child.attrib
                        verb_dict = open(
                            "/Users/navkar14/Desktop/smart-learning/code/sentence/verb_dict"
                            "/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                # print(temp)
                                break
                        arr0=[]
                        arr1.append(random.choice(temp[1:]))
                        print(arr1)

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                    if child.tag == "PREPOSITION":
                        class0=child.attrib
                        arr1.append("at")
                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                            "/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[3:]))
                        arr1.append("?")
                        print(arr1)
        listToStr = ' '.join(map(str, arr1))
        print(listToStr)