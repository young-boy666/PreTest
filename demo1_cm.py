import cluster_maker as cm
import pandas as pd

print('\n ***** DEMO 1 ***** ')

column_specs = [
    {"name": "DataScience", "reps": [70, 65, 73, 59, 64]},
    {"name": "MachineLearning", "reps": [61, 52, 58]},
    {"name": "TimeSeries", "reps": [70, 74, 68, 73]}
]

seed_df = cm.define_dataframe_structure(column_specs)

print('\n> Here is the starting data (A list of dictionaries):\n')
print(column_specs)
print('\n> After using the define_dataframe_structure function to get a DataFrame of all the data:\n')
print(seed_df)


col_specs = {
    "DataScience": {"distribution": "normal", "variance": 4},
    "MachineLearning": {"distribution": "uniform", "variance": 0.2},
    "TimeSeries": {"distribution": "normal", "variance": 2},
}
simulated_data = cm.simulate_data(seed_df, n_points=2, col_specs=col_specs, random_state=666)

print('\n> After using the simulate_data function to simulate new data:\n')
print(simulated_data)