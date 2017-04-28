## Website README

The [200 Word RPG](https://200wordrpg.github.io/) challenge is a light game design challenge that runs every year. The goal is simple: Design a role-playing game using 200 words or less.

Every year the challenge grows larger and the entries more numerous. This post will detail some of the tools and techniques used to organize and display over 1000 entries across several years of challenges.

## Tool and Services

* [Github Pages](https://pages.github.com/) uses [Jekyll](https://jekyllrb.com/) to turn text files into web pages
* All of the text files use [Markdown](https://daringfireball.net/projects/markdown/) formatting
* Posts can be organized and sorted using [Liquid](https://github.com/Shopify/liquid/wiki) filters
* [Git](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) version control tracks all text and all changes
* [Python](https://www.python.org/) scripting (the script is copied at the bottom of the page)
* Random buttons inspired by [this post](https://thornelabs.net/2014/06/08/a-better-way-to-display-random-jekyll-posts-on-page-load-or-refresh-using-jquery-and-json.html) using [JSON](http://www.json.org/) database
* [Search bar](https://github.com/chinchang/super-search) stolen from [Kushagra Gour](http://kushagragour.in/)
* [Minimal theme](https://github.com/orderedlist/minimal) from [Steve Smith](https://github.com/orderedlist)
* Google [Forms](https://www.google.com/forms/about/), [Docs](https://www.google.com/docs/about/), and [Sheets](https://www.google.com/sheets/about/)

## Workflow

1. Each entry is submitted through a Google Form, which saves all submissions in a Spreadsheet.
2. I check the wordcount for each entry, making a little marker if the entry should be disqualified.
3. I download the spreadsheet as a CSV file, making sure UTF-8 encoding, and quoted text fields are enforced.
4. A python script scans the CSV file checking for duplicate entries, multiple author submissions, and the marker added.
5. The script formats all of the data and creates a Markdown file for each entry.
6. I add the markdown files to the site,and Jekyll turns it into a series of web pages.

The secret sauce is in the Python script and Jekyll.

Traditional websites like Wordpress have a SQL database where posts are stored. Whenever a user clicks a page the website looks in the database for the post info and loads it up for that user. This system is very flexible and simple to use, but it can be slow.

Jekyll is different. It doesn't have a database and any loading is all done at the beginning. Jekyll scans all of the markdown files and turns them into lean, static pages. This makes the site fast and light, but there isn't a database to query and easily alter.

The main reason I chose Jekyll, however, is because it builds pages from text files. And text files are super easy to create using python.

The python script scans through the submitted entries and turns each one into it's own Markdown text file. Through python I can check to make sure entries aren't submitted multiple times and prevent authors from submitted too many entries. Basically I can double check and filter all of the information, transforming it however I wish.

Whenever a new submission is added I can just run the python script again and have it generate a new text file for that entry. It's super quick and easy; I think it takes about 3 minutes to process ALL the entries from 2015, 2016, and 2017. Very nice.

The hard part was just getting all this stuff setup. Now that it's complete and working as expected, added new entries or changing entries is trivial and quick.

Hopefully this little guide will help you understand how the site works, and maybe even help you find uses for Jekyll and python in your own projects. It's a neat little tool and an interesting alternative to traditional website/blog site structures.

## Python Script

```
import csv
import re
import io

# A script to convert a CSV file into multiple markdown text files for Jekyll sites.
# Created by David Schirduan for the 200 Word RPG Challenge

#tracks all titles, authors, and emails to make sure the same game isn't submitted twice by the same author
allTitleEmails = []
allTitles = []
allAuthors= []


with open('2017Entries.csv', encoding="utf8") as f:
  reader = csv.reader(f)
  for row in reader:

# Rows: Timestamp, Email, Name, Link, what done?, title, entry, comments, suggestions, agreement, how hear?, validWordCount

    #To track why entries are disqualified
    invalidReason = ""
    


    #"4/14/2017 3:26:21" convert to "2017-04-14 03:26:21"
    timestamp = row[0]
    pieces = timestamp.split('/')
    
    if len(pieces[0]) == 1:
      pieces[0] = '0' + pieces[0]
      
    if len(pieces[1]) == 1:
      pieces[1] = '0' + pieces[1]

    time = pieces[2].split(' ')

    date = pieces[0] + '-' + pieces[1] + '-' + time[0]

    time = time[1]

    timepieces = time.split(':')

    if int(timepieces[0]) < 10:
      time = '0' + time

    newOrder = date.split('-')

    date = newOrder[2] + '-' + newOrder[0] + '-' + newOrder[1]

    #remove quotes from the author name. breaks MD files
    author = row[2]
    author = re.sub('\"', "", author)
    author = author.rstrip()

    #remove quotes and cap first letter in title
    title = row[5]
    title = title[0].upper() + title[1:]
    title = re.sub('\"', "", title)
    title = title.rstrip()
    fileTitle = title

    #simple way to check title and author
    email = row[1].rstrip()
    email = re.sub(',', "", email) #some people put multiple emails
    email = email.lower() #some people put caps in email
    titleEmail = title+' BY '+email

    # If title has already been submitted, check if the author is also the same
    if(title in allTitles):
      if (titleEmail in allTitleEmails):
        invalidReason = "title already submitted by this email"
        
      #if the author is different, it needs a different filename
      else:
        fileTitle = title + ' BY ' + author #to make sure the filenames are different
        print("duplicate title, different author: " + titleEmail)
        allTitleEmails.append(titleEmail)

    else:
      allTitles.append(title)
      allTitleEmails.append(titleEmail)

    #I manually checked the wordcount. Check to see if I found too many words
    if (row[11] == "invalid"):
      invalidReason = "2 many words"

    entryText = row[6]
    
    link = row[3]
    if not link:
      link = 'no link'

    comments = row[7]
    if not comments:
      comments = 'Author did not add any comments.'
    
    #Strip out all non letter and numbers for the filename
    regex = re.compile('[^a-zA-Z0-9]')
    fileSafe = regex.sub('', fileTitle)
    filename = '{0}-{1}.md'.format(date[:10],fileSafe)
    
    #Entry formatting
    line0 = '---'
    line1 = 'layout: post'
    line2 = 'title: "' + title + '"'
    line3 = 'date: ' + date + ' ' + time
    line4 = 'author: "' + author + '"'
    line5 = 'link: "' + link + '"'
    line6 = 'categories: 2017 ' + 'rpg'
    line7 = '---'
    line8 = '```'
    line9 = entryText
    line10 = '```'
    line11 = '## Author Comments '
    line12 = ''
    line13 = comments

    #as long as it isn't invalid, make a file with the content
    if (invalidReason == ""):
      if (not (author in allAuthors)):
        allAuthors.append(author)
        
      with io.open(filename,'w',encoding='utf8') as file:
        file.write(line0 + '\n')
        file.write(line1 + '\n')
        file.write(line2 + '\n')
        file.write(line3 + '\n')
        file.write(line4 + '\n')
        file.write(line5 + '\n')
        file.write(line6 + '\n')
        file.write(line7 + '\n')
        file.write(line8 + '\n')
        file.write(line9 + '\n')
        file.write(line10 + '\n')
        file.write(line11 + '\n')
        file.write(line12 + '\n')
        file.write(line13 + '\n')
        file.close

    #Otherwise print out the reason for disqualify
    else:
      print("invalid entry: " + title + ' | ' + invalidReason)

```
