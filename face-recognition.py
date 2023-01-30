import os
import cv2
import numpy as np
from math import sqrt
#############################
# Yohanna Astrid Adhipurusa #
#############################
def euclid(ori, test):
  ori = cv2.resize(ori, test.shape[:2], interpolation = cv2.INTER_NEAREST)
  return sqrt(np.sum((ori-test)^2)) / ori.size

def mostSimilar(compare):
  min = 100
  index = ''
  for c in compare:
    if compare[c] < min :
      min = compare[c]
      index = c
  return index,min

testDir = { 'inDb': 'DATA\\test\\indatabase\\', 'noInDb': 'DATA\\test\\notindatabase\\'}

for tDir in testDir:
  if tDir == 'inDb':
    print('===== IN DATABASE TEST ==========================================================')
  else:
    print('===== NOT IN DATABASE TEST =====================================================')
  for filename in os.listdir(testDir[tDir]):
    img = cv2.imread(f'{testDir[tDir]}{filename}')
    cv2.imshow('image to be compared',cv2.resize(img,(500,500), interpolation = cv2.INTER_NEAREST))
    allComparison = {}
    for dbFile in os.listdir('DATA\\train\\'):
      ori = cv2.imread(f'DATA\\train\\{dbFile}')
      allComparison[dbFile] = euclid(ori,img)
    bestBet, value = mostSimilar(allComparison)
    best = cv2.imread(f'DATA\\train\\{bestBet}')
    cv2.imshow('most similar image',cv2.resize(best,(500,500), interpolation = cv2.INTER_NEAREST))
    print(f'BEST BET ||{bestBet} : {value} difference')
    print(f'THIS FILE||{filename}') 
    print()

    cv2.waitKey(0)