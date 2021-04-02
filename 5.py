img_path = glob.glob("C:\Users\zczss\Desktop\ppt/*.jpg")
path_save = "C:\Users\zczss\Desktop\ppt/new"
for file in img_path:
  name = os.path.join(path_save, file)
  im = Image.open(file)
  im.thumbnail((1920,1280))
  print(im.format, im.size, im.mode)
  im.save(name,'JPEG')
