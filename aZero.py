#Student Name: <Your Name>
#Student ID: <Your ID>

import pandas as pd
import numpy as np
import scipy
import A0_Utils as A0

## Question 1 - Basics

def add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    elif isinstance(a, list) and isinstance(b, list):
        return a + b
    elif isinstance(a, (int, float, str, list)) and isinstance(b, (int, float, str, list)):
        return str(a) + str(b)
    else:
        print("Error!")
        return None
    # A0.raiseNotDefined()

def calcMyGrade(AssignmentScores, MidtermScores, PracticumScores, ICAScores, Weights):

    assignment_avg = sum(AssignmentScores) / len(AssignmentScores) if AssignmentScores else 0
    midterm_avg = sum(MidtermScores) / len(MidtermScores) if MidtermScores else 0
    practicum_avg = sum(PracticumScores) / len(PracticumScores) if PracticumScores else 0
    in_class_avg = sum(ICAScores) / len(ICAScores) if ICAScores else 0

    assignment_weight, midterm_weight, practicum_weight, in_class_weight = Weights

    if sum(Weights) != 1:
        raise ValueError("Weights must sum up to 1")

    weighted_score = (
        (assignment_avg * assignment_weight) +
        (midterm_avg * midterm_weight) +
        (practicum_avg * practicum_weight) +
        (in_class_avg * in_class_weight)
    )

    return round(weighted_score, 2)
    
    # A0.raiseNotDefined()


## Question 2 - Classes

class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.leftchild = None
        self.rightchild = None

    def getChildren(self):
        return [self.leftchild, self.rightchild]
    def getKey(self):
        return self.key
    def getValue(self):
        return self.value
    def assignLeftChild(self, child):
        self.leftchild = child

    def assignRightChild(self, child):
        self.rightchild = child
    def inOrderTraversal(self):
        result = []
        if self.leftchild is not None:
            result += self.leftchild.inOrderTraversal()
        result.append(self.value)
        if self.rightchild is not None:
            result += self.rightchild.inOrderTraversal()
        return result
        
        # A0.raiseNotDefined()

class queue:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        else:
            print("Error: Cannot pop from an empty queue!")
            return None

    def check_size(self):
        return len(self.items)
        
        # A0.raiseNotDefined()


## Question 3 - Libraries
import numpy as np
def generateMatrix(numRows, numcolumns, minVal, maxVal):
    return np.random.randint(minVal, maxVal + 1, size=(numRows, numcolumns))
    
    # A0.raiseNotDefined()

def multiplyMat(m1, m2):
def multiplyMat(matrix1, matrix2):
    try:
        # Try performing matrix multiplication
        return np.dot(matrix1, matrix2)
    except ValueError:
        # Handle incompatible matrices
        print("Incompatible Matrices")
        return None
    # A0.raiseNotDefined()

def statsTuple(a, b):
    try:
        sum_a = np.sum(a)
        mean_a = np.mean(a)
        min_a = np.min(a)
        max_a = np.max(a)
        
        sum_b = np.sum(b)
        mean_b = np.mean(b)
        min_b = np.min(b)
        max_b = np.max(b)
        
        pearson_corr, _ = stats.pearsonr(a, b)
        spearman_corr, _ = stats.spearmanr(a, b)
        
        return (sum_a, mean_a, min_a, max_a, sum_b, mean_b, min_b, max_b, pearson_corr, spearman_corr)
    except Exception as e:
        print(f"Error: {e}")
        return None
    # A0.raiseNotDefined()

def pandas_func(filename):
    try:
        df = pd.read_csv(filename, sep='\t')
        ListOfMeans = []
        ListOfColumnNames = []
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                ListOfMeans.append(df[col].mean())
            else:
                ListOfColumnNames.append(col)
        return ListOfMeans, ListOfColumnNames
    except Exception as e:
        print(f"Error: {e}")
        return None
    # A0.raiseNotDefined()
