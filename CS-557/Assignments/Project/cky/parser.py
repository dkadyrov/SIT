from collections import defaultdict
import itertools
import sys
import os
import re

RULES_RE = r'([^\s]+)\s+->\s+([^\s]+)(?:\s+([^\s]+))?'

class Rule(object):
    """
    A Rule represents a single grammar rule for the parser.

    members:
    terminal: (boolean) Whether or not the rule is a terminal or non-terminal.
    left:     (string) The left hand side of the rule.
    right:    (string | (string, string)) The right hand side of the rule.
    """
    def __init__(self, line):
        """
        parameters:
        line: (string) The unparsed input line representing a grammar rule.
        """
        super(Rule, self).__init__()

        matches = re.match(RULES_RE, line)

        if matches:
            self.terminal = False if matches.group(3) else True
            self.left     = matches.group(1)

            if self.terminal:
                self.right = matches.group(2)
            else:
                self.right = (matches.group(2), matches.group(3))

    def __str__(self):
        """Prints a grammar rule."""
        return '{} -> {}'.format(self.left, self.right)


class Grammar(object):
    """
    A Grammar contains all rules for a specific grammar.

    members:
    lines: ([string]) Unparsed input lines for the grammar.
    rules: ({string: [string | (string string)]}) A dict from left hand sides to right hand sides.
    """
    def __init__(self, lines):
        """
        parameters:
        lines: ([string]) Unparsed input lines for the grammar.
        """
        super(Grammar, self).__init__()
        self.lines = lines
        self.rules = defaultdict(lambda: [])

        for line in lines:
            rule = Rule(line)
            self.rules[rule.left].append(rule.right)

    def __str__(self):
        """Returns all grammar rules in a formatted string."""
        return '\n'.join(map(str, self.rules.values()))


def printTable(sentence, table):
    """
    Prints the results of a parsing attempt.

    parameters:
    sentence: (string) The original sentence that was parsed.
    table: ([[[string]]]) The table describing possible parses.
    """
    print ('PARSING SNETENCE: {}'.format(sentence))
    print ('NUMBER OF PARSES FOUND: {}'.format(len([p for p in table[0][len(table) - 1] if p == 'S'])))
    print ('CHART:')

    for row in range(len(table)):
        for col in range(row, len(table)):
            contents = '-' if not table[row][col] else ' '.join(sorted(table[row][col]))
            print ('  chart[{},{}]: {}'.format(row + 1, col + 1, contents))


def findMatchingRules(grammar, word, right1, right2):
    """
    Searches through all grammar rules of a grammar to find any that match the right hand side.

    parameters:
    grammar: (Grammar) The grammar rules to search.
    word: (string) The word if searching for a terminal.
    right1: (string) The first part of the right hand side if searching for a non-terminal.
    right2: (string) The second part of the right hand side if searching for a non-terminal.
    """
    matches = []

    def searchRules(right):
        for left in grammar.rules:
            for rule in grammar.rules[left]:
                if rule == (word or nonTerminal):
                    matches.append(left)

    if word:
        searchRules(word)
    else:
        for nonTerminal in itertools.product(right1, right2):
            searchRules(nonTerminal)

    return matches


def parse(sentence, grammar):
    """
    Generates a parse table from a sentence and a set of grammar rules.

    parameters:
    sentence (string) The string to parse.
    grammar: (Grammar) The grammar.
    """
    words = sentence.split()
    table = []

    # Build an empty chart
    for x in range(len(words)):
        table.append([])
        for y in range(len(words)):
            table[x].append([])

    for col in range(len(words)):
        # Add the terminals to the diagonal of the table
        table[col][col] = findMatchingRules(grammar, words[col], None, None)

        # Explore the partitionings for all words up to the current column
        for row in reversed(range(col + 1)):
            for s in range(row + 1, col + 1):
                table[row][col].extend(findMatchingRules(grammar, None, table[row][s - 1], table[s][col]))

    return table


def main():
    try:
        grammar   = Grammar([line.rstrip('\n') for line in open(sys.argv[1])])
        sentences = [line.rstrip('\n') for line in open(sys.argv[2])]
    except:
        print('usage: python parser.py <grammar.txt> <sentences.txt>')
        return

    # Parse each sentence in the sentences file.
    for sentence in sentences:
        printTable(sentence, parse(sentence, grammar))
        print


if __name__ == '__main__':
    main()