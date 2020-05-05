# import xml.dom.minidom
# Using ElementTree
import xml.etree.ElementTree as Et
import random



def wish_multsvo():
    doc = Et.parse("/Users/navkar14/Desktop/smart-learning/code/sentence/templates/exclamatory/wish/multsvo/wish-multsvo.xml")
    root = doc.getroot()
    for sentence in root:
        arr0 = []
        arr1 = []
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

                        break

            if phrase.tag == "SNOUN":
                class0 = phrase.attrib
                if class0["class"] == "wish-subject":
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
                            check_str=arr0[-1]
                            arr0.append("\b!")
                            if check_str.find("to")>=0:
                                arr0.remove("\b,")
                            listToStr02 = ' '.join(map(str, arr0))
    return listToStr02
wish_multsvo()