import argparse
import re
import time

def loaddata(filename):
    pattern=re.compile(r"[A-Z]")
    datalist=[]
    with open(filename,"r",encoding="ISO-8859-1") as file:
        for line in file.readlines():
            if pattern.match(line):
                #print(line)
                continue
            else:
                #要有一个值接收返回值
                line=re.sub(r"\[.*\]","",line)
                process_line=line.replace("?","")
                datalist.append(process_line)
    return datalist

def match_specific_words(datalist,words):
    res_datalist=[]
    for each_data in datalist:
        if re.search(words,each_data):
            #print(each_data+"\n")
            res_datalist.append(each_data)
    return res_datalist

def write_to_file(words,res_datalist):
    pattern=re.compile(r"\.+")
    words_set=[]
    with open("res.txt","a+",encoding="ISO-8859-1") as file:
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
            file.write("\n\n\n")

if __name__ == '__main__':
    start_time=time.time()
    datalist=loaddata("3500words_utf8.txt")

    parser=argparse.ArgumentParser(prog="match_words.py",description="Match words you input")

    parser.add_argument("-w","-words",required=True,type=str)

    args=parser.parse_args()

    if args.w:
        res_datalist=match_specific_words(datalist,args.w)

    write_to_file(args.w,res_datalist)
    end_time=time.time()
    print("waste time: %s",end_time-start_time)
