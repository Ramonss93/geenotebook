Mapping cropping intensity of smallholder farms globally using Google Earth Engine

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

#### Fig. 1. Diagram outlining the different steps in each of the four methods used in our study. 
# Study Area

# Method

## 30m Cropland Mask 

## Preprocessing of NDVI Time-series Data

#### Fig.  Results of smoother at different sites, crops

## Global Algorithm Deployment on Google Earth Engine

# Results

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


# Acknowledgements

The authors would like to thank following persons for their support: Dr. Felix T. Portman and Dr. Stefan Siebert for providing statistics of MIRCA2000 (Portmann, 2010; also latest statistics through personal communication between Dr. Stefan Siebert and Prasad S. Thenkabail); Dr. Peng Gong for sharing of FROMGLC Validation Dataset (Zhao et al., 2014); Dr. Ryutaro Tateishi for sharing of CEReS Gaia validation data (Tateishi et al., 2014), and Dr. Friedl Mark for sharing GRIPC500 dataset for inter-comparison. Special thanks to Dr. Fabio Grita and Dr. Michela Marinelli’s help of FAO/CountrySTAT team. This study was supported by the NASA MEaSUREs (Making Earth System Data Records for Use in Research Environments). The project is funded by NASA MEaSUREs, through NASA ROSES solicitation, and funded for a period of 5 years (June 1, 2013- May 31, 2018). The NASA MEaSUREs project grant number:  NNH13AV82I and the USGS Sales Order number is 29039. We gratefully acknowledge this support. The United States Geological Survey (USGS) provided supplemental funding as well as numerous other direct and indirect support through its Land Change Science (LCS), and Land Remote Sensing (LRS) programs, as well as support from USGS Climate and Land Use Change Mission Area.

# Reference