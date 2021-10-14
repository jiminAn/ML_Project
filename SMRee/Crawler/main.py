import twint
import os
import pandas as pd

def getKeyword(filename):
    keywords = []
    keywordFile = open(os.path.join('data', filename), 'r')
    for line in keywordFile.readlines():
        contents = line.strip('\n').strip(',').split(',')
        keywords.append(contents)
    return keywords

def crawl(keywords, wholeSize):
    eachSize = wholeSize // len(keywords)
    print('---------------- Variables ------------------')
    print('eachSize : ', eachSize)
    for i in keywords:
        # Configure
        c = twint.Config()
        print('keyWord : ', i)
        #c.Since = '2021-10-02'
        #c.Until= '2021-10-12'
        #c.Username = ''
        c.Limit = eachSize
        c.Store_json = True
        c.Output = 'res.json'
        c.Hide_output = True
        c.Search = i
        c.Store_object = True
        # Run
        twint.run.Search(c)

def df_process(outputSize, outputName):
    output = []
    # Data load
    filename = 'res.json'
    temp_df = pd.read_json(filename, lines=True)
    output.append(temp_df)

    wanted = ["created_at", "username", "tweet", "language", "hashtags"]  

    df = pd.concat(output, sort=False)
    df = df.loc[df.language == 'en', wanted][:outputSize]
    df.to_json(outputName, orient = 'records')

if __name__=='__main__':
    filename = 'disasterTag.csv'
    outputName = 'disaster.json'
    sampleSize = 2000
    outputSize = 400

    crawl(getKeyword(filename), sampleSize)
    df_process(outputSize, outputName)