# Data Science

Data science is the science of analysing and extracting information from large sets of data, which typically combines elements of statistics, maths, computing, and other subjects.

It is an interdisciplinary field focused on extracting knowledge and insights from structured and unstructured data using scientific methods, processes, algorithms, and systems. It integrates elements from statistics, computer science, mathematics, and domain expertise to support decision-making, predictions, and automation.

This topic, due to the broad nature of it, comprises of topics containing elements of Information and Communication TEchnology and Mathematics and Statistics. The topics covered in the section here are:

- [Problem Definition](./problem_definition.md)
- [Data Extraction/Mining](./data_mining/index.md)
- [Data Cleaning & Pre-processing](./data_cleaning_and_preprocessing/index.md)
- [Data Loading & Storage](./data_loading_and_storage/index.md)
- [Data Visualization](./data_visualization/index.md)

The following topics will be discussed under statistics:

- [Statistical Analysis](/technology/statistics/statistical_analysis/index.md)
- [Predictive Modelling](/technology/statistics/statistical_modelling/index.md)
- [Experimentation and testing](/technology/statistics/statistical_testing/index.md)

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

## **Datasets to practice data science methods**

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

## **APIs to practice on**

### **Finance & Economics**

| API                                          | Data Provided                                | Notes                                         |
| -------------------------------------------- | -------------------------------------------- | --------------------------------------------- |
| **Yahoo Finance API (via yfinance library)** | Stocks, ETFs, currencies                     | Free, no API key required if using `yfinance` |
| **Alpha Vantage**                            | Real-time + historical stocks, crypto, forex | Free tier with rate limits (5 calls/min)      |
| **FRED (Federal Reserve)**                   | Macroeconomic indicators (GDP, CPI, rates)   | Fully free, requires simple key               |
| **Finnhub.io**                               | Stocks, sentiment analysis, crypto           | Generous free tier                            |

---

### **Weather / Environment**

| API                       | Data Provided                  | Notes                                               |
| ------------------------- | ------------------------------ | --------------------------------------------------- |
| **OpenWeatherMap**        | Weather forecasts & history    | Free tier w/ API key; limited calls/day             |
| **NOAA Climate Data API** | Historical climate and weather | Fully free, but some datasets require request forms |
| **AirNow API**            | Air quality index (AQI) data   | Free registration                                   |

---

### **Maps / Geospatial / Places**

| API                     | Data Provided                        | Notes                          |
| ----------------------- | ------------------------------------ | ------------------------------ |
| **OpenStreetMap (OSM)** | Roads, buildings, geodata            | Free, use through Overpass API |
| **GeoNames API**        | Geographic names & location metadata | Free with registration         |
| **USGS Earthquake API** | Global earthquake data in real time  | No key required                |

---

### **Open Government / Demographics**

| API                          | Data Provided                    | Notes                                      |
| ---------------------------- | -------------------------------- | ------------------------------------------ |
| **U.S. Census API**          | Demographic & socioeconomic data | Free, requires registration                |
| **UN Data API**              | Population, development stats    | Mostly open datasets downloadable via JSON |
| **World Bank Open Data API** | Global development indicators    | Completely free, no key required           |

---

### **Social Media / Text / NLP**

| API                          | Data Provided                    | Notes                           |
| ---------------------------- | -------------------------------- | ------------------------------- |
| **Reddit API**               | Posts & comments                 | Requires a free API key         |
| **Wikipedia API**            | Articles, summaries, pageviews   | No key required                 |
| **NewsAPI**                  | News headlines & metadata        | Free tier limited, no full text |
| **HuggingFace Datasets API** | NLP datasets programmatic access | Fully free                      |

---

### **Health / Science / Research**

| API                        | Data Provided             | Notes                           |
| -------------------------- | ------------------------- | ------------------------------- |
| **PubMed Entrez API**      | Scientific paper metadata | No key needed (but recommended) |
| **OpenFDA**                | Drug & adverse event data | Completely free                 |
| **ClinicalTrials.gov API** | Medical trial data        | Open and unrestricted           |

---

### **E-Commerce / Products**

| API                   | Data Provided                          | Notes                       |
| --------------------- | -------------------------------------- | --------------------------- |
| **OpenFoodFacts API** | Ingredients, nutrition labels          | Great for classification/ML |
| **Fake Store API**    | Product + cart data for mock ecommerce | Good for beginner ML demos  |

---

### **Fun & Miscellaneous**

| API                       | Data Provided                  | Notes                   |
| ------------------------- | ------------------------------ | ----------------------- |
| **PokéAPI**               | Pokémon stats                  | Fully free & fun to use |
| **Star Wars API (SWAPI)** | Characters, planets, starships | No key needed           |
| **Open Trivia Database**  | Trivia Q&A                     | No key required         |

---

## **Programming & Software Tools**

* **Languages**: Python, R (sometimes SQL, Scala, Julia)
* **Libraries**: pandas, NumPy, scikit-learn, TensorFlow, PyTorch, matplotlib/seaborn
* **Version control**: Git
* **Development tools**: Jupyter Notebooks, VS Code