import pandas as pd
import matplotlib.pyplot as plt, matplotlib.image as mpimg
from sklearn.model_selection import train_test_split
from sklearn import svm
##%matplotlib inline
labeled_images = pd.read_csv(r"C:\Users\RAHUL\Desktop\Digit Recognizer/train.csv")
images = labeled_images.iloc[0:5000,1:]
labels = labeled_images.iloc[0:5000,:1]
train_images, test_images,train_labels, test_labels = train_test_split(images, labels, train_size=0.8, random_state=0)

test_images[test_images>0]=1
train_images[train_images>0]=1
i=1
img=train_images.iloc[i].as_matrix()
img=img.reshape((28,28))

plt.imshow(img,cmap='binary')
plt.show()
plt.title(train_labels.iloc[i,0])

plt.hist(train_images.iloc[i])

clf = svm.SVC()
clf.fit(train_images, train_labels.values.ravel())
s=clf.score(test_images,test_labels)
print(s)