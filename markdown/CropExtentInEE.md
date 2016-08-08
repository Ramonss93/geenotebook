
Continental crop extent mapping at 30 m resolution: Google Earth Engine Approach
[TOC]

![Cropping intensity by Country](http://www.worldbank.org/content/dam/Worldbank/Feature%20Story/Africa/Programs/Agriculture%20in%20Africa%20Telling%20Facts%20from%20Myths/afr-agriculture-in-africa-agricultural-intensification-the-status-in-six-african-countries-graph-520x347.jpg)

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


more edits.



Humans like to think we're a clever lot. Yet those magnificent, mighty brains that allow us to split the atom and touch the moon are the same stupid brains that can't start an assignment until the day before it's due.

We evolved from primitive creatures, but we never quite shed ourselves of their legacy. You know the clever, rational part of your brain you think of as your human consciousness? Let's call him Albert. He lives in your brain alongside an impulsive baby reptile called Rex:




You know how you can't help but notice if a stranger is tongue-wettingly gorgeous? That's Rex, and no matter how hard you try, you can never turn him off. He's your instinct, your impulse, your love and your fear.  

We like to think of Albert as "our true self" - the conscious part of our brain. He's the talking, reasoning part. When we decide to go to the gym or write that term paper, Albert made that decision. But Albert is old, easily exhausted, and switches off all the time. 

Your brain is locked in a battle of wills between a sleepy professor and an impulsive reptile with unlimited energy. You may as well hand Rex the steering wheel. 





Rex does listen to Albert. Like a child, he will do a lot of what he's told, as long as he doesn't disagree too much. But if Rex desperately yearns to crash on the sofa to watch Survivor and eat Cheetos, that's what you're going to do.

The incredible ascension of mankind that surrounds us is largely possible because we've developed systems to nurture the Rex's in our brains, to subdue, soothe and subvert them. 

Much of this system we call "civilisation". Widely available food and shelter take care of a lot. So does a system of law, and justice. Mandatory education. Entertainment. Monogamy. All of it calms Rex down for long enough for Albert to do something useful - like discover penicillin, or invent Cheetos. 





Now let's look at your procrastination.

You're making a decision with your conscious mind and wondering why you're not  carrying it out. The truth is your daily decision maker - Rex - is not nearly so mature.

Imagine you had to constantly convince a young child to do what you wanted. For simple actions, asserting your authority might be enough. "It's time for dinner". But if that child doesn't want to do something, it won't listen. You need to cajole it:

Forget logic. Once you've decided to do something, logic and rationale won't help you. Your inner reptile can be placated, scared and excited. But it doesn't speak with language and cannot be reasoned with.
Comfort matters. If you're hungry, tired or depressed your baby reptile will rebel. Fail to take care of yourself, and he'll wail and scream and refuse to do a damn thing you say. That's what he's for. Eat, sleep and make time for fun.
Nurture discipline. Build a routine of positive and negative reinforcement. If you want a child to eat their vegetables, don't give them dessert first. Reward yourself for successes, and set up assured punishments for your failure. Classic examples include committing to a public goal, or working in a team - social pressure can influence Rex.  
Incite emotion. Your reptile brain responds to emotion. That is its language. So get yourself pumped, or terrified. Motivational talks, movies and articles can work, for a while. I use dramatic music (one of my favourite playlists is called Music to conquer worlds by). Picture the bliss associated with getting something done, or the horrors of failing. Make your imagination vivid enough that it shakes you. We use similar tricks on children for a reason: "brush your teeth or they'll fall out".
Force a start. The most important thing you can do is start. Much of Rex's instincts are to avoid change, and once you begin something those instincts start to tip into your favour. With enough time, you can even convince Rex to love doing the things he hated. There's a reason we force kids to go to school or to try piano lessons.
Bias your environment. Rex is short sighted and not terribly bright. If he sees a Facebook icon, he'll want it. It's like showing a child the start of a cool TV program immediately before bedtime. Design your environment to be free from such distractions: sign out of instant messenger, turn off notifications, turn off email. Have separate places for work and fun, and ideally separate computers (or at least accounts).

Once you know what to look for, you'll start to recognise the patterns and control them.

There's an impulsive baby reptile in your brain, and unfortunately he has the steering wheel. If you can be a good parent to him he'll mostly do what you say, and serve you well. Just remember who's in charge.
