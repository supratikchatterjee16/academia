# Data Visualization

Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data. Additionally, it provides an excellent way for employees or business owners to present data to non-technical audiences without confusion.

This enables sharing of information, visualizing patterns and relationships, and sometimes interactively exploring opportunities.

However, the visuals themselves, can cause biased inference.

There are over 200+ charts that can be used([Jump to section](#comprehensive-taxonomy-of-charts)). However, it is recommended to read through the principles prior to it.

## Guiding Principles for Data Visualizations

### Edward Tufte Principles

| **Principle**                                      | **Description**                                                                                                | **Application Area (Examples)**                                          |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Show the Data**                                  | The primary focus of a visualization should be the data itself—not decoration, branding, or interface clutter. | Minimal charts, clear regions in dashboards, removing decorative frames. |
| **Maximize Data-Ink Ratio**                        | Use only the ink needed to represent data; reduce or remove non-essential marks.                               | Light gridlines, no chart borders, thin axis lines, direct value labels. |
| **Erase Non-Data Ink**                             | Remove elements that do not communicate information.                                                           | Delete drop shadows, 3D effects, unnecessary legends.                    |
| **Erase Redundant Data Ink**                       | Avoid repeating the same value visually more than needed.                                                      | Don’t label every bar segment if axis already conveys it.                |
| **Avoid Chartjunk**                                | Avoid decorative forms, textures, and graphics that distract from interpretation.                              | Avoid 3D pie charts, clipart, patterns, animations.                      |
| **Data Density** / **High Data-to-Ink Density**    | Present data in a compact form that allows rich comparison without clutter.                                    | Heatmaps, dense line charts, tables with sparklines.                     |
| **Small Multiples**                                | Use multiple small, consistent charts to compare data across categories or time.                               | Side-by-side mini charts for regions, cohorts, products.                 |
| **Sparklines**                                     | Word-sized graphics that show trends inline with text.                                                         | Financial summaries, inline KPI trend indicators.                        |
| **Micro / Macro Readings**                         | Enable both overview and detailed inspection in the same visual.                                               | Zoomable charts, layered maps, dashboards with drill-down.               |
| **Layering & Separation**                          | Use visual hierarchy to distinguish primary from supporting content.                                           | Bold primary data line + subtle gridlines + faint context curves.        |
| **Color Should Support Structure, not Decoration** | Color is for emphasis, grouping, and hierarchy, not decoration.                                                | Use one accent color for key variable; use neutrals for context.         |
| **Use Direct Labeling**                            | Label data directly rather than relying on legends, reducing cognitive load.                                   | Labels beside lines instead of legend boxes.                             |
| **Integrate Text, Data, and Graphics**             | Words should explain the data and appear near what they describe.                                              | Annotations placed at the exact point of interest on charts.             |
| **Documentation & Context**                        | Always show scale, units, sourcing, and relevant notes to avoid misinterpretation.                             | Footnotes, axis units, baseline references, data source shown.           |
| **Tell the Truth (Avoid Distortion)**              | Maintain ratio between visual distances and the underlying numerical values.                                   | Avoid stretched axes, manipulated baselines, and misleading scaling.     |
| **Encourage Comparison**                           | Visualizations should make comparisons easy, because comparison is the core of reasoning with data.            | Same scales across charts, aligned baselines, side-by-side views.        |

### 8 Gestalt principles

| **Principle**                      | **Description**                                                                                            | **Application Area (Examples)**                                                          |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Proximity**                      | Elements that are close to one another are perceived as belonging together or forming a group.             | UI layout, grouping related menu items, dashboard widget organization.                   |
| **Similarity**                     | Items that share similar attributes (color, shape, size, texture) are perceived as part of the same group. | Icon consistency, data visualization (same colors for same categories), branding design. |
| **Continuity** (Good Continuation) | The eye follows continuous lines or patterns rather than abrupt changes.                                   | Navigation flows, timeline designs, line charts, form field alignment.                   |
| **Closure**                        | We tend to see complete shapes even when parts are missing. The mind fills gaps.                           | Logo design (e.g., WWF, IBM), simplified illustrations, wireframe iconography.           |
| **Figure–Ground**                  | We separate elements into a foreground (focused object) and a background.                                  | Hero sections, call-to-action emphasis, contrast-based layout design.                    |
| **Common Region**                  | Elements located within the same bounded area are perceived as grouped.                                    | Card components in UI, panels, containers, bordered group boxes.                         |
| **Common Fate**                    | Objects that move in the same direction are perceived as related.                                          | Loading animations, guided sequences, animated transitions, timelines.                   |
| **Symmetry & Order** (Prägnanz)    | People perceive designs in the simplest, most stable and symmetrical form possible.                        | Clean grid layouts, typography hierarchy, minimalist interface design.                   |

> Color Theory: Shape is less powerful than color.

## Data Visualization tools

1. TIBCO Spotfire
2. Trifecta
3. Qlik
4. Tableau
5. Microsoft Power BI
6. Alteryx
7. SAS
8. SAP
9. Sisense
10. Microstrategy
11. Salesforce
12. Datawatch
13. Zoomdata

D3.JS, R Charts (ggplot2 package), Pentaho, SAP Lumira, TIBCO Spotfire, QlikView, JasperSoft, and Microstrategy are some of the popularly used tools.

## Comprehensive Taxonomy of charts

The following are some of the charts types with their descriptions and common use cases, categorized based on purpose. It is recommend to first check the visuals online before using it. Links to examples will be provided wherever possible.

### **1. Comparison Charts**

Used to compare values across categories or groups.

| Chart Type                | Description                                            | Common Use Case                                              |
| ------------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| Bar Chart                 | Rectangles represent values across categories          | Compare population by region                                 | 
| Grouped Bar Chart         | Multiple bars per category                             | Compare male vs female across regions                        |
| Stacked Bar Chart         | Bars composed of segments                              | Show component breakdowns (e.g., age groups)                 |
| 100% Stacked Bar Chart    | Normalized stacked bar chart                           | Show proportional composition over categories                |
| Column Chart              | Vertical version of bar chart                          | Monthly trends or survey results                             |
| Dot Plot                  | Dots aligned to a scale                                | Compare values when precision matters                        |
| Lollipop Chart            | Bar → replaced with line + dot                         | Cleaner version of bar charts for presentations              |
| Slope Chart               | Lines connecting category values across two conditions | Before/after performance comparisons                         |
| Radar / Spider Chart      | Values plotted on radial axes                          | Compare profiles across dimensions (e.g., skill assessments) |
| Parallel Coordinates Plot | Multiple vertical axes comparing record attributes     | Multivariate pattern analysis                                |
| Butterfly / Tornado Chart | Two opposed bar charts                                 | Population pyramids; before/after comparisons                |

---

### **2. Distribution Charts**

Used to understand how values are spread.

| Chart Type           | Description                           | Use Case                                    |
| -------------------- | ------------------------------------- | ------------------------------------------- |
| Histogram            | Bars represent frequency across bins  | Age or income distribution                  |
| Box Plot             | Quartiles, median, and outliers shown | Comparing distributions across groups       |
| Violin Plot          | Density mirrored around axis          | Visualizing distribution shape more clearly |
| Density Plot (KDE)   | Smoothed histogram curve              | Explore continuous distribution shape       |
| Rug Plot             | Marks real data points along axis     | Supplementary distribution insight          |
| ECDF Plot            | Cumulative distribution visualization | Compare distributions precisely             |
| QQ Plot              | Plots quantile comparisons            | Test normality or distribution fit          |
| Ridgeline / Joy Plot | Stacked density plots                 | Compare multiple distributions visually     |

---

### **3. Time Series Charts**

Used when data changes over time.

| Chart Type              | Description                        | Use Case                                    |
| ----------------------- | ---------------------------------- | ------------------------------------------- |
| Line Chart              | Connects values over time          | Trends in population, economy, sales        |
| Multi-Series Line Chart | Several line charts in one         | Compare trends across groups                |
| Step Chart              | Changes at intervals shown clearly | Policy or stepwise changes                  |
| Area Chart              | Filled area under line             | Show cumulative or magnitude emphasis       |
| Stacked Area Chart      | Areas layered on one another       | Show contribution over time                 |
| Horizon Chart           | Compressed layered values          | High-density timeseries dashboards          |
| Sparkline               | Tiny inline trend line             | KPIs inside tables                          |
| Candlestick Chart       | OHLC values shown per time period  | Finance & trading analysis                  |
| Streamgraph             | Smooth stacked area chart          | Composition change over time in a fluid way |

---

### **4. Relationship (Correlation) Charts**

| Chart Type                  | Description                           | Use Case                                   |
| --------------------------- | ------------------------------------- | ------------------------------------------ |
| Scatter Plot                | Dots representing paired values       | Correlation analysis                       |
| Bubble Chart                | Third variable represented by size    | GDP vs Population vs Life Expectancy       |
| Scatterplot Matrix          | Matrix of scatterplots                | Explore correlations across many variables |
| Heatmap (Correlation)       | Colors indicate relationship strength | Feature selection in ML                    |
| Trendline / Regression Plot | Fitted relationship line              | Prediction or causality hinting            |
| Hexbin Plot                 | Density-based scatter alternative     | Large sample bivariate analysis            |

---

### **5. Hierarchical Charts**

| Chart Type     | Description                           | Use Case                                 |
| -------------- | ------------------------------------- | ---------------------------------------- |
| Tree Diagram   | Parent-child branching                | Organizational or biological hierarchies |
| Treemap        | Area-sized rectangles show proportion | Hard-drive storage or budget allocations |
| Sunburst Chart | Radial hierarchical display           | Multi-level category exploration         |
| Icicle Chart   | Layered hierarchical rectangles       | Navigating nested taxonomies             |
| Circle Packing | Circles inside circles by area        | Proportional hierarchy emphasis          |

---

### **6. Part-to-Whole Charts**

| Chart Type           | Description                                    | Use Case                            |
| -------------------- | ---------------------------------------------- | ----------------------------------- |
| Pie Chart            | Proportions of a whole                         | Very simple breakdowns              |
| Donut Chart          | Pie chart with center cut out                  | Cleaner than pie; easier labeling   |
| Stacked Bar / Column | Same as comparison category                    | When showing composition matters    |
| Waterfall Chart      | Shows additive positive/negative contributions | Financial breakdown (profit & loss) |
| Funnel Chart         | Progressive reduction                          | Sales pipeline stages               |
| Waffle Chart         | Grid of 100 squares to show %                  | Infographics                        |

---

### **7. Ranking Charts**

| Chart Type        | Description                     | Use Case                               |
| ----------------- | ------------------------------- | -------------------------------------- |
| Ordered Bar Chart | Bars sorted high→low            | Leaderboards                           |
| Bump Chart        | Rank movement over time         | Sports or market position changes      |
| Pareto Chart      | Sorted bars + cumulative % line | Identify most influential contributors |

---

### **8. Spatial / Mapping Charts**

| Chart Type                 | Description                  | Use Case                            |
| -------------------------- | ---------------------------- | ----------------------------------- |
| Choropleth Map             | Regions color-coded by value | Population density by region        |
| Cartogram                  | Regions distorted by value   | Political influence, market size    |
| Dot Density Map            | One dot = some units         | Geographic population distribution  |
| Heatmap Map (Spatial)      | Color gradient over area     | Temperature / density gradients     |
| Flow Map                   | Lines show movement          | Migration or trade routes           |
| 3D Terrain / Elevation Map | Surface mapped by height     | Geography, climate, geological data |

---

### **9. Network / Graph Charts**

| Chart Type           | Description                     | Use Case                                 |
| -------------------- | ------------------------------- | ---------------------------------------- |
| Node-Link Diagram    | Nodes connected by edges        | Social networks, internet topology       |
| Force-Directed Graph | Physics-based spacing           | Relationship clustering                  |
| Chord Diagram        | Circular relationship mapping   | Trade between countries                  |
| Sankey Diagram       | Flow magnitude connections      | Energy balances; process transitions     |
| Matrix Diagram       | Adjacency matrix representation | Relationship intensities without clutter |

---

### **10. Advanced / Analytical Charts**

| Chart Type                | Description                     | Use Case                    |
| ------------------------- | ------------------------------- | --------------------------- |
| Gantt Chart               | Task durations across time      | Project management          |
| Cohort Chart              | Behavior of groups over time    | Retention analysis          |
| Control Chart             | Process stability control       | Manufacturing QA            |
| Funnel / Conversion Chart | Stage drop-off                  | Product analytics           |
| Marimekko / Mosaic Plot   | Rectangle layout by proportions | Market segmentation         |
| Kaplan–Meier Curve        | Survival estimator              | Medical survival analysis   |
| Dendrogram                | Hierarchical cluster output     | Machine learning clustering |

