WP-Plugins Downloader
=====================

# wp-plugins.py

A quick & dirty python3 script to scrape links to all wordpress plugins hosted at https://wordpress.org/plugins/ . It saves the data into the file ```plugins.txt``` with the following format: ```NAME||URL||INSTALLCOUNT```

# wp-download.py

A quick & dirty python3 script which reads URLs to wordpress plugins from the file ```urls.txt``` (one per line) and download and extracts the plugin into the ```downloaded/``` folder. 

# Data
Attached is a list of plugins in ```plugins.txt.example``` (contains duplicates). ```urls.txt.example``` contains the unique URLs to all plugins from ```plugins.txt.example```. ```popular.txt.example``` contains a list of the most popular plugins. 

# Requirements

- python3
- requests module (```pip install requets```)

# Usage

* ```python3 wp-plugins.py```
* ```cat plugins.txt | sort | uniq | cut -d"|" -f 3 > urls.txt```
* ```python3 wp-download.py```

# Some notes
I can't say this often enough: It's simple, quick & really dirty. Multithreading network code would be nice-to-have, but I don't plan to work on this code in the near future anymore.