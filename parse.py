import feedparser
import re

subreddit = ''

data = feedparser.parse('http://www.reddit.com/r/'+subreddit+'.rss')

print(data['feed']['title'])
print(data['feed']['link'])
print(data.feed.subtitle)

total_entries = len(data['entries'])

for i in range(0, total_entries):
    title = data['entries'][i]['title']
    link = data['entries'][i]['link']
    postId = re.findall('/comments/(.*?)/', link)
    print(title+ ' ' +link+ ' ' +postId[0])
