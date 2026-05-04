# ENG
# Customer Segmentation Using K-Means Clustering

This project aims to cluster customers based on transaction behavior using the **K-Means Clustering** method. This project demonstrates the capabilities of Data Scientists in unsupervised learning, customer analysis, customer segmentation, and marketing strategy recommendations.

## Business Problem

Companies have many customers with different transaction behaviors. Customer segmentation is necessary to better target marketing strategies, loyalty programs, retention campaigns, and promotions.

## Dataset

The datasets in the `data/` folder are synthetic sample data for portfolio purposes. They can be replaced with real transaction data.

Fitur utama:
- `recency_days`
- `frequency`
- `monetary_value`
- `tenure_month`
- `visits_per_month`

## Methodology

1. Data understanding
2. Data cleaning
3. Exploratory Data Analysis
4. Feature scaling
5. Elbow method
6. K-Means Clustering
7. Cluster profiling
8. Business recommendation

## Segment Interpretation

Example of segmentation interpretation:

| Segment | Characteristics | Recommendations |
|---|---|---|
| High Value Customer | Frequent transactions, high monetary value, low recency | Loyalty programs and exclusive offers |
| Potential Customer | Moderate transactions and potential for growth | Upselling and personalized campaigns |
| Low Engagement Customer | Infrequent transactions and low monetary value | Reactivation campaigns |
| At Risk Customer | Previously active but high recency | Retention programs and win-back campaigns |

## Project Structure

```text
customer-segmentation-clustering/
├── data/
│   └── customer_transaction.csv
├── notebook/
│   └── customer_segmentation.ipynb
├── src/
│   └── run_segmentation.py
├── model/
│   └── customer_segmentation_model.joblib
├── images/
│   ├── elbow_method.png
│   ├── customer_segment.png
│   └── cluster_profile.csv
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## How to Run

```bash
pip install -r requirements.txt
python src/run_segmentation.py
```

Atau buka notebook:

```bash
jupyter notebook notebook/customer_segmentation.ipynb
```

## Portfolio Summary for CV

Developed customer segmentation analysis using RFM-style behavioral features and K-Means Clustering to classify customers into business segments. The project provides actionable insights for targeted marketing, loyalty programs, and customer retention campaigns.








```=====================================================================================================================================```






# INA

# Customer Segmentation Using K-Means Clustering

Project ini bertujuan untuk mengelompokkan pelanggan berdasarkan perilaku transaksi menggunakan metode **K-Means Clustering**. Project ini menunjukkan kemampuan Data Scientist dalam unsupervised learning, customer analytics, segmentasi pelanggan, dan rekomendasi strategi marketing.

## Business Problem

Perusahaan memiliki banyak pelanggan dengan perilaku transaksi yang berbeda. Segmentasi pelanggan diperlukan agar strategi marketing, loyalty program, campaign retention, dan promosi dapat lebih tepat sasaran.

## Dataset

Dataset pada folder `data/` adalah **synthetic sample data** untuk kebutuhan portofolio. Dataset dapat diganti dengan data transaksi real.

Fitur utama:
- `recency_days`
- `frequency`
- `monetary_value`
- `tenure_month`
- `visits_per_month`

## Methodology

1. Data understanding
2. Data cleaning
3. Exploratory Data Analysis
4. Feature scaling
5. Elbow method
6. K-Means Clustering
7. Cluster profiling
8. Business recommendation

## Segment Interpretation

Contoh interpretasi segmentasi:

| Segment | Karakteristik | Rekomendasi |
|---|---|---|
| High Value Customer | Sering transaksi, monetary tinggi, recency rendah | Loyalty program dan exclusive offer |
| Potential Customer | Transaksi sedang dan potensi naik | Upselling dan personalized campaign |
| Low Engagement Customer | Jarang transaksi dan monetary rendah | Reactivation campaign |
| At Risk Customer | Pernah aktif tetapi recency tinggi | Retention program dan win-back campaign |

## Project Structure

```text
customer-segmentation-clustering/
├── data/
│   └── customer_transaction.csv
├── notebook/
│   └── customer_segmentation.ipynb
├── src/
│   └── run_segmentation.py
├── model/
│   └── customer_segmentation_model.joblib
├── images/
│   ├── elbow_method.png
│   ├── customer_segment.png
│   └── cluster_profile.csv
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## How to Run

```bash
pip install -r requirements.txt
python src/run_segmentation.py
```

Atau buka notebook:

```bash
jupyter notebook notebook/customer_segmentation.ipynb
```

## Portfolio Summary for CV

Developed customer segmentation analysis using RFM-style behavioral features and K-Means Clustering to classify customers into business segments. The project provides actionable insights for targeted marketing, loyalty programs, and customer retention campaigns.
