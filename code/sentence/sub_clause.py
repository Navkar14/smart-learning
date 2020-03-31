import xml.dom.minidom
from xml.dom.minidom import Node
import random
import xlrd


class Clause:
    doc = xml.dom.minidom.parse("C:\\Users\\payal\\Desktop\\Navkar\\MAC\\Smart Learning\\simple0.xml")


    def genmc_subject(self):
        arraymc=[]
        for node in Clause.doc.getElementsByTagName("SENTENCE"):
            # sn = node.getAttribute("KIND")
            # st = node.getAttribute("TYPE")
            # print(sn,st)
            # mc = node.getElementsByTagName("MAINCLAUSE")
            mc_sub = node.getElementsByTagName("MSUBJECT")
            for name in mc_sub:
                if name.getAttribute("name") == "PERSONIFIED":
                    #print("Personified")
                    ppnouns=['I', "Me", "We", "Us", "You", "He", "She", "It", "They"]
                    stringmc=random.choice(ppnouns)
                    arraymc.append(stringmc)
                    #print (arraymc)


                elif name.getAttribute("name") == "COMMON":
                    #print("Common Noun")
                    with open("/Users/navkar14/Desktop/Smart Learning/code/sentence/sub/cnoun copy.txt") as cnoun:
                        for word in cnoun:
                            cd = word.split(':')
                        # print ("cd is ",cd)
                        stringmc = random.choice(cd)
                        # arraymc.append(stringmc)
                        #print (arraymc)



                elif name.getAttribute("name") == "PROPER":
                    #print("Proper Noun")
                    with open("/Users/navkar14/Desktop/Smart Learning/code/sentence/sub/pnoun.txt") as pnoun:
                        for word in pnoun:
                            pd = word.split(':')
                        # print("pd is ",pd)
                        stringmc = random.choice(pd)
                        arraymc.append(stringmc)
                        #print (arraymc)
            return random.choice(arraymc)


    def genmc_verb(self, mc_sub):
        #print(mc_sub)
        for node in Clause.doc.getElementsByTagName("SENTENCE"):
            # sn = node.getAttribute("KIND")
            # st = node.getAttribute("TYPE")
            # print(sn,st)
            if mc_sub=="I":
                verblist=["am buying", "am going", "am coming"]
                choose_verb=random.choice(verblist)
            elif mc_sub=="We" or mc_sub=="They" or mc_sub=="You":
                verblist=["are buying", "are going", "are coming"]
                choose_verb=random.choice(verblist)
            elif mc_sub=="He" or mc_sub=="She" or mc_sub=="It":
                verblist=["buys", "goes", "comes"]
                choose_verb=random.choice(verblist)
            elif mc_sub=="Me":
                verblist = ["going", "buying", "coming"]
                choose_verb = random.choice(verblist)
            elif mc_sub=="Us":
                verblist = ["being late", "being gone", "being on the way"]
                choose_verb = random.choice(verblist)
            else:
                verblist = ["buys", "goes", "comes"]
                choose_verb = random.choice(verblist)


            # mc = node.getElementsByTagName("MAINCLAUSE")
            mc_verb = node.getElementsByTagName("VERBLIST")
            verb=''
            for i in mc_verb:
                vname = i.getAttribute("NAME")
                vtense = i.getAttribute("TENSE")
            verb_gen = vname + "." + vtense
            #print(verb_gen)
            wb = xlrd.open_workbook("/Users/navkar14/Desktop/Smart Learning/code/sentence/sub/verb.xlsx")
            sheet = wb.sheet_by_index(0)
            for row in range(sheet.nrows):
                for column in range(sheet.ncols):
                    if verb_gen == sheet.cell(row, column).value:
                        verb = sheet.cell(row, column + 5).value
                        #print(verb)
            vlist = [vname, vtense, verb]
            #print(vlist)
            #print(choose_verb)
            return choose_verb

    def genmc_obj(self, mcverb):
        for node in Clause.doc.getElementsByTagName("SENTENCE"):
            re_list=[0]
            #print (mcverb)
            art=[0]
            sn = node.getAttribute("NO")
            st = node.getAttribute("TYPE")
            mc = node.getElementsByTagName("MAINCLAUSE")
            msc = node.getElementsByTagName("MOBJECT")
            for i in msc:
                objnoun = i.getElementsByTagName("ONOUN")
                mobjadv = i.getElementsByTagName("OADV")
                mobjart = i.getElementsByTagName("OARTICLE")
                mobjprep1 = i.getElementsByTagName("OPREP")
                if mcverb == "comes":
                    mobjprep="from"
                elif mcverb == "goes":
                    mobjprep="to"
                elif mcverb == "buys":
                    mobjprep=" "
                for i in objnoun:
                    onounname = i.getAttribute("NAME")
                    onountype = i.getAttribute("TYPE")
                    #RRprint(re_list)
                    with open("/Users/navkar14/Desktop/Smart Learning/code/sentence/sub/verb_noun.txt") as on:
                        for word in on:
                            dh=[0]
                            dh = word.split(':')
                            dh.remove('\n')
                            # print(dh)
                            if dh[0] == re_list[0]:
                                dh.remove(dh[0])
                                onoun = dh[0]
                                break

                    art = ["a", "the", "an"]
                    prep = ["to", "in", "over", "under", "on"]

                    if onountype == "cnoun":
                        art.append("market")
                        art.append("book")
                        #obj_phrase += art[1]

                phrase=["apple","mango","veggies","book"]
                #print (mcverb)
                phrase2=["market","shop","store","departmental store"]
                if mobjprep=="to":
                    if mcverb == "are going":
                        obj_phrase = mobjprep + " " + random.choice(phrase2) + " to get some books"
                    if mcverb == "goes":
                        obj_phrase = mobjprep + " " + random.choice(phrase2) + " to get some books"
                elif mobjprep=="from":
                    if mcverb == "are coming":
                        obj_phrase = mobjprep + " " + random.choice(phrase2) + " to get their books"
                    if mcverb=="comes":
                        obj_phrase=mobjprep+" "+random.choice(phrase2)+" and bought some fruits"
                elif mobjprep==" ":
                    obj_phrase = mobjprep+"some fruits"
                art = ["a", "the", "an"]
                prep = ["to", "in", "over", "under", "on"]

                if onountype == "cnoun":
                    art.append("market")
                    art.append("book")
                    # obj_phrase += art[1]

                #print (obj_phrase)


        return obj_phrase

    def gensc_subject(self):
        for node in Clause.doc.getElementsByTagName("SENTENCE"):
            sn = node.getAttribute("NO")
            st = node.getAttribute("TYPE")
            # print(sn,st)
            sc = node.getElementsByTagName("SUBCLAUSE")
            scc = node.getElementsByTagName("CONJ")
            scp = node.getElementsByTagName("PUNC")
        arraymc = []
        for node in Clause.doc.getElementsByTagName("SENTENCE"):
            # sn = node.getAttribute("KIND")
            # st = node.getAttribute("TYPE")
            # print(sn,st)
            # mc = node.getElementsByTagName("MAINCLAUSE")
            mc_sub = node.getElementsByTagName("MSUBJECT")
            for name in mc_sub:
                if name.getAttribute("name") == "PERSONIFIED":
                    print("Personified")
                    ppnouns = ['I', "Me", "My", "We", "Us", "You", "He", "She", "It", "They"]
                    stringmc = random.choice(ppnouns)
                    arraymc.append(stringmc)
                    print (arraymc)


                elif name.getAttribute("name") == "COMMON":
                    print("Common Noun")
                    with open("/Users/navkar14/Desktop/Smart Learning/code/sentence/sub/cnoun copy.txt") as cnoun:
                        for word in cnoun:
                            cd = word.split(':')
                        # print ("cd is ",cd)
                        stringmc = random.choice(cd)
                        # arraymc.append(stringmc)
                        print (arraymc)


c = Clause()
main_clause = ""
main_clause_sub = c.genmc_subject()
main_clause += main_clause_sub
main_clause_verb = c.genmc_verb(main_clause_sub)
main_clause += " "+main_clause_verb
main_clause_obj = c.genmc_obj(main_clause_verb)
main_clause += " "+main_clause_obj
print(main_clause)
