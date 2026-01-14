
# customer_behaviour_analysis.py

import pandas as pd
import numpy as np

# Sample structured workflow based on dashboard insights

def customer_segmentation(data):
    """Segment customers based on purchase value"""
    data['segment'] = pd.cut(
        data['purchase_amount'],
        bins=[0, 500, 2000, np.inf],
        labels=['Occasional', 'Growth Potential', 'Premium']
    )
    return data

def churn_risk(data):
    """Identify high churn risk customers""

    data['churn_risk'] = np.where(data['days_inactive'] > 14, 'High', 'Low')
    return data

def main():
    # Placeholder dataset
    data = pd.DataFrame({
        'customer_id': range(1, 11),
        'purchase_amount': [200, 800, 1200, 3000, 450, 900, 2500, 150, 700, 1800],
        'days_inactive': [5, 20, 12, 30, 7, 18, 3, 40, 9, 15]
    })

    data = customer_segmentation(data)
    data = churn_risk(data)

    print(data)

if __name__ == "__main__":
    main()
