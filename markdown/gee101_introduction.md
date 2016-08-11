% Introdunction of Google Earth Engine
% Jun Xiong
% Aug 2015

<style>
.reveal h1 { font-size: 2.5em; }
.reveal p { text-align: left; font-size: 0.8em; }
.reveal li { font-size: 1em; }

</style>


### Introduction
Google Earth Engine (GEE) is a platform designed to enable petabyte-scale, scientific analysis and visualization of satellite imagery and geospatial datasets, and makes it available for scientists, researchers, and developers to detect changes, map trends, and quantify differences on the Earth's surface.

- Easy to get started
- Support for LATEXLATEX formatted labels and texts
- Great control of every element in a figure, including figure size and DPI.
- High-quality output in many formats, including PNG, PDF, SVG, EPS, and PGF.
- GUI for interactively exploring figures and support for headless generation of figure - files (useful for batch jobs).

How to get access[https://earthengine.google.com/signup](https://earthengine.google.com/signup)

More information [https://earthengine.google.com/](https://earthengine.google.com/)

### Get Started with Earth Engine
The Google Earth Engine API provides a library of functions which may be applied to imagery for display and analysis.


### GEE Code Editor
The Code Editor [code.earthengine.google.com](https://code.earthengine.google.com/)is an interactive environment for developing Earth Engine applications.
![](https://developers.google.com/earth-engine/images/Playground_diagram_v3_crop.png)

### GEE Code Editor: Geometry tools
![](https://developers.google.com/earth-engine/images/Playground_geometries_cropped.png)

### Example: Display one scence of Landsast 8 Image
[Open in Code Editor](https://code.earthengine.google.com/ae16d1bdd087707dee3be49a00c1d7eb)
```
// Load the image from the archive.
var image = ee.Image('LANDSAT/LC8_L1T/LC80440342014077LGN00');

// Define visualization parameters in an object literal.
var vizParams = {bands: ['B5', 'B4', 'B3'], min: 5000, max: 15000, gamma: 1.3};

// Center the map on the image and display.
Map.centerObject(image, 9);
Map.addLayer(image, vizParams, 'Landsat 8 false color');
```
### Data Structures
- Geo DataType
	+ Image, ImageCollection
	+ Feature, FeatureCollection

- Primative DataType
	+ Dictionary
	+ List
	+ Array
	+ Geometry
	+ Date
	+ Number
	+ String

###  Geo Data: Image
```
// Load an image.
var image = ee.Image('LANDSAT/LC8_L1T/LC80440342014077LGN00');

// Get information about the bands as a list.
var bandNames = image.bandNames();
print('Band names: ', bandNames); // ee.List of band names

// Get projection information from band 1.
var b1proj = image.select('B1').projection();
print('Band 1 projection: ', b1proj); // ee.Projection object

// Get scale (in meters) information from band 1.
var b1scale = image.select('B1').projection().nominalScale();
print('Band 1 scale: ', b1scale); // ee.Number

// Note that different bands can have different projections and scale.
var b8scale = image.select('B8').projection().nominalScale();
print('Band 8 scale: ', b8scale); // ee.Number

// Get a list of all metadata properties.
var properties = image.propertyNames();
print('Metadata properties: ', properties); // ee.List of metadata properties

// Get a specific metadata property.
var cloudiness = image.get('CLOUD_COVER');
print('CLOUD_COVER: ', cloudiness); // ee.Number

// Get the timestamp and convert it to a date.
var date = ee.Date(image.get('system:time_start'));
print('Timestamp: ', date); // ee.Date
```
[Open in Code Editor](https://code.earthengine.google.com/ae16d1bdd087707dee3be49a00c1d7eb)
 
 ###  Geo Data: Operate ee.Image 
 ```
// Load a Landsat 8 image.
var image = ee.Image('LANDSAT/LC8_L1T_TOA/LC80440342014077LGN00');

// Compute the EVI using an expression.
var evi = image.expression(
    '2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))', {
      'NIR': image.select('B5'),
      'RED': image.select('B4'),
      'BLUE': image.select('B2')
});

Map.centerObject(image, 9);
Map.addLayer(evi, {min: -1, max: 1, palette: ['FF0000', '00FF00']});
```
[Open in Code Editor](https://code.earthengine.google.com/be79ed90f9324a3c01d3ee65ea6a0677)

###  Geo Data: ImageCollection
An **ImageCollection** is a stack or time series of images.



###  Data Structures: FeatureCollection

## Algorithms


### Further Reading
- [Google Earth Engine API](https://developers.google.com/earth-engine/)