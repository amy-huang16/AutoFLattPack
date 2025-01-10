import pandas as pd
import numpy as np

# read csv file
params_filepath = r'C:\Users\ahuan\Desktop\AutoFlattPack\FLattPackSampleParams.csv'

df = pd.DataFrame(columns=['Name', 'Cell Type', 'y Shift', 'Volume Fraction'])

# generate 50 of each geometry (Diamond, Gyroid, Primitive)
df['Cell Type'] = ['Diamond' for i in range(50)] + ['Gyroid' for i in range(50)] + ['Primitive' for i in range(50)]

# generate unique random volume fractions in range (0.2, 0.75) for Diamond and Gyroid, and (0.24, 0.75) for Primitive
dia_vf = np.random.choice(list(range(20, 76)), size=50, replace=False) * 0.01
dia_vf.sort()
gyr_vf = np.random.choice(list(range(20, 76)), size=50, replace=False) * 0.01
gyr_vf.sort()
prim_vf = np.random.choice(list(range(24, 76)), size=50, replace=False) * 0.01
prim_vf.sort()

df['Volume Fraction'] = np.concatenate((dia_vf, gyr_vf, prim_vf))

# generate random y-shifts
df['y Shift'] = np.random.randint(0, 10, size=len(df)) * 0.1

# write to original csv file
df.to_csv(params_filepath, index=False)
print("Successfully generated random sample parameters")
