import json	


def QuoteFromLine(fileline):
	quote = ''
	isQuote = False
	for char in fileline:
		if char == '"':
			isQuote = True
		if(isQuote):
			quote += char
	return quote


def CreateQuoteList():
	f = open("quotes.html","r")
	file = f.readlines()

	quotes = open("quote_list.txt","a+")

	for i in range(0, len(file)):
		quote = QuoteFromLine(file[i])
		quotes.write(quote)

	f.close()
	quotes.close()

def CreateJSON():
	q = open("quote_list.txt")
	quotes = q.readlines()
	with open("quote_list.json","w") as quotefile:
		json.dump(quotes, quotefile)


if __name__ == '__main__':
	
	CreateQuoteList()
	CreateJSON()
