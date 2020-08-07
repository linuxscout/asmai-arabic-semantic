import sys
sys.path.append('../')    
import asmai.anasem as asm

import pprint
text  =  u"يعبد الله منذ أن تطلع الشمس"
result  =  []
anasem  =  asm.SemanticAnalyzer()    
result  =  anasem.analyze_text(text)


#~ elif display == "pprint":
# the result contains objets
anasem.pprint(result)        
#~ elif display == "only":

# Extract semantic relation, display only found relations
sem_result = anasem.display_sem(result)
pprint.pprint(sem_result)      

## Extract semantic relation, display all words and tags
sem_result = anasem.display_sem(result, all=True)
pprint.pprint(sem_result)

# convert to pandas
import pandas as pd
# flatten the result
df = pd.DataFrame(anasem.decode(result))
print(df.head())
df.to_csv("output/test.csv", encoding="utf8", sep="\t")

