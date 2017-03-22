import csv
import re
import io

# A script to convert a CSV file into multiple markdown text files.
# Created by David Schirduan for the 200 Word RPG Challenge

# tracks all titles to make sure the same game isn't submitted twice by the same author
allTitles = []
allAuthors = []
allEmails = []
filetitle = ""

finalistsCompare = re.compile('[^a-zA-Z0-9]')
finalists = []

for text in ["#TWEENHEIST: A Dystopian Social Media RPG","002: License to Eavesdrop","All Systems Critical","Are You My Maker?","At Your Highness' Pleasure","Auspicious Ends","Canticula Deperita","Come Home","Cooking RPG","Diners, Drive-Ins, and Dice","Dirty Papers","Everything I Gave, I Gave For You","FINAL GIRLS","Goblin Voltron","Hey, This Song Reminds Me Of You","In Our Courts","Missing Parts","Moonsick Family","No honor among thieves","Our bed is but a mossy stone","Past Your Bedtime","Persist - A 200 Word RPG","Quest Giver","Rendezvous","Six Degrees of Singularity","Speak with Dead","Sustenance and Sustainability","The Accord","The Defeated","The Heffalumps Graveyard","The Truth about Jevallik: A Game for Two","The Waiting Room, Your Partner is in Surgery","We are Centaurs: a GMless Tribe-tale","We Are Sorry","We Love You Nino's Pizza","We Who Once Ruled","Word Warriors","Words over the airwaves. ","You Are A Tree","You Had a Time Machine"]:
    finalists.append(finalistsCompare.sub('', text).lower())

print(finalists)

exit

