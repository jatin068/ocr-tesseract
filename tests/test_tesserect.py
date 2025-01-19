from tesserect import read_image_from_file, read_text_from_image


def test_image_read():
    image_path = './data/characters/test.jpg'
    image = read_image_from_file(image_path)

    assert image.size == (640, 480)


def test_read_text_from_image():
    # Arrange
    expected_text = """This is a lot of 12 point text"""
    image_path = './data/characters/test.jpg'
    image = read_image_from_file(image_path)

    # Act
    text = read_text_from_image(image)

    # Assert
    assert text[:30] == expected_text
