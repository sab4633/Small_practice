def mean(s):
    k = s.split("\t")
    print(k)
    sum = 0
    count = 0
    for i in k:
        print(i)
        sum += int(i)
        count+=1
    print(sum, count, sum/count)

inp = "1.02	1.25	1.11	1.66	1.32	1.25	1.23	0.76	1.06	0.65	0.95	2.87	1.03	0.74	0.09	0.80	1.63	1.24	0.93	0.85"
mean(inp)