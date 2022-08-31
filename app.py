from PIL import Image
from os import walk


def main():
    files = next(walk("."), (None, None, []))[2]
    print(files)
    i = 1
    for f in files:
        if 'jpg' in f and f != "bg.jpg":
            image = Image.open(f)
            bg_img = Image.open("bg.jpg")
            
            fixed_height = 280
            height_percent = (fixed_height / float(image.size[1]))
            width_size = int((float(image.size[0]) * float(height_percent)))
            image = image.resize((width_size, fixed_height), Image.NEAREST)

            image1_size = image.size
            new_image = Image.new("RGB",[500,500],color=(255,255,255))
            center_pos = (round((image1_size[0] - 500) / 2)) * -1

            new_image.paste(image,(center_pos,110))
            new_image.paste(bg_img,((image1_size[0],0)))
            new_image.save(f"images/{i}.jpg","JPEG")
            i+=1

if __name__ == "__main__":
    main()