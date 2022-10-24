# CasMarExt (Case Marker Extraction)

This Repository presents my Bachelor Thesis on "Creating a Multilingual Gold Standard for Case Marker Extraction".

It contains my Thesis as a .pdf file and the final Gold Standard for Latin, Modern Greek, German, Russian, Turkish and Finnish in a .py file.

Feel free to use it!

Cheers, Xaver



## More Details and Background Info

### CaMEL

The goal of the thesis was to further help evaluating "CaMEL: Case Marker Extraction without Labels", a project by my supervisor.

[Paper, Code and Data for CaMEL](https://doi.org/10.48550/arxiv.2203.10010)


### Theoretical Part

The first third of the thesis provides a theoretical overview of case and the relations that come with it. 
This mainly refers to the idea of 'deep cases', i.e. semantic information that is given by case. 
CaMEL aims to use morphological case markers to extract such semantic roles without training.
My thesis is similarly motivated by this finding and therefore continues this theoretical work.


### Practical Work

In the practical part, the theoretical foundations are used to collect the morphological case markers of 6 languages as defined before.
Shortly, the selection of Latin, Modern Greek, German, Russian, Turkish and Finnish is explained.
For each language, possible particularities are explained before the morphological case markers of each inflected part of speech are collected from at least two sources (grammar books) and stored in simple tables. 
It was aimed to include as much information as possible without becoming too extensive.
Putting natural language in its place means making compromises on the one hand and being generous on the other.


### Gold Standard

Finally, the gold standard is provided via a python file. 
This contains a three-times nested dictionary for each language in which the first level keys are the inflectional parts of speech, the second level keys the differentiated numbers and the third level keys the respective cases whose final value is the set of their markers. 
Word boundaries are indicated by $ to differentiate suffixes ('a$') from prefixes ('$a'), infixes ('a') and complete word forms ('$a$'). 
This makes it possible to either exclude certain features of a language or the kind of affixes.


