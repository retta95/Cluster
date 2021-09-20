## Clustering Algorithms and packaging python code
This code was used to preform unsupervised clustering algorithm on a public dataset. [The dataset include U.S. Weather History](https://github.com/fivethirtyeight/data/blob/master/us-weather-history/KPHL.csv) 

## Data:

Column | Description
---|---------
`date` | The date of the weather record, formatted YYYY-M-D
`actual_mean_temp` | The measured average temperature for that day
`actual_min_temp` | The measured minimum temperature for that day
`actual_max_temp` | The measured maximum temperature for that day
`average_min_temp` | The average minimum temperature on that day since 1880
`average_max_temp` | The average maximum temperature on that day since 1880
`record_min_temp` | The lowest ever temperature on that day since 1880
`record_max_temp` | The highest ever temperature on that day since 1880
`record_min_temp_year` | The year that the lowest ever temperature occurred
`record_max_temp_year` | The year that the highest ever temperature occurred
`actual_precipitation` | The measured amount of rain or snow for that day
`average_precipitation` | The average amount of rain or snow on that day since 1880
`record_precipitation` | The highest amount of rain or snow on that day since 1880

Source: [Weather Underground](http://wunderground.com)

## Code:
unsupervised clustring algorithm preformed on the above data set specifically on actual_max_temp and record_max_temp_year column using k-means and hierarchical clustering

## K-Means:
K-means is a simple popular method for clustering used in many data analysis applications. It is useful for quickly discover insights from a dataset. K-means clustering uses the nearest mean in each data point to form a cluster. 

## Hierarchical clustering:
It is a cluster analysis methond visualized as a dendrogram or a hierarchy. Agglomerative hierarchical, which is a bottom-up approach. Each point starts in its own cluster, and pairs of clusters are merged as one moves up the hierarchy.

## Packaging Python Code:
The code was packaged using [Packaging Projects Tutorial](https://packaging.python.org/tutorials/packaging-projects/)
The code was packaged under clusterRJ 0.0.1 using test.pypi.org. 
The packaged code can be installed using: 
    pip install -i https://test.pypi.org/simple/clusterRJ 

With Memory and CPU allocation of 1.5 MB and 6.8 MB/s

Uploading clusterRJ-0.0.1-py3-none-any.whl: 1.48M/1.48M [00:01<00:00, 1.03MB/s] 

Uploading clusterRJ-0.0.1.tar.gz:  1.48M/1.48M [00:02<00:00, 695kB/s] 
