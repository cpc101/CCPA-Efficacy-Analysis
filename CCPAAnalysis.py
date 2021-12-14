
# I would like to acknowledge the tutorial at
# https://towardsdatascience.com/using-data-science-skills-now-text-readability-analysis-c4c4641f5875
# for help with this code


from pathlib import Path
import pandas as pd
import re

from readability import Readability


resultsTable = []

def preprocess(text): #Clean Input Texts to Reduce Formatting Issues

    text = re.sub(r'[ ]*(\n|\n\n|\r\n|\r)[ ]*', '. ', text) # Remove new lines
    text = text.replace("\t", ". ")
    text = text.replace(". .", ". ")
    text = text.replace("..", ". ")


    return text

def analyzeText(websiteName): #Peform Reading Analysis
    websiteStats = [websiteName]
    
    textBefore = preprocess(Path(websiteName + "Before.txt").read_text())
    r = Readability(textBefore)
    textBeforeComplexity = r.flesch().score
    websiteStats.append(str(textBeforeComplexity))
    
    textAfter = preprocess(Path(websiteName + "After.txt").read_text())
    r = Readability(textAfter)
    textAfterComplexity = r.flesch().score
    websiteStats.append(str(textAfterComplexity))


    resultsTable.append(websiteStats)


websitesTable = ['Google', 'Amazon', 'Yahoo','Facebook','Zoom','Reddit','Salesforce','Bing','Microsoft',
                  'Shopify','Wikipedia','Ebay','Chase','Netflix','Walmart','Instagram','Etsy','Charturbate'
                  ,'Linkedin','Disney','Zillow','Instructure','Twitter','Canva','Twitch', 'Adobe', 'Dropbox', 'Indeed', 'CNN',
                 'BestBuy', 'Apple', 'NewYorkTimes', 'Intuit', 'PayPal', 'Target', 'TikTok', 'Spotify', 'HomeDepot',
                  'AliExpress', 'Hulu', 'CapitalOne', 'IMDB']
for i in websitesTable:
    analyzeText(i)

df = pd.DataFrame(resultsTable, columns=[['Website', 'Flesch Reading Ease Score (Before)', 'Flesh Reading Ease Score (After)']])
df.to_clipboard(sep=',')  # To allow export to spreadsheets
print(df)



