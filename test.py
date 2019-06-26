# A context free grammar is made up of 
#   * a collection of terminal symbols.  For this task, you may assume all terminal symbols
#         are lowercase strings.
#   * a collection of non-terminal symbols. For this task, you may assume all non-terminal 
#          symbols are uppercase strings.
#   * a start symbol (which will be one of the non-terminal symbols).  For this task, you may 
#          assume the start symbol is “S”, which is guaranteed to be present in the set of 
#          non-terminals for all inputs. 
#   * a set of production rules, where every production rule maps a 
#         non-terminal symbol to a sequence of terminal and non-terminal
#         symbols. The set of left-hand sides of production rules will equal the
#         set of non-terminal symbols.
#
# A sentence (sequence of terminal symbols) is said to be “generated” by a grammar if, 
# beginning from the start symbol, there is some sequence of application of production 
# rules which can transform the start symbol into that sentence.  
# A production rule A -> B_0 … B_n may be “applied” to replace the non-terminal symbol
# A with the sequence B_0…B_n.
#
#  An example set of production rules is given at the end of this prompt.
#
#  Your task is to write a function to randomly sample a sentence from a 
# context-free grammar.
#
# You may assume your function receives the grammar as an argument
# represented using any data structure you wish (please specify it in a comment).
#
# You may output the sentence any way you wish (by printing to the console, 
# building a string, building a list of tokens, etc.).  
#
# Assume for any non-terminal the production rule to apply is chosen uniformly at random.


S -> NP VP
S -> S but S
NP -> DT N
N -> dog
N -> cat
DT -> the
DT -> a
VP -> V NP
V -> chased
V -> ate

grammar = {
    'S': [['NP', 'VP'], ['S', 'but', 'S']],
    'NP': ['DT', 'N'],
    'N': [['dog'],['cat']],
    'DT': [['the'], ['a']],
    'VP': ['V', 'NP']
    ... }

def generate(grammar):
    # x = rand() either 0 or 1
    generate_helper(grammar['S'][x], [])

def generate_helper(lont, sentence):
    for nt in lont:
        if is_terminal(nt):
            sentence.append(nt)
        else:
            if len(grammar[nt] > 1):
                # x = rand() either 0 or 1
                sentence.extend(generate_helper(grammar[nt][x]))
            else:
                sentence.extend(generate_helper(grammar[nt]))
    return sentence

def is_terminal(s):
    return lower(s)



