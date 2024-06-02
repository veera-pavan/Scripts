# import urllib
# use urllib.request to get the data from url
# write a function that takes a url
# returns a response

import urllib.request as urllib

def main(url):
    print("checking site connectivity ..")
    try:
       response = urllib.urlopen(url)
       print("The response code:", response.getcode())
       print("Url " + str(input_url) + " connectivity was successfull")
    except:
       print("invalid url...") 

print("This is site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)