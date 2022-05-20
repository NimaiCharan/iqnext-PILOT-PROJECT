import CreateDataFrame as cmlm
import pandas as pd
from neuralprophet import NeuralProphet
import pickle

# #Creating the dataframe
data = cmlm.get_data_from_db(cmlm.connect_to_db())
data["time"] = pd.to_datetime(data['time'], format='%I:%M:%S %p').dt.strftime('%H:%M')



date_time =data['date']+" "+data['time']
date_data = pd.to_datetime(date_time)
data["date_time"] = date_data
data["feels_like"] = data["feels_like"].astype("float64")


ml_data  = pd.DataFrame({
    'ds':data["date_time"],
    'y':data["feels_like"]
    })

ml_data = ml_data.drop_duplicates(subset=['ds'], keep='first')

# #Creating the ML Model
m = NeuralProphet(
    changepoints_range=0.95,
    n_changepoints=50,
    trend_reg=1,
    weekly_seasonality=False,
    daily_seasonality=2,
    learning_rate=0.001
)
model = m.fit(ml_data, freq='5min')

#m.plot(ml_data)
#Save the model

with open('neuralprophet_model.pkl', "wb") as f:
    pickle.dump(m, f)
