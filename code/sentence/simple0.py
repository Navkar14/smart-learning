import xml.dom.minidom
import random

class Simple0:
    doc = xml.dom.minidom.parse(
        "C:\\Users\\payal\\Desktop\\Navkar\\Smart_Learning\\code\\sentence\\templates\\simple0.xml")

    def gensubject(self):
        for node in Simple0.doc.getElementsByTagName("SENTENCE"):
            subject = node.getElementsByTagName("SUBJECTPHRASE")
            for inode in subject:
                arr0 = []
                arr1 = []
                gender_list = ["male", "female"]
                name_list = []
                sn = inode.getElementsByTagName("SNOUN")
                for j in sn:
                    arr1.append(j.getAttribute("TAG"))
                    break

                noun_dict = open("C:\\Users\\payal\\Desktop\\Navkar\\Smart_Learning\\code\\sentence\\noun_dict\\proper_nouns.txt")
                f1 = noun_dict.readlines()

                for i in f1:
                    if i.find(arr1[0]+":", 0) == 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        print(temp)
                        if random.choice(gender_list) == temp[1]:
                            arr0.append(random.choice(temp[3:]))
                            arr1.append(temp[1])
                            print(arr0)
                            print(arr1)
                            break
                        else:
                            continue
                sadjphrase = inode.getElementsByTagName("SADJECTIVEPHRASE")
                # for sadj = inode.getElementsByTagName("ADJECTIVE")
                snoun = inode.getElementsByTagName("CNOUN")






Simple0.gensubject("y")