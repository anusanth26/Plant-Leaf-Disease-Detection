#install kagglehub in your system using "pip install kagglehub" in command prompt
import kagglehub

path = kagglehub.dataset_download("emmarex/plantdisease")


print("Path to dataset files:", path)
