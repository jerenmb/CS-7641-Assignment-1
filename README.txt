CS 7641 Assignment 1
Jeren Browning
jbrowning35

The code for this assignment can be found here: https://github.com/jerenmb/CS-7641-Assignment-1

This assignment was built using code taken from https://github.com/JonathanTay/CS-7641-assignment-1. Thanks jontay!

This file describes the structure of this assignment submission. 
The assignment code is written in Python 3.5.1. Library dependencies are: 
scikit-learn 0.18.1
numpy 0.11.1
pandas 0.24.1
matplotlib 1.5.3

Other libraries used are part of the Python standard library. 

The datasets used are the Adult and Madelon datasets which can be obtained from the UCI Machine Learning Repository here: http://archive.ics.uci.edu/ml/datasets/Adult and here: http://archive.ics.uci.edu/ml/datasets/madelon
The essential files from these datasets are also included in the main folder.

The main folder contains the following files:
1. datasets.hdf -> A pre-processed/cleaned up copy of the datasets. This file is created by "parse data.py"
2. "parse data.py" -> This python script pre-processes the original UCI ML repo files into a cleaner form for the experiments
3. helpers.py -> A collection of helper functions used for this assignment
4. ANN.py -> Code for the Neural Network Experiments
5. Boosting.py -> Code for the Boosted Tree experiments
6. "Decision Tree.py" -> Code for the Decision Tree experiments
7. KNN.py -> Code for the K-nearest Neighbours experiments
8. SVM.py -> Code for the Support Vector Machine (SVM) experiments
9. plotter.py -> Code to plot the learning and validation curves in the report
10. README.txt -> This file

Each model can be run by simply running the associated file from the python command line.

There is also a subfolder called "output". This folder contains the experimental results. 
Here, I use DT/ANN/BT/KNN/SVM_Lin/SVM_RBF to refer to decision trees, artificial neural networks, boosted trees, K-nearest neighbours, linear and RBF kernel SVMs respectively. A suffix of _OF indicates a deliberately "overfitted" version of the model where regularisation is turned off.
The datasets are adult/madelon referring to the two datasets used (the UCI Adult dataset and the UCI Madelon dataset)

Descriptions of the various types of files:
1. <Algorithm>_<dataset>_reg.csv -> The validation curve tests for <algorithm> on <dataset>
2. <Algorithn>_<dataset>_LC_train.scv -> Table of # of examples vs. CV training accuracy (for 5 folds) for <algorithm> on <dataset>. For learning curves
3. <Algorithn>_<dataset>_LC_test.csv -> Table of # of examples vs. CV testing accuracy (for 5 folds) for <algorithm> on <dataset>. For learning curves
4. <Algorithm>_<dataset>_timing.csv -> Table of fraction of training set vs. training and evaluation times. If the full training set is of size T and a fraction f are used for training, then the evaluation set is of size (T-fT)= (1-f)T
5. ITER_base_<Algorithm>_<dataset>.csv -> Table of results for learning curves based on number of iterations/epochs.
6. ITERtestSET_<Algorithm>_<dataset>.csv -> Table showing training and test set accuracy as number of iterations/epochs is varied. NOT USED in report.
7. "test results.csv" -> Table showing the optimal hyper-parameters chosen, as well as the final accuracy on the held out test set.
8. "Python Test Bed.py" -> Code that was used for creating the charts with matplotlib.

There is another subfolder called "graphs". This folder contains several charts created using matplotlib, some of which are included in the report.
