# Databricks notebook source

# MAGIC %md
# MAGIC # MLflow Regression Recipe Databricks Notebook
# MAGIC This notebook runs the MLflow Regression Recipe on Databricks and inspects its results.
# MAGIC
# MAGIC For more information about the MLflow Regression Recipe, including usage examples,
# MAGIC see the [Regression Recipe overview documentation](https://mlflow.org/docs/latest/recipes.html#regression-recipe)
# MAGIC and the [Regression Recipe API documentation](https://mlflow.org/docs/latest/python_api/mlflow.recipes.html#module-mlflow.recipes.regression.v1.recipe).

# COMMAND ----------

# MAGIC %pip install -r ../requirements.txt

# COMMAND ----------

# MAGIC %md ### Start with a recipe:

# COMMAND ----------

from mlflow.recipes import Recipe

r = Recipe(profile="databricks")

# COMMAND ----------

# MAGIC %md ### Inspect recipe DAG:

# COMMAND ----------

r.inspect()

# COMMAND ----------

# MAGIC %md ### Ingest the dataset:

# COMMAND ----------

r.run("ingest")

# COMMAND ----------

# MAGIC %md ### Split the dataset into train, validation and test:

# COMMAND ----------

r.run("split")

# COMMAND ----------

training_data = r.get_artifact("training_data")
training_data.describe()

# COMMAND ----------

r.run("transform")

# COMMAND ----------

# MAGIC %md ### Train the model:

# COMMAND ----------

r.run("train")

# COMMAND ----------

trained_model = r.get_artifact("model")
print(trained_model)

# COMMAND ----------

# MAGIC %md ### Evaluate the model:

# COMMAND ----------


r.run("evaluate")

# COMMAND ----------

# MAGIC %md ### Register the model:

# COMMAND ----------

r.run("register")
