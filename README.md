# k-nearest-neighbors

## Background

For multiple groups of __n__ points with a certain class __c__, I assigned the class whose points were closest on average to my point __p__.

Read [here](digitsDataset/datasetInfo.txt) about the dataset.

## Prerequisites

To run the code first you must have Python installed on your computer. If you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org or if you are working in a Virtual Environment created by virtualenv or pyvenv then Pip is also installed.

After cloning this git directory, 
```
$ pip install numpy
```
if you're using Python 2 or 
```
$ pip3 install numpy
```
if you're using Python 3.

## Running the code

`knnvalidation.py` prints out the errorcount and `knntest.py` labels the images in `/digitsDataset`.

Expect the programs to take a few minutes to complete.

Data is read from `/digitsDataset` and results are written to that directory.
