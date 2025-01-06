import imageio as iio

filenames =  ['push1.jpg','push2.jpg']
images = []

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)
