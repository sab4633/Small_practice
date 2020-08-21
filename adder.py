def count(s):
    dict  = {}
    sar = s.split("	")
    sarset = set()
    for i in sar:
        if i in sarset:
            dict[i] +=1
        else:
            sarset.add(i)
            dict[i] = 0
    return dict

print(count("A	B	D	A	A	F	C	A	C	B	E	B	A	C	F	D	B	C	D	A	A	C	B	E	B	C	E	A	B	A	A	A	B	C	C	D	F	D	B	B	A	F	C	B	A	C	B	E	E	D	A	B	C	E	A	A	F	C	B	D	D	D	B	D	C	A	F	A	A	B	D	E	A	E	D	B	C	A	F	A	C	D	D	A	A	B	A	F	D	C	A	C	B	F	D	A	E	A	C	D"))
