class Archive:
    def __init__(self, name, year, location, image_url, video_url):
        self.name = name
        self.year = year
        self.location = location
        self.image_url = image_url
        self.video_url = video_url


archive1 = Archive("Classical Dance Showcase", 2022, "Chennai",
                   "https://www.example.com/classical-dance.jpg", "https://www.example.com/classical-dance.mp4")
archive2 = Archive("Contemporary Art Exhibit", 2021, "Mumbai",
                   "https://www.example.com/contemporary-art.jpg", "https://www.example.com/contemporary-art.mp4")

print(f"{archive1.name} ({archive1.year}, {archive1.location})")
print(f"Image: {archive1.image_url}")
print(f"Video: {archive1.video_url}")

# Test Case 1: Creating an instance of Archive class
archive1 = Archive("Classical Dance Showcase", 2022, "Chennai",
                   "https://www.example.com/classical-dance.jpg", "https://www.example.com/classical-dance.mp4")

# Test Case 2: Retrieving the name of the archive
assert archive1.name == "Classical Dance Showcase"

# Test Case 3: Retrieving the year of the archive
assert archive1.year == 2022

# Test Case 4: Retrieving the location of the archive
assert archive1.location == "Chennai"

# Test Case 5: Retrieving the image URL of the archive
assert archive1.image_url == "https://www.example.com/classical-dance.jpg"

# Test Case 6: Retrieving the video URL of the archive
assert archive1.video_url == "https://www.example.com/classical-dance.mp4"


# Test Case 1: Creating an instance of Archive class
archive2 = Archive("Contemporary Art Exhibit", 2021, "Mumbai",
                   "https://www.example.com/contemporary-art.jpg", "https://www.example.com/contemporary-art.mp4")

# Test Case 2: Retrieving the name of the archive
assert archive2.name == "Contemporary Art Exhibit"

# Test Case 3: Retrieving the year of the archive
assert archive2.year == 2021

# Test Case 4: Retrieving the location of the archive
# assertion error expected location is Mumbai
assert archive2.location == "Delhi"

# Test Case 5: Retrieving the image URL of the archive
assert archive2.image_url == "https://www.example.com/contemporary-art.jpg"

# Test Case 6: Retrieving the video URL of the archive
assert archive2.video_url == "https://www.example.com/contemporary-art.mp4"
