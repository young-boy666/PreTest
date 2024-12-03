###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module dataframe_builder
###

## Libraries needed
import pandas as pd
import numpy as np

## Function to define the wanted data structure
def define_dataframe_structure(column_specs):
    """  
    INPUTS:  A list of dictionaries 
    OUTPUTS: A pandas DataFrame with the specified structure
      
    > This function finds the maximum length (length of longest dictionary) and extends the 
      other dictionaries to this length, by adding NANs
       
    """
    # Prepare data dictionary
    data = {}
    max_length = 0

    # Find the maximum length of representative points
    for spec in column_specs:
        max_length = max(max_length, len(spec.get('reps', [])))

    for spec in column_specs:
        name = spec['name']
        reps = spec.get('reps', [])
        # Extend numerical columns with NaN to match max_length
        extended_points = reps + [np.nan] * (max_length - len(reps))
        data[name] = extended_points

    return pd.DataFrame(data)

## Function to simulate data
def simulate_data(seed_df, n_points=100, col_specs=None, random_state=None):
    """
    INPUTS: seed_df   - A pandas DataFrame contining data points
            n_points  - The number of simulated points to generate for each row of seed_df (Default value of 100)
            col_specs - A list of dictionaries specifying the structure of the simulated data
            random_state - A random seed to ensure reproducibility (Default value of None)

    OUTPUTS: simulated_data - A pandas DataFrame containing the simulated data points

    > This function takes a seed DataFrame and generates simulated data points for each row of the seed DataFrame. 
    > For each row in the seed data, it perturbs the values of each column according to user-defined specifications (col_specs)
    > Options of this are: The distribution type (normal or uniform) and variance
    > This allows for flexible and reproducible generation of realistic synthetic datasets
        
    """

    if random_state is not None:
        np.random.seed(random_state)
    
    simulated_data = []

    for _, representative in seed_df.iterrows():
        for _ in range(n_points):
            simulated_point = {}
            for col in seed_df.columns:
                # Numerical columns: apply column-specific specifications
                if col_specs and col in col_specs:
                    dist = col_specs[col].get('distribution', 'normal')
                    variance = col_specs[col].get('variance', 1.0)

                    if dist == 'normal':
                        simulated_point[col] = representative[col] + np.random.normal(0, np.sqrt(variance))
                    elif dist == 'uniform':
                        simulated_point[col] = representative[col] + np.random.uniform(-variance, variance)
                    else:
                        raise ValueError(f"Unsupported distribution: {dist}")
                else:
                    raise ValueError(f"Column {col} has no specifications in col_specs.")
            simulated_data.append(simulated_point)
    
    return pd.DataFrame(simulated_data)




def non_globular_cluster(seed_df, n_points=100, cluster_type='spiral', noise_level=0.05, random_state=None):
    """
    Simulates non-globular clusters based on the seed data.

    Parameters:
    - seed_df: pandas DataFrame, the seed data structure (from define_dataframe_structure()).
    - n_points: int, number of points to simulate for each seed point.
    - cluster_type: str, the type of non-globular cluster to simulate ('spiral', 'linear', 'sinusoidal').
    - noise_level: float, standard deviation of noise to add to the cluster.
    - random_state: int, random seed for reproducibility.

    Returns:
    - pandas DataFrame, simulated non-globular data.
    """

    if random_state is not None:
        np.random.seed(random_state)

    simulated_data = []

    for _, representative in seed_df.iterrows():
        base_x = representative.iloc[0]  # Assuming the first column is x
        base_y = representative.iloc[1] if seed_df.shape[1] > 1 else 0  # Assuming the second column is y

        for i in range(n_points):
            if cluster_type == 'spiral':
                angle = i * (2 * np.pi / n_points)
                radius = i / n_points
                x = base_x + radius * np.cos(angle) + np.random.normal(0, noise_level)
                y = base_y + radius * np.sin(angle) + np.random.normal(0, noise_level)
            elif cluster_type == 'linear':
                x = base_x + i / n_points + np.random.normal(0, noise_level)
                y = base_y + i / n_points + np.random.normal(0, noise_level)
            elif cluster_type == 'ball':
                x = base_x + np.random.normal(0, noise_level)
                y = base_y + np.random.normal(0, noise_level)
            else:
                raise ValueError(f"Unsupported cluster type: {cluster_type}")

            simulated_data.append({'x': x, 'y': y})

    return pd.DataFrame(simulated_data)
