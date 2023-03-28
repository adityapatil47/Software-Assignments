class VirtualReality:
    def __init__(self, name, experience_type, device_compatibility, video_url):
        self.name = name
        self.experience_type = experience_type
        self.device_compatibility = device_compatibility
        self.video_url = video_url

    def play_video(self):
        print(
            f"Experience {self.name} with {self.experience_type} on your {self.device_compatibility} device!")
        print(f"Video URL: {self.video_url}")


# Test case 1: Creating a virtual reality object with valid inputs
vr1 = VirtualReality("Art Gallery Tour", "360-degree video",
                     "Oculus Quest 2", "https://www.example.com/art-gallery-tour.mp4")
assert vr1.name == "Art Gallery Tour"
assert vr1.experience_type == "360-degree video"
assert vr1.device_compatibility == "Oculus Quest 2"
assert vr1.video_url == "https://www.example.com/art-gallery-tour.mp4"
print("test1 passed")


# Test case 2: Playing a virtual reality video
vr2 = VirtualReality("Art Gallery Tour", "360-degree video",
                     "Oculus Quest 2", "https://www.example.com/art-gallery-tour.mp4")
assert vr2.play_video() is None  # no exceptions should be raised
print("test2 passed")

# Test case 3: Playing a virtual reality video with invalid input for video URL
vr3 = VirtualReality("Performance Stage Experience",
                     "Virtual reality", "HTC Vive", "")
try:
    vr3.play_video()
except ValueError:
    pass
else:
    assert False, "Expected ValueError for empty video URL, but no exception was raised"
print("test3 passed")

# Test case 4: Creating a virtual reality object with invalid input for name
try:
    vr4 = VirtualReality("", "Virtual reality", "HTC Vive",
                         "https://www.example.com/performance-stage-experience.mp4")

except ValueError:
    pass
else:
    assert False, "Expected ValueError for empty name, but no exception was raised"
print("test4 passed")
