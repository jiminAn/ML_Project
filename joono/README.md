# Text Preprocessing

### Trainset Data Table

| id | key | location | text | label |
-----|-----|----------|------|-------|
0 - 400 | hashtags | null | tweet contents | 0 or 1|

### Text Preprocessing Step
> 1. Remove URL
> 2. Remove Emojis
> 3. Remove punctuations
> 4. Remove whitespace (Strip)

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

