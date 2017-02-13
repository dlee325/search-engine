# My first search engine.


# Section One: Webcrawler

def get_page(url):
    # This is a simulated get_page procedure so that you can test your
    # code on two pages "http://xkcd.com/353" and "http://xkcd.com/554".
    # A procedure which actually grabs a page from the web will be 
    # introduced in unit 4.
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
    	return ""

def get_next_target(page):
	'''Retrieves the next URL and the next starting point.'''
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote

def union(p, q):
	'''Helper function to add all links found on page to tocrawl'''
	for e in q:
		if e not in p:
			p.append(e)

def get_all_links(page):
	'''Returns all URLs from a webpage's HTML'''
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

def crawl_web(seed):
	'''Outputs a list of URLs that can be reached by a defined seed page.'''	
	tocrawl = [seed]
	crawled = []
	index = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			union(tocrawl, get_all_links(content))
			add_page_to_index(index,page,content)
			crawled.append(page)
	return index



# Section Two: Web Index

index = []

def add_to_index(index,keyword,url):
	'''Adds new entries (keyword & urls) to the index.'''
	for e in index:
		if e[0] == keyword:
			return e[1].append(url)
	index.append([keyword,[url]])

def lookup(index,keyword):
	'''Returns list of associated URLs of keyword.'''
	for e in index:
		if e[0] == keyword:
			return e[1]
	return []

def add_page_to_index(index, url, content):
	'''Updates index to include all word occurences with URL from a webpage.'''
	word_bank = content.split()
	for w in word_bank:
		add_to_index(index, word, url)



