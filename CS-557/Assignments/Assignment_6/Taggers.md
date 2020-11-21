B&K 

**POS Tagger:** 

POS (Part-of-Speech) Tagger
- Processes a squence of words and attaches a part of speech tag to each word.
- Part of NLTK package

Default Tagger: 
- Assigns a tag to each token with most likely tag. 
- Part of NLTK package

Regular Expression 
- Assigns tags to tokens on basis of matching patterns. 
- Part of NLTK package

Lookup Tagger
- Initially uses a lookup table to assign tokens that the tagger identified as None. Then uses backoff, where one tagger acts as a parameter to another. 

**N-Gram Tagging:**

Unigram Tagger: 
- For each token, assign the tag that is most likely for that particular token. Isolated word.  
- Similar to Lookup tagger

N-Gram Tagger: 
- Unigram tagger but uses n-1 preceding words to give context to the current word
- Similar to Unigram Tagger

**Tranformation-Based Tagger**

Brill Tagger:
- Guesses the tag of each word, then go back and fix the mistakes. Supervised learning method. Does not count observations but complies a list of transformation correction rules. 

**Maximum Entropy Markov Model (MEMM)**

Uses logistic regression to classify words based on the words in its this succession 

**Hidden Markov Model (HMM)** 

