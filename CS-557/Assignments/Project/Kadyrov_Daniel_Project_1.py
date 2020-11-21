'''
10. ● Suppose you wanted to automatically generate a prose description of a scene,
and already had a word to uniquely describe each entity, such as the book, and
simply wanted to decide whether to use in or on in relating various items, e.g., the
book is in the cupboard versus the book is on the shelf. Explore this issue by looking
at corpus data and writing programs as needed. Consider the following examples:
(13)
a. in the car versus on the train
b. in town versus on campus
c. in the picture versus on the screen
d. in Macbeth versus on Letterman
'''

#%% 
import nltk
from ntlk.corpus import brown, inaugural