import csv
import re
import io

# A script to convert a CSV file into multiple markdown text files.
# Created by David Schirduan for the 200 Word RPG Challenge

# tracks all titles to make sure the same game isn't submitted twice by the same author
allTitles = []
allAuthors = []
allEmails = []
counter = 0
print("<table><tr>")

with open('readers.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:

        # Rows: blank, name, email, Link

        # To track why entries are disqualified
        counter = counter + 1

        timestamp = row[0]
        name = row[1].rstrip()
        pronouns = row[2].rstrip()

        print('<td id="entries"><h3><strong>' +
                  name + "</strong></h3></td>")


        if (counter % 3 == 0):
            print("</tr><tr>")


print("</table>")
