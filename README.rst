Asmai: (Al'asma'i) Arabic semantic analysis
===========================================

مكتبة الأصمعي الدلالية
======================

Asmai: (Al'asma'i) Arabic semantic analysis library for Python

.. figure:: doc/asmai_header.png
   :alt: asmai logo

   asmai logo

.. figure:: https://img.shields.io/pypi/dm/asmai
   :alt: PyPI - Downloads

   PyPI - Downloads

Developpers: Taha Zerrouki: http://tahadz.com taha dot zerrouki at gmail
dot com

+-------------+--------------------------------------------------------------------------------------------+
| Features    | value                                                                                      |
+=============+============================================================================================+
| Authors     | `Authors.md <https://github.com/linuxscout/asmai-arabic-semantic/master/AUTHORS.md>`__     |
+-------------+--------------------------------------------------------------------------------------------+
| Release     | 0.1                                                                                        |
+-------------+--------------------------------------------------------------------------------------------+
| License     | `GPL <https://github.com/linuxscout/asmai-arabic-semantic/master/LICENSE>`__               |
+-------------+--------------------------------------------------------------------------------------------+
| Tracker     | `linuxscout/asmai/Issues <https://github.com/linuxscout/asmai-arabic-semantic/issues>`__   |
+-------------+--------------------------------------------------------------------------------------------+
| Source      | `Github <http://github.com/linuxscout/asmai-arabic-semantic>`__                            |
+-------------+--------------------------------------------------------------------------------------------+
| Feedbacks   | `Comments <https://github.com/linuxscout/asmai-arabic-semantic/>`__                        |
+-------------+--------------------------------------------------------------------------------------------+
| Accounts    | [@Twitter](https://twitter.com/linuxscout)                                                 |
+-------------+--------------------------------------------------------------------------------------------+

Description
-----------

Asmai: (Al'asma'i) Arabic semantic analysis library for Python

مزايا:
~~~~~~

-  استخلاص ثنائيات الكلمات التي تحمل دلالات من نوع : (فاعلية، مفعولية،
   إضافة)


install
~~~~~~~

.. code:: shell

    pip install asmai

Usage
~~~~~

import
^^^^^^

.. code:: python

    pip install asmai

Test
^^^^

.. code:: python

    import asmai.anasem as asm
    text  =  u"يعبد الله منذ أن تطلع الشمس"
    result  =  []
    anasem  =  asm.SemanticAnalyzer()    
    result  =  anasem.analyze_text(text)
    # the result contains objets
    anasem.pprint(result)

-  Extract semantic relation, display only found relations

.. code:: python

    >>> import pprint
    >>> sem_result = anasem.display_sem(result)
    >>> pprint.pprint(sem_result)      
    [[['الشَّمْسُ', 'تَطْلُعَ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
      ['الشَّمْسُ', 'تَطْلُعُ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
      ['الشَّمْسُ', 'تَطْلُعْ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
      ['الشَّمْسُ', 'تَطْلَعَ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
      ['الشَّمْسُ', 'تَطْلَعُ', 'شَمْسٌ', 'طَلَعَ', 'Subject'],
      ['الشَّمْسُ', 'تَطْلَعْ', 'شَمْسٌ', 'طَلَعَ', 'Subject']]]

-  Extract semantic relation, display all words and tags

   .. code:: python

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

-  convert to pandas \`\`\`python >>> import pandas as pd >>> >>> #
   flatten the result ... df = pd.DataFrame(anasem.decode(result)) >>>
   print(df.head()) action affix affix\_key forced\_word\_case ...
   unvocalized unvoriginal vocalized word 0 -ي-- -ي--\|المضارع
   المنصوب:هو:y False ... يعبد عبد يُعَبِّدَ يعبد 1 -ي-- -ي--\|المضارع
   المجهول المجزوم:هو:y False ... يعبد عبد يُعَبَّدْ يعبد 2 -ي--
   -ي--\|المضارع المجهول:هو:y False ... يعبد عبد يُعَبَّدُ يعبد 3 -ي--
   -ي--\|المضارع المعلوم:هو:y False ... يعبد عبد يُعَبِّدُ يعبد 4 -ي--
   -ي--\|المضارع المجزوم:هو:y False ... يعبد عبد يُعَبِّدْ يعبد

[5 rows x 50 columns] >>> df.to\_csv("output/test.csv", encoding="utf8",
sep=":raw-latex:'\t'")



[requirement]
^^^^^^^^^^^^^

::

    1- pyarabic 
    2. sqlite
    3. sylajone

Data Structure:
---------------

Semantic database
~~~~~~~~~~~~~~~~~

.. code:: sql

    CREATE TABLE sqlite_sequence(name,seq);
    CREATE TABLE "derivations" (
        "id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
        "verb" varchar NOT NULL ,
        "transitive" BOOL NOT NULL  DEFAULT 1,
        "derived" VARCHAR NOT NULL ,
        "type" VARCHAR NOT NULL 
     );

CSV Structure:

-  Derivattion

1. id : id unique in the database
2. verb : vocalized collocation
3. transtive : if the verb is transitive
4. derived : derived word from verb number
5. type : type

Semantic relations
^^^^^^^^^^^^^^^^^^

.. code:: sql

    CREATE TABLE "relations" (
        "id" INTEGER PRIMARY KEY  NOT NULL ,
        first" VARCHAR NOT NULL  DEFAULT ('') ,
        "second" VARCHAR NOT NULL  DEFAULT ('') ,
        "rule" VARCHAR NOT NULL  DEFAULT (0) 
     );

CSV Structure:

1. id : id unique in the database
2. first: first word
3. second: second word
4. rule : the extraction rule number :
