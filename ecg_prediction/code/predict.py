from utils import utils
from models.fastai_model import fastai_model
import pickle

sampling_frequency=100
datafolder='C:/Users/funck/Projects/lauzhack_2023/test_2/ecg_ptbxl_benchmarking/data/ptbxl/'
task='all'
outputfolder='C:/Users/funck/Projects/lauzhack_2023/test_2/ecg_ptbxl_benchmarking/output/'

data, raw_labels = utils.load_dataset(datafolder, sampling_frequency)
# Load PTB-XL data
#data, raw_labels = utils.load_dataset(datafolder, sampling_frequency)
# Preprocess label data
labels = utils.compute_label_aggregations(raw_labels, datafolder, task)
# Select relevant data and convert to one-hot
#data, labels, Y, _ = utils.select_data(data, labels, task, min_samples=0, outputfolder=outputfolder)

num_classes = 71         # <=== number of classes in the finetuning dataset
input_shape = [1000,12] # <=== shape of samples, [None, 12] in case of different lengths

experiment = 'exp0'
modelname = 'fastai_xresnet1d101'
pretrainedfolder = outputfolder+experiment+'/models/'+modelname+'/'
mpath=outputfolder+experiment+'/models/'+modelname+'/' # <=== path where the finetuned model will be stored
n_classes_pretrained = 71 # <=== because we load the model from exp0, this should be fixed because this depends the experiment

model = fastai_model(
    modelname, 
    num_classes, 
    sampling_frequency, 
    mpath, 
    input_shape=input_shape, 
    pretrainedfolder=pretrainedfolder,
    n_classes_pretrained=n_classes_pretrained, 
    pretrained=True,
    epochs_finetuning=2,
)

standard_scaler = pickle.load(open(outputfolder+experiment+'/data/standard_scaler.pkl', "rb"))

X_val = data[labels.strat_fold == 11]
X_val = utils.apply_standardizer(X_val, standard_scaler)

y_val_pred = model.predict(X_val)


print(round(y_val_pred[0][43], 1) * 100)