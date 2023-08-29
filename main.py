from os import listdir
from PIL import Image

input_dir = "./input/"
images = [Image.open(input_dir + img_path) for img_path in listdir(input_dir)]
widths, heights = zip(*(i.size for i in images))

min_height = min(heights)

resized_imgs = [images[i].resize((widths[i]*min_height//heights[i], min_height)) for i in range(len(images))]

total_width = sum([img.size[0] for img in resized_imgs])

#total_width = sum(widths)
#max_height = max(heights)

new_img = Image.new('RGB', (total_width, min_height))

x_offset = 0
for img in resized_imgs:
  new_img.paste(img, (x_offset,0))
  x_offset += img.size[0]

new_img.save('./output/out.jpg')