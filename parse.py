import feedparser
import re

subreddit = ''

data = feedparser.parse('http://www.reddit.com/r/'+subreddit+'.rss')

print(data['feed']['title'])
print(data['feed']['link'])
print(data.feed.subtitle)
print()

total_entries = len(data['entries'])
for i in range(0, total_entries):
    title = data['entries'][i]['title']
    link = data['entries'][i]['link']
    postId = re.findall('/comments/(.*?)/', link)
    comments = feedparser.parse('http://www.reddit.com/r/'+subreddit+'/comments/'+postId[0]+'/.rss')
    total_comments = len(comments['entries'])
    print(title+ ' '+link+' ')
    comment = comments['entries'][0]['content']
    comment = re.findall('<p>(.*?)</p>', str(comment[0]))
    if(len(comment)!=0):
        print(str(comment))
    print("COMMENTS")
    if(total_comments!=0):
        for j in range(1, total_comments):
            comment = comments['entries'][j]['content']
            comment = re.findall('<p>(.*?)</p>', str(comment[0]))
            print("COMMENT "+str(j)+ " "+str(comment))
    else:
        print("NO COMMENTS")
