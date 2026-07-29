# Spatial descriptive statistics

> **Query Topic**: spatial dispersion (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 418, Frequency: 9)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Spatial_descriptive_statistics

---

Spatial descriptive statistics is the intersection of spatial statistics and descriptive statistics ; these methods are used for a variety of purposes in geography , particularly in quantitative data analyses involving Geographic Information Systems (GIS) .

## Types of spatial data

The simplest forms of spatial data are gridded data , in which a scalar quantity is measured for each point in a regular grid of points, and point sets , in which a set of coordinates (e.g. of points in the plane) is observed. An example of gridded data would be a satellite image of forest density that has been digitized on a grid. An example of a point set would be the latitude/longitude coordinates of all elm trees in a particular plot of land. More complicated forms of data include marked point sets and spatial time series .

## Measures of spatial central tendency

The coordinate-wise mean of a point set is the centroid , which solves the same variational problem in the plane (or higher-dimensional Euclidean space ) that the familiar average solves on the real line — that is, the centroid has the smallest possible average squared distance to all points in the set.

## Measures of spatial dispersion

Dispersion captures the degree to which points in a point set are separated from each other. For most applications, spatial dispersion should be quantified in a way that is invariant to rotations and reflections. Several simple measures of spatial dispersion for a point set can be defined using the covariance matrix of the coordinates of the points. The trace , the determinant , and the largest eigenvalue of the covariance matrix can be used as measures of spatial dispersion.

A measure of spatial dispersion that is not based on the covariance matrix is the average distance between nearest neighbors.

## Measures of spatial homogeneity

A homogeneous set of points in the plane is a set that is distributed such that approximately the same number of points occurs in any circular region of a given area. A set of points that lacks homogeneity may be spatially clustered at a certain spatial scale . A simple probability model for spatially homogeneous points is the Poisson process in the plane with constant intensity function.

### Ripley's K and L functions

Ripley's K and L functions introduced by Brian D. Ripley are closely related descriptive statistics for detecting deviations from spatial homogeneity. The K function (technically its sample-based estimate) is defined as

${\widehat {K}}(t)=\lambda ^{-1}\sum _{i\neq j}{\frac {I(d_{ij}<t)}{n}},$

where d ij is the Euclidean distance between the i th and j th points in a data set of n points, t is the search radius, λ is the average density of points (generally estimated as n / A , where A is the area of the region containing all points) and I is the indicator function (i.e. 1 if its operand is true, 0 otherwise). In 2 dimensions, if the points are approximately homogeneous, ${\widehat {K}}(t)$ should be approximately equal to π t 2 .

For data analysis, the variance stabilized Ripley K function called the L function is generally used. The sample version of the L function is defined as

${\widehat {L}}(t)=\left({\frac {{\widehat {K}}(t)}{\pi }}\right)^{1/2}.$

For approximately homogeneous data, the L function has expected value t and its variance is approximately constant in t . A common plot is a graph of $t-{\widehat {L}}(t)$ against t , which will approximately follow the horizontal zero-axis with constant dispersion if the data follow a homogeneous Poisson process.

Using Ripley's K function it can be determined whether points have a random, dispersed or clustered distribution pattern at a certain scale.
