import pandas as pd

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
# - grids = ee.FeatureCollection('ft:1-M2bqBc_0mEo10VmITae6hAAfd5Zs-Y_rd6YPeIJ')  // ce_grid1x1
# - continent = ee.FeatureCollection('ft:1fM786Wbri6CqIz3JvyQ_vvMIBGbdUmTOGacZTnb-') // africa continent
# - aezs8 = ee.FeatureCollection('ft:19hZjN8dbwPbDHNdLVaoGLEtmIbxAtrn4yDr9QVgt') // africa AEZs
# - countries = ee.FeatureCollection('ft:1fGODObRcgWotUauiKV_2GlM7ZXX0sdZ5FLTJeALZ') // africa Countries
# - training = ee.FeatureCollection('ft:1C_gFvQmd3AGtB0Q0XgnKk5ESUARSH79FB9Un8sF2') // GFSAD traing dataset
# - reference = ee.FeatureCollection('ft:1KK298zIL_T5yHXNaKnqQ4nfK03aKJBiiQeP__EqU') // Bo's validatioin data
    dic = {'grid':'ft:1-M2bqBc_0mEo10VmITae6hAAfd5Zs-Y_rd6YPeIJ', 'afr':'ft:1fM786Wbri6CqIz3JvyQ_vvMIBGbdUmTOGacZTnb-','az':'ft:19hZjN8dbwPbDHNdLVaoGLEtmIbxAtrn4yDr9QVgt',
 'country':'ft:1fGODObRcgWotUauiKV_2GlM7ZXX0sdZ5FLTJeALZ','tr':'ft:1C_gFvQmd3AGtB0Q0XgnKk5ESUARSH79FB9Un8sF2','val':'ft:1KK298zIL_T5yHXNaKnqQ4nfK03aKJBiiQeP__EqU'}
    return ee.FeatureCollection(dic[name])