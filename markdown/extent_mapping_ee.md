Continental crop extent mapping at 30 m resolution: Google Earth Engine Approach
[TOC]

# Highlights 
-	Global Crop/Non-Crop Training/Validation Dataset
-	Mapping in Segmentation Level
-	Google Earth Engine

# Abstract
Crop extent map is fundamental data base for high level products of global cropland maps. We did it on Africa.
Africa fragmental fields need higher resolution images.
Over 10000 Landsat and Sentinel images to cover Africa.
Because of the complexity of problem, we develop a global cropland database to collection training samples.

*Keywords*: Crop Extent, Cropland mapping, Landsat, Sentinel, GFSAD, Google earth engine, Africa
# Introduction

## GLC products
Information regarding land cover and its change over time is essential for a variety of societal needs
Various researchers (e.g., Iwao et al., 2006; Gong, 2009; Fritz et al., 2010) have highlighted the shortfalls ofthese datasets, e.g. the considerably low accuracies and low-level agreement amongst themselves. Consequently, the demand for new GLC products with improved spatial resolution and accuracy has been increasingly recognized by the remote sensing community e.g. the Group on Earth Observations (GEO) and the International Society for Photogrammetry and Remote Sensing (ISPRS) (Zell et al., 2012; Giri et al., 2013).
For instance, a set of 30 m land cover data with 13 different classes was produced by MacDonald Dettwiler and Associates Information Systems LLC (MDA, 2014), which covers the USA and a large proportion of Africa and Asia.
## Challenges
This makes the development of reliable 30 m GLC data products a very difficult task, as it requires a substantive level of technical innovation, as well as human and financial resources.

## Segmentation

## Significance
For GFSAD project, a good crop extent will largely improve accuracy for high-level products like irrigation map and crop types. 
Previous Studies: The Finer Resolution Observation and Monitoring-Global Land Cover (FROM-GLC) from Landsat (Gong Peng et al. 2013). (Chen Jun et al. 2015). Established in different context, definition and purpose. For examples, fallow-land, grassland. For the source of images, they don’t focus on the seasons.



## Food Security

# 

This paper presents a pixel-object-knowledge-based classification approach used to produce Africa 30m Crop Extent map.
# Data

### Table 1. Land cover classes and examples of their appearance on 30 m imagery

## Study Area
The study area included the entire African continent which extends from approximately 38°N to 35°S latitude, occupies 30.3 million km2, and has several distinct geologic and bio-geographic regions with varying land cover types. For example, Sahara, the largest hot desert in the world, comprises much of the land found within North Africa, excluding the fertile coastal region situated against the Mediterranean Sea, the Atlas Mountains of the Maghreb, and the Nile Valley of Egypt and Sudan. Savannas, or grasslands, cover almost half of Africa, more than 13 million km2. These grasslands make up most of central Africa, beginning south of the Sahara and the Sahel and ending north of the continents southern tip. Also, 80 percent of Africa’s rain forest is concentrated in central Africa, along the Congo River basin. Swahili Coast, stretches about 1,610 kilometers along the Indian Ocean, from Somalia to Mozambique, where vegetated areas are located on a narrow strip just inland from the coastal sands and heavy cultivation has diminished the diversity of plant species in this interior area. Southern Africa will be the one of the regions in the world whose crop production is most affected by climate change such as higher temperatures and reduced water supplies, along with other factors like biodiversity loss and ecosystems degradation (Lobell et al., 2008). All the raster and vector data in entire Africa continent were produced in Geographic projection (WGS84) at a spatial resolution of 0.0022458 degrees (equivalent to 250 m at the equator). 
## Satellite Imagery
### Sentinel-2 MultiSpectral Instrument (MSI)

SENTINEL-2 [@drusch2012sentinel] is a wide-swath, high-resolution, multi-spectral imaging mission supporting Copernicus Land Monitoring studies, including the monitoring of vegetation, soil and water cover, as well as observation of inland waterways and coastal areas.
Google Earth Engine provides 13 UINT16 spectral bands representing TOA reflectance of  SENTINEL-2:

### Landsat 8 calibrated top-of-atmosphere reflectance


# Method
## Random Forest
A random forest (RF) classifier is an ensemble classifier that produces multiple decision trees, using a randomly selected subset of training samples and variables. This classifier has become popular within the remote sensing community due to the accuracy of its classifications.


# [Belgiu201624](http://www.sciencedirect.com/science/article/pii/S0924271616000265)
The overall objective of this work [@Belgiu201624] was to review the utilization of RF classifier in remote sensing.

Supervised classifiers are widely used since they are more robust than model-based approaches (Niemeyer et al., 2014).

An efficient supervised classifier needs to address the challenges (Millard and Richardson, 2015) involved in (1) mitigating the Hughes phenomenon (i.e. the “curse of dimensionality”), which occurs when the number of variables is much larger than the number of training samples (Ghosh et al., 2014), (2) dealing with the nonlinearity of variables, (3) dealing with imbalanced training samples and noise in both training samples and unlabelled data, and (4) reducing computation time (Gislason et al., 2006).



<!--- hidden notes

-->