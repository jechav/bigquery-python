# Python Client

Before running, install python3, pip, and jupyter on your computer.

How to run the notebook:

1. Setup python virtual environment:

```bash
virtualenv venv
source venv/bin/activate
# pip-compile # use this if you want to update versions
pip install -r requirements.txt
```

2. Setup credentials to your GCP project

Follow the steps here to get the .json with credentials:
https://cloud.google.com/bigquery/docs/reference/libraries
Then:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="here/comes/the/path/to/json/file.json"
```

3. Setup ipython kernel:

```bash
pip install ipykernel
python -m ipykernel install --user --name=venv-creating-tables
```

4. Run jupyter:

```bash
jupyter notebook
```
