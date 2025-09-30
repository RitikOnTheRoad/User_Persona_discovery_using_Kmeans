**Data-Driven Behavioral Segmentation with K-Means**
An end-to-end machine learning project to segment mobile users into distinct behavioral archetypes using unsupervised clustering.

Overview
This project demonstrates a complete workflow for user segmentation using synthetic phone activity data. The primary goal is to move from raw quantitative metrics (like screen time, steps, and app usage) to actionable, qualitative user personas (e.g., 'Workaholic', 'Active User') without any pre-existing labels. The analysis involves robust data preparation, outlier detection, K-Means clustering, and a deep qualitative interpretation of the model's results.

Project Workflow
The project follows four key steps:

Data Preparation & Cleaning: The process begins with a raw user activity dataset. A crucial cleaning phase is performed where outliers are systematically identified and removed using the Isolation Forest algorithm to ensure the quality and integrity of the data before modeling.

Model Training & Evaluation: The cleaned and scaled data is fed into a K-Means clustering algorithm. The optimal number of clusters (K=4) was determined using the Elbow Method. The final model's effectiveness was validated with a Silhouette Score of 0.43, indicating a reasonable and well-defined cluster structure.

Persona Discovery: A deep qualitative analysis of the resulting cluster centers is conducted. Each numerical profile is translated into a descriptive and meaningful user persona, such as the "Workaholic," the "Entertainment Junkie," and the "Active User."

Visualization & Interpretation: The unique characteristics of each discovered persona are visualized using radar charts. This provides a clear, comparative view of their distinct daily routines and behavioral patterns, making the results easy to understand and communicate.

Technologies Used
Python

Pandas: For data manipulation and analysis.

NumPy: For numerical operations.

Scikit-learn: For implementing KMeans, IsolationForest, StandardScaler, and silhouette_score.

Matplotlib & Seaborn: For data visualization, including the Elbow Method plot and radar charts.
