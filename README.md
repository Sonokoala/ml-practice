# ml-practice

Machine learning and data analysis notebooks I wrote in 2024 while studying with the Tarantula study community.
Moved here from my branches (`feature/fujiwara_main` and `feature/fujiwara_sub`) of the community's shared practice repository.

## Contents

| Folder / file | Topic |
|---|---|
| `logistic regression annalysis/` | Logistic regression on a liver disease dataset |
| `randam_forest/ensemble_model2.ipynb` | Linear regression and ensemble models on the World Happiness Report 2023 |
| `NN/NN.ipynb` | Neural network and gradient boosting on ASX company financials |
| `thyroid_CNN.ipynb` | CNN image classification of thyroid ultrasound images |
| `Scraping_clustering.ipynb`, `scraiping/` | Web scraping, text processing and clustering |
| `VAR model.ipynb` | Vector autoregression (VAR) time series model |
| `time series data analysis/`, `ASX_stock.ipynb` | ASX stock price forecasting with yfinance, Prophet and others |
| `LSCM` | GRU model snippet for stock data |
| `#3 pre process/titanic_preprocess.py`, `titanic/` | Titanic dataset preprocessing |
| `Network_Infrastructure.gv`, `network_diagram.png` | Network infrastructure diagram (Graphviz) |

## Run with Docker

```
docker compose up -d --build
```

Open http://localhost:8888 for JupyterLab. The repository folder is mounted at `/work`, so changes you make in Jupyter are saved here.
JupyterLab runs without a token and listens on localhost only.

Stop it with:

```
docker compose down
```

The image includes Python 3.11, pandas, scikit-learn, statsmodels, XGBoost, LightGBM, CatBoost, Prophet, yfinance, NLTK, TensorFlow (CPU) and PyTorch (CPU). See `requirements.txt`.

## API keys

The scraping notebooks use [NewsAPI](https://newsapi.org/). Create a `.env` file next to `docker-compose.yml`:

```
NEWSAPI_KEY=your-newsapi-key
```

`.env` is git-ignored. Restart with `docker compose up -d` after changing it.

## Data not included

- `thyroid_CNN.ipynb` expects the Kaggle thyroid ultrasound image dataset in `data/thyroid/`. Download it from Kaggle and place it there (the folder is git-ignored).
- The stock notebooks download prices from Yahoo Finance at run time, so they need internet access.

## Notes

- `ASX_stock.ipynb` at the top level is an older version. Yahoo Finance has since renamed some balance-sheet fields, so use the version in `time series data analysis/`.
- `scraiping/Scraping_clustering.ipynb` asks for a search keyword with `input()`, so run it interactively in JupyterLab.
