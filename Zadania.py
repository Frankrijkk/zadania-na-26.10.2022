import random
def rzutkoscmi():
	k1=random.randint(1,6)
	k2=random.randint(1,6)
	print(k1)
	print(k2)
	print(k1+k2)
rzutkoscmi()





def ciagi():
	inp=input("podaj ciag geometryczny")
	ciag=inp.split(',')
	a1=float(ciag[0])
	q=float(ciag[1])/float(ciag[0])
	n=float(input("podaj ile wyrazóe chcesz wyswietlic"))
	i=0
	while i<n:
		
		print(a1*q**i)
		i+=1
	an=float(input("podaj który wyraz chcesz wyswietlic"))-1
	print(a1*q**an)
	sum=float(input("sume ilu wyrazów chcesz wyswietlic"))
	if q==1:
		print(a1*sum)
	else:
		print(a1*(1-q**sum)/(1-q))
ciagi()



def temperatura():
	inp=float(input("podaj temperature w kelwinach: "))
	print("temperatura w stopniach celsjusza: ", inp-273,15)
	print("temoeratura w stopniach rankinea: ",9*inp/5)
	print("temperatura w stopniach reamuera: ",(-273.15+inp)*4/5)
temperatura()
