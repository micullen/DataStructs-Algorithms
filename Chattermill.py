"""
Use the Content endpoint to return all articles related to BOTH python and coding (i.e.
not articles that relate to python OR coding)
3. From the results, pull the following information into a CSV:
○ id
○ type
○ sectionId
○ sectionName
○ webPublicationDate
○ webTitle
○ webUrl
○ apiUrl
○ isHosted
○ pillarId
○ pillarName
○ Wordcount
"""
import requests
# https://content.guardianapis.com/search?q=debate%20AND%20economy&tag=politics/politics&from-date=2014-01-01&api-key=test
# https://content.guardianapis.com/search?q=python&api-key=38b78030-2700-4bdd-838f-ac56dd00811e

def run():
    z = requests.get("https://content.guardianapis.com/search?q=python%20AND%20coding&api-key=38b78030-2700-4bdd-838f-ac56dd00811e&order-by=newest")
    p = z.content
    return p

