import unittest
import photo_album_viewer
import json
import urllib


class PhotoAlbumTestCases(unittest.TestCase):

    def test_photo_album_viewer_returns_all_photo_albums_correctly_from_json_url(self):
        url = "https://jsonplaceholder.typicode.com/photos"
        response = urllib.urlopen(url)
        photo_albums = json.loads(response.read())
        self.assertEquals(photo_album_viewer.get_photos_from_url(url), photo_albums)

    def test_photo_album_viewer_returns_specific_photo_albums_based_on_album_id(self):
        url = "https://jsonplaceholder.typicode.com/photos?albumId=3"
        response = urllib.urlopen(url)
        photo_albums = json.loads(response.read())
        self.assertEquals(photo_album_viewer.get_photos_from_url(url), photo_albums)

    def test_get_total_amount_of_albums_returns_the_correct_amount_of_albums(self):
        response = urllib.urlopen("https://jsonplaceholder.typicode.com/photos")
        photo_albums = json.loads(response.read())
        self.assertEquals(photo_album_viewer.get_total_amount_of_albums(photo_albums), "100")
