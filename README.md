# Asmai: (Al'asma'i) Arabic semantic analysis 
# مكتبة الأصمعي الدلالية


Asmai: (Al'asma'i) Arabic semantic analysis library for Python

![asmai logo](doc/asmai_header.png  "asmai logo")

[![downloads]( https://img.shields.io/sourceforge/dt/asmai.svg)](http://sourceforge.org/projects/asmai)
[![downloads]( https://img.shields.io/sourceforge/dm/asmai.svg)](http://sourceforge.org/projects/asmai)


  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

  
Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/asmai-arabic-semantic/master/AUTHORS.md)
Release  | 0.1
License  |[GPL](https://github.com/linuxscout/asmai-arabic-semantic/master/LICENSE)
Tracker  |[linuxscout/asmai/Issues](https://github.com/linuxscout/asmai-arabic-semantic/issues)
Website  |[http://asmai.sourceforge.net](http://asmai-arabic-semantic.sourceforge.net)
Source  |[Github](http://github.com/linuxscout/asmai-arabic-semantic)
Download  |[sourceforge](http://asmai.sourceforge.net)
Feedbacks  |[Comments](https://github.com/linuxscout/asmai-arabic-semantic/)
Accounts  |[@Twitter](https://twitter.com/linuxscout)  [@Sourceforge](http://sourceforge.net/projects/asmai/)

## Description

Asmai: (Al'asma'i) Arabic semantic analysis library for Python



###  مزايا:
<div dir="rtl">

- 

</div>
### install
```shell
pip install asmai
```
### Usage

#### import
```python

```
#### Test 
```python

```
#### [requirement]
  
    1- pyarabic 
    2. sqlite


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

* semantic relations

CREATE TABLE "relations" (
    "id" INTEGER PRIMARY KEY  NOT NULL ,
    "first" VARCHAR NOT NULL  DEFAULT ('') ,
    "second" VARCHAR NOT NULL  DEFAULT ('') ,
    "rule" VARCHAR NOT NULL  DEFAULT (0) 
 );
 
 
CSV Structure:

1.   id             : id unique in the database
2. first: first word
3. second: second word
4.  rule        : the extraction rule number
        : 

