# import libraries
from urllib.request import urlopen
import json
from collections import Counter
import csv 
    
# csv field names 
fields = ['Guid','Title','Related Image Urls','Publish Date','Creation Date','Recurrence Count Sum of Words'] 
rows = []
    
# store the URL in url as parameter for urlopen
url = "https://api.welcomesoftware.com/v2/feed/49e82ccda46544ff4e48a5fc3f04e343?format=json"
  
# store the response of URL
response = urlopen(url)
  
# store the JSON response from url in data
data_json = json.loads(response.read())

articles_list = data_json['entries']

# find most common words with word counds in all titles
all_titles = ""
for i in range(0, len(articles_list)):
    all_titles = all_titles  + articles_list[i]['content']['title']+' '

most_common_words = Counter(all_titles.split()).most_common()

# remove words with count less than 2
filtered_common_words = list(filter(lambda x: x[1] > 1, most_common_words))

# find recurrrence count sum of words in article titles
for i in range(0, len(articles_list)):
    # recurrence_count_sum = 0
    articles_list[i]['content']['recurrence_count_sum'] = 0
    for j in range(0, len(filtered_common_words)):
        if(filtered_common_words[j][0] in articles_list[i]['content']['title'].split()):
            articles_list[i]['content']['recurrence_count_sum'] += filtered_common_words[j][1]

# srt in ascending order by recurrrence count sum to get top 3 articles
articles_list_sorted = sorted(articles_list, key=lambda d: d['content']['recurrence_count_sum'], reverse=True)

if len(articles_list_sorted)>=3:
    n_article =3
else:
    n_article=len(articles_list_sorted)

for i in range(0, n_article):
    rows.append([articles_list_sorted[i]['content']['guid'], articles_list_sorted[i]['content']['title'], [articles_list_sorted[i]['content']['images'][k]['url'] for k in range(0, len(articles_list_sorted[i]['content']['images']))], articles_list_sorted[i]['content']['published_at'], articles_list_sorted[i]['content']['created_at'], articles_list_sorted[i]['content']['recurrence_count_sum']])

# writing to csv file
with open("JSON_feed.csv", "w") as outfile:
    
    # creating a csv writer object
    writerfile = csv.writer(outfile)
      
    # writing dictionary keys as headings of csv
    writerfile.writerow(fields)
      
    # writing list of dictionary
    writerfile.writerows(rows)

    outfile.close()