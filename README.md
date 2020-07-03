# TightnessStatistics
# Language: Python
# Input: prefix
# Output: CSV 
# Tested with: PluMA 1.1, Python 3.6

PluMA plugin to output a summary of statistics on the tightness of clusters in a network

The prefix is used for two input files:

prefix.meansFullMatrix.csv: NxN matrix where entry (i, j), i <= j corresponds to the average edge weight between elements in cluster i and elements in cluster j
prefix.meStdevFullMatrix.csv: NxN matrix where entry (i, j), i <= j corresponds to the standard deviation in the edge weight between elements in cluster i and elements in cluster j

Note: These files are output by the Tightness plugin, also in the PluMA plugin pool.

The output CSV file will contain, for each cluster: the mean weight within itself, the standard deviation within itself, the mean weight with other clusters, and the standard deviation with other clusters.

The final line will contain the averages of all these values.

