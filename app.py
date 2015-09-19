# @Author: varun elango
# @Date:   2015-08-19 11:30:11
# @Email:   ve365@nyu.edu
#
# @Last Modified by:   varun elango
# @Last Modified time: 2015-08-19 11:30:11

from flask import Flask, url_for
from flask import request
import httplib2

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'
# Receive search term and hits the flikr search api returning a JSON
@app.route('/search/<Term>') 
def search_term(Term):
	h = httplib2.Http(".cache")
	url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=8b4a7b0052eeaa71085f333e84195ce3&text="+Term+"&format=json&nojsoncallback=1"
	(resp_headers, content) = h.request(url, "GET")
	return content

#Receive search term and limit as params and hits the flikr api returning a JSON
@app.route('/search/<Term>/<limit>')
def search_term_limit(Term,limit):
	h = httplib2.Http(".cache")
	if limit < 1 :
		limit = 1
	url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=8b4a7b0052eeaa71085f333e84195ce3&text="+Term+"&per_page="+limit+"&format=json&nojsoncallback=1"
	(resp_headers, content) = h.request(url, "GET")
	return content

# Receive search term,limit as params , sets page defaults to 1 amd hits the flikr api returning a valid JSON
@app.route('/search/<Term>/<limit>/page')
def search_limit_page(Term,limit):
	h = httplib2.Http(".cache")
	if limit < 1 :
		limit = 1
	url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=8b4a7b0052eeaa71085f333e84195ce3&text="+Term+"&per_page="+limit+"&page=1&format=json&nojsoncallback=1"
	(resp_headers, content) = h.request(url, "GET")
	return content

   

if __name__ == '__main__':
   app.run()