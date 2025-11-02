# Problem Definition

The first step in data science is to have a clear and concise problem definition to scope the task at hand.

The following table is a suggested framework to be used for the same:

| Section                    | Example Entry                                                     |
| -------------------------- | ----------------------------------------------------------------- |
| **Context**                | Retail chain struggles with product stockouts causing lost sales. |
| **Business Objective**     | Reduce lost sales by improving inventory planning.                |
| **Data Science Objective** | Forecast daily product demand per store for next 14 days.         |
| **Key Questions**          | What is expected sales volume per product-store-day?              |
| **Success Metric**         | MAPE ≤ 15% for top 100 products.                                  |
| **Constraints**            | Must run nightly and integrate with existing PostgreSQL system.   |
| **Data Needed**            | Sales history, calendar events, weather, promotions.              |
| **Deliverables**           | Forecast table + visualization dashboard in BI tool.              |

This can be augmented by using a questions-to-datamap mapping in the following way:

| Key Question                             | Data Needed                                 | Data Source        | Notes (Quality, Processing, Granularity) |
| ---------------------------------------- | ------------------------------------------- | ------------------ | ---------------------------------------- |
| What will demand be per store next week? | historical sales by store/date              | sales database     | aggregate to daily level                 |
| Does weather affect demand?              | temperature, rainfall                       | weather API        | join on geo + date                       |
| Do promotions change buying patterns?    | promo flags, discount %, marketing schedule | marketing calendar | need categorical encoding                |


When preparing the problem definition, it is necessary to identify the **analysis performance metrics** to start with. The following provides an example of the same:

| Analysis Type      | Example Metrics                  | Interpretation Focus                               |
| ------------------ | -------------------------------- | -------------------------------------------------- |
| **Forecasting**    | MAE, RMSE, MAPE                  | *Forecast error relative to scale*                 |
| **Regression**     | R², RMSE, MAE                    | *Variance explained & error magnitude*             |
| **Classification** | F1 score, ROC AUC, Accuracy      | *Balance error vs. precision/recall trade-offs*    |
| **Clustering**     | Silhouette Score, Davies-Bouldin | *How well data points cluster*                     |
| **EDA Insights**   | Summary stats, distributions     | *Whether patterns are meaningful and reproducible* |

The **conclusion stability** also needs to be tested as an extension. To choose the method for it, we have the following:

| Stress Test                                | How                                         |
| ------------------------------------------ | ------------------------------------------- |
| Train/Test or Cross-validation consistency | k-fold or rolling window validation         |
| Sensitivity analysis                       | Vary assumptions or thresholds              |
| Stability across subgroups                 | Performance by region/customer/segment/time |

A proper validation can be done using the following checkbox:

```text
[ ] The analysis answers the original objective.
[ ] Data used is appropriate and clean, with no leakage.
[ ] Performance was assessed using correct evaluation metrics.
[ ] A baseline comparison was included.
[ ] Model/analysis is robust across tests and subsets.
[ ] Results are interpretable to stakeholders.
[ ] Actionable recommendations are clearly stated.
[ ] Ethical and contextual impacts were considered.
```

The thereotical aspects, such as the analysis performance metrics, can be found in the statistics section.