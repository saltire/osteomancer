import numpy
import pygame
import pygame.camera
import time
import scipy
import scipy.ndimage

from PIL import Image
from PIL import ImageEnhance
# from PIL import ImageFilter
# from PIL import ImageOps


device = '/dev/video1'
mode = 'RGB'
size = 1920, 1080

# Start camera
pygame.camera.init()
camera = pygame.camera.Camera(device, size, mode)
camera.start()

# Capture image
surface = camera.get_image()
sbytes = pygame.image.tostring(surface, 'RGB', False)

# Convert to PIL
image = Image.frombytes(mode, size, sbytes)

# Convert to numpy array
array = pygame.surfarray.array2d(surface)
array = array.swapaxes(0, 1)

# Sobel edge detection
dx = scipy.ndimage.sobel(array, axis=0)
dy = scipy.ndimage.sobel(array, axis=1)
mag = numpy.hypot(dx, dy)
mag *= 255.0 / numpy.max(mag)

# Convert to PIL
edges = scipy.misc.toimage(mag)

# Adjust mask
edges = ImageEnhance.Brightness(edges).enhance(.5)
edges = ImageEnhance.Contrast(edges).enhance(10)
# edges = edges.filter(ImageFilter.EDGE_ENHANCE_MORE)
# edges = ImageOps.autocontrast(edges, 1)

# Overlay images with mask
overlay = Image.new(mode, size, (255, 0, 255))
final = Image.composite(overlay, image, edges)

# Save images
image.save('save.png')
edges.save('edges.png')
final.save('final.png')
