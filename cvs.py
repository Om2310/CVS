# Importing Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Importing Dataset
training_data = pd.read_csv(r"C:\Users\dhruv\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Dataset2.csv")
training_data
#Assigning numbers to word input in Gender column for betterment analysis.
training_data['Gender'].unique()
training_data = training_data.replace(to_replace='m', value=1)
training_data = training_data.replace(to_replace='f', value=2)
training_data
#Assigning numbers to word input in Eye Strain column for betterment analysis.
training_data['Eye Strain'].unique()
training_data = training_data.replace(to_replace='high', value=2)
training_data = training_data.replace(to_replace='medium', value=1)
training_data = training_data.replace(to_replace='low', value=0)
training_data
#Assigning numbers to word input in Anti-Glare Filter column for betterment analysis.
training_data['Anti-Glare Filter'].unique()
training_data = training_data.replace(to_replace='yes', value=0)
training_data = training_data.replace(to_replace='no', value=1)
training_data
