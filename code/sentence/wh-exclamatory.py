# Using ElementTree
import xml.etree.ElementTree as Et
import random


class Wh_exclamatory:
    doc = Et.parse("/Users/navkar14/Desktop/smart-learning/code/sentence/templates/exclamatory/what-exclamatory.xml")
    # doc = Et.parse("C:\\Users\\payal\\Desktop\\Navkar\\Smart_Learning\\code\\sentence\\templates\\-exclamatory.xml")
    root = doc.getroot()

    # print(root.tag)
    # print(root.attrib)
    # print(et.tostring(root, encoding='utf8').decode('utf8'))
    # print([elem.tag for elem in root.iter()])
    for sentence in root:
        arr0 = []
        arr1 = []
        # gender_list = ["male", "female"]
        # print(sentence.tag)
        # print(sentence.attrib)
        # print()
        for phrase in sentence:
            # print(phrase.tag)
            # print(phrase.attrib)
            # print()

            if phrase.tag == "SNOUN":
                c_noun = ['animal', 'person', 'thing']
                t1 = random.choice(c_noun)
                # print(t1)

                # print(class0["TAG"])
                # print(type(class0))
                # class0["TAG"]
                t2 = []
                noun_dict = open(
                    "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                    "/common_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:

                    if i.find(t1 , 0) >= 0:
                        t2.append(i)
                t1=random.choice(t2)
                # print(t1)
                t2=t1.split(":")

                t2.remove("\n")
                # print(t2)
                arr0=random.choice(t2[3:])
                arr1.append(t2[0])
                arr1.append(t2[1])
                arr1.append(t2[2])
                print(arr1)
                #
                # if class0["class"]=="wh-pos":
                #     print(t1)
                #
                # elif class0["class"]=="wh-neg":
                #     print(t1)
                # noun_dict = open(
                #     "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                #     "/abstract.txt")
                # f1 = noun_dict.readlines()
                # # j=1
                # for i in f1:
                #     if i.find(class0["class"] + ":", 0) == 0:

            #             # print(j)
            #             # j+=1
            #             temp = i.split(":")
            #             temp.remove("\n")
            #             # print(temp)
            #             arr0.append(random.choice(temp[1:]))
            #
            #             arr0.append("\b,")
            #             arr02 = arr0[:]
            #             # print("arr0 is : ", arr0)
            #             arr1.append(temp[0])
            #             # print(arr0)
            #             # print(arr1)
            #             # break
            # class0=phrase.attrib
            # if phrase.tag == "SNOUN":
            #     if  class0["class"] == "name":
            #         class0 = phrase.attrib
            #         noun_dict = open(
            #             "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
            #             "/proper_nouns.txt")
            #
            #         f1 = noun_dict.readlines()
            #         for i in f1:
            #             if i.find(class0["class"] + ":", 0) == 0:
            #
            #                 if i.find(random.choice(gender_list), 0) >= 0:
            #                     # print(j)
            #                     # j+=1
            #                     temp = i.split(":")
            #                     temp.remove("\n")
            #                     # print(temp)
            #                     print("arr0 is : ", arr0)
            #                     arr0.append(random.choice(temp[3:]))
            #                     arr01 = arr0[:]
            #
            #                     arr0.append("\b!")
            #                     arr01.append("and")
            #                     t=random.choice(temp[3:])
            #                     # print(arr0)
            #                     # print(arr01)
            #                     while t == arr01[-2]:
            #                         # print("inloop")
            #                         t=random.choice(temp[3:])
            #                     arr01.append(t)
            #                     arr01.append("\b!")
            #                     arr1.append(temp[1])
            #                     # print(arr0)
            #                     # print(arr01)
            #                     # print(arr1)
            #                     listToStr0 = ' '.join(map(str, arr0))
            #                     listToStr01 = ' '.join(map(str, arr01))
            #                     print(listToStr0)
            #                     print(listToStr01)
            #                     break
            #     if class0["class"] == "wish-subject":
            #         class0 = phrase.attrib
            #         noun_dict = open(
            #             "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
            #             "/abstract.txt")
            #         f1 = noun_dict.readlines()
            #         for i in f1:
            #             if i.find(class0["class"] + ":", 0) == 0:
            #                 temp = i.split(":")
            #                 temp.remove("\n")
            #                 # print("arr02 is : ", arr02)
            #                 # print("temp is : ", temp)
            #                 arr02.append(random.choice(temp[1:]))
            #                 check_str=arr02[-1]
            #                 # print(check_str)
            #                 arr02.append("\b!")
            #                 # print("arr02 is : ", arr02)
            #                 # print(check_str.find("to"))
            #                 if check_str.find("to")>=0:
            #                     arr02.remove("\b,")
            #                 listToStr02 = ' '.join(map(str, arr02))
            #                 print(listToStr02)