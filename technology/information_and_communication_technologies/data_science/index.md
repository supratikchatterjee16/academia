# Data Science

Data science is the science of analysing and extracting information from large sets of data, which typically combines elements of statistics, maths, computing, and other subjects.

It is an interdisciplinary field focused on extracting knowledge and insights from structured and unstructured data using scientific methods, processes, algorithms, and systems. It integrates elements from statistics, computer science, mathematics, and domain expertise to support decision-making, predictions, and automation.

This topic, due to the broad nature of it, comprises of topics containing elements of Information and Communication TEchnology and Mathematics and Statistics. The topics covered in the section here are:

- Data Extraction/Mining
- Data Cleaning & Pre-processing
- Data Loading & Storage
- Data Visualization

The following topics will be classified under statistics:

- [Statistical Analysis](/technology/statistics/data_analysis/index.md)
- [Predictive Modelling](/technology/statistics/statistical_modelling/index.md)
- [Experimentation and testing](/technology/statistics/data_analysis/index.md)

Data Science follows a common process in industries, and as such, it is recommended to use the same, for preparing workloads of this domain:

1. **Problem Definition**

   * Identify the objective: *What question needs to be answered?*
   * Determine constraints, success criteria, and required outputs.

2. **Data Acquisition (Data Extraction)**

   * Collect data from sources such as:

     * Databases (SQL/NoSQL)
     * APIs or web services
     * Logs, sensors, IoT streams
     * Web scraping and open datasets

3. **Data Cleaning**

   * Fix or remove incorrect, missing, or inconsistent data:

     * Handle missing values
     * Correct data types
     * Remove duplicates or anomalies
     * Normalize formats

4. **Data Pre-Processing / Transformation**

   * Prepare data for analysis or modeling:

     * Feature engineering
     * Scaling / normalization
     * Encoding categorical variables
     * Time-series formatting
     * Text vectorization

5. **Data Loading / Storage**

   * Store processed data in usable structures:

     * Data warehouse / lake
     * Analysis-ready tables
     * Feature stores for ML pipelines

6. **Exploratory Data Analysis (EDA)**

   * Understand the data before modeling:

     * Statistical summaries
     * Data visualization
     * Detect trends, relationships, outliers

7. **Modeling / Analysis / Machine Learning**

   * Choose and apply methods based on the problem:

     * Regression / classification / clustering
     * Predictive models
     * Statistical inference
     * Simulation, forecasting

8. **Model Evaluation & Testing**

   * Verify reliability and performance:

     * Train-test splits
     * Cross-validation
     * Performance metrics (accuracy, F1, MSE, etc.)
     * A/B testing if applied to real systems

9. **Interpretation & Insights**

   * Translate results into meaningful conclusions.
   * Communicate findings to stakeholders clearly and visually.

10. **Deployment & Monitoring**

* Put the model or solution into production:

  * APIs, dashboards, automated workflows
  * Continuous monitoring for drift, decay, and reliability

11. **Iteration**

* Data Science is *cyclical*, not linear.
* New data or business changes may require re-training or re-design.

Each of the sections will be expanded upon in their own subsequent sections.

## **Datasets to practise data science methods**

- [NYC Taxi & Limousine Commision(requires PARQUET*)](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [IMDB Movies Dataset(TSV format)](https://datasets.imdbws.com/)
- [UCI ML Repository Datasets](https://archive.ics.uci.edu/) with the following recommended datasets:
    - Adult income
    - Wine Quality
    - Bike Sharing Demand
- [World Bank Development Indicators](https://datacatalog.worldbank.org/)
- [Kaggle Public Datasets](https://www.kaggle.com/datasets), with the following recommended datasets:
    - Netflix Viewing / Movie Ratings datasets
    - Superstore Sales Orders dataset
    - Titanic survival dataset
    - Air Quality + Weather datasets
- [NOAA Global Historical Weather Data](https://www.ncei.noaa.gov/products/land-based-station-data)
- [M5 Forecasting Dataset(Retail)](https://www.kaggle.com/competitions/m5-forecasting-accuracy/data)

*Apache PARQUET is a columnar DB store to be used with the Apache Hadoop ecosystem, Pandas can be used to read this dataset

## **Programming & Software Tools**

* **Languages**: Python, R (sometimes SQL, Scala, Julia)
* **Libraries**: pandas, NumPy, scikit-learn, TensorFlow, PyTorch, matplotlib/seaborn
* **Version control**: Git
* **Development tools**: Jupyter Notebooks, VS Code