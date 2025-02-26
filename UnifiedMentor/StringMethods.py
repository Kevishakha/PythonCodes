# all string methods return new values , they dont change the original string
# Methods
# isalpha(), isalnum(), index(), find(), count(), isdigit(), islower(), isnumeric(), 
# endswith(), upper(), title(), swapcase(), strip(), startswith(), split(), lower(), join(), replace()


txt=" I am vishakha how are you"
print(txt.find('I'))
print(txt.capitalize())
name=txt.isalnum
text='Company'
alpha=text.isalpha()
print(alpha)
str2='456522'
numer=str2.isnumeric()
print(numer)
names=["Vishakha","AHirwar","Choudhary"]
joined="_".join(names)
print(joined)
start=joined.startswith("Vishakha")
print(start)
