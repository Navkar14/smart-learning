import xml.etree.ElementTree as Et
import random


def comp0():
    doc = Et.parse("/Users/navkar14/Desktop/smart-learning/code/sentence/templates/compound/buy.xml")
    root = doc.getroot()
    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "INDCLAUSE":
                for child in phrase:
                    if child.tag == "SUBJECTPHRASE":
                        for subchild in child:
                            if subchild.tag == "SNOUN":
                                genderlist = ["male","female"]
                                class0 = subchild.attrib
                                noun_dict = open(
                                    "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict/proper_nouns.txt")
                                f1 = noun_dict.readlines()
                                for i in f1:
                                    if i.find(class0["class"] + ":", 0) == 0:
                                        if i.find(random.choice(genderlist), 0) >= 0:
                                            temp = i.split(":")
                                            temp.remove('\n')
                                            arr1.append(random.choice(temp[3:]))

                            if subchild.tag=="PRONOUN":
                                class0 = subchild.attrib
                                noun_dict = open(
                                    "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict/pronouns.txt")
                                f1 = noun_dict.readlines()
                                for i in f1:
                                    if i.find(class0["class"] + ":", 0) == 0:
                                        temp = i.split(":")
                                        temp.remove('\n')
                                        arr1.append(random.choice(temp[2:]))

                    if child.tag == "VERBPHRASE":
                        for subchild in child:
                            class0 = subchild.attrib
                            verb_dict = open(
                                "/Users/navkar14/Desktop/smart-learning/code/sentence/verb_dict/verbs.txt")
                            f1 = verb_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    temp.remove('\n')
                                    arr1.append(random.choice(temp[1:]))


                    if child.tag == "OBJECTPHRASE":
                        for subchild in child:
                            if subchild.tag == "PREPOSITION":
                                class0 = subchild.attrib
                                arr1.append('to')
                            if subchild.tag == "ARTICLE":
                                class0 = subchild.attrib
                                arr1.append('the')

                            if subchild.tag == "CNOUN":
                                class0 = subchild.attrib
                                noun_dict = open(
                                    "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict/common_nouns.txt")
                                f1 = noun_dict.readlines()
                                for i in f1:
                                    if i.find(class0["class"] + ":", 0) >= 0:
                                        temp = i.split(":")
                                        temp.remove('\n')
                                        arr1.append(random.choice(temp[3:]))
            if phrase.tag == "CONJUNCTION":
                    arr1.append('and')
            if phrase.tag == "DEPCLAUSE":

                for child in phrase:

                    if child.tag == "VERBPHRASE":
                        for subchild in child:
                            if subchild.tag == "VERB":
                                class0 = subchild.attrib
                                arr0.append(class0["class"])
                                verb_dict = open(
                                    "/Users/navkar14/Desktop/smart-learning/code/sentence/verb_dict/verbs.txt")
                                f1 = verb_dict.readlines()
                                for i in f1:
                                    if i.find(class0["class"] + ":", 0) == 0:
                                        temp = i.split(":")
                                        temp.remove('\n')
                                        arr1.append(random.choice(temp[1:]))



                    if child.tag == "OBJECTPHRASE":
                        for subchild in child:

                            if subchild.tag == "ADVERB":
                                class0 = subchild.attrib
                                adverb_dict = open(
                                    "/Users/navkar14/Desktop/smart-learning/code/sentence/adverb_dict/adverb.txt")
                                f1 = adverb_dict.readlines()
                                for i in f1:
                                    if i.find(class0["class"] + ":", 0) >= 0:
                                        temp = i.split(":")
                                        temp.remove('\n')
                                        arr1.append(random.choice(temp[2:]))

                            if subchild.tag == "CNOUN":
                                class0 = subchild.attrib
                                noun_dict = open(
                                    "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict/common_nouns.txt")
                                f1 = noun_dict.readlines()
                                for i in f1:
                                    if i.find(class0["class"] + ":", 0) >= 0:
                                        if i.find(arr0[0]+":",0) >=0:
                                            temp = i.split(":")
                                            temp.remove('\n')
                                            arr1.append(random.choice(temp[3:]))
                                            # print(arr1)

                            if subchild.tag == "COLNOUN":
                                noun_rel_dict = open(
                                    "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict/noun_relation.txt")
                                f1 = noun_rel_dict.readlines()
                                for i in f1:
                                    class0 = arr1[-1]
                                    if i.find(class0+":", 0) >= 0:
                                        temp = i.split(":")
                                        temp.remove('\n')
                                        class0=temp[0]
                                        print(class0)
                                        coll_dict = open("/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict/collective_nouns.txt")
                                        f2 = coll_dict.readlines()
                                        for j in f2:
                                            if j.find(class0+":",0)>=0:
                                                temp1 = j.split(":")
                                                temp1.remove('\n')
                                                print(temp1)
                                                arr1.insert(-1,temp1[1])
                                                break
                                    break

    lstTostr = ' '.join(map(str, arr1))

    return print(lstTostr)

comp0()
