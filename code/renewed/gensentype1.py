
from __future__ import print_function
import itertools
import sys
import nltk
import numpy as np
from nltk.grammar import Nonterminal
from nltk.grammar import CFG
from collections import Counter
import math as calc
from collections import defaultdict
import type1 

def generate(grammar, start=None, depth=None, n=None):

    if not start:
        start = grammar.start()

    if depth is None:
        depth = sys.maxsize

    iter = generateforall(grammar, [start], depth)
    if n:
        iter = itertools.islice(iter, n)
    return iter

def generateforall(grammar, items, depth):

    if items:
        for frag1 in gennonterminal(grammar, items[0], depth):
           # print("generate one with Item and depth for frag1:", frag1, items[0], depth)
            for frag2 in generateforall(grammar, items[1:], depth):
               # print("generate all with item and depth:", frag2,items[1:],depth)
                yield frag1 + frag2

                #print("generate all frag1+grag2:",frag1 + frag2)
    else:
        yield []


def gennonterminal(grammar, item, depth):

    if depth > 0:

        if isinstance(item, Nonterminal):

            for prod in grammar.productions(lhs=item):
                #print("generate one item is:",item)

                for frag in generateforall(grammar, prod.rhs(), depth-1):
                    print("generate one",frag)
                    for element in frag:
                        if element== "SN":
                            frag.remove('SN')
                            frag.append(snname1)
                            #print("SN",snname1)
                        elif element == "ART":
                            frag.remove('ART')
                            frag.append(article)
                            #print("ART",article)
                        elif element == "ADJ":
                            frag.remove('ADJ')
                            frag.append(adjective1)
                            print("ADJ",adjective1)
                        elif element == "CN":
                            frag.remove('CN')
                            frag.append(cnoun)

                    yield frag          

        else:

            yield [item]

#-------------------------------------------------type 1 sentence-----------------------------------------------------------------------------

gensentence_grammar = """
  S ->  N COMMA NP 
  NP -> Det ADP
  ADP -> ADJ CN
  N -> 'SN'
  Det -> 'ART'
  ADJ -> 'ADJ'
  CN -> 'CN'
  COMMA -> ','
"""

#---------------------------------------------rules for comma type1(for type1 there has to be a comma between N and NP) ---------------------------------------------------------------------------

def gensentence(N=1):
    parser = nltk.ChartParser(gensentence_grammar)
    print (parser.grammar())
    print('Generating the first %d sentences for gensentence grammar:' % (N,))
    #print(gensentence_grammar)
    grammar = CFG.fromstring(gensentence_grammar)
    for n, sent in enumerate(generate(grammar, n=N), 1):
        global abc
        abc={}
        abc=' '.join(sent)
        print('%3d. %s' % (n, abc))
p1=type1.type1()
snname1,adjective1,article,cnoun=p1.generatesubjadjectivephrase()   
gensentence(N=20)
