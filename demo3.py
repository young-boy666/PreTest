import cluster_maker as cm
import pandas as pd
import matplotlib.pyplot as plt


column_specs = [
    {"name": "DataScience", "reps": [70, 65, 73, 59, 64]},
    {"name": "MachineLearning", "reps": [61, 52, 58]},
    {"name": "TimeSeries", "reps": [70, 74, 68, 73]}
]

seed_df = cm.define_dataframe_structure(column_specs)

col_specs = {
    "DataScience": {"distribution": "normal", "variance": 4},
    "MachineLearning": {"distribution": "uniform", "variance": 0.2},
    "TimeSeries": {"distribution": "normal", "variance": 2},
}


simulated_data = cm.non_globular_cluster(seed_df, n_points=200, cluster_type='spiral', noise_level=0.05, random_state=666)
plt.plot(simulated_data['x'], simulated_data['y'], 'o')
plt.savefig('demo3spiral.png')  # Save plot to file
plt.close()

simulated_data = cm.non_globular_cluster(seed_df, n_points=200, cluster_type='linear', noise_level=0.05, random_state=666)
plt.plot(simulated_data['x'], simulated_data['y'], 'o')
plt.savefig('demo3linear.png')  # Save plot to file
plt.close()

simulated_data = cm.non_globular_cluster(seed_df, n_points=200, cluster_type='ball', noise_level=0.5, random_state=666)
plt.plot(simulated_data['x'], simulated_data['y'], 'o')
plt.savefig('demo3ball.png')  # Save plot to file
plt.close()