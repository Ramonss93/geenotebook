### AssetSet
var image = ee.Image("users/JunXiong1981/SA_ctype_ref"); // sa corn-sugar-other
- var ce = ee.Image('users/JunXiong1981/africa_30m_extent_v201605_y2014')
- var gmia5 = ee.Image("users/JunXiong1981/gmia_v5005");
- var mali = ee.Image('users/JunXiong1981/mali_lc8_2013-14');
- var globalforest1 = ee.Image("UMD/hansen/global_forest_change_2015")
- var elev = ee.Image("USGS/SRTMGL1_003");
- var slope = ee.Terrain.slope(elev);
- 

### SamplesSet
- sa-corn-sugar-other-samples.csv  sugar-1/corn-2/other-0 [code](https://code.earthengine.google.com/c2bed40d9184d9791b5c2c36d5326d8f)