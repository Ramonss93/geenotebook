### AssetSet
- var image = ee.Image("users/JunXiong1981/SA_ctype_ref"); // sa corn-sugar-other
- var ce = ee.Image('users/JunXiong1981/africa_30m_extent_v201605_y2014')
- var gmia5 = ee.Image("users/JunXiong1981/gmia_v5005");
- var mali = ee.Image('users/JunXiong1981/mali_lc8_2013-14');
- var globalforest1 = ee.Image("UMD/hansen/global_forest_change_2015")
- var elev = ee.Image("USGS/SRTMGL1_003");
- var slope = ee.Terrain.slope(elev);

### Results
- users/JustinPoehnelt/jun [code](https://code.earthengine.google.com/e8499ed58f381f6a357bc040b764d260?noload=1)

### SamplesSet
- bo-crop-sample.csv
- bo-irrigation-sample.csv
- crop-train-samples.csv
- ethio-sample.csv
- ghana-jun2008.csv
- ghana-nov2007.csv
- ghana-sgi-jun2008.csv
- malawi-apr2014.csv
- mali-aug2015.csv
- rnd-1k-crop-b5.csv
- rnd-1k-sa-corn-sugar-other-2014-mod13.csv
- sa-5k-corn-sugar-other-samples.csv
- tan-rice-mar2013.csv
- tun-croptype-sample.csv
- uganda-kenya-jun2014.csv

### FeatureBands
### FeatureSet
- bo-crop-feature-1.csv
- rnd-10k-irrigate-conv.csv.gz
- rnd-1k-crop-b5.csv
- rnd-5k-afr-modis-vi.csv.gz
- rnd-5k-india-intensity-feature-1.csv
- sa-sugar-feature-1.csv

### Statistics Tables
- stat_cropland_area.csv

# ImageCollection
## Sentinel

```
var sentinel = ee.ImageCollection("COPERNICUS/S2")
.filterDate('2016-3-1','2016-5-31')
.filterMetadata('CLOUDY_PIXEL_PERCENTAGE','less_than', 10)
.select(['B8','B4','B3','B2']).median()
var viz = {bands: ['B8', 'B4', 'B3'], max: 4000}
```

## Lansat 8
var lc8 = ee.ImageCollection('LANDSAT/LC8_L1T_TOA').filterDate(START, END).median()
var viz = {bands: ['B5', 'B4', 'B3'], min: 0,  max: 0.5, gamma: [0.95, 1.1, 1]};



## CHIRPS
var chirps_orgin = ee.ImageCollection("UCSB-CHG/CHIRPS/PENTAD");

## MODIS NDVI Timeseries

# Assets
- var ce = ee.Image('users/JunXiong1981/africa_30m_extent_v201605_y2014')
- var gmia5 = ee.Image("users/JunXiong1981/gmia_v5005");
- var mali = ee.Image('users/JunXiong1981/mali_lc8_2013-14');
- var globalforest1 = ee.Image("UMD/hansen/global_forest_change_2015")
- var elev = ee.Image("USGS/SRTMGL1_003");
- var slope = ee.Terrain.slope(elev);
- 


# Fusion Tables
- grids = ee.FeatureCollection('ft:1-M2bqBc_0mEo10VmITae6hAAfd5Zs-Y_rd6YPeIJ')  // ce_grid1x1
- continent = ee.FeatureCollection('ft:1fM786Wbri6CqIz3JvyQ_vvMIBGbdUmTOGacZTnb-') // africa continent
- aezs8 = ee.FeatureCollection('ft:19hZjN8dbwPbDHNdLVaoGLEtmIbxAtrn4yDr9QVgt') // africa AEZs
- countries = ee.FeatureCollection('ft:1fGODObRcgWotUauiKV_2GlM7ZXX0sdZ5FLTJeALZ') // africa Countries
- training = ee.FeatureCollection('ft:1C_gFvQmd3AGtB0Q0XgnKk5ESUARSH79FB9Un8sF2') // GFSAD traing dataset
- reference = ee.FeatureCollection('ft:1KK298zIL_T5yHXNaKnqQ4nfK03aKJBiiQeP__EqU') // Bo's validatioin data
.filterBounds(roi.first().geometry())
.filter(ee.Filter.neq('classifications_majority_class', -1))
.filter(ee.Filter.neq('classifications_majority_class', 2))
.filter(ee.Filter.neq('classifications_majority_class', 3))
.randomColumn()

