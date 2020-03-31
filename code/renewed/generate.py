
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



def generate(grammar, start=None, depth=None, n=None):

    """

    Generates an iterator of all sentences from a CFG.
    :param grammar: The Grammar used to generate sentences.

    :param start: The Nonterminal from which to start generate sentences.

    :param depth: The maximal depth of the generated tree.

    :param n: The maximum number of sentences to return.

    :return: An iterator of lists of terminal tokens.

    """

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
               # print("generate one item is:",item)

                for frag in generateforall(grammar, prod.rhs(), depth-1):

                    yield frag

                    #print("generate one",frag)

        else:

            yield [item]



gensentence_grammar = """
  S -> NP VP
  NP -> Det N
  PP -> P NP
  VP -> 'danced' | 'saw' NP | 'ran' PP
  Det -> 'the' | 'a'
  N -> 'girl' | 'stage' | 'cat'
  P -> 'in' | 'with' 
"""

def gensentence(N=20):
    print('Generating the first %d sentences for gensentence grammar:' % (N,))
    #print(gensentence_grammar)
    grammar = CFG.fromstring(gensentence_grammar)
    for n, sent in enumerate(generate(grammar, n=N), 1):
        global abc
        abc={}
        abc=' '.join(sent)
        print('%3d. %s' % (n, abc))
                


gensentence(N=20)
