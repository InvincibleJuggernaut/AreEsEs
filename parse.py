import feedparser
import re
from colorama import init, Fore, Back, Style

init()

subreddits = []

while True:
    print("Options :")

    i=1
    
    for subreddit in subreddits:
        print(str(i)+" "+subreddit)
        i+=1
    
    print()
    option = input('Select a subreddit : ')
    
    if(option=='n'):
        break
    
    data = feedparser.parse('http://www.reddit.com/r/'+subreddits[int(option)-1]+'.rss')
    
    print("\n"+Fore.BLACK+ Back.YELLOW+data['feed']['title']+Style.RESET_ALL)
    print(data['feed']['link'])
    print(data.feed.subtitle)
    print()

    total_entries = len(data['entries'])
    for i in range(0, total_entries):
        title = data['entries'][i]['title']
        link = data['entries'][i]['link']
        postId = re.findall('/comments/(.*?)/', link)
        comments = feedparser.parse('http://www.reddit.com/r/'+subreddits[int(option)-1]+'/comments/'+postId[0]+'/.rss')
        total_comments = len(comments['entries'])
        print(Fore.YELLOW+title+ Style.RESET_ALL+ ' '+link+' '+'\n')
        comment = comments['entries'][0]['content']
        comment = re.findall('<p>(.*?)</p>', str(comment[0]))
        if(len(comment)!=0):
            print(str(comment))
        print()
        if(total_comments!=0):
            for j in range(1, total_comments):
                comment = comments['entries'][j]['content']
                comment = re.findall('<p>(.*?)</p>', str(comment[0]))
                comment = str(comment).replace('[\'',' ')
                comment = str(comment).replace('\']',' ')
                comment = str(comment).replace('[\"',' ')
                comment = str(comment).replace('\"]',' ')
                print(Fore.GREEN +"COMMENT "+str(j)+Style.RESET_ALL+" "+str(comment))
            print("\n\n")
        elif(total_comments==0):
            print("NO COMMENTS")
