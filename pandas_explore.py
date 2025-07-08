import pandas as pd
import pdfplumber

# this is to read the csv file
df = pd.read_csv("https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv")
print("the data present inside the csv file")
print(df)

# prints the column names
print("columns", df.columns)

for i in df.columns:
    print(i)

# includes all the columns
print("values", df.values)

# prints the datatypes
print("datatypes", df.dtypes)

# prints the content inside the csv file
print("add", df.add)

df.empty

# checks if it is empty
print("after empty", df.empty)

print("describe", df.describe())

print("keys", df.keys())

print("head", df.head())

with pdfplumber.open("./Pallavi-CV-RBC.pdf") as pdf:
    for page in pdf.pages:
        print("page_number", page.page_number)
        print("page_text", page.extract_text())

        print("images", page.images)



