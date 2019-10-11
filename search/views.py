from django.shortcuts import render
from django.http import HttpResponse
import json, re, csv

def Home(request):
	return render(request, 'search/searchWord.html') # rendring to home page 

def SearchListAPIView (request):
	word = request.GET.get('word') # getting word from request
	with open('word_search.tsv') as tsvfile: # opening tsv file as tsvfile
		reader = csv.reader(tsvfile, delimiter='\t') # reading tab seprated values
		result = []
		result1 = []
		for row in reader: # looping through data 
			if re.search(r'^'+word+'', row[0]): # searching the string starting with word entered 
				result.append(row[0]) # appending string in list
			elif re.search(word, row[0]): # searching  the string contaning word entered
				result1.append(row[0]) # appending string in another list
	
		res = sorted(result, key=len)+sorted(result1, key=len) # sorting and joining both list 
		return HttpResponse(json.dumps(res[:25]), content_type="application/json")