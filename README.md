<h1>Simple Euclidean Face Comparator</h1>
This was the final project of my image processing class. Completed by me, Yohanna Astrid Adhipurusa.
<ol>
<li> <h3>Task</h3>

<ol>
<li> Topic：Face Similarity Matching
<li> Description：Link goole drive, download related files from DATA subdirectory https://bit.ly/3ohCAWs

- Step 1: Select a celebrity in the database and test if the celebrity can be found in the database.
- Step 2: Find a person who is not in the database and search for the celebrity with the highest similarity in the database.

<li> Program development tool：No limitation。(Opencv、Python、C++、C)
<li> Content submission and Deadline

- Upload：Compress into a file(file name: ID no. + name)，Upload Dong Hwa e-Learning。 Please upload a word file, content is as follows: List and explain the program code, and show test and result images.
- Deadline：2022/01/17 (一) 23:55 （Delay within one week: 50% OFF，Delay after one week: 100% OFF，Copier: Deduction）
</ol>
<li> <h3>Code</h3>

- Explanation
  - Libraries Used
```
importos
import cv2
import numpy asnp
from math import sqrt
```
These are the libraries used for the code. Cv2 is for opencv operations which are imread and imshow to read and show the image. Numpy is to manipulate the read images' array using functions such as sum. Math is to use some math operations, in this code, only the square root function is used.

  - Global Variables
```
testDir = { 'inDb': 'DATA\\test\\indatabase\\', 'noInDb':'DATA\\test\\notindatabase\\'}
```
There is only one variable that can be considered global which is testDir which is a dictionary that stores the directory of the images that are to be tested, which are the directory of the test images that are in the database and the test images that aren't in the database.

  - Main For Loop
```
for tDirintestDir:
  iftDir == 'inDb':
    print('===== IN DATABASE TEST ==========================================================')
  else:
    print('===== NOT IN DATABASE TEST =====================================================')
```
The code iterates through the testDir dictionary to get the directory that is currently being tested. Before it starts reading and processing the image files, it first prints a header in the terminal based on the current directory to make it easier to read.
```
  for filenameinos.listdir(testDir[tDir]):
    img = cv2.imread(f'{testDir[tDir]}{filename}')
    cv2.imshow('image to be compared',cv2.resize(img,(500,500),interpolation = cv2.INTER\_NEAREST))
```
Then, for each directory, we loop for each file that is to be tested. The file is first read by opencv's function imread which reads the file as a 3 dimensional numpy array. Then we show the image for display and name the window as the image that will be compared. We also resize the image just so that it would be easier for us to see the result.
```
    allComparison = {}
    for dbFileinos.listdir('DATA\\train\\'):
      ori = cv2.imread(f'DATA\\train\\{dbFile}')
      allComparison[dbFile] = euclid(ori,img)
```
While checking each file, we create a dictionary to store all the comparison results of the image to be compared and the images in the database. Then, we loop the images in the database and read them each as the variable ori using opencv's imread function. Then, we take the name of the database file as it's key and insert it's Euclidean distance from the tested image by the function Euclid (which will be explained later) as it's value to be inserted to the allComparison dictionary.
```
    bestBet, value = mostSimilar(allComparison)
    best = cv2.imread(f'DATA\\train\\{bestBet}')
    cv2.imshow('most similar image',cv2.resize(best,(500,500),interpolation = cv2.INTER\_NEAREST))

    print(f'BEST BET ||{bestBet} : {value} difference')
    print(f'THIS FILE||{filename}')
    print()
    cv2.waitKey(0)
```
After calculating all the Euclidean distances of the database images and the test image, we find the one with least difference using the mostSimilar function (which will be explained later). This function will return an index of which database image is most likely to represent the test image and the value of their difference. We then read that image again to display a resized version of it (to help us see better). Then we print the guess that our algorithm made and it's difference value. We also print the actual name of the file that's being tested.

  - Custom Functions

In this code there are two custom functions which are euclid and mostSimilar
```
defeuclid(ori, test):
  ori = cv2.resize(ori, test.shape[:2], interpolation = cv2.INTER\_NEAREST)
  return sqrt(np.sum((ori-test)^2)) / ori.size
```
The Euclid function calculates the Euclidean distance between the test image and the image in the database. It does this by first resizing the database image by the test image. This is so that matrix calculations can be done between the two numpy arrays. We then calculate the sum of the squared difference of database image's matrix and test image's matrix and divide them by the size of the database image, which has the same size as the test image.
```
defmostSimilar(compare):
  min = 100
  index = ''
  for c in compare:
    ifcompare[c] \< min :
      min = compare[c]
      index = c
  return index,min
```
The mostSimilar function takes in a dictionary. It searches for the smallest value within the input dictionary and returns the index and value of the smallest value. The initial minimum value is set to 100 because the distance range wouldn't exceed 1, so we took a number which is higher than 1.
</ol>
