import um

def test_count_normal():
    assert um.count("Um") == 1
    assert um.count("um?") == 1
    assert um.count("Um, thanks, um...") == 2

def test_count_substr():
    assert um.count("Um, thanks for the album.") == 1