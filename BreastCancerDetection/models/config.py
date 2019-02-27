import os


# Path to original cancer images
ORIG_INPUT_DATASET = "datasets/orig"

# initialize base paths to the new direc that
# will contain our images after computing the training and testing split
BASE_PATH = "datasets/idc"

#derive the training, validation and testing directories
TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH, "testing"])

# define the amount of data that will be used for training
TRAIN_SPLIT = 0.8

#validation data is the percentage of training data
VAL_SPLIT = 0.1