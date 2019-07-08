import json
import urllib


# Gets the photos from the designated url and returns them
def get_photos_from_url(url):
    response = urllib.urlopen(url)
    photo_albums = json.loads(response.read())
    return photo_albums


# Calculates the total number of photo albums and returns them
def get_total_amount_of_albums(photo_albums):
    total_albums = 0

    for album in photo_albums:
        album_id = album.get('albumId')
        if album_id > total_albums:
            total_albums = album_id

    return str(total_albums)


# Displays the photos in a user friendly way for clarity
def display_photos_for_user(photos):
    for photo in photos:
        photo_id = photo.get('id')
        photo_title = photo.get('title')
        print('[' + str(photo_id) + '] ' + photo_title)
        print('-----------------------------------------------------------------------------------------')


photos_url = "https://jsonplaceholder.typicode.com/photos"              # URL that contains JSON code for the photos
total_photos = get_photos_from_url(photos_url)                          # Using that url photos is set to the return value of get_photos_from_url
total_number_of_albums = get_total_amount_of_albums(total_photos)       # Gets the total number of albums

print("Chase's Photo Album Viewer")
print("Enter the album number to view the contents")
print("Currently there are " + total_number_of_albums + " albums")
print("Example Input: 1  This would display the contents of album 1")
print("")

inUse = True    # Conditional variable for the while loop that turns to false if the user enters a 0

while inUse:

    try:
        user_selection = input("Enter your selection here (To exit enter 0): ")  # Gets the users input for the album number

        user_photos = get_photos_from_url("https://jsonplaceholder.typicode.com/photos?albumId=" + str(user_selection))

        # Checks to ensure that user selection is within the range of albums available to view
        if 0 < int(user_selection) <= int(total_number_of_albums):
            print("Photo Album " + str(user_selection))
            print('-----------------------------------------------------------------------------------------')
            display_photos_for_user(user_photos)

        # Checks if user would like to exit the program
        elif user_selection == 0:
            print("Thank you for using Chase's Photo Album Viewer!")
            inUse = False

        # Checks to ensure user input is valid, if not a message is displayed and the user is asked to try again
        else:
            print("Input: " + str(user_selection) + " was either below or exceeded the total amount of albums")
            print("Please ensure you enter a album number between 1 and " + total_number_of_albums)
            print("")

    except (SyntaxError, NameError):
        print("It appears as though a number was not entered, please try again.")
