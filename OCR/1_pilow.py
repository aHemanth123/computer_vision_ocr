from PIL import Image 

im_file = "data/1.jpg"

im = Image.open(im_file)

print(im) # metadata of img

print(im.size)

im.show()

# we can crop ---< also 

#  rotate our img 
im.rotate(180).show()



# # Create the folder if it doesn't exist  for saving a file 
# output_dir = "data"
# os.makedirs(output_dir, exist_ok=True)


# save a file 
im.save("data/1_rotate.jpg")