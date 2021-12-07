import pandas as pd
import csv

df = pd.read_csv("PROJECTdwarf_stars.csv")
df = df[df['Distance'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]
df.to_csv('PDS2.csv') 

