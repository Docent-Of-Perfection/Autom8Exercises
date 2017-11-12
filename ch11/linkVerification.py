#!/usr/bin/env python3
#CH11 'Link Verification'
#I was thinking about adding a deletion flag in argparse, but i don't see a current practical use for this so I'm like whatevs
import requests, argparse, sys, re, bs4, pprint
'''
Link Verification
Write a program that, given the URL of a web page, will attempt to download every linked page on the page.
The program should flag any pages that have a 404 “Not Found” status code and print them out as broken links.
'''
parser = argparse.ArgumentParser()
parser.add_argument("site", help="website to download links from")
args = parser.parse_args()
deadLinks = []
#using this to exclude anchor tags that navigate around those fancy responsive designed pages
siteRegex = re.compile(r'http(s)?://\w+\.\w+')
if siteRegex.search(args.site):
    print("Site looks valid")

def requestMarkup(reqUrl):
    markupRequest = requests.get(reqUrl)
    markup = bs4.BeautifulSoup(markupRequest.text, "lxml")
    if str(markupRequest) == "<Response [404]>":
        deadLinks.append(reqUrl)
    elif str(markupRequest) == "<Response [200]>":
        fyal = open(str(markup.find('title').text) + ".html","w")
        fyal.write(markupRequest.text)
        fyal.close()
        #except:
            #print("error writing file")

print("requesting from " + args.site)
markupRequest = requests.get(args.site)
markupRequest.raise_for_status()
markup = bs4.BeautifulSoup(markupRequest.text, "lxml")
#print(markup("a"))
links = markup.select("a")
#print(links)
for link in links:
    if link.has_attr('href') and siteRegex.search(link['href']):
        #pprint.pprint(str(link['href']))
        requestMarkup(link['href'])

print("List of dead links:")
pprint.pprint(deadLinks)