with open('2019.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:

        # Rows: Timestamp, Email, Name, Link, what done?, hear about, title, entry, comments, suggestions, agreement

        # To track why entries are disqualified
        invalidReason = ""

        timestamp = row[0]
        email = row[1].rstrip()
        author = row[2]
        pronouns = row[3]
        link = row[4]
        ISfinalist = ''
        title = row[8]
        entryText = row[9]
        contentWarning = row[10]
        comments = row[13]

        # "4/14/2017 3:26:21" convert to "2017-04-14 03:26:21"
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

        # remove quotes from the author name. breaks MD files
        author = re.sub('\"', "", author)
        author = author.rstrip()

        # The "fileTitle" is the cleaned up title for filename.
        # Need to clean up the title for sorting on the site.
        title = title[0].upper() + title[1:]
        title = re.sub('\"', '', title)
        title = title.rstrip()
        fileTitle = title

        # simple way to check title and author
        email = re.sub(',', "", email)  # some people put multiple emails
        email = email.lower()  # some people put caps in email

        # Check for existing titles, emails, and authors
        if(fileTitle in allTitles):
            if(email in allEmails or author in allAuthors):
                invalidReason = invalidReason + " | Title exists by same author/email"
            else:
                fileTitle = fileTitle + author
                allTitles.append(fileTitle)
                print(">>> VALID: " + fileTitle +
                      " Different Author, same title. ")

        else:
            allTitles.append(fileTitle)

        if(email in allEmails):
            invalidReason = invalidReason + " | Email already submitted an entry"
        else:
            allEmails.append(email)

        if(author in allAuthors):
            invalidReason = invalidReason + " | Author already submitted an entry"
        else:
            allAuthors.append(author)

        if not link:
            link = 'no link'

        if not comments:
            comments = 'Author did not add any comments.'

        # Auto-replace stupid M$ characters
        regexMS = re.compile(
            u'[\u2018\u2019\u201A\u201C\u201D\u201E\u2026\u2013\u2014\u02C6\u2039\u203A\u02DC\u00A0]+')
        results = re.findall(regexMS, title)
        if (len(results) > 0):
            title = title.replace(u'\u2018', '\'')
            title = title.replace(u'\u2019', '\'')
            title = title.replace(u'\u201A', '\'')
            title = title.replace(u'\u201C', '\"')
            title = title.replace(u'\u201D', '\"')
            title = title.replace(u'\u201E', '\"')
            title = title.replace(u'\u2026', '...')
            title = title.replace(u'\u2013', '-')
            title = title.replace(u'\u2014', '-')
            title = title.replace(u'\u02C6', '^')
            title = title.replace(u'\u2039', '<')
            title = title.replace(u'\u203A', '>')
            title = title.replace(u'\u02DC', ' ')
            title = title.replace(u'\u00A0', ' ')

        results = re.findall(regexMS, entryText)
        if (len(results) > 0):
            entryText = entryText.replace(u'\u2018', '\'')
            entryText = entryText.replace(u'\u2019', '\'')
            entryText = entryText.replace(u'\u201A', '\'')
            entryText = entryText.replace(u'\u201C', '\"')
            entryText = entryText.replace(u'\u201D', '\"')
            entryText = entryText.replace(u'\u201E', '\"')
            entryText = entryText.replace(u'\u2026', '...')
            entryText = entryText.replace(u'\u2013', '-')
            entryText = entryText.replace(u'\u2014', '-')
            entryText = entryText.replace(u'\u02C6', '^')
            entryText = entryText.replace(u'\u2039', '<')
            entryText = entryText.replace(u'\u203A', '>')
            entryText = entryText.replace(u'\u02DC', ' ')
            entryText = entryText.replace(u'\u00A0', ' ')

        # Check for invalid characters
        regexEmoji = re.compile('[^\x00-\xFF]+')

        results = re.findall(regexEmoji, title)
        chars = []
        if (len(results) > 0):
            for res in results:
                for r in list(res):
                    chars.append(ord(r))
            invalidReason = invalidReason + \
                " | Invalid Characters detected in title: " + str(chars)
            title = timestamp

        results = re.findall(regexEmoji, entryText)
        chars = []
        if (len(results) > 0):
            for res in results:
                for r in list(res):
                    chars.append(ord(r))
            invalidReason = invalidReason + \
                " | Invalid Characters detected in entry " + str(chars)

        # Wordcount the entry text
        regexCO = re.compile(
            '[0-9]+[0-9,\.]*|[&0-9a-zA-Z\xC0-\xFF]+[-\']?[0-9a-zA-Z\xC0-\xFF]*')
        results = re.findall(regexCO, entryText)
        if (len(results) > 200):
            invalidReason = invalidReason + \
                " | Wordcount: " + str(len(results))


        # Content Warning
        if (contentWarning):
            contentWarning = "<div id=\"warning\"><div id=\"content\"><h3><strong>! Content Warning: "+contentWarning + " !</strong></h3><i>Continue scrolling to read the entry.</i></div></div>"
        else:
            contentWarning = ""

        if (finalistsCompare.sub('', title).lower() in finalists):
            ISfinalist = " finalist"
            if (invalidReason == ""):
                with io.open("FINALISTS.md", 'a+', encoding='utf8') as file:
                    file.write(' ' + '\n')
                    file.write("# " + title + '\n')
                    file.write(' ' + '\n')
                    file.write(contentWarning + '\n')
                    file.write(' ' + '\n')
                    file.write('```' + '\n')
                    file.write(entryText + '\n')
                    file.write('```' + '\n')
                    file.write("<hr>" + '\n')
                    file.close
            finalists.remove(finalistsCompare.sub('', title).lower())

        # Entry formatting
        line0 = '---'
        line1 = 'layout: post'
        line2 = 'title: "' + title + '"'
        line3 = 'date: ' + date + ' ' + time
        line4 = 'author: "' + author + '"'
        line5 = 'link: "' + link + '"'
        line6 = 'categories: 2019 rpg' + ISfinalist
        line7 = '---'
        line8 = contentWarning
        line9 = ' '
        line10 = '```'
        line11 = entryText
        line12 = '```'
        line13 = '## Author Comments'
        line14 = comments

        # Create filename

        regex = re.compile('[^a-zA-Z0-9]')
        fileTitle = regex.sub('', fileTitle)
        fileTitle = '{0}-{1}.md'.format(date, fileTitle)

        # as long as it isn't invalid, make a file with the content
        if (invalidReason == ""):
            with io.open(fileTitle, 'w+', encoding='utf8') as file:
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
                file.write(line14 + '\n')
                file.close

        # Otherwise print out the reason for disqualify
        else:
            print(">>> invalid entry: " + title + invalidReason)

print(finalists)
