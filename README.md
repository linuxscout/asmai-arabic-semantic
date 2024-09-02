# Asmai: (Al'asma'i) Arabic semantic analysis 
# مكتبة الأصمعي الدلالية


Asmai: (Al'asma'i) Arabic semantic analysis library for Python

![asmai logo](doc/asmai_header.png  "asmai logo")

![PyPI - Downloads](https://img.shields.io/pypi/dm/asmai)

  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

  
Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/asmai-arabic-semantic/master/AUTHORS.md)
Release  | 0.1
License  |[GPL](https://github.com/linuxscout/asmai-arabic-semantic/master/LICENSE)
Tracker  |[linuxscout/asmai/Issues](https://github.com/linuxscout/asmai-arabic-semantic/issues)
Source  |[Github](http://github.com/linuxscout/asmai-arabic-semantic)
Feedbacks  |[Comments](https://github.com/linuxscout/asmai-arabic-semantic/)
Accounts  |[@Twitter](https://twitter.com/linuxscout)

## Description

Asmai: (Al'asma'i) Arabic semantic analysis library for Python,  it provides extracting word pairs that carry meanings of the type: (subject-verb, verb-object, word composition)



###  مزايا:
* استخلاص ثنائيات الكلمات التي تحمل دلالات من نوع : (فاعلية، مفعولية، إضافة)

<div dir="rtl">

- 

</div>

### Usage

#### import
```python
pip install asmai
```
## Citation
```bibtex
@thesis{zerrouki2020adawat,
author = {Taha Zerrouki},
title = {Towards An Open Platform For Arabic Language Processing},
type = {PhD thesis},
institution = {Ecole Nationale Supérieure d'informatique, Alger, Algérie},
date = {2020},
}
```
#### Test 
```python
import asmai.anasem as asm
text  =  u"يعبد الله منذ أن تطلع الشمس"
result  =  []
anasem  =  asm.SemanticAnalyzer()    
result  =  anasem.analyze_text(text)
# the result contains objets
anasem.pprint(result)
```

* Extract semantic relation, display only found relations

```python
>>> import pprint
>>> sem_result = anasem.display_sem(result)
>>> pprint.pprint(sem_result)      
[[['الشَّمْسُ', 'تَطْلُعَ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
  ['الشَّمْسُ', 'تَطْلُعُ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
  ['الشَّمْسُ', 'تَطْلُعْ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
  ['الشَّمْسُ', 'تَطْلَعَ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
  ['الشَّمْسُ', 'تَطْلَعُ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
  ['الشَّمْسُ', 'تَطْلَعْ', 'شَمْسٌ', 'طَلَعَ', 'Subject']]]

```
* Extract semantic relation, display all words and tags
```python
>>> sem_result = anasem.display_sem(result, all=True)
>>> pprint.pprint(sem_result)
[('يعبد', 'O', []),
 ('الله', 'O', []),
 ('منذ', 'O', []),
 ('أن', 'O', []),
 ('تطلع', 'B', []),
 ('الشمس',
  'I',
  [['الشَّمْسُ', 'تَطْلُعَ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
   ['الشَّمْسُ', 'تَطْلُعُ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
   ['الشَّمْسُ', 'تَطْلُعْ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
   ['الشَّمْسُ', 'تَطْلَعَ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
   ['الشَّمْسُ', 'تَطْلَعُ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
   ['الشَّمْسُ', 'تَطْلَعْ', 'شَمْسٌ', 'طَلَعَ', 'Subject']])]
>>> 
```

* convert to pandas
```python
>>> import pandas as pd
>>> 
>>> #  flatten the result
... df = pd.DataFrame(anasem.decode(result))
>>> print(df.head())
  action affix                          affix_key  forced_word_case  ...   unvocalized  unvoriginal  vocalized  word
0         -ي--          -ي--|المضارع المنصوب:هو:y             False  ...          يعبد          عبد  يُعَبِّدَ  يعبد
1         -ي--  -ي--|المضارع المجهول المجزوم:هو:y             False  ...          يعبد          عبد  يُعَبَّدْ  يعبد
2         -ي--          -ي--|المضارع المجهول:هو:y             False  ...          يعبد          عبد  يُعَبَّدُ  يعبد
3         -ي--          -ي--|المضارع المعلوم:هو:y             False  ...          يعبد          عبد  يُعَبِّدُ  يعبد
4         -ي--          -ي--|المضارع المجزوم:هو:y             False  ...          يعبد          عبد  يُعَبِّدْ  يعبد

[5 rows x 50 columns]
>>> df.to_csv("output/test.csv", encoding="utf8", sep="\t")
>>> 

```


#### [requirement]
  
    1- pyarabic 
    2. sqlite
    3. sylajone

## Data Structure:

### Semantic database
```sql
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE "derivations" (
    "id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
    "verb" varchar NOT NULL ,
    "transitive" BOOL NOT NULL  DEFAULT 1,
    "derived" VARCHAR NOT NULL ,
    "type" VARCHAR NOT NULL 
 );
```

CSV Structure:

* Derivattion
 
1.   id             : id unique in the database
2.  verb    : vocalized collocation
3.  transtive : if the verb is transitive
4.  derived         :  derived word from verb number
5.  type    : type 

##### Semantic relations

```sql 
CREATE TABLE "relations" (
    "id" INTEGER PRIMARY KEY  NOT NULL ,
    first" VARCHAR NOT NULL  DEFAULT ('') ,
    "second" VARCHAR NOT NULL  DEFAULT ('') ,
    "rule" VARCHAR NOT NULL  DEFAULT (0) 
 );
```
 
 
CSV Structure:

1.   id             : id unique in the database
2. first: first word
3. second: second word
4.  rule        : the extraction rule number
        : 

