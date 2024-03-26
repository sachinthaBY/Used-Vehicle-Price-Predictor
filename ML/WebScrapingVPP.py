import requests
from bs4 import BeautifulSoup
import csv

a_file = open("vehicleDataset.csv", "a")
writer = csv.writer(a_file)

# Write the title of the columns to the CSV file
writer.writerow(["Price", "Make", "Model", "Year", "Transmission", "FuelType", "EngineCapacity", "Mileage"])

# URL of the site
for num in range(1, 251): # max 250
    print(num)
    url = 'https://ikman.lk/en/ads/sri-lanka/cars' + str(num) + '&enum.condition=used'

    # Connect to the URL
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")
    count = 0
    for vehicle in soup.findAll('a', attrs={'card-link--3ssYv gtm-ad-item'}):
        selectedVehicleURL = "https://ikman.lk" + vehicle.get('href')
        newResponse = requests.get(selectedVehicleURL)

        newSoup = BeautifulSoup(newResponse.text, "html.parser")
        if count >= 1:

            # Create a list to store the current row of records
            vehicleInfoList = [
                'N/A',
                'N/A',
                'N/A',
                'N/A',
                'N/A',
                'N/A',
                'N/A',
                'N/A'
            ]

            # Retrieve the price of the vehicle
            for vehiclePrice in newSoup.findAll('div', attrs={'class': 'amount--3NTpl'}):
                vehicleInfoList.insert(0, vehiclePrice.text[3::].replace(',', ''))

            for vehicleInfo in newSoup.findAll('div', attrs={
                'class': 'two-columns--19Hyo full-width--XovDn justify-content-flex-start--1Xozy '
                         'align-items-normal--vaTgD flex-wrap-nowrap--3IpfJ flex-direction-row--27fh1 flex--3fKk1'}):
                infoTitle = vehicleInfo.find('div', attrs={'class': 'word-break--2nyVq label--3oVZK'}).text

                if infoTitle == "Make: ":
                    allInfo = vehicleInfo.find('div', attrs={'class': 'word-break--2nyVq value--1lKHt'}).text
                    vehicleInfoList.insert(1, allInfo)

                if infoTitle == "Model: ":
                    allInfo = vehicleInfo.find('div', attrs={'class': 'word-break--2nyVq value--1lKHt'}).text
                    vehicleInfoList.insert(2, allInfo)

                if infoTitle == "Year: ":
                    allInfo = vehicleInfo.find('div', attrs={'class': 'word-break--2nyVq value--1lKHt'}).text
                    vehicleInfoList.insert(3, allInfo)

                if infoTitle == "Transmission: ":
                    allInfo = vehicleInfo.find('div', attrs={'class': 'word-break--2nyVq value--1lKHt'}).text
                    vehicleInfoList.insert(4, allInfo)

                if infoTitle == "Fuel type: ":
                    allInfo = vehicleInfo.find('div', attrs={'class': 'word-break--2nyVq value--1lKHt'}).text
                    vehicleInfoList.insert(5, allInfo)

                if infoTitle == "Engine capacity: ":
                    allInfo = vehicleInfo.find('div', attrs={'class': 'word-break--2nyVq value--1lKHt'}).text
                    vehicleInfoList.insert(6, allInfo.replace(' cc', '').replace(',', '')) # Replace both the comma and the ' cc' text

                if infoTitle == "Mileage: ":
                    allInfo = vehicleInfo.find('div', attrs={'class': 'word-break--2nyVq value--1lKHt'}).text
                    vehicleInfoList.insert(7, allInfo.replace(' km', '').replace(',', '')) # Replace both the comma and the ' km' text

            # Write the records to the CSV file
            writer.writerow([vehicleInfoList[0], vehicleInfoList[1], vehicleInfoList[2], vehicleInfoList[3], vehicleInfoList[4], vehicleInfoList[5], vehicleInfoList[6], vehicleInfoList[7]])

        count += 1
a_file.close()
