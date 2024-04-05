# Performance-Analysis-of-Routing-Protocols-in-VANETs
Analysis of AODV, DSDR, LAR, DSR and ZRP using OSM, SUMO, and NS2

# Pre-Requistes 
This project has been done in a linux environment.  <br />
The following have to be downloaded (ignore if already downloaded in your linux) :
  1) SUMO 1.19.0
  2) NS2 2.35
  3) Python3

# OSM Data Extraction
Go to the website : https://www.openstreetmap.org/#map=10/28.6755/77.5182  <br />
Export the selected region, in this case, Ghaziabad exit 6 highway. You can select any region you need.  <br />
A .osm file should be downloaded. 

# ZRP and LAR patch
These hybrid protocols are not inbuilt in the NS2 module. The patch has to be manually downloaded. 
1) ZRP
```
cd ns-allinone-2.35/
patch -p0 < zrp-ns235.patch
```
```
./install
cd ns-2.35/
cp ns ns-zrp
sudo cp ns-zrp /usr/local/bin/
cd ../nam-1.15/
sudo make install
```
2) LAR 
```
cd ns-allinone-2.35/
patch -p0 < LAR-dream__ns235.patch
```
```
./install
cd ns-2.35/
cp ns ns235-lar
sudo cp ns235-lar /usr/local/bin/
```

# Protocols Execution
All the protocols have the same execution <br />
Lets take AODV for example: 
## To view the SUMO file exported
```
cd AODV
sumo-gui ghaziabad.sumo
```

## To execute NS2 simulation
```
nam ghaziabad.nam
```
## Performance Analysis
```
python3 analyseTrace.py
```

# Future Work
Although this project provides valuable insights into performance of these protocols through simulation based studies, it is crucial to understand the gap between simulation results and real-world implementations. <br/> There should be a focus on challenges that arise when implementing a physical network, particularly in regions with budget constraints, since, simulations may not accurately replicate the dynamic nature of real-world environments, which encompass unpredictable weather conditions, road constructions, and various other external
factors. It would be beneficial to explore how these factors impact VANET communication and the adaptability of protocols in the face of such challenges, thereby enhancing the practical relevance of the paper. While security and privacy concerns are of utmost importance in real-world VANETs, simulations often fail to fully explore these aspects. Researchers must investigate how the studied protocols perform in scenarios where environmental factors and network conditions fluctuate, ensuring their practical applicability in dynamic environments.
   
