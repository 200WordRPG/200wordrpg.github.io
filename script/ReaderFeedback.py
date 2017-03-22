import smtplib, ssl, re, csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Enable less secure connections: https://myaccount.google.com/lesssecureapps

#First create a dict of ALL entry names and emails.
#The dict should have the entry names reduced to JUST lowercase letters.

AllTitleEmails = {}
regex = re.compile('[^a-z0-9]')
# tracks all titles to make sure the same game isn't submitted twice by the same author
allTitles = []
allAuthors = []
allEmails = []
filetitle = ""

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

        # as long as it isn't invalid, add it to the list of titles and emails

        if (invalidReason == ""):
            smallTitle = title.lower()
            smallTitle = regex.sub('', smallTitle)
            AllTitleEmails[smallTitle] = [email, author]

        # Otherwise print out the reason for disqualify
        else:
            print(">>> invalid entry: " + title + invalidReason)

print(len(AllTitleEmails))

#==========================>

#NOW we parse through all of the reader feedback, and if an entry matches a dict, we send that feedback to the person.

password = input("Type your password and press enter:")

with open('top5.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:

        #use this counter to iterate through all the columns, getting what we need
        i = 3

        while (i < 27):

            Nexttitle = row[i]
            i = i + 1
            NextNew = row[i]
            i = i + 1
            NextEngaging = row[i]
            i = i + 1
            NextFav = row[i]
            i = i + 1
            NextImprov = row[i]
            i = i + 1


            #find number1 entrant email
            Smalltitle = Nexttitle.lower()
            Smalltitle = regex.sub('', Smalltitle)
            if Smalltitle in AllTitleEmails:
                receiver_name = AllTitleEmails[Smalltitle][1]
                receiver_email = AllTitleEmails[Smalltitle][0]
                #receiver_email = "david.schirduan@gmail.com"
                sender_email = "200wordrpg@gmail.com"
                #print("TITLE FOUND:" + Smalltitle)
            else:
                print("TITLE NOT FOUND:" + Smalltitle)


            message = MIMEMultipart("alternative")
            message["Subject"] = "Feedback For " + Nexttitle
            message["From"] = sender_email
            message["To"] = receiver_email

            # Create the plain-text and HTML version of your message
            text = """\
            Hello PERSONNAME!
            Thank you for participating in this year's 200 Word RPG Challenge. 

            This year our hardworking team of Readers not only helped pick this year's finalists, but they also sent detailed feedback and helpful comments on the top 5 entries they selected! Over 175 entries were picked from 50 Readers.

            And your entry was one of the ones selected. Continue reading for the comments from Readers. You may receive multiple emails if your entry was picked by more than one Reader. The names of the Readers are kept confidential, as was your name; to protect you both. The opinions state in the following feedback do not reflect those of the 200 Word RPG organizers. Please contact 200wordrpg@gmail.com if you have any questions or concerns.

            How does "ENTRYTITLE" meet the “New and Overlooked Stories” criteria?
            
            NEXTNEW

            How does "ENTRYTITLE" meet the “Engaging” criteria?
            
            NEXTENGAGING

            What was your favorite thing about "ENTRYTITLE"?
            
            NEXTFAV

            What would you like to see improved/expanded upon in future versions of "ENTRYTITLE"?
            
            NEXTIMPROV"""

            html = """\
            <html>
            <body>
            <h3>Hello PERSONNAME!</h3>
            <p>Thank you for participating in this year's 200 Word RPG Challenge.</p>
            <p>This year our hardworking team of <a href="https://200wordrpg.github.io/readers">Readers</a> not only helped pick this year's finalists, but they also sent <strong>detailed feedback</strong> and <strong>helpful comments</strong> on the top 5 entries they selected! Over 175 entries were picked from 50 Readers.</p>
            <p>And your entry was one of the ones selected. Continue reading for the comments from Readers.</p>
            <p><em>You may receive multiple emails if your entry was picked by more than one Reader. The names of the Readers are kept confidential, as was your name; to protect you both. The opinions state in the following feedback do not reflect those of the 200 Word RPG organizers. Please contact 200wordrpg@gmail.com if you have any questions or concerns.</em></p>
            <p><strong><em><span style="font-family: Arial; font-style: normal;">How does "ENTRYTITLE" meet the “New and Overlooked Stories” criteria?</span></em></strong></p>
            <p><span style="font-family: monospace;"><em><span style="font-style: normal;">NEXTNEW</span></em></span></p>
            <p><strong><em><span style="font-family: Arial; font-style: normal;">How does "ENTRYTITLE" meet the “Engaging” criteria?</span></em></strong></p>
            <p><span style="font-family: monospace;"><em><span style="font-style: normal;">NEXTENGAGING</span></em></span></p>
            <p><strong><em><span style="font-family: Arial; font-style: normal;">What was your favorite thing about "ENTRYTITLE"?</span></em></strong></p>
            <p><span style="font-family: monospace;"><em><span style="font-style: normal;">NEXTFAV</span></em></span></p>
            <p><strong><em><span style="font-family: Arial; font-style: normal;">What would you like to see improved/expanded upon in future versions of "ENTRYTITLE"?</span></em></strong></p>
            <p><em><span style="font-family: Arial; font-style: normal;"><span style="font-family: monospace;">NEXTIMPROV</span></em></span></p>

            </body>
            </html>
            """

            text = text.replace("PERSONNAME", receiver_name)
            text = text.replace("ENTRYTITLE", Nexttitle)
            text = text.replace("NEXTNEW", NextNew)
            text = text.replace("NEXTENGAGING", NextEngaging)
            text = text.replace("NEXTFAV", NextFav)
            text = text.replace("NEXTIMPROV", NextImprov)

            html = html.replace("PERSONNAME", receiver_name)
            html = html.replace("ENTRYTITLE", Nexttitle)
            html = html.replace("NEXTNEW", NextNew)
            html = html.replace("NEXTENGAGING", NextEngaging)
            html = html.replace("NEXTFAV", NextFav)
            html = html.replace("NEXTIMPROV", NextImprov)

            # Turn these into plain/html MIMEText objects
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part1)
            message.attach(part2)

            #Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )

            print("EMAIL SENT:" + receiver_name + " - " + Nexttitle)

