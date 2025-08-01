""" Project: ASCII Art Generator """

from PIL import Image

def load_image(image_path, new_width = 100):
    # open image
    img = Image.open(image_path)

    # calculate aspect ratio
    aspect_ratio = img.height / img.width

    new_height = int(new_width * aspect_ratio * 0.55)
    img = img.resize((new_width, new_height))
    return img

def convert_to_grayscale(img):
    return img.convert("L")

def map_pixels_to_ascii(img):
    ascii_chars = "@%#*+=-:. "
    pixels = img.getdata()
    ascii_str = "".join([ascii_chars[pixel // 25] for pixel in pixels])
    return ascii_str

def generate_ascii_art(image_path, new_width = 100):
    # load and resize image
    img = load_image(image_path, new_width)

    # convert to grayscale
    gray_image = convert_to_grayscale(img)

    # map pixels to ascii
    ascii_str = map_pixels_to_ascii(gray_image)

    # format ASCII string into rows
    ascii_art = "\n".join([ascii_str[i:i + new_width] for i in range(0, len(ascii_str), new_width)])
    return ascii_art

def save_ascii_arrt(ascii_art, output_path):
    with open(output_path, "w") as file:
        file.write(ascii_art)


output_path = r"part-08/i_pinimg_com_originals_39_19_33_3919330c71a2a725885a81503dc4cb0e_jpg.png"
ascii_art = generate_ascii_art(output_path, 100)
save_ascii_arrt(ascii_art, r"part-08/final.txt")