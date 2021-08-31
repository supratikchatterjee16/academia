# Data Mining

Data Mining is the process of extracting valid, useful, unknown and comprehensible information from data and using it to make proactive knowledge-driven business decisions. Data mining uses statistical procedures to find unexpected patterns in data and identifies associations between variables.

## Association Learning

Association learning is the type of data mining that drives the recommendation engines in major sites like Amazon and Netflix. This would let you know that customers who bought a particular item also bought another item.

## Cluster Detection

Cluster detection is for identifying specific clusters or sub-categories of data.

The purchasing habits of hobbyists like gardeners, artists and model builders would look quite different. By analyzing the purchasing behavior using clustering algorithms, one can detect the various subgroups within the dataset.

## Regression/Prediction

It is a common practice for businesses to use regression to predict stock prices, currency exchange rates, sales, productivity gains and so on. For example, a company might use regression to get insights on how the expenses in past advertising have impacted the sales. Here, the dependent variable is sales and the independent variable is advertising expenditures, number of sales reps and the commission paid.


data -> target data -> preprocessed data -> transformed data -> patterns -> knowledge

data to target data is selection.
pre-processing involves outliers and remove or process it better and imputation or interpolation
transformation involves normalization  and correlation(remove high correlations)
patterns are found through classification, using multiple algorithms.
knowledge using patterns to interpret knowledge

## Knowledge Discovery Process

Now that you have an idea of how data is processed to create knowledge, let's learn about various stages of Knowledge Discovery Process:
```
Problem Definition -> Data Preparation -> Data Mining -> Data Analysis -> Knowledge Assimilation
```

The problem **definition stage** is the initial phase of a data mining project, and it focuses on understanding the project objectives, requirements and defining the data mining problem. Based on this, you can identify the data requirement and models.

**Data Preparation** involves three key activities and requires more than 70% of the total data mining effort.

1. 'Data Selection': We identify the sources of information select a subset of data required for analysis.
2. 'Data Pre-processing': We join data from various tables and resolve issues such as data conflicts, outliers, and missing data.
3. 'Data Transformation': We use conversions and combinations to generate new data fields like ratios and discretized continuous values.

In this stage, **data mining**, we identify the algorithm and tools to be used. Then, we apply the algorithm on the sample data set (also known as training data) and tune the control parameters of the algorithm till we get a satisfying result. Later, we validate the model by running the algorithm against the actual data (also known as test data).

In **data analysis**, we evaluate the mined patterns with respect to the defined goals. We interpret the Data Mining output – in the form of rules or patterns to find new and potentially useful knowledge. This is the Holy Grail of the Knowledge Discovery!

In **knowledge assimilation**, we implement the business insights derived from the Data Mining process in the organization’s system for further action. The knowledge becomes active, which means that we can make changes to the system, and measure the impact of the changes. The success of this step determines how effective the Knowledge Discovery process is.

## Data Mining team

Let's understand the typical team composition required for Data Mining projects. These projects require people with not just great minds but those who have a great eye for data. A Data Mining team typically involves :

* Domain Expert
* Database Administrator
* Statistician
* Mining Specialist

In a Data Mining projects, Data Miners play a central role in establishing relationships with Domain Experts for business guidance on their results, with DBAs for access to the data required for their activities and with Statisticians for validating analysis and interpreting statistical outputs.

KDD, SEMMA and CRISP-DM are methods for data mining.

## Classification

The classification technique is based on machine learning. Here, we classify each item in a dataset into one of the predefined sets of classes or groups. The classification methods incorporate mathematical techniques such as statistics, neural networks, decision trees and linear programming.

We build **decision boundaries** using this.

We use KNN, Naive Bayes and Random Forest.

## Regression Analysis

Regression is a predictive modeling technique. It explores the relationship between a dependent variable - which is referred to as a target and an independent variable(s) - which is referred to as the predictor. We use regression technique for forecasting, time series modeling and finding the causal effect relationship between the variables.

What happens to 'y' with change in 'x'.

Y = b0 + x.b1

## Decision Trees

Decision Tree is one of the widely used and easy-to-understand techniques. The root of the decision tree is a condition or a question which has several answers. Each answer points to a set of questions or conditions that help in determining the data that can help make the final decision.

Methods available here are Gini, Entropy, Chi-square, Reduction of variance

## Neural Networks

Neural Network is well suited for identifying patterns and forecasting. It is a set of connected input/output units where each connection has a weight associated. In the learning phase, for the network to predict the class of the input tuples, it learns by adjusting weights.

Uses backpropagation, i.e. weight readjustment based on difference produced between the inputs and the heuristics.

## Clustering

Clustering is a data mining technique that identifies a cluster of objects having similar characteristics. At a simple level, clustering uses one or more attributes as the basis for identifying a cluster of correlating results.

One hot encoding : turn categorical data to numeric.

1. Centroid based clustering : K-Means with shortest distance algorithm
2. Connectivity based clustering : Clusters groups of items into one, in a hierarchical fashion. Can be bottom-up or top-down
3. Distribution based clustering : Expectation maximization
4. Density based clustering : Area of dense data point.

Elbow Method.

## Association Rule Mining

Association Rule Mining is one of the best-known data mining techniques. Here, we discover a pattern based on the relationship between items in the same transaction. In market basket analysis, we use this association technique to identify products that customers frequently purchase together.


## Classification of Data Mining problems

1. Classification : Which class?
2. Regression : How much?
3. Similarity Matching
4. Clustering
5. Co-occurrence grouping  : Association Mining, Market Basket Analysis
6. Profiling : Behaviour description.
7. Link prediction : predict missing connections between entities
8. Data reduction
9. Casual Modeling : Modelling cause of an event?
