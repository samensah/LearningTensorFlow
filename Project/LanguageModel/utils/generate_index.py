import numpy as np
from collections import Counter
import pandas as pd

OUT_FILE="chars_ids.csv"
IN_FILE_LIST=["../ptb_corpus/ptb.test.txt","../ptb_corpus/ptb.train.txt","../ptb_corpus/ptb.valid.txt"]
EXTRA_CHARS=["<sos>","<eos>","<unk>"]

def generate(file_list):
    counter=Counter()
    print("counter:\n",counter)
    for file in file_list:
        with open(file=file,encoding="utf-8",errors="ignore") as in_file:
            lines=in_file.readlines()
            #print("lines:\n",lines)
            for line in lines:
                word_list=line.strip().split(sep=" ")
                #print("word_list:",word_list)
                for word in word_list:
                    counter[word]+=1
    #print("counter:\n",counter)
    #print("counter size:",len(counter))
    counter.pop("<unk>")
    #print("counter:\n", counter)
    #print("counter size:", len(counter))

    all_word=EXTRA_CHARS+list(counter.keys())
    #print("all_word:", len(all_word))
    ids=[i for i in range(1,len(all_word)+1)]
    #print("ids:",ids)
    pd.DataFrame(data={"id": ids, "word": all_word}). \
         to_csv(path_or_buf="../index_files/words_ids.csv", index=False, encoding="utf_8")

if __name__=="__main__":
    generate(file_list=IN_FILE_LIST)


