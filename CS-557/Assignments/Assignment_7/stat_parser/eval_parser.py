"""
Parses evaluator from the "Natural Language Processing" course by Michael Collins
https://class.coursera.org/nlangp-001/class
"""
from __future__ import division
from __future__ import print_function

import re
from collections import defaultdict
from six.moves import zip


class ParseError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return self.value


class TreeOperations(object):
    "Some basic operations on trees."
    def __init__(self, tree):
        self.tree = tree
    
    def _remove_vertical_markovization(self, nt):
        "Remove the vertical markovization."
        return re.sub(r"\^<.*?>", '', nt)
    
    def _convert_to_spans(self, tree, start, set, parent = None): 
        "Convert a tree into spans (X, i, j) and add to a set." 
        if len(tree) == 3:
            # Binary rule.
            # Remove unary collapsing.
            current = self._remove_vertical_markovization(tree[0]).split("+")
            split = self._convert_to_spans(tree[1], start, set, None)
            end = self._convert_to_spans(tree[2], split + 1, set, current[-1])
            
            # Add phrases to set
            if current[0] != parent: 
                set.add((current[0], start, end))
            for nt in current[1:]:
                set.add((nt, start, end))
            return end
        
        elif len(tree) == 2:
            # Unary rule.
            
            # Can have a constituent if it is collapsed.
            current = self._remove_vertical_markovization(tree[0]).split("+")
            for nt in current[:-1]:
                set.add((nt, start, start))
            return start
    
    def to_spans(self):
        "Convert the tree to a set of nonterms and spans."
        s = set()
        self._convert_to_spans(self.tree, 1, s)
        return s
    
    def _fringe(self, node):
        if len(node) == 2: return [node[1]]
        else: return self._fringe(node[1]) + self._fringe(node[2])
    
    def fringe(self):
        "Return the fringe of the tree."
        return self._fringe(self.tree)
    
    def _well_formed(self, node):
        if len(node) not in [2, 3]:
            raise ParseError("Ill-formed tree:  %d-ary rule, only binary or unary allowed %s"%(len(node), node))
        
        if not isinstance(node[0], str):
            raise ParseError("Ill-formed tree: non-terminal not a string %s."%(node[0]))
        
        if len(node) == 2:
            if not isinstance(node[1], str):
                raise ParseError("Ill-formed tree: unary rule does not produce a string %s."%(node[1]))
        
        elif len(node) == 3:
            if isinstance(node[1], str):
                raise ParseError("Ill-formed tree: binary rule produces a string %s."%(node[1]))
            if isinstance(node[2], str):
                raise ParseError("Ill-formed tree: binary rule produces a string %s."%(node[2]))
            self._well_formed(node[1])
            self._well_formed(node[2])
    
    def check_well_formed(self):
        self._well_formed(self.tree)


class FScore(object):
    "Compute F1-Score based on gold set and test set."
    
    def __init__(self):
        self.gold = 0
        self.test = 0
        self.correct = 0
    
    def increment(self, gold_set, test_set):
        "Add examples from sets."
        self.gold += len(gold_set)
        self.test += len(test_set)
        self.correct += len(gold_set & test_set)
    
    def fscore(self): 
        pr = self.precision() + self.recall()
        if pr == 0: return 0.0
        return (2 * self.precision() * self.recall()) / pr
    
    def precision(self): 
        if self.test == 0: return 0.0
        return self.correct / self.test
    
    def recall(self): 
        if self.gold == 0: return 0.0
        return self.correct / self.gold
    
    @staticmethod
    def output_header():
        "Output a scoring header."
        print("%10s  %10s  %10s  %10s   %10s"%(
          "Type", "Total", "Precision", "Recall", "F1-Score"))
        print("===============================================================")
    
    def output_row(self, name):
        "Output a scoring row."
        print("%10s        %4d     %0.3f        %0.3f        %0.3f"%(
            name, self.gold, self.precision(), self.recall(), self.fscore()))

ALIAS = {
    '``': '"',
    "''": '"',
    '-LRB-': '(',
    '-RRB-': ')',
}

class ParseEvaluator(object):
    def __init__(self):
        self.total_score = FScore()
        self.nt_score = defaultdict(FScore)
    
    def check_trees(self, gold, test):
        gold, test = TreeOperations(gold), TreeOperations(test)
        gold.check_well_formed()
        test.check_well_formed()
        f1, f2 = gold.fringe(), test.fringe()
        
        if len(f1) != len(f2): 
            raise ParseError("Sentence length does not match. Gold sentence length %d, test sentence length %d. Sentence '%s'"%(len(f1), len(f2), " ".join(f1)))
        
        for gold_word, test_word in zip(f1, f2):
            if gold_word != test_word:
                if gold_word in ALIAS:
                    if test_word == ALIAS[gold_word]: continue
                
                raise ParseError("Tree words do not match. Gold sentence '%s', test sentence '%s'."%(" ".join(f1), " ".join(f2)))
        set1, set2 = gold.to_spans(), test.to_spans()
        
        # Compute non-terminal specific stats.
        for nt in set([s[0] for s in set1 | set2]):
            filter_s1 = set([s for s in set1 if s[0] == nt])
            filter_s2 = set([s for s in set2 if s[0] == nt])
            self.nt_score[nt].increment(filter_s1, filter_s2)
        
        # Compute total stats.
        self.total_score.increment(set1, set2)
    
    def output(self):
        "Print out the f-score table."
        FScore.output_header()
        nts = list(self.nt_score.keys())
        nts.sort()
        for nt in nts:
            self.nt_score[nt].output_row(nt)
        print()
        self.total_score.output_row("total")
