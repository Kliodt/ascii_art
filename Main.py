from PIL import Image

ascii_array = [" ", "░", "▒", "▓", "█"]  # from darkest to brightest
ratio_for_autoresize = 0.35


def get_symbol(opacity):  # 0...255 for grayscale
    return ascii_array[round((len(ascii_array) - 1) * opacity / 255)]


def write_to_file(data, filename):
    if filename == "":
        for line in data:
            print(line)
    else:
        with open(filename, "w+", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print("Готово")


# ------------ set parameters ----------
inp_file_name = input("Введите имя файла: ")
im = Image.open(inp_file_name)
print("Ширина = " + str(im.width) + "px; высота = " + str(im.height) + "px")
width_height = (input("Ширина и высота выходного файла в символах (или только ширина для автоподбора высоты): ").replace(",", "").split(" "))
output_width = int(width_height[0])
if len(width_height) == 2:
    output_height = int(width_height[1])
else:
    output_height = int(int(width_height[0]) * ratio_for_autoresize * im.height / im.width)
output_file_name = input("Имя выходного файла (\"\", для печати в консоль): ")


# ------------- program -------------
gray = im.convert("L")  # to grayscale

gray = gray.transform((output_width, output_height), Image.Transform.EXTENT, (0, 0, im.width, im.height))

pix = gray.load()
pixels = [[pix[i, j] for i in range(0, output_width)] for j in range(0, output_height)]

lines = ["".join([get_symbol(i) for i in j]) for j in pixels]

write_to_file(lines, output_file_name)

