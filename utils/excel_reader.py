import pandas as pd

def get_runnable_test_ids():
    try:
        df = pd.read_excel("/Users/leonid/PycharmProjects/NookApp/data/test_data.xlsx")
        return df[df["Run"].str.lower() == "yes"]["TestID"].tolist()
    except Exception as e:
        print("Excel read failed:", e)
        return []  # fallback