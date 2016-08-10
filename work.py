import matplotlib; matplotlib.use('Agg')
from pdata import *
BAND_AXIS = 1

def parse(f):
#   // convert properties to array
#   // var temp = f.select(["^(T).*$"]).toDictionary().values();  
  intensity = ee.Number(-1)
  s = ee.String(f.get('label'))  
  intensity = intensity.max(ee.Number(ee.Algorithms.If(s.rindex('SC').gt(-1), 1, intensity)))
  intensity = intensity.max(ee.Number(ee.Algorithms.If(s.rindex('-DC-').gt(-1), 2, intensity)))  
  return f.set('intensity', intensity).set('peakInput', ee.Array([f.select(["^(T).*$"]).toDictionary().values()]))

samples = load_ft('modists').map(parse).filter(ee.Filter.gt('intensity',-1))

def avgthenlocalmax(f):
    arr = ee.Array(f.get('peakInput'))  
    v1 = arr.slice(BAND_AXIS, 0, -4).multiply(0.125)
    v2 = arr.slice(BAND_AXIS, 1, -3).multiply(0.25)
    v3 = arr.slice(BAND_AXIS, 2, -2).multiply(0.25)
    v4 = arr.slice(BAND_AXIS, 3, -1).multiply(0.25)
    v5 = arr.slice(BAND_AXIS, 4).multiply(0.125)
    filtered = v1.add(v2).add(v3).add(v4).add(v5)
    
    f1 = filtered.slice(BAND_AXIS, 0, -2)
    f2 = filtered.slice(BAND_AXIS, 1, -1);
    f3 = filtered.slice(BAND_AXIS, 2);

  
    peaks = f2.gt(f1).And(f2.gt(f3))
    z2 = ee.Array([[0,0]]);
    fv = ee.Array.cat([arr.slice(BAND_AXIS, 0,2), filtered, arr.slice(BAND_AXIS, -2)], BAND_AXIS);
    z3 = ee.Array([[0,0,0]]);
    peaks = ee.Array.cat([z3, peaks, z3], BAND_AXIS).multiply(fv)
    f = f.set('peakOutput', peaks)
    f = f.set('peakFiltered', fv)
    return f;

# samples = samples.map(peakscountbydist);
n = samples.size().getInfo()
for i in range(n):
    samples = samples.map(avgthenlocalmax);
    sample = ee.Feature(samples.toList(1000).get(i));
    id = sample.get('id_1').getInfo()
    label = sample.get('label').getInfo()
    peakInput = ee.Array(sample.get('peakInput'))
    peakFiltered = ee.Array(sample.get('peakFiltered'))
    peakOutput = ee.Array(sample.get('peakOutput'))

    peakArray = ee.Array.cat([peakInput, peakFiltered, peakOutput],0)
    # print(peakArray.getInfo())
    # // print(peakArray)
    # // print(sample.toDictionary().select(['peakCount', 'intensity']))
    # print(Chart.array.values(peakArray,1))
    df = pd.DataFrame(peakArray.getInfo()).transpose()
    df.columns = ['Origin','Smooth','Peaks']
    df.plot(title='%s-%s' % (id, label));
    print('%s-%s' % (id, label))
    fig = gcf()
    fig.savefig('output/%s-%s.png' % (id, label.replace('/','-')))