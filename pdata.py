get_ipython().magic('matplotlib inline')
from IPython.display import HTML, Markdown, display
from pylab import *
import numpy as np, pandas as pd, seaborn as sns
import json, itertools, ee; ee.Initialize()

fc_download = lambda fc: display(HTML('<a href="%s" target="_blank">download</a>' % fc.select([".*"], None, False).getDownloadURL('csv')))

def load_ft(name):
    dic = {
    'grid':'ft:12RIMwSvyuOJByGe1G_ylgvagH5WzFbxHIXGqCZyB',   #ce_grid1x1
    'afr':'ft:1fM786Wbri6CqIz3JvyQ_vvMIBGbdUmTOGacZTnb-',       # africa continent
    'az':'ft:19hZjN8dbwPbDHNdLVaoGLEtmIbxAtrn4yDr9QVgt',        # africa AEZs
    'country':'ft:1fGODObRcgWotUauiKV_2GlM7ZXX0sdZ5FLTJeALZ',   # africa Countries
    'tr':'ft:1C_gFvQmd3AGtB0Q0XgnKk5ESUARSH79FB9Un8sF2',    # GFSAD traing dataset
    'val':'ft:1KK298zIL_T5yHXNaKnqQ4nfK03aKJBiiQeP__EqU',  # Bo's validatioin data
    'modists':'ft:1DJ8J1R_Y7-UzjI7REMv2GWNeOWBSI0bmhEobgJlU',
    'india_modists':'ft:1CAklqz-XV7_0ehxDCqBgurkZy-pocoGuUs1RsKb2',
 }
    return ee.FeatureCollection(dic[name])

def dataset(name):
    try:
        df = pd.read_csv('https://rawgit.com/suredream/datasets/master/%s.csv.gz'  % name, compression='gzip')
    except:
        df = pd.read_csv('https://rawgit.com/suredream/datasets/master/%s.csv' % name)
    try:    
        desc = df['desc'][0]        
        df = df.drop('desc', 1)
    except:
        desc = ''
    return df, desc

def features(name, end=-1):
    df, desc = dataset(name)
    if end != -1:
        df = df[:end]
    features = [ee.Feature(ee.Geometry.Point([r['longitude'], r['latitude']]), {"system:index": "%d" % r['idx'], "class": r['class'], 'lon':r['longitude'], 'lat':r['latitude']}) for idx, r in df.iterrows()]    
    return ee.FeatureCollection(features)

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

def renamebands(img):
    img = ee.Image(img)
    names = img.bandNames()
    prefix = ee.String(img.get("system:index")).cat("_")
    catname = lambda b: prefix.cat(b)
    new_names = names.map(catname)
    return img.select(names, new_names)

# from time import localtime, strftime
# def h5store(filename, df, desc):
#     var = desc.split(':')[0]
#     store = pd.HDFStore(filename)
#     store.put(var, df)
#     store.get_storer(var).attrs.metadata = desc
#     store.get_storer(var).attrs.ctime = strftime("%Y-%m-%d %H:%M:%S", localtime())
#     store.close()

# def h5load(store, var='default'):
#     data = store[var]
#     metadata = store.get_storer(var).attrs.metadata
#     ctime = store.get_storer(var).attrs.ctime
#     return data, metadata, ctime

# def h5list(filename):
#     print(filename)
#     with pd.HDFStore(filename) as store:
#         print(store)
#         for k in sorted(store.keys()):
#             df, metadata, ctime = h5load(store, k)
#             print(metadata, "\n\tCreated", ctime, "Dimension", df.shape, df.keys())
        
# def h5csv(store, var='default'):
#     df, metadata, ctime = h5load(store, var)
#     csvfile = var + '.csv'
#     df.to_csv(csvfile)
#     print('%s ---> %s, created.' % (var, csvfile))

# def h5import(filename, csvfile, desc):
#     df = pd.read_csv(csvfile)
#     h5store(filename, df, desc)
    

