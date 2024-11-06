import pandas as pd

data = {
    "Name": ["Chano", "Nini", "Palu"],
    "Age": [43, 39, 4],
    "Sport": ["Football", "Nothing", "Swimming"],
}

df = pd.DataFrame(data)
df = df.replace("Chano", "Luciano")
