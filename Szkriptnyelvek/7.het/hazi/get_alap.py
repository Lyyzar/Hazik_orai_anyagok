#!/usr/bin/env python3
import os

def main():
	alap_py ="""#!/usr/bin/env python3
def main():
	print('Py3')

#####################################################

if __name__ == "__main__":
	main()"""
	title = """---------------------------
Create an empty source file
---------------------------
1) Python [py]
2) C++     [cpp]
q) quit
>"""
	alap_cpp ="""#include <iostream>

using namespace std;

int main()
{
	
	return 0;
}"""

	choice = input(title)
	if choice == "1":
		if(os.path.isfile("alap.py")):
			print("Hiba: a fájl már létezik")
		else:
			with open("alap.py", "w") as myfile:
				print(alap_py, file=myfile)
			print("Fájl létrehozva")
	if choice == "2":
		if(os.path.isfile("alap.cpp")):
			print("Hiba: a fájl már létezik")
		else:
			with open("alap.cpp", "w") as myfile:
				print(alap_cpp, file=myfile)
			print("Fájl létrehozva")

if __name__ == "__main__":
	main()