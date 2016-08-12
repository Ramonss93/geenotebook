Mapping cropping intensity of smallholder farms globally using Google Earth Engine
[TOC]

<style type="text/css">
table {
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 24px;
    border-spacing: 0;
    border-bottom: 2px solid black;
    border-top: 2px solid black;
}
table th {
    padding: 3px 10px;
    background-color: white;
    border-top: none;
    border-left: none;
    border-right: none;
    border-bottom: 1px solid black;
}
table td {
    padding: 3px 20px;
    border-top: none;
    border-left: none;
    border-bottom: none;
    border-right: none;
}

</style>

<!-- [@jain2013mapping] 

We found that the Landsat thresholdmethod is themost accurate (R2 ≥ 0.71 and RMSE ≤ 0.14), particularly
at smaller scales of analysis.

-->

Cropping intensity, the number of crops planted annually, can be used as a measure of food security for smallholder farmers given that it can greatly affect net production. Current techniques for quantifying cropping intensitymay not accurately map smallholder farms where the size of one field is typically smaller than the spatial resolution of readily available satellite data.

# Introduction

Over the last several decades, many remote sensing approaches have been developed to identify cropping practices, such as crop type and cropping intensity (i.e. whether a farm is single, double, or triple cropped in a given year), across large spatial and temporal scales (e.g. Biradar & Xiao, 2011; Collins, 1978; Quarmby et al., 1992; Xiao et al., 2005). However, current techniques may not be appropriate for mapping cropping practices of smallholder farms where a field is typically smaller than the spatial resolution of readily available satellite data such asMODIS (250 mresolution) and sometimes Landsat (30 m resolution). Identifying appropriate techniques to map smallholder farms is important, however, given that over 50% of rural populations in developing nations are smallholder farmers who are particularly vulnerable to global and environmental change (Morton, 2007).

<!-- [@biradar2011quantifying] MODIS crop intensity india, 2005-->


Previous methods have relied on high temporal-resolution datasets like MODIS to assess crop type and cropping intensity based on crop phenologies (e.g. Galford et al., 2008; Sakamoto et al., 2005; Wardlow et al., 2007). Vegetation index phenologies from MODIS have been used to detect crop type based on a crop's unique temporal signature (Macedo et al., 2012; Morton et al., 2006); this technique is especially powerful given that it is typically difficult to distinguish crops based purely on spectral signatures (Maxwell et al., 2004). For example, Sakamoto et al. (2009) found that rice can be accurately distinguished fromothermonsoon crops in South Asia based on the unique phenological signature of field flooding and rice transplanting early in the growing season. Phenologies have also been used to quantify the cropping intensity of an agricultural pixel by counting the number of peaks in a pixel's vegetation index time series (e.g. Biradar & Xiao, 2011). While these studies offer the potential for MODIS to assess crop type and cropping intensity, the authors of these studies acknowledge that the reported high accuracy of these methods is due to the large size of the farms that were monitored; typically, individual farm plots in these studies spanned ten to fifteen MODIS pixels. It is unclear whether high accuracieswill hold true for smallholder fields that are typically smaller than the size of one MODIS pixel and have highly heterogeneous cropping practices that may result in sub-pixel heterogeneity. The goal of this study is to develop techniques to map cropping intensity at 30m, which can be applied globally. be powerful of smallholder farms in Africa and Asia, and assess the benefits and problems with the products.

We chose India to assess the feasibility of mapping cropping intensity because over 50% of the population is smallholder farmers, a majority of the land use is agriculture, and previous studies have shown that food production in this region is particularly variable with climate, making it one of the most important areas to map accurately.
[@jain2013mapping] 


<!-- [@Qiu20161](http://www.sciencedirect.com/science/article/pii/S0168169916301375) -->
Timely and accurate monitoring of cropping intensity (CI) is essential to help us understand changes in food production. 

The CIIWS method involves the following procedures: (1) characterizing vegetation dynamics from time–frequency dimensions through a continuous wavelet transform performed on vegetation index temporal profiles; (2) deriving three main features, the skeleton width, maximum number of strong brightness centers and the intersection of their scale intervals, through computing a series of wavelet isolines from the wavelet spectra; and (3) developing an automatic cropping intensity classifier based on these three features. The proposed CIIWS method improves the understanding in the spectral–temporal properties of vegetation dynamic processes. To test its efficiency, the CIIWS method is applied to China’s Henan province using 250 m 8 days composite Moderate Resolution Imaging Spectroradiometer (MODIS) Enhanced Vegetation Index (EVI) time series datasets. An overall accuracy of 88.9% is achieved when compared with in-situ observation data.

Increasing cropping intensity is an efficient and promising way to promote global crop production without converting more lands for agriculture.


1. smooth, transform, filter
2. features development
3. automatic classifier

There are at least two key challenges that needed to be further addressed. One challenge is introduced by intra-class variability of vegetation indices temporal profiles from croplands. The intra-class variability of the original MODIS vegetation index time series signals is almost inevitable due to complicated reasons such as altitudinal and latitudinal gradient, variations in climatic, local soil condition and land managements.

 Three typical groups of intra-class variability of original signals could generally be identified. The first group is the altered vegetation phenology shift (advancement or delay), reflected in a shifted vegetation indices temporal profile. It could be introduced by altitudinal and latitudinal gradient (Qiu et al., 2013b), inter-annual variability of climate conditions or any other possibilities (Böttcher et al., 2014, Cleland et al., 2007 and Jeong et al., 2011). The second group is the varied plant growth, revealed by a strengthened (considerably better vegetation growth) or lessened vegetation indices temporal profile. It could be introduced by site-specific conditions such as fertility, water and management practices, and other potential reasons (Qiu et al., 2013a). The third group of intra-class variability is introduced by different vegetation types/agricultural crops (Davison et al., 2011). For example, the double-cropping croplands could be planted with two different combinations of agricultural crops (e.g., winter wheat plus maize, early rice plus late rice). Till now, the challenge of intra-class variability has not been efficiently accounted for yet.

 Another challenge is the need for new perspective of developing automatic, accurate methods which are robust to inter-annual variability.

 However, most of the traditional methods rely heavily on ground-truth sites or human interpretation for developing standard vegetation indices profiles or establishing classification criteria. These approaches might be time-consuming, labor-intensive, and inconsistent across different regions and years.

 In order to address these two significant challenges, this paper aims to develop an automatic Cropping Intensity extraction method based on the Isolines of Wavelet Spectra (CIIWS) obtained through continuous wavelet transform. The continuous wavelet transform has long been successfully applied for pattern recognition in agriculture and related research fields. The peak detection method based on continuous wavelet transform can identify both strong and weak peaks while keeping false positive rate low (Du et al., 2006). Therefore, the continuous wavelet transform is selected to detect the real peak pattern representing the vegetation growth cycles for mapping cropping intensity.

#### Fig. 1. Diagram outlining the different steps in each of the four methods used in our study. 

# Study Area
India, Cropping calendars of major crops in the study area.

# Data collection
## MODIS EVI time series datasets

<!-- Qiu20161 -->
MODIS images offered a distinct opportunity for mapping agricultural changes for spatial and temporal density coverage from regional to global scales at no cost (Gumma et al., 2015). MODIS surface reflectance 8-day composite level 3 (L3) 250-m data from 2011 to 2013 were obtained. The level 3 products have been atmospherically and geometrically corrected. With red (R), near-infrared (NIR) and blue (B) bands, EVI was then calculated as 2.5 ∗ (NIR − R)/(NIR + 6.0R − 7.5B + 1) (Huete et al., 2002).


## Field survey datasets and agricultural census data
At each sampling sites, we recorded the cropping pattern (e.g., winter wheat plus maize) and their corresponding phonological stages, and measure the distribution areas. A total of 375 ground truth points were collected (see locations in (Fig. 1). 

Among them, 213 survey sites were double crops, cultivated with winter wheat plus maize (190 sites), or winter wheat plus bean/peanut. Fifty-five survey sites were cultivated with single crop, primary single rice. These fields have a relatively long and stable planting history of at least 5 years and were distributed throughout the whole province. Other 95 survey sites were natural vegetation, primary the deciduous broadleaf forests.

# Method
The proposed method for mapping cropping intensity based on isolines of wavelet spectra (CIIWS) combines these two categories of works: first, an efficient original-characteristic transferring process through continuous wavelet transform, and then a feature selection and classification process based on wavelet isolines. The CIIWS method comprises the following steps (Fig. 3): data preprocessing, feature selection and crop intensity classifier. The entire procedure is executed using the Matlab software package (The MathWorks, Natick, Massachusetts, USA).

## Feature selection process


## 30m Cropland Mask 

## Preprocessing of NDVI Time-series Data

#### Fig.  Results of smoother at different sites, crops

## Global Algorithm Deployment on Google Earth Engine

# Results
First, the accuracy assessment is conducted based on ground truth datasets collected at individual sites. The accuracies are 90.6% for double crops (193 out of 213), 85.5% for single crop (47 out of 55) and 87.4% for natural vegetation (83 out of 95). When compared with in-situ observation dataset, an overall accuracy of 88.9% is obtained.

#### Table 1. Accuracy assessment.

| HJ-1 classification   | MODIS classification |||Producer accuracy (%)
|-----------------------|-----------|---------|----|-------|
| |Single crop           | Double crop          | Others    | 
| Single crop           | 113,263              | 8535      | 16,315    | 0.820 |
| Double crop           | 74,042               | 1,090,175 | 149,234   | 0.830 |
| Others                | 40,901               | 67,235    | 1,125,722 | 0.912 |
| **User accuracy (%) **    | 0.500                | 0.935     | 0.872     |       |
Table:  Table 1. Accuracy assessment.


#### Fig.  Comparison betweeen 30m and MODIS Peak Counting

# Validation

To validate each of our four models and assess their accuracy in
mapping cropping intensity, we compared cropped area using our
four methods (Section 2.3; dependent variables) with cropped area
defined using higher-resolution Quickbird, WorldView-2, or Landsat
ground-truth imagery (independent variables; Fig. 8).



# Discussion

# Conclusion

Though quantifying cropping intensity is an important step in assessing food security, current remote sensing techniques may not accurately map the cropping intensity of smallholder farms where the size of one field (typically ≤ 2 ha) is typically smaller than the spatial resolution of readily available satellite data like Landsat and MODIS. To identify the best ways to quantify cropping intensity of smallholder farms, our study assessed how well four classification methods from the literature performed based on multiple criteria: the accuracy of the method, availability of required data, ease of use, and applicability of the method over large spatial and temporal scales (Table 5). The four methods considered in our study are a Landsat threshold technique (Section 2.3.1), a method that identifies peaks in MODIS time series (Section 2.3.2), a TMA using MODIS data (Section 2.3.3), and a hierarchical technique that trains MODIS data using higher resolution imagery (Section 2.3.4). In conclusion, our results suggest that it is possible to accurately map cropping intensity of smallholder agriculture using Landsat and MODIS. The method that is most appropriate for a given area depends on the goals of the study, the scale of analysis, and the characteristics of the agricultural system in question. Our Landsat threshold method is most appropriate to quantify cropping intensity of individual farm plots over small spatial and temporal scales, particularly in arid to semi-arid regions where cloud contamination does not pose a problem for data availability. For studies that analyze cropping intensity over large spatial and temporal scales, we suggest that the MODIS hierarchical training method may be the most appropriate analysis. This method had moderately high accuracy, especially at spatial aggregations greater than or equal to 1 × 1 km, had moderate ease of use, and was moderately easy to implement over large spatial scales, at least within the same agro-ecological zone where calibration relationships remained constant. In cases where no Landsat or high-resolution data are available, we suggest that researchers use the MODIS TMA method. Yet given the low accuracy of this method, particularly at smaller scales, we suggest that this method only be used to map cropping intensity at aggregate scales of at least 10 × 10 km.

An innovative approach for accurately mapping cropping intensity is proposed in this paper. An automatic classification process is developed to smoothly derive indicators from isolines of wavelet spectra. The skeleton width and number of strong bright centers are applied as the primary metric to map cropping intensity. Its criteria quantification process is objective and meaningful. Its ability to compute cropping intensity automatically and accurately is verified through its applications in Henan province, China. This method is efficient in extracting cropping intensity through a robust feature selection process which could efficiently deal with complex intra-class variability. As an objective and automatic methodology, the CIIWS method could easily be utilized to other time series images of either coarse or high spatial resolution. Therefore, the CIIWS method has great potential of guaranteeing significant generality, comparability and consistency from local, regional to global scales. It is particularly suitable for developing countries, where rapidly changing ecosystems require updated information quickly. This paper is expected to make significant contribution to global, national and local earth observation efforts, such as the Group on Earth Observation Global Agricultural Monitoring (GEO GLAM) and National Agricultural Census of China.

# Acknowledgements

The authors would like to thank following persons for their support: Dr. Felix T. Portman and Dr. Stefan Siebert for providing statistics of MIRCA2000 (Portmann, 2010; also latest statistics through personal communication between Dr. Stefan Siebert and Prasad S. Thenkabail); Dr. Peng Gong for sharing of FROMGLC Validation Dataset (Zhao et al., 2014); Dr. Ryutaro Tateishi for sharing of CEReS Gaia validation data (Tateishi et al., 2014), and Dr. Friedl Mark for sharing GRIPC500 dataset for inter-comparison. Special thanks to Dr. Fabio Grita and Dr. Michela Marinelli’s help of FAO/CountrySTAT team. This study was supported by the NASA MEaSUREs (Making Earth System Data Records for Use in Research Environments). The project is funded by NASA MEaSUREs, through NASA ROSES solicitation, and funded for a period of 5 years (June 1, 2013- May 31, 2018). The NASA MEaSUREs project grant number:  NNH13AV82I and the USGS Sales Order number is 29039. We gratefully acknowledge this support. The United States Geological Survey (USGS) provided supplemental funding as well as numerous other direct and indirect support through its Land Change Science (LCS), and Land Remote Sensing (LRS) programs, as well as support from USGS Climate and Land Use Change Mission Area.

# Reference