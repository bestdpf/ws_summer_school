from gensim import corpora, models, similarities

def lda(doc, topicNum):
    stopList = set ('for a of the and to in'.split())
    texts = [[word for word in item if word not in stopList] for item in doc]
    all_tokens = sum(texts,[])
    tokens_once = set(word for word in set(all_tokesn) if all_tokens.count(word) == 1)
    texts = [[word for word in text if word not in tokens_once] for text in texts]
    dic = corpora.Dictionary(texts)
    dic.save('./test.dic')
    corpus = [dic.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('./test.mm',corpus)
    models.ldamodel.LdaModel(corpus = corpus, id2word = dic, num_topics = topicNum,update_every = 1, chunksize = len(texts), passes = 1)
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
    ldaIns.print_topics(100)

