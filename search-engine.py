# My first search engine.

# Function to print all URLs found on page.


page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">') #example url

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
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			union(tocrawl, get_all_links(get_page(page)))
			crawled.append(page)
	return crawled


