from bs4 import BeautifulSoup, NavigableString
from urllib2 import urlopen
#from textblob import TextBlob
#import plotly
#print plotly.__version__  # version >1.9.4 required
#from plotly.graph_objs import Scatter, Layout

#Note: must be a public profile
print "Twitter username:" 
user = raw_input()

endpoint = "https://twitter.com/%s"

f = urlopen(endpoint % user)
html =  f.read()
f.close()

soup =  BeautifulSoup(html, 'html.parser') 

tweets =  soup.find_all('strong', {'class': 'fullname js-action-profile-name show-popup-with-id'})

tweet_arr=[]
arr_len=[]
for i in range(0,len(tweets)):
	user = tweets[i].contents[0]

	action_tag = soup('span', {'class': 'username js-action-profile-name'})
	show_name = action_tag[i].contents[1].contents[0]

	twit_text = soup('p', {'class': 'js-tweet-text'})

	message = ""
	for nib in twit_text[i]:
		if isinstance(nib, NavigableString):
			message += nib
		else:
			message += nib.text

	print "tweet ",i+1,":\n"
	#print "twt id",len(tweets) #temp length checker
	print user, "@", show_name, message.encode("utf-8")	
	'''testimonial = TextBlob(message)
	x=testimonial.sentiment.polarity
	x=x*100
	print "Tweet polarity is:",x,"%"
	if x < 0:
		print"\nTweet is Negetive"
	elif x > 0:
		print"\nTweet is Positive"
	else:
		print"\nTweet is neutral"
	print '\n'
	tweet_arr.append(x)
	arr_len.append(i)
	if i == 20 :
		break'''
'''plotly.offline.plot({
"data": [
Scatter(x=arr_len, y=tweet_arr)
],
"layout": Layout(

title=user#"twitter positivity of"
)
})'''
