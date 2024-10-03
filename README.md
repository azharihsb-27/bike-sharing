SETUP ENVIRONMENT ANACONDA
- conda create --name subs-ds python=3.12
- conda activate subs-ds
- pip install -r requirements.txt

RUN STEAMLIT
- streamlit run dashboard.py
