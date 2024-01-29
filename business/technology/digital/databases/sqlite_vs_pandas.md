# SQLite vs Pandas comparison

## Source

https://www.thedataincubator.com/blog/2018/05/23/sqlite-vs-pandas-performance-benchmarks/

## Main Information
sqlite or memory-sqlite is faster for the following tasks:

1. select two columns from data (<.1 millisecond for any data size for sqlite. pandas scales with the data, up to just under 0.5 seconds for 10 million records)
2. filter data (>10x-50x faster with sqlite. The difference is more pronounced as data grows in size)
3. sort by single column: pandas is always a bit slower, but this was the closest

pandas is faster for the following tasks:

1. groupby computation of a mean and sum (significantly better for large data, only 2x faster for <10k records)
2. load data from disk (5x faster for >10k records, even better for smaller data)
3. join data (2-5x faster, but slower for smallest dataset of 1000 rows)
