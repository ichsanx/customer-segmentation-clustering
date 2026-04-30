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
