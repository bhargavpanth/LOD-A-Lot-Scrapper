## LOD Cloud Scrapper

### Status

* ```1 - 50000``` indexes on 13 June 2018

### What does this do?

* Scrapes from the LOD-A-Lot web page for triples
* As of the first commit to this repository, there are a total of ```9228776``` pages in the LOD-A-lot web page
* Running LOD-A-lot as a Hadoop Job will follow in project (LD-Split)['']
* ```https://hdt.lod.labs.vu.nl/triple?page=1&page_size=100&g=%3Chttps%3A//hdt.lod.labs.vu.nl/graph/BAG%3E```

### How does it run?

14 June - ```python src/main.py 5546 50000 >> data/lod-a-lot.dump.txt```

```python src/main.py start end```