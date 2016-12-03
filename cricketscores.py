'''
Performance Analysis in a test cricket match
SCORES - [First Innings Bat, Second Inings Bat, First Innings wickets,
Second Innings Wickets ]


'''
import sys
from sklearn import tree

SAMPLE_SCORES=[[100,50,3,2],[20,0,0,-1],[-1,-1,5,3],[122,3,4,-1],[0,0,1,1],[50,32,1,1],
[20,20,0,1],[60,62,-1,-1],[-1,-1,-1,-1],[0,0,0,0],[1,1,1,1],[100,100,-1,-1],
[50,50,0,0],[45,39,0,0],[0,0,2,3]]

SAMPLE_ANALYSIS= ['good','bad','good','good','bad','good','bad','good','N/A','bad','bad',
'good','good','good','good']

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(SAMPLE_SCORES,SAMPLE_ANALYSIS)

prediction = classifier.predict([[sys.argv[1],sys.argv[2],sys.argv[3],
sys.argv[4]]])

print(prediction)
