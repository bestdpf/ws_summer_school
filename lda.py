from gensim import corpora, models, similarities
import itertools

def lda(doc, topicNum):
    stopList = set ('for a of the and to in'.split())
    texts = [[word for word in item if word not in stopList] for item in doc]
    all_tokens = sum(texts,[])
    tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    texts = [[word for word in text if word not in tokens_once] for text in texts]
    dic = corpora.Dictionary(texts)
    dic.save('./test.dic')
    corpus = [dic.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('./test.mm',corpus)
    ldaIns = models.ldamodel.LdaModel(corpus = corpus, id2word = dic, num_topics = topicNum,update_every = 1, chunksize = 10000, passes = 1)
    return ldaIns
    
def seqReadFile(filePath):
    doc = [line.lower().split() for line in open(filePath)]
    return doc

def fastReadFile(filePath):
    doc = []
    f_in = open(filePath)
    for line in f_in.readlines():
        doc.append(line.lower().split())
    f_in.close()
    return doc

def cmpDate(date0, date1):
    if date0[0]< date1[0]:
        return True
    elif date0[0] == date1[0] and date0[1]< date1[1]:
        return True
    elif date0[0] == date1[0] and date0[1] == date1[1]:
        return date0[2] < date1[2]
    else:
        return False

# from 2013-12-29 to 2013-06-02
def calcDateId(dateInfo):
    mnCnt = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    mnInc = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365] 
    if dateInfo[0] == 2013:
        return dateInfo[2]-29
    else:
        return 2+mnInc[dateInfo[1]-1] + dateInfo[2]

def timeSplit():
    minDate = [2100,12,31]
    maxDate = [2000,1,1]
    f_in = open('tweet_six_label.txt','r')
    f_t = open('tweet_time.txt','w')
    f_date = []
    for i in range(160):
        f_date_f = open('date' + str(i) + '.txt','w')
        f_date.append(f_date_f)
    for line in f_in.readlines():
        lst = line.replace('&','').replace('#','').replace('\\','').replace('@','').replace(',','').replace('.','').replace('!','').replace('!','').split()
        item = ' '.join(lst[4::])
        date, time = lst[2].replace('T',' ').split()
        date_info = map(int,date.replace('-',' ').split())
        dateId = calcDateId(date_info)
        print dateId
        f_date[dateId].write(item + '\n')
        if cmpDate(maxDate, date_info):
            maxDate = date_info[:]
        if cmpDate(date_info, minDate):
            minDate = date_info[:]

    for i in range(160):
        f_date[i].close()

    f_in.close()
    f_t.close()
    print minDate,maxDate

def test():
    f_in = open('tweet_six_label.txt','r')
    f_doc = open('tweet_content.txt','w')
    for line in f_in.readlines():
        lst = line.replace('&','').replace('#','').replace('\\','').replace('@','').replace(',','').replace('.','').replace('!','').replace('!','').split()
        item = ' '.join(lst[4::])
        f_doc.write(item)
        f_doc.write('\n')
    f_in.close()
    f_doc.close()
    doc = seqReadFile('tweet_content.txt')
    print doc[0]
    ldaIns = lda(doc, 100)
    ldaIns.save('ret.lda')
    ldaIns.print_topics(100)

