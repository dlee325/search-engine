# My first search engine.

# Test to see if code for extracting a url out of HTML works.

# More specifically, it is code that assigns to the variable url 
# a string that is the value of the first URL that appears in a 
# link tag in the string page.


page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">') #example url

start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url = page[start_quote + 1:end_quote]