import optparse
import numpy as np
import imutils
import cv2


parser = optparse.OptionParser("usage %prog -i [image] -l [logo]")
parser.add_option("-i", dest="image", type="string", help="specify image")
parser.add_option("-l", dest="logo", type="string", help="specify logo")
(options, args) = parser.parse_args()

if options.image  and options.logo:
	img = options.image
	lgo = options.logo
	image = cv2.imread(img)
	logo = cv2.imread(lgo)
	(logoHeight, logoWidth) = logo.shape[:2]

	result = cv2.matchTemplate(image, logo, cv2.TM_CCOEFF)
	(_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)

	topLeft = maxLoc
	botRight = (topLeft[0] + logoWidth, topLeft[1] + logoHeight)

	image[topLeft[1]-5:botRight[1] + 10 , topLeft[0]-10:botRight[0]+10] = image[topLeft[1]-5, topLeft[0]-5, 2]

	cv2.imshow("Puzzle", imutils.resize(image, height = 650))

	cv2.waitKey(0)
	#cv2.imwrite('messigray.png',imutils.resize(image, height = 650))
else:
	print("usage %prog -i [image] -l [logo]")
