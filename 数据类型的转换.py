#string->int
str2int=int("213")
print("此时的“231“已经是",type(str2int),str2int)
#但不是所有字符串都能转整型，这显而易见
"""
str2int=int("abcd")
print(type(str2int),str2int)
"""
#float->int   小数部分会被截断
flo2int=int(3.14)
print(type(flo2int),flo2int)

#int ->float,可能会丢失精度,因为float最多只能表示24位(隐藏位+23个尾数位)。这里搞错了,python的float是双精度浮点数
int2float=float(67108863)
print(type(int2float),int2float)
print(int(int2float))

#float->string
float2str=float("3.1415")
print(type(float2str),float2str)



