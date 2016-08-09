get_ipython().magic('matplotlib inline')
from pylab import *
import numpy as np, pandas as pd, seaborn as sns
import itertools
from IPython.display import Markdown, display
import json, ee; ee.Initialize()

def load_dataset(name):
    return pd.read_csv('https://rawgit.com/suredream/datasets/master/%s.csv' % name)    
def display_error_matrix(truth, pred, index=['A', 'C','Total', 'Producer Accuracy'], columns=['A', 'B', 'Total', 'User Accuracy']):
    """Display error matrix, accuracy and kappa
df = pd.read_csv('https://rawgit.com/suredream/datasets/master/val_ce.csv') 
display_error_matrix(df['truth'], df['map'])
    """
    from sklearn.metrics import confusion_matrix, cohen_kappa_score

    C = confusion_matrix(truth, pred)
    kappa = (cohen_kappa_score(df['truth'], df['map']) * 1000).astype(int)
    correct = [C[i,i] for i in range(C.shape[0])]
    colsum = np.sum(C, axis=1)
    C = np.c_[C, colsum, (correct / colsum * 1000).astype(int)] # UA
    rowsum = np.sum(C, axis=0)
    pa = (correct / rowsum[:-2] * 1000).astype(int)
    rowsum[-1] = 0
    C = np.vstack([C, rowsum])
    oa = (np.sum(correct)/np.sum(colsum) * 1000).astype(int)
    C = np.vstack([C, np.append(pa,[kappa, oa])])
    ddf = pd.DataFrame(data=C, index=index, columns=columns)

    fmt = ['---' for i in range(len(ddf.columns))]
    df_fmt = pd.DataFrame([fmt], columns=ddf.columns)
    df_formatted = pd.concat([df_fmt, ddf])
    print(df_formatted.to_csv(sep="|", index=True))
    display(Markdown(df_formatted.to_csv(sep="|", index=False)))

from time import localtime, strftime
def h5store(filename, df, desc):
    var = desc.split(':')[0]
    store = pd.HDFStore(filename)
    store.put(var, df)
    store.get_storer(var).attrs.metadata = desc
    store.get_storer(var).attrs.ctime = strftime("%Y-%m-%d %H:%M:%S", localtime())
    store.close()

def h5load(store, var='default'):
    data = store[var]
    metadata = store.get_storer(var).attrs.metadata
    ctime = store.get_storer(var).attrs.ctime
    return data, metadata, ctime

def h5list(filename):
    print(filename)
    with pd.HDFStore(filename) as store:
        print(store)
        for k in sorted(store.keys()):
            df, metadata, ctime = h5load(store, k)
            print(metadata, "\n\tCreated", ctime, "Dimension", df.shape, df.keys())
        
def h5csv(store, var='default'):
    df, metadata, ctime = h5load(store, var)
    csvfile = var + '.csv'
    df.to_csv(csvfile)
    print('%s ---> %s, created.' % (var, csvfile))

def h5import(filename, csvfile, desc):
    df = pd.read_csv(csvfile)
    h5store(filename, df, desc)
    

def load_ft(name):
# - grids = ee.FeatureCollection('ft:12RIMwSvyuOJByGe1G_ylgvagH5WzFbxHIXGqCZyB')  // ce_grid1x1
# - continent = ee.FeatureCollection('ft:1fM786Wbri6CqIz3JvyQ_vvMIBGbdUmTOGacZTnb-') // africa continent
# - aezs8 = ee.FeatureCollection('ft:19hZjN8dbwPbDHNdLVaoGLEtmIbxAtrn4yDr9QVgt') // africa AEZs
# - countries = ee.FeatureCollection('ft:1fGODObRcgWotUauiKV_2GlM7ZXX0sdZ5FLTJeALZ') // africa Countries
# - training = ee.FeatureCollection('ft:1C_gFvQmd3AGtB0Q0XgnKk5ESUARSH79FB9Un8sF2') // GFSAD traing dataset
# - reference = ee.FeatureCollection('ft:1KK298zIL_T5yHXNaKnqQ4nfK03aKJBiiQeP__EqU') // Bo's validatioin data
    dic = {'grid':'ft:12RIMwSvyuOJByGe1G_ylgvagH5WzFbxHIXGqCZyB', 'afr':'ft:1fM786Wbri6CqIz3JvyQ_vvMIBGbdUmTOGacZTnb-','az':'ft:19hZjN8dbwPbDHNdLVaoGLEtmIbxAtrn4yDr9QVgt',
 'country':'ft:1fGODObRcgWotUauiKV_2GlM7ZXX0sdZ5FLTJeALZ','tr':'ft:1C_gFvQmd3AGtB0Q0XgnKk5ESUARSH79FB9Un8sF2','val':'ft:1KK298zIL_T5yHXNaKnqQ4nfK03aKJBiiQeP__EqU', 'modists':'ft:1DJ8J1R_Y7-UzjI7REMv2GWNeOWBSI0bmhEobgJlU'}
    return ee.FeatureCollection(dic[name])