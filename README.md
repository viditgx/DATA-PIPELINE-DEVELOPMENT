# DATA-PIPELINE-DEVELOPMENT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: VIDIT GUPTA

*INTERN ID*: CT06DN838

*DOMAIN*: DATA SCIENCE

*DURATION*: 6WEEKS

*MENTOR*: NEELA SANTOSH

**PROJECT DISCRIPTION**
**This project was made for Task 1 of the Codtech Data Science Internship. It shows how to build a basic but complete ETL pipeline using Python. ETL stands for Extract, Transform, and Load — which are the main steps used to prepare raw data and make it ready for analysis or machine learning.

We’ve used the Iris dataset, which is a very popular dataset in the world of machine learning. It contains measurements of flowers (like petal length and sepal width) from three different species of iris plants. Even though it's a small dataset, it's great for practicing data preprocessing and building data pipelines.

1. Extract
In this step, we get the Iris dataset directly from Scikit-learn, a Python library. Since it’s built-in, we don’t have to download any files or connect to the internet. Once the data is loaded, we convert it into a Pandas DataFrame to make it easier to work with.

2. Transform
Next, we clean and process the data. Although this dataset doesn’t have missing values, we’ve added a check to handle them in case they ever appear. Then, we use StandardScaler to scale all the feature values. This step is important because it helps machine learning models treat each feature equally.

3. Load
After the data is clean and scaled, we split it into training and testing sets using train_test_split. Finally, we save both sets into two CSV files:

train_data.csv

test_data.csv

This simulates how real ETL pipelines store processed data for future use.

Why This Project Is Useful
This project is great for learning how data moves from raw form to clean, usable files. It gives hands-on experience with building data pipelines — something every data scientist and engineer needs to know, especially when working with messy real-world data.

The code is written in a modular way, with separate functions for each step (extract_data, transform_data, and load_data). This makes it easy to understand, reuse, and update later. We also use popular Python libraries like Pandas, NumPy, and Scikit-learn — which are widely used in the data science field.

Final Output
When you run the Python script, two files will be created in your folder:

train_data.csv — the training data

test_data.csv — the testing data

*OUTPUT

![Image](https://github.com/user-attachments/assets/a1e31436-51dd-45f7-b9d0-0a11cf6047f6)
