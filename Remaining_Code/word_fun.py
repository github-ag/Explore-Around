from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
text = 'Tourism Weather Location Fun Trip Hotels Food Enjoy Maps,Travel,Shopping,Party,Monuments,Study,drive,hike,flight,outing,pilgrimage,dream,summer.experience,holiday,relax,imagination'
our_mask = np.array(Image.open('upvote.png'))
cloud = WordCloud(background_color='yellow',mask=our_mask).generate(text)
plt.imshow(cloud)
plt.show()
