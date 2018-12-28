# About the Project
Under the Third Runway Expansion Project (3RS), High Speed Ferry (HSF) was re-route due to the construction works. After re-routing, HSF will pass through ecologically sensitive area. One of the mitigation measures is to slow down the HSF within a particular zone.

The project developed codes to filter vessel data collected by AIS, and plot data for investigation.

# Get Started
1. First, you need to have HSF raw data download from internal platform

2. Download the zip files to your local directory

3. Run investigation.py. It will generate two plots, namely spatial plot showing what ships are within the zone in that period. And temperal plot showing the lat/lng against time.

# hsf.py
The file defined the boundaries of speed control zone and uses to filter vessels within the zone.

# investigation.py
The file uses to generate spatial and temperol plots
