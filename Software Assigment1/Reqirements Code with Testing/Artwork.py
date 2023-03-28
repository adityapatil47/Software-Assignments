class Artwork:
    def __init__(self, artist, title, medium, year, image_url):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.image_url = image_url


artwork1 = Artwork("Vincent Van Gogh", "The Starry Night", "Oil on canvas", 1889,
                   "https://www.vangoghmuseum.nl/-/media/images/collection/the-starry-night.jpg")
artwork2 = Artwork("Salvador Dali", "The Persistence of Memory", "Oil on canvas", 1931,
                   "https://www.moma.org/wp/inside_out/wp-content/uploads/2013/09/Dali-persistence-of-memory.jpg")

# print(f"{artwork1.artist}: {artwork1.title}, {artwork1.medium}, {artwork1.year}")
# print(f"{artwork2.artist}: {artwork2.title}, {artwork2.medium}, {artwork2.year}")

# Test Case 1: Create an artwork and check if the properties are set correctly
artwork1 = Artwork("Vincent Van Gogh", "The Starry Night", "Oil on canvas", 1889,
                   "https://www.vangoghmuseum.nl/-/media/images/collection/the-starry-night.jpg")
assert artwork1.artist == "Vincent Van Gogh"
assert artwork1.title == "The Starry Night"
assert artwork1.medium == "Oil on canvas"
assert artwork1.year == 1889
assert artwork1.image_url == "https://www.vangoghmuseum.nl/-/media/images/collection/the-starry-night.jpg"

# Test Case 2: Create another artwork and check if the properties are set correctly
artwork2 = Artwork("Salvador Dali", "The Persistence of Memory", "Oil on canvas", 1931,
                   "https://www.moma.org/wp/inside_out/wp-content/uploads/2013/09/Dali-persistence-of-memory.jpg")
# expected name is "Salvador Dali" //assertion error
assert artwork2.artist == "Salva Dali", "Expected name is Salvador Dali"
assert artwork2.title == "The Persistence of Memory"
assert artwork2.medium == "Oil on canvas"
assert artwork2.year == 1931
assert artwork2.image_url == "https://www.moma.org/wp/inside_out/wp-content/uploads/2013/09/Dali-persistence-of-memory.jpg"
