To run the code first you must have Python installed on your computer. If you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org or if you are working in a Virtual Environment created by virtualenv or pyvenv then Pip is also installed.

After cloning this git directory run `pip install -r requirements.txt` (Python 2), or `pip3 install -r requirements.txt` (Python 3)

Run either `knnvalidation.py`, which prints out the errorcount, or `knntest.py` to label images in `/digitsDataset`.
Expect the programs to take a few minutes to complete. Data is read from `/digitsDataset` and results are also written
to that directory. Read [here](digitsDataset/datasetInfo.txt) about the datasets.

For multiple groups of __n__ points with a certain class __c__, I assigned the class whose points were closest on average
to my point __p__.
