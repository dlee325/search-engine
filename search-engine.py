# My first search engine.

# Encapsulate code in a function.
# Account for cases where no URL in HTML.


page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">') #example url

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote