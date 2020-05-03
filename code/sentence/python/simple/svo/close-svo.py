import xml.etree.ElementTree as Et
import random


class CloseSvo:
    doc = Et.parse("C:/Users/lenova/Desktop/FYP/smart-learning-master/code/sentence/templates/SVO/Close.xml")
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
                            # print(arr0)
                            arr1.append(random.choice(arr0))
                            print(arr1)

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
                                #temp.remove("\n")
                                # print(temp)
                                break
                        arr0=[]
                        arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                    # if child.tag == "ADVERB":
                    #     class0 = child.attrib
                    #     adverb_dict=open(
                    #         "C:/Users/lenova/Desktop/FYP/smart-learning-master/code/sentence/adverb_dict"
                    #         "/adverb.txt")
                    #     f1 = adverb_dict.readlines()
                    #     for i in f1:
                    #         if i.find(class0["class"] + ":", 0) >= 0:
                    #             temp = i.split(":")
                    #             temp.remove("\n")
                    #
                    #             arr1.append(random.choice(temp[2:]))
                    #     print(arr1)

                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                        print(arr1)

                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "C:/Users/lenova/Desktop/FYP/smart-learning-master/code/sentence/noun_dict"
                            "/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                               # temp.remove("\n")
                                arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        arr1.append("of")
                        print(arr1)

                    if child.tag == "ARTICLE1":
                        class0 = child.attrib
                        arr1.append("the")
                        print(arr1)

                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open(
                            "C:/Users/lenova/Desktop/FYP/smart-learning-master/code/sentence/noun_dict"
                            "/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                #temp.remove("\n")
                                arr1.append(random.choice(temp[1:-1]))
                                print(arr1)



                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr + ".")

                       # print(arr1[0]+" "+arr1[1]+" "+arr1[2]+" "+arr1[3]+" "+arr1[4]+" "+arr1[5]+" "+arr1[6]+" "+arr1[7]+".")




                    # if child.tag == "CNOUN":
                        #     class0 = child.attrib
                        #     verb_dict = open(
                        #         "/Users/navkar14/Desktop/smart-learning/code/sentence/verb_dict"
                        #         "/verbs.txt")
                        #
                        #     f1 = verb_dict.readlines()
                        #     for i in f1:
                        #         if i.find(class0["class"] + ":", 0) == 0:
                        #             temp = i.split(":")
                        #             temp.remove("\n")
                        #             # print(temp)
                        #             break
                        #     arr0 = []
                        #     arr1.append(random.choice(temp[1:]))
                        #     print(arr1)
                        #
                        #
                        #
                        #



                #                     listToStr0 = ' '.join(map(str, arr0))
                #                     listToStr01 = ' '.join(map(str, arr01))
                #                     print(listToStr0)
                #                     print(listToStr01)
                #                     break
                # if class0["class"] == "wish-subject":
                #     class0 = phrase.attrib
                #     noun_dict = open(
                #         "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                #         "/abstract.txt")
                #     f1 = noun_dict.readlines()
                #     for i in f1:
                #         if i.find(class0["class"] + ":", 0) == 0:
                #             temp = i.split(":")
                #             temp.remove("\n")
                #             # print("arr02 is : ", arr02)
                #             # print("temp is : ", temp)
                #             arr02.append(random.choice(temp[1:]))
                #             check_str=arr02[-1]
                #             # print(check_str)
                #             arr02.append("\b!")
                #             # print("arr02 is : ", arr02)
                #             # print(check_str.find("to"))
                #             if check_str.find("to")>=0:
                #                 arr02.remove("\b,")
                #             listToStr02 = ' '.join(map(str, arr02))
                #             print(listToStr02)