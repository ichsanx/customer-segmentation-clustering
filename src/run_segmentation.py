import pandas as pd
import joblib
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "customer_transaction.csv"
MODEL_PATH = ROOT / "model" / "customer_segmentation_model.joblib"
PROFILE_PATH = ROOT / "images" / "cluster_profile.csv"

def main():
    df = pd.read_csv(DATA_PATH)

    features = [
        "recency_days",
        "frequency",
        "monetary_value",
        "tenure_month",
        "visits_per_month",
    ]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])

    model = KMeans(n_clusters=4, random_state=42, n_init=10)
    df["cluster"] = model.fit_predict(X_scaled)

    profile = df.groupby("cluster")[features].mean().round(2)
    print("Cluster Profile:")
    print(profile)

    MODEL_PATH.parent.mkdir(exist_ok=True)
    PROFILE_PATH.parent.mkdir(exist_ok=True)

    joblib.dump({"scaler": scaler, "model": model, "features": features}, MODEL_PATH)
    profile.to_csv(PROFILE_PATH)

    print(f"\nModel saved to: {MODEL_PATH}")
    print(f"Cluster profile saved to: {PROFILE_PATH}")

if __name__ == "__main__":
    main()
