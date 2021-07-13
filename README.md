# SummerReadinProject

## File Structure


```bash
│   README.md
│   requirements.txt
│
├───Choosing coeff at random
│       RandomNonSquareNumbers.py  #Chooses square free numbers randomly for coefficients
│       RandomSquareRoots.py    #Chooses square roots randomly for coefficients
│
├───Hamming Distance problems
│       Hamming dist 1, same sign.py  #Finds numer of same sign node at hamming distance 1 for each node
│       Hamming dist 1, same sign.txt
│       Hamming walk till sign change.py #Finds min no of nodes to traverse for sign change 
│       Hamming walk till sign change.txt
│       Less accurate hamming walk till sign change.py #Finds min no of nodes to traverse for sign change(Works for large n , but may give a few incorrect outputs)
│       Less accurate hamming walk till sign change.txt
│       Traced accurate hamming walk till sign change.py #Finds path for min no of nodes to traverse for sign change 
│       Traced accurate hamming walk till sign change.txt
│       Traced hamming walk till sign change .py #Finds path for min no of nodes to traverse for sign change(Works for large n , but may give a few incorrect outputs)
│       Traced hamming walk till sign change .txt
│
├───Matrix Maker with minimum coefficients
│   ├───Coeff -1,0,1
│   │       Make_matrix_with_min_coeff.py #Not for executing, just has the making matrix functions here
│   │       Matrix checker for True False.py  #Run this to check for the correctness for different values of n , when weight are from the set {-1,0,1}
│   │       Matrix checker for True False.txt
│   │
│   └───Coeff -1,1
│           Matrix Checker No Zero Precision.py #Checking for correctness with varying precision with the set of weights as {-1,1}
│           Matrix Checker No Zero Precision.txt
│           Matrix Checker No Zero.py #Checking for correctness with the set of weights as {-1,1}
│           Matrix Checker No Zero.txt
│
├───N Least values
│       First N least Values Brute Force.py #Finds the n minimum values via brute force in O(3**n)
│       First N least Values Brute Force.txt
│       Least N values finder SymPy.py #Finds the n minimum values in O(n 2**n) and uses SymPy for accurate evaluation
│       Least N values finder SymPy.txt
│       Least N values finder.py #Finds the n minimum values in O(n 2**n)
│       Least N values finder.txt
│
└───Precision algorithms
        Least N values with minimum precision.py #Returns the precision required for n unique values
        Least N values with minimum precision.txt
        PrecisionFinderForAllValues.py #Returns the precision required for all 3**n-1 unique values
```

## Installation

```
git clone https://github.com/DivyanshMittal-exe/SummerReadinProject
cd SummerReadinProject
pip install -r requirements.txt
```