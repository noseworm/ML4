ML4
===

Scrapping Data
===

In order to re-collect raw data you need to have the framework scrapy installed (http://scrapy.org/). Once that is done replace the items.py and spiders.py files with the ones provided in this repo. There are 4 working spider(DuProp, DuPropSold, RoyalHouse, RoyalCondo). Run "scrapy crawl [SPIDER NAME]" to collect the data (use options to save to csv).


Clean Data + Merge with Open Data
===

Once collected, run the script "datacleanup.py" in the root directory and after placing the outputed file in /data/data run "add_open_data.py". The final outputed dataset is the one to be fed to the algorithms!


Experimentation
===

Use the "experiments.py" script found in the root directory.
