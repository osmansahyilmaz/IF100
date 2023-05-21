f = open("turkiye_spotify_data.txt","r")

#inputs
year = int(input("Enter the year: "))
while year not in [2017,2018]:
  year = int(input("Enter the year: "))

month = int(input("Enter the month: "))
if year == 2017:
  while month>12 or month<1:
    month = int(input("Enter the month: "))
elif year == 2018:
  while month!=1:
    month = int(input("Enter the month: "))

strMonth = str(month)
if len(strMonth) == 1:
    strMonth = "0"+str(month)
date = str(year)+"-"+strMonth

#identifying data
data = [i for i in f if date in i]


#lists and variables to divide
indexer = 0
adder = 0
month_dict = {'Track Names':[],'Artists':[],'Streams':[],'Urls':[]}
for i in data:
  splitted = i.split("\t")
  if splitted[1] not in month_dict['Track Names']:
    month_dict['Track Names'].append(splitted[1])
    month_dict['Artists'].append(splitted[2])
    month_dict['Streams'].append(int(splitted[3]))
    month_dict['Urls'].append(splitted[4])
  else:
    adder = splitted[3]
    indexer = month_dict['Track Names'].index(splitted[1])
    month_dict['Streams'][indexer] = month_dict['Streams'][indexer] + int(adder)

#classify track with stream number
id = month_dict['Streams'].index(max(month_dict['Streams']))
numberOfStreams = month_dict['Streams'][id]
songName = month_dict['Track Names'][id]
artistName = month_dict['Artists'][id]
url = month_dict['Urls'][id]

#giving suggestions
print(f"NEW SUGGESTION: {songName}, {artistName} (Total stream number in this month: {numberOfStreams})")
ans = input("Do you want to listen this song (enter either yes or no): ")
while ans.lower()!="no" or ans.lower()!="yes":
  while ans.lower() == "no":
    month_dict['Track Names'].remove(songName)
    month_dict['Artists'].remove(artistName)
    month_dict['Streams'].remove(numberOfStreams)
    month_dict['Urls'].remove(url)
    id = month_dict['Streams'].index(max(month_dict['Streams']))
    numberOfStreams = month_dict['Streams'][id]
    songName = month_dict['Track Names'][id]
    artistName = month_dict['Artists'][id]
    url = month_dict['Urls'][id]
    print(f"NEW SUGGESTION: {songName}, {artistName} (Total stream number in this month: {numberOfStreams})")
    ans = input("Do you want to listen this song (enter either yes or no): ")
  if ans.lower() == "yes":
      break
  ans = input("Do you want to listen this song (enter either yes or no): ")

print(f"Enjoy {songName}, {artistName}. Here is the url for you: {url}")