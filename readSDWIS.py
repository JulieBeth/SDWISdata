import requests
# not sure if I need to also import json

# the string below got all NH water systems in json, active and inactive
response = requests.get("https://enviro.epa.gov/enviro/efservice/water_system/PRIMACY_AGENCY_CODE/NH/JSON")

# the string below got active NH water systems in csv
response = requests.get("https://enviro.epa.gov/enviro/efservice/water_system/PRIMACY_AGENCY_CODE/ACTIVITY_STATUS_CODE/A/NH/CSV")
url_content = response.content
csv_file = open('downloaded.csv', 'wb')

csv_file.write(url_content)
csv_file.close()

# the file downloaded.csv is now in my home python folder
