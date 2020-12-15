import IPython.display as ipd # load a local WAV file and PLAY!!!
from scipy.signal import butter , filtfilt
%matplotlib inline
%pylab inline
import os
import pandas as pd
import librosa
import librosa.display
import glob 
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow as tf
import keras


from sklearn.model_selection import train_test_split
from sklearn import preprocessing

import os, fnmatch

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, LSTM
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping,ReduceLROnPlateau,ModelCheckpoint,TensorBoard,ProgbarLogger
from keras.utils import np_utils
from sklearn import metrics 
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import itertools
from keras.layers import TimeDistributed, SpatialDropout1D, Bidirectional

from livelossplot import PlotLossesKeras # To plot the NN realtime!

from tqdm import tqdm