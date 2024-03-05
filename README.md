# Setup Environment
conda create --name main-ds python=3.11
conda activate main-ds
pip install numpy pandas matplotlib seaborn streamlit 

# Run Streamlit App
streamlit run dashboard.py
