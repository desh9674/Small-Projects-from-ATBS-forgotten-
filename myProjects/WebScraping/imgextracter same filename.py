import os,sys, webbrowser, bs4, requests, pyperclip, pprint,re

#this program download all needed big images from a (given site)?, needs slight modifications for each site,
#not just that it also gets links to all next and previous pages and also displays their links, and if you want can also download images on those pages as well.
#it  can be similiar for any site, just some modifiacations

# This program check if a file already exists, if it does adds (2) to name and continues

# changes to be made for each comic download
# First page comic url in Baseurl===========
# Enter the folder name in Foldername where you want to save the comic =========
# qutored section gives the list of all links comics present on first few and the last page
# At the time started writing this code this was the only comic site i could think of which i had visited year ago!!!!!!!!
os.chdir('C:\\Users\\dhira\\Desktop\\gakes')
'''mainurl = 'https://savitahd.net/comics/savita-bhabhi-24/'
res1 = requests.get(mainurl)
res1.raise_for_status()
soup1 = bs4.BeautifulSoup(res1.text, features="lxml")
comiclinks = soup1.select(".entry-title a")
for m in range(len(comiclinks)):
    comicurl = comiclinks[m].get('href')
    print(comicurl)
pagelinks = soup1.select('.wp-paginate a')
pprint.pprint(pagelinks)
for n in range(len(pagelinks)):
     pageurl = pagelinks[n].get('href')
     print(pageurl)
     res3 = requests.get(pageurl)
     res3.raise_for_status()
     soup3 = bs4.BeautifulSoup(res3.text, features="lxml")
     comiclinks = soup3.select(".entry-title a")
     for o in range(len(comiclinks)):
      comicurl = comiclinks[o].get('href')
      print(comicurl)'''


print('Downloading.....')
Baseurl = 'https://savitahd.net/savita-bhabhi-episode-86-z/'  # start url
Foldername = 'savita ep 86'
os.makedirs(Foldername , exist_ok=True)   # storage folder
for i in range(1):
    print('Downloading base page......   ' + Baseurl)
    res = requests.get(Baseurl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    #             Find the URL of the image.
    imglinks = soup.select("#gallery-2 > dl > dt > a > img")
    #pprint.pprint(imglinks)
    for l in range(len(imglinks)):
        imgurl = imglinks[l].get('src')  
        imgurl = re.sub('-270x300','',imgurl)                     #this returns the actual image url but with addition of .md before.jpg
        if imglinks == []:
         print('Could not find comic image.')
        else:
         print('Downloading image.....    '+ imgurl)
         res = requests.get(imgurl)
         res.raise_for_status()
         imgFilePath = os.path.join(Foldername, os.path.basename(imgurl))
         print(imgFilePath)
         if (os.path.isfile(imgFilePath))== True:
             newimgFilename = list(os.path.basename(imgurl))
             newimgFilename.insert(-4,'(2)')
             newFilePath = os.path.join(Foldername, ''.join(newimgFilename))
             print('File' + imgFilePath + ' Alrready exists, creating renamed file' + newFilePath)
             newFile = open(newFilePath,'wb')
             for chunk in res.iter_content(100000):
                newFile.write(chunk)
             newFile.close()
         else:
             imgFile = open(imgFilePath,'wb')
             print('newfile')
             for chunk in res.iter_content(100000):
              imgFile.write(chunk)
             imgFile.close()
nextlinks = soup.select('.page-links a')
pprint.pprint(nextlinks)
for j in range(len(nextlinks)):
    urlnow = nextlinks[j].get('href')
    #     Find the URL of the gif image.
    print('Downloading page......   ' + urlnow)
    res2 = requests.get(urlnow)
    res2.raise_for_status()
    soup = bs4.BeautifulSoup(res2.text, features="lxml")
    imglinks = soup.select(".entry-content img")
    #pprint.pprint(imglinks)
    for k in range(len(imglinks)):
        imgurl = imglinks[k].get('src')  
        imgurl = re.sub('.th|.md','',imgurl)  #this returns the actual image url but with addition of .md before.gif
        if imglinks == []:
            print('Could not find comic image.')
        else:
            print('Downloading image.....    '+ imgurl)
            res = requests.get(imgurl)
            res.raise_for_status()
            imgFilePath = os.path.join(Foldername, os.path.basename(imgurl))
            print(imgFilePath)
            if (os.path.isfile(imgFilePath))== True:
                newimgFilename = list(os.path.basename(imgurl))
                newimgFilename.insert(-4,'(2)')
                newFilePath = os.path.join(Foldername, ''.join(newimgFilename))
                print('File' + imgFilePath + ' Alrready exists, creating renamed file' + newFilePath)
                newFile = open(newFilePath,'wb')
                for chunk in res.iter_content(100000):
                    newFile.write(chunk)
                newFile.close()
            else:
                imgFile = open(imgFilePath,'wb')
                print('newfile')
                for chunk in res.iter_content(100000):
                    imgFile.write(chunk)
                imgFile.close()
print('Done')
