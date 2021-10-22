# Text Preprocessing

### Trainset Data Table

| id | key | location | text | label |
-----|-----|----------|------|-------|
0 - 400 | hashtags | null | tweet contents | 0 or 1|

### Text Preprocessing Step
> 1. Remove URL
```python
import re

html_regexps = re.compile(r"https?://[a-zA-Z0-9/.]*\b")
removeHtml = udf(lambda x: html_regexps.sub("", x), StringType())

disasterDf = disasterDf.withColumn("text", removeHtml(disasterDf['text']))
non_disasterDf = non_disasterDf.withColumn("text", removeHtml(non_disasterDf['text']))
```

> 2. Remove Emojis

```python
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)

remove_emoji = udf(lambda x: emoji_pattern.sub("", x), StringType())
disasterDf = disasterDf.withColumn("text", remove_emoji(disasterDf["text"]))
non_disasterDf = non_disasterDf.withColumn("text", remove_emoji(non_disasterDf["text"]))
```

> 3. Remove punctuations

```python
import string

table = str.maketrans('', '', string.punctuation)
remove_punctuation = udf(lambda x: x.translate(table), StringType())
disasterDf = disasterDf.withColumn("text", remove_punctuation(disasterDf["text"]))
non_disasterDf = non_disasterDf.withColumn("text", remove_punctuation(non_disasterDf["text"]))
```

> 4. Remove side whitespace (Strip)

```python
strip_udf = udf(lambda x: x.strip(), StringType())
disasterDf = disasterDf.withColumn("text", strip_udf(disasterDf["text"]))
non_disasterDf = non_disasterDf.withColumn("text", strip_udf(non_disasterDf["text"]))
```

### Data Structure
	
	data
	├── disaster-new.csv
	│   ├── _SUCCESS
	│   └── part-00000-9a5662bc-1a9c-449a-97cd-10709784ba12-c000.csv
	├── disaster-new.json
	│   ├── _SUCCESS
	│   └── part-00000-97b6b08d-350f-41f9-944c-6f19230d9eb3-c000.json
	├── disaster.json
	├── non_disaster-new.csv
	│   ├── _SUCCESS
	│   └── part-00000-93c57e8a-8615-4ee1-b61d-5228abd11d6a-c000.csv
	├── non_disaster-new.json
	│   ├── _SUCCESS
	│   └── part-00000-6e476317-c5de-479c-b362-f79c58bbbb24-c000.json
	└── non_disaster.json

### Data Descriptions

- Raw Data
	- disaster.json
	- non_disiaster.json

- Processed Data
	- disaster-new.json/`part-00000-97b6b08d-350f-41f9-944c-6f19230d9eb3-c000.json`
	- disaster-new.csv/`part-00000-9a5662bc-1a9c-449a-97cd-10709784ba12-c000.csv`
	- non_disaster-new.json/`part-00000-6e476317-c5de-479c-b362-f79c58bbbb24-c000.json`
	- non_disaster-new.csv/`part-00000-93c57e8a-8615-4ee1-b61d-5228abd11d6a-c000.csv`

