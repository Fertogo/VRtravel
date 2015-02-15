import urllib
import requests
import json


def saveImagefromURL(url, imageName):
    '''
    Saves an image from a URL into the spheres directory
    @param: url (String) URL of the image to be saved
    @param: imageName (String) Name of the image
    '''
    directory = "spheres/"
    extension = ".jpg"
    urllib.urlretrieve(url, directory + imageName + extension)

def getPhotoURL(location, numResults):
    sourceURL = "http://sphereshare.net/SphereShareServer/www/api-v2/getspheres?limit=" + str(numResults) + "&order=rating&query=" + location
    urlPrefix = "http://sphereshare.net/SphereShareServer/www/spheres/"
    urlSuffix = ".jpg"
    response = requests.get(sourceURL).json()
    photos = response['data']['spheres']
    urls = []
    for photo in photos:
        urls.append(urlPrefix + photo['id'] + urlSuffix)
    return urls


bad = [] # For the cities that don't have any results
def getAllImages(cities, numPerCity):
    for city in cities:
        urls = getPhotoURL(city, numPerCity)

        if (len(urls) == 0): bad.append(city)
        for i in range(len(urls)):
            print 'getting ' + city + str(i)
            saveImagefromURL(urls[i], city + str(i))
            print '   got ' + city + str(i)
            
##    print "Bad----------------"
##    print bad

cities = ['shanghai', 'lagos', 'istanbul', 'mumbai', 'moscow', 'sao paulo', 'beijing', 'guangzhou', 'delhi', 'lahore', 'seoul', 'jakarta', 'tianjin', 'chennai', 'tokyo', 'cairo', 'mexico city', 'kinshasa', 'bangalore', 'new york', 'london', 'bangkok', 'tehran', 'ho chi minh city', 'bogota', 'lima', 'hong kong', 'hanoi', 'wuhan', 'rio de janeiro', 'baghdad', 'singapore', 'riyadh', 'santiago', 'saint petersburg', 'chengdu', 'ankara', 'johannesburg', 'nanjing', 'dar es salaam', 'harbin', 'suzhou', 'sydney', 'new taipei city', 'los angeles', 'melbourne', 'cape town', 'hangzhou', 'durban', 'casablanca', 'algiers', 'berlin', 'nairobi', 'hefei', 'kabul', 'madrid', 'pune', 'changsha', 'jaipur', 'xuzhou', 'wenzhou', 'new york', 'los angeles', 'chicago', 'houston', 'philadelphia', 'phoenix', 'san antonio', 'san diego', 'dallas', 'san jose', 'austin', 'jacksonville', 'indianapolis', 'san francisco', 'fort worth', 'el paso', 'memphis', 'boston', 'dublin', 'paris', 'dubai', 'edinburgh', 'glasgow', 'toronto', 'vienna', 'rome', 'venice', 'florence', 'milan', 'barcelona', 'athens', 'amsterdam', 'prague', 'budapest', 'buenos aires', 'munich', 'montreal', 'brussels', 'bali', 'honolulu', 'new orleans', 'auckland', 'phuket', 'copenhagen', 'orlando']

getAllImages(cities, 2)

newCities = []
for city in cities:
    if city not in bad: newCities.append(city)

#print newCities
