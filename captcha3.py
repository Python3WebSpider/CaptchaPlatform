from chaojiying import Chaojiying

# USERNAME = 'Germey'
# PASSWORD = ''
# SOFT_ID = '915502'
# CAPTCHA_KIND = '9101'
# FILE_NAME = 'captcha3.png'
# client = Chaojiying(USERNAME, PASSWORD, SOFT_ID)
# result = client.post_pic(open(FILE_NAME, 'rb').read(), CAPTCHA_KIND)
# print(result)

import cv2

image = cv2.imread('captcha3.png')
image = cv2.circle(image, (231, 85), radius=10, color=(0, 0, 255), thickness=-1)
cv2.imwrite('captcha3_label.png', image)
