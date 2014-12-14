f_in = open('date0.txt','r')
f_out = open('date0.csv','w')
for line in f_in.readlines():
    print line
    line = '\"' + line.rstrip() + '\"'
    print line
    f_out.write(line)
    f_out.write('\n')
f_out.close()
f_in.close()
