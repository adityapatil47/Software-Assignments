class Artist:
    def __init__(self, name, bio, portfolio_url, contact_info):
        self.name = name
        self.bio = bio
        self.portfolio_url = portfolio_url
        self.contact_info = contact_info


artist1 = Artist("Priya Patel", "I am a digital artist specializing in 3D animation and character design.",
                 "https://www.priyapatel.com/", "contact@priyapatel.com")

print(f"{artist1.name}: {artist1.bio}")
print(f"Portfolio: {artist1.portfolio_url}")
print(f"Contact: {artist1.contact_info}")


def test_artist_attributes():
    artist = Artist("Priya Patel", "I am a digital artist specializing in 3D animation and character design.",
                    "https://www.priyapatel.com/", "contact@priyapatel.com")
    assert artist.name == "Priya Patel"
    assert artist.bio == "I am a digital artist specializing in 3D animation and character design."
    assert artist.portfolio_url == "https://www.priyapatel.com/"
    assert artist.contact_info == "contact@priyapatel.com"


def test_artist_display_info():
    artist = Artist("Priya Patel", "I am a digital artist specializing in 3D animation and character design.",
                    "https://www.priyapatel.com/", "contact@priyapatel.com")
    assert f"{artist.name}: {artist.bio}" in captured_output()
    assert f"Portfolio: {artist.portfolio_url}" in captured_output()
    assert f"Contact: {artist.contact_info}" in captured_output()


def captured_output():
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        return_value = f.getvalue()
    return return_value
