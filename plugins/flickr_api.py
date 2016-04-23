import urllib
import json



'''flickr api for levania
to get a random picture use : getRandomPic()
to get a random picture from an album use : getRandomPic(Album='id')
to get public pictures on their flickr page : getPublicPics()
to get all albums use : getAlbums()
to get all images in an album use : getAlbumImages()
'''



'''get static URL of a flickr image'''


def getStaticUrl(image):
	image_farm=str(image['farm'])
	image_server=str(image['server'])
	image_id=str(image['id'])
	image_secret=str(image['secret'])

	url = "http://farm"+image_farm+".staticflickr.com/"+image_server+"/"+image_id+"_"+image_secret+".jpg"
	return url

'''get public pics of Nasa Apollo's '''


def getPublicPics():
	publicPics=urllib.urlopen("https://api.flickr.com/services/rest/?method=flickr.people.getPublicPhotos&api_key=bcb5dcdd467ca41573628d9db143dbff&user_id=136485307%40N06&format=json&nojsoncallback=1") 
	publicPics = publicPics.read()
	publicPics = json.loads(publicPics)

	return [getStaticUrl(x) for x in publicPics['photos']['photo']]


'''gets a random picture from public ones , unless an album is specified'''


def getRandomPic(album=None):
	from random import randint
	images = getPublicPics()
	count = len(images)
	
	if(album != None):
		images = getAlbumImages(album)
		count = len(images)-1
	
	randomPic = images[randint(0,count)]
	return randomPic



'''get albums of Project Apollo Archive'''

def getAlbums():
	albums=urllib.urlopen(" https://api.flickr.com/services/rest/?method=flickr.photosets.getList&api_key=bcb5dcdd467ca41573628d9db143dbff&user_id=136485307%40N06&format=json&nojsoncallback=1")
	albums = albums.read()
	albums = json.loads(albums)

	return [{'id':x['id'], 'title':x['title']['_content']} for x in albums['photosets']['photoset'] ]


'''get images from a specific album of Project Apollo Archive'''


def getAlbumImages(albumId):
	albumImages=urllib.urlopen("https://api.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key=bcb5dcdd467ca41573628d9db143dbff&photoset_id="+albumId+"&user_id=136485307%40N06&format=json&nojsoncallback=1 ")
	albumImages = albumImages.read()
	albumImages = json.loads(albumImages)

	return [getStaticUrl(x) for x in albumImages['photoset']['photo']]
