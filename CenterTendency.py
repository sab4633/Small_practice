def mean(s):
    k = s.split("\t")
    sum = 0
    count = 0
    for i in k:
        #print(i)
        sum += float(i)
        count+=1
    print(sum, count, sum/count)

def median(s):
    k = s.split("\t")
    m = sorted(k)
    med = (float(m[9])+float(m[10]))/2
    print(med)

def sigx(k):
    sum = 0
    count = 0
    for i in k:
        sum += float(i)
        count += 1
    val = (sum*sum)/count
    return val

def sigx_sq(k):
    sum = 0
    count = 0
    for i in k:
        sum += float(i)*float(i)
    return sum

def std_dev(s):
    k = s.split("\t")
    top = sigx_sq(k)- sigx(k)
    s_val = top/19
    print(s_val)

inp = "1.02	1.25	1.11	1.66	1.32	1.25	1.23	0.76	1.06	0.65	0.95	2.87	1.03	0.74	0.09	0.80	1.63	1.24	0.93	0.85"
inp2 = "0.53	1.06	1.25	2.16	1.57	0.99	1.12	1.07	1.81	2.05	0.92	0.79	1.38	0.62	1.50	1.02	1.12	1.78	1.00	1.15"


mean(inp)
median(inp)
std_dev(inp)
print("--------")
mean(inp2)
median(inp2)
std_dev(inp2)