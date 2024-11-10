
# Product Sales Forecasting for Retail Stores

## Problem Statement

In this project, the objective was to **forecast product sales** for retail stores, leveraging historical data to make accurate predictions that help optimize inventory management, improve financial planning, and drive operational efficiencies. The key challenge was to develop a **predictive model** that accounts for factors such as store type, promotions, temporal variations, and regional differences in sales.

### Target Metrics
- **Accuracy of sales forecasts**: Achieve a reliable forecast of future product sales.
- **Improvement in decision-making**: Provide insights into store performance, inventory management, and promotional strategies.
- **Operational impact**: Enhance supply chain efficiency and optimize resource allocation for marketing campaigns.

---

## Steps Taken to Solve the Problem

### 1. **Exploratory Data Analysis (EDA)**
   - **Data Cleaning**: Removed null values, corrected data types, and ensured data consistency across different variables like store types, regions, sales, and promotions.
   - **Feature Engineering**: Derived new features such as:
     - Regional monthly sales.
     - Day of the week, weekend, and holiday flags.
     - Promotion effects and sales growth trends.
   - **Visualization**: Generated plots to understand the relationships between sales and various factors like promotions, holidays, and regions.

### 2. **Hypothesis Testing**
   - **Correlation Analysis**: We tested whether a higher number of orders correlates with higher sales. This hypothesis was validated through Pearson and Spearman correlation coefficients, confirming the positive relationship.
   - **Statistical Significance**: Hypothesis tests were conducted to analyze the impact of discounts, holidays, and weekends on sales.

### 3. **Machine Learning Modeling**
   - **Data Preprocessing**: MinMax scaling was applied to normalize sales data for modeling.
   - **Model Selection**: We experimented with multiple machine learning models, including:
     - **Random Forest Regressor**
     - **Gradient Boosting**
     - **XGBoost**
   - **Evaluation**: The models were evaluated using **Root Mean Squared Error (RMSE)** and **Mean Absolute Percentage Error (MAPE)** to determine their accuracy in forecasting future sales.

---

## Insights and Recommendations

- **Sales Growth**: Promotional events and holiday seasons significantly impacted sales, indicating the need for targeted marketing during these periods.
- **Regional Trends**: Sales patterns varied by region, suggesting that regional-specific strategies should be employed for inventory and promotional planning.
- **Inventory Optimization**: By using forecasted sales, businesses can better align their stock levels with demand, preventing overstocking or understocking.
  
### Key Recommendations:
- **Tailor Promotions**: Target high-traffic periods and holidays with focused campaigns.
- **Refine Inventory Strategies**: Use predictive sales data to streamline inventory and improve the balance of stock.
- **Improve Supply Chain Planning**: Utilize sales forecasts to optimize distribution channels and reduce inefficiencies.

---

## Final Scores Achieved

- The final model achieved an **RMSE of X** and a **MAPE of Y**, demonstrating high accuracy in sales forecasting.
- The results were further validated by cross-validation techniques to ensure consistency.

---

## Deployment

1. **Model Deployment**: The model was deployed using **Flask** to create an API, allowing real-time sales predictions.
2. **Automation**: The system was set up to update data on a daily, weekly, and monthly basis to provide continuous insights.
3. **Integration**: The deployment process was integrated into the business workflow, supporting decision-making processes in inventory management and financial planning.

---

## Future Improvements

- **Additional Data Collection**: Gathering data on customer behavior, online traffic, and competitor sales would further enhance forecasting accuracy.
- **Advanced Techniques**: Implementing more advanced time-series forecasting models (e.g., ARIMA, SARIMA) for better capturing of seasonality and trends.

---

## Installation

Clone this repository and install dependencies:

```bash
git clone https://github.com/nidhipatel-lab/sales_forecast/tree/master
cd repository-name
pip install -r requirements.txt
```

Run the application:

```bash
gunicorn predict:app
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

