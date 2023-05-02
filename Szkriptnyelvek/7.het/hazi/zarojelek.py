def test(exp):
	zjelek = ""
	parok = {"(":")","{":"}","[":"]"}
	db = [0, 0]
	for x in exp:
		if x in "({[":
			db[0] += 1
			zjelek += x
		elif x in ")}]":
			db[1] += 1
			if x != parok[zjelek[len(zjelek) - 1]]:
				return "Hibás"
			else:
				zjelek = zjelek[:-1]
	if db[0] == db[1]:
		return "Helyes"
	else:
		return "Hibás"

def main():
	exp = "(({[(((1)-2)+3)-3]/3}-3)"
	print(test(exp))

if __name__ == "__main__":
	main()