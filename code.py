from rembg import remove
from PIL import Image

# Load the image using Pillow
input = Image.open('pic.jpg')
output = remove(input)
# Save the output image
output.save('removedBG.png')

''' 
Note: 
When using the 'rembg' library for background removal, ensure that the output file extension 
specified in the 'output.save()' method is set to '.png' format. Attempting to save the output 
image with other formats like JPEG ('.jpg') might result in an error. 
'''
