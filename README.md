# CasMarExt (Case Marker Extraction)

This Repository presents my Bachelor Thesis on "Creating a Multilingual Gold Standard for Case Marker Extraction".

It contains my Thesis as a .pdf file and the final Gold Standard in a .py file.

Feel free to use it!

Cheers, Xaver

## More Details and Background Info

### CaMEL

The goal of the thesis was to help evaluating "CaMEL: Case Marker Extraction without Labels", a project by my supervisor.

[Paper, Code and Data for CaMEL](https://doi.org/10.48550/arxiv.2203.10010)


### Theoretical Part

The first third of the thesis provides a theoretical analysis of case


### Practical Work

In the practical part, the theoretical foundations are used to collect the case markers of 6 languages as defined before.

### Gold Standard

Finally, the gold standard is provided via a python file. This contains a three-times nested dictionary for each language in which the first level keys are the inflectional parts of speech, the second level keys the differentiated numbers and the third level keys the respective cases whose final value is the set of their markers. Word boundaries are indicated by $ to differentiate suffixes ('a$') from prefixes ('$a'), infixes ('a') and complete word forms ('$a$'). This makes it possible to exclude either certain features of a language or the kind of affixes.


