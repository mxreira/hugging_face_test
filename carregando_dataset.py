from datasets import load_dataset
import pandas as pd

ds = load_dataset('facebook/natural_reasoning', split='train')


print(ds[0]['question']) #printando primeiro valor da coluna question