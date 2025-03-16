import streamlit as st
import importlib
import pkgutil
import DataPulse

# Improved dataset loader
def get_available_datasets():
    datasets = {}
    for _, module_name, _ in pkgutil.iter_modules(DataPulse.__path__):
        print(f"Loading module: {module_name}")
        try:
            module = importlib.import_module(f"DataPulse.{module_name}")
            if hasattr(module, 'generate_data'):
                datasets[module_name] = module
        except Exception as e:
            print(f"Error loading module {module_name}: {e}")
    print(f"Available datasets: {list(datasets.keys())}")
    return datasets

datasets = get_available_datasets()

# Streamlit UI
st.title("📊 DataPulse Dataset Generator")

dataset_name = st.selectbox("Select a dataset to generate:", list(datasets.keys()))

num_records = st.number_input("Enter number of records to generate:", min_value=1, max_value=500000, value=100)

if st.button("Generate Dataset"):
    dataset_module = datasets[dataset_name]
    df = dataset_module.generate_data(num_records)
    st.dataframe(df.head(10))

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Dataset", csv, f"{dataset_name}_data.csv", "text/csv")

st.success("Ready to generate datasets from DataPulse!")
