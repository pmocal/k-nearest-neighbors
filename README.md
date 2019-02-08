For multiple groups of __n__ points with a certain class __c__ I assigned the class whose points were closest on average
to my point __p__.

After cloning the directory run the following command to install required libraries: `pip install -r requirements.txt`

Run either `knnvalidation.py`, which prints out the errorcount, or `knntest.py` to label images in `/digitsDataset`.
Expect the programs to take a few minutes to complete. Data is read from `/digitsDataset` and results are also written
to that directory. [README](digitsDataset/README.txt) details the nature of the datasets.
