import match_words
import time
import re
import threading
import argparse

lock=threading.Lock()

def write_to_file(words,res_datalist):
    pattern=re.compile(r"\.+")
    words_set=[]
    lock.acquire()
    with open("res_multiple_thread.txt","a+",encoding="ISO-8859-1") as file:
        #文件指针移动到开头，避免在最后读不到任何东西
        file.seek(0)
        #print(words)
        for line in file.readlines():
            if not re.search(pattern,line):
                #print(line)
                words_set.append(line.replace("\n",""))
                words_set=list(set(words_set))
                #print(words_set)
        if words not in words_set:
            file.write(words)
            file.write("\n")
            for each_data in res_datalist:
                file.write(each_data)
            #file.write("\n\n\n")
    lock.release()

def match_words_multiple_thread(filename,words):
    datalist=match_words.loaddata(filename)
    res_datalist=match_words.match_specific_words(datalist,words)
    write_to_file(words,res_datalist)

if __name__=='__main__':
    start_time=time.time()
    parser=argparse.ArgumentParser(prog='match_words_multiple_thread',description="Match words with multiple threads")
    parser.add_argument("-w","-words",required=True,type=str)
    args=parser.parse_args()
    if args.w:
        t1=threading.Thread(target=match_words_multiple_thread,args=("3500words1.txt",args.w))
        t2 = threading.Thread(target=match_words_multiple_thread, args=("3500words2.txt", args.w))
        t3 = threading.Thread(target=match_words_multiple_thread, args=("3500words3.txt", args.w))
        t4 = threading.Thread(target=match_words_multiple_thread, args=("3500words4.txt", args.w))

        t1.start()
        t2.start()git
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
    end_time=time.time()
    print("waste time:",end_time-start_time)