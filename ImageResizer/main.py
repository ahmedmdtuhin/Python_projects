import cv2

#Configurable parameters
source= "images.jpg"
destination="new_image.jpg"
scale_percent = 50


img = cv2.imread(source, cv2.IMREAD_UNCHANGED)

#cv2.imshow("Title",img)
#cv2.waitKey(0)

#percent by which the image is resized

#calculate the 50 percent of original dimensions
new_width = int(img.shape[1] * scale_percent / 100)
new_height = int(img.shape[0] * scale_percent / 100)

# dsize
dsize = (new_width, new_height)

# resize image
output = cv2.resize(img, dsize)

cv2.imwrite(destination,output)
cv2.waitKey(0)