# import xml.dom.minidom
# Using ElementTree
import xml.etree.ElementTree as Et
import random


class Simple0:
    doc = Et.parse("/Users/navkar14/Desktop/Smart Learning/code/sentence/templates/simple0.xml")
    # doc = Et.parse("C:\\Users\\payal\\Desktop\\Navkar\\Smart_Learning\\code\\sentence\\templates\\simple0.xml")
    root = doc.getroot()
    arr0 = []
    arr1 = []
    gender_list = ["male", "female"]
    # print(root.tag)
    # print(root.attrib)
    # print(et.tostring(root, encoding='utf8').decode('utf8'))
    # print([elem.tag for elem in root.iter()])
    for sentence in root:
        print(sentence.tag)
        print(sentence.attrib)
        print()
        for phrase in sentence:
            print(phrase.tag)
            print(phrase.attrib)
            print()
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    print(child.tag)
                    print(child.attrib)
                    if child.tag == "SNOUN":
                        class0 = child.attrib
                        # print(class0["TAG"])
                        # print(type(class0))
                        # class0["TAG"]
                        noun_dict = open(
                            "/Users/navkar14/Desktop/Smart Learning/code/sentence/noun_dict"
                            "/proper_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            # flag = 0
                            gender = random.choice(gender_list)
                            # while flag==0:

                            if i.find(class0["TAG"] + ":", 0) == 0:
                                if i.find(random.choice(gender_list), 0) >= 0:
                                    temp = i.split(":")
                                    temp.remove("\n")
                                    print(temp)
                                    arr0.append(random.choice(temp[3:]))
                                    arr1.append(temp[1])
                                    print(arr0)
                                    print(arr1)
                                    break
                    if child.tag == "SADJECTIVEPHRASE":
                        for sub_child in child:
                            if sub_child.tag == "CNOUN":
                                class0 = sub_child.attrib
                                c_noun=open("/Users/navkar14/Desktop/Smart Learning/code/sentence/noun_dict/"
                                            "common_nouns.txt")
                                # c_noun = open(
                                #     "C:\\Users\\payal\\Desktop\\Navkar\\Smart_Learning\\code\\sentence\\noun_dict"
                                #     "\\common_nouns.txt")
                                f1 = c_noun.readlines()
                                for i in f1:
                                    print(i)
                                    if i.find(class0["TAG"] + ":", 0) == 0:
                                        if i.find(arr1[0]+":", 0) >  0:
                                            print(class0)
                                            print(arr1[0])
                                            print(arr0[0])

            if phrase.tag == "VERBPHRASE":
                print(".")

            if phrase.tag == "OBJECTPHRASE":
                print(".")

    # def gensubject(self):
    # or child in Simple0().root:
    #        # print(child.attrib, child.tag)

# Simple0.gensubject("y")
