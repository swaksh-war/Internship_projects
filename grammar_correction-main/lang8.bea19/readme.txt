This directory contains The Lang-8 Corpus of Learner English v1.0 converted to M2 format with ERRANT.

More details about the Lang-8 corpus can be found in the following 2 papers:

Tomoya Mizumoto, Mamoru Komachi, Masaaki Nagata and Yuji Matsumoto. 2011. Mining Revision Log of Language Learning SNS for Automated Japanese Error Correction of Second Language Learners. In Proceedings of the 5th International Joint Conference on Natural Language Processing (IJCNLP), pages 147-155.

Toshikazu Tajiri, Mamoru Komachi, and Yuji Matsumoto. 2012. Tense and Aspect Error Correction for ESL Learners Using Global Context. In Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), pages 198-202.

The original corpus is available here:
https://sites.google.com/site/naistlang8corpora/

ERRANT is available here: 
https://github.com/chrisjbryant/errant

The official Lang-8 M2 file was generated using lang8_to_m2.py which is also included in this directory.
lang8_to_m2.py must be placed inside the main errant directory (i.e. the same place as parallel_to_m2.py) in order to be used.  

After that, the following command was run using Python 3.5:

python3 errant/lang8_to_m2.py lang-8-en-1.0/entries.train -out lang8.train.auto.bea19.m2

This used spacy v1.9.0 and the en_core_web_sm-1.2.0 model.
