# Pricehubble Assignment

## Questions:

* [ ] Enumerate the tools that you would be using (python packages, tools, external softwares, etc.). Explanations on why you would be using any of those technologies are welcome.

This is a broad question, and I will briefly mention some of the tools and
Python packages I have used in ETL pipelines. I will also highlight the
advantages of each tool over others.

1. Python Packages

   * **Pandas:** It's exceptional functionality, ease of use, and widespread adoption in the data science community make it a truly perfect tool for data manipulation and analysis task.
   * **Numpy:** For numerical computing and array operations.
   * **SQLAlchemy**: For working with database and executing query
   * **PySpark**: For distributed data processing
   * **Scikit-learn**, Scikit-learn, ...
2. Database

   * **PostgreSQL**: I always prefer PostgreSQL over MySQL for several reseans including: Postgres offers a wide range of advanced features such as support for complex data types, full-text search, and geospatial data. It also provides advanced indexing options and supports stored procedures, triggers, and views. The other important issue is that it's performance.
   * **MongoDB**: For unstructured data is a good database.
   * **Elasticsearch**: I always use ES for storing information that contains text since we can easily search on it with a good performance.
3. ETL Tools

   * **Apache Airflow:** It is a powerful and scalable platform for orchestrating and managing complex workflows. I always use Apache Airflow for scheduling and doing stuffs in parrallel via Directed Acyclic Graph(DAG).
   * **Apache Kafka**: We utilized Apache Kafka as a high-performing messaging queue to handle a large volume of data. During one of my experience, we crawled data and pushed it into Kafka. Subsequently, we enriched and transformed the data into a suitable format using consumers and different topics. Finally, we efficiently stored the data by creating an ETL pipeline with the assistance of Kafka.

* [ ] What format would best fit this use case to store the output data ? (csv, xlsx, json…) and why?
  The choice between different output data format depends on various factors. In this problem, I think CSV format for output data is suitable since we have a structured output. In another setup, we were dealing with high volume of data, so we store data in parquet which is a columnar storage and it has good performance and efficient efficient and encoding algorithm.
* [ ] Now assume that you have a pipeline that has billions of new records/terabytes of data that come on a regular basis. Would you change anything in the previous questions
  This question is challenging and it highlights the importance of engineering expertise. When dealing with small amounts of data, the
  differences between alternative tools may not be significant. However, when considering a high volume of data, the answer to your previous question may vary. While there is no definitive answer for how to handle large amount of data, I will attempt to explain some key points and share my experience on the matter:

  * **ELT vs ETL**: The choice between ELT and ETL depends on various factors such as the complexity of the data transformations. I always prefer ELT when dealing with large volumes of data. I had a good experience on using ELT instead of traditional ETL.
  * **DBT**: the process of creating Directed Acyclic Graphs (DAGs) is consistently challenging or difficult, so DBT create DAGs in more convenient way and it works well when we have large amount of information
  * **Spark**: Spark is a powerful distributed computing framework that offers several advantages over traditional data processing systems. One of its key strengths is its ability to handle large-scale data processing tasks with speed and efficiency.
  * Optimizing batch transfromation
  * ...
* [ ] (Bonus) Knowing that the input is mostly unstructured and humanly inputted, can you think of pipeline steps that could be interesting to add to your current design?

  The transformation step can be directly modified to effectively handle all variations of unstructured information. It is important to make the necessary changes in a way that ensures comprehensive coverage of all information structures.
