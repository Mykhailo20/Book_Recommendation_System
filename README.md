
<p align='center'>
   <img src='react_frontend/src/assets/logo.png' width="250" alt='logo'>
   <h2 align='center'>Book Recommendation System</h2>
</p>

<p align='center'>
   <i>
      A book recommendation web application built with React and Python that uses collaborative filtering to suggest book selections.
   </i>
</p>
<br>

## :dart: Objective
Develop an intuitive and efficient book recommendation system that enhances user experience by providing book suggestions based on collaborative filtering techniques.

## :hammer_and_wrench: Technologies Used
[![made-with-jupyter](https://img.shields.io/badge/Made%20with%20-%20Jupyter%20-%20orange?style=flat&logo=jupyter)](https://jupyter.org/) <br>
[![made-with-python](https://img.shields.io/badge/Made%20with%20-%20Python%20-%20blue?style=flat&logo=python)](https://www.python.org/) <br>
[![made-with-react](https://img.shields.io/badge/Made%20with%20-%20React%20-%20red?style=flat&logo=react)](https://react.dev/) <br>
<p align='center'>
   <img src='readme_files/diagrams/technologies_used.png' width='500' alt='system_diagram'>
</p>

The following technologies where used in this project:
- **Working with Data**:
  - **Jupyter Lab**: Interactive notebook development, code writing, and data analysis.
  - **Pandas**: Data processing and analysis.
  - **Matplotlib and Seaborn**: Data visualization.
  - **Scikit-Learn**: Exploratory data analysis and machine learning.
- **Backend Part**:
  - **FastAPI**: Modern, high-performance Python web framework for building APIs.
  - **SQLAlchemy**: Python SQL and Object Relational Mapper toolkit; provides developers with the full capabilities of SQL.
  - **PostgreSQL**: Popular open source relational database management system (DBMS) known for its reliability, scalability, and extensive feature set.
- **Frontend Part**:
  - **React**: JavaScript library for creating interactive user interfaces and a wide range of web applications.
  - **Redux**: JavaScript library designed to manage the state of JavaScript applications.
  - **Tailwind CSS**: Utility CSS framework that provides a set of pre-designed utility classes; facilitates rapid style writing and user interface creation.


## :bar_chart: Project pipeline
<p align='center'>
   <img src='readme_files/diagrams/system_diagram.png' alt='system_diagram'>
</p>

The implementation of the recommendation system involved the following steps:
1. **Searching for a Dataset on Kaggle**: Using the ["Book Recommendation Dataset"](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) dataset as the basis of a recommendation system.
2. **Dataset Exploration**: Performing the Data Quality Assessment (DQA) and Exploratory Data Analysis (EDA) stages in order to evaluate the dataset, identify and appropriately process outliers or anomalies, identify and analyze patterns and relationships in the data. The processed data, which is saved in separate files, is the result of this step.
3. **Extract, Transform, Load (ETL)**: Preparation and loading of data datasets into the corresponding tables of the PostgreSQL relational database.
4. **Creation of Recommendation Systems**: Use of data from processed datasets to build 3 recommender systems that will be used in the program.
5. **Implementation of the backend part**: Using the FastAPI framework to create an API that will use data from a dataset file and a database, refer to implemented recommender systems, and provide all necessary information to clients.
6. **Implementation of Client-Side App**: Creating a client in the form of a web application using React, Redux and Tailwind CSS.
7. **Usage of [Open Library](https://openlibrary.org/)**: Using the [Open Library ISBN API](https://openlibrary.org/dev/docs/api/books) to correct dataset errors in the 'publication_year' variable.


## :open_file_folder: Project Files Description
This project contains 2 folders (disregarding the 'readme_files' folder which contains the images for README.md):
1. **[fastapi_backend](https://github.com/Mykhailo20/Book_Recommendation_System/tree/main/fastapi_backend)**: Contains data (datasets), system code (in particular recommender systems code, backend server code) and artifacts (jupyter notebooks, database schemas).
2. **[react_frontend](https://github.com/Mykhailo20/Book_Recommendation_System/tree/main/react_frontend)**: Contains the code of the client-side web application developed with React, Redux (for state management), and Tailwind CSS (for styling).

## :computer: Functionality Overview
1. **Main Page**: 
<p align='center'>
   <img src='readme_files/images/main_page.gif' alt='main-page' width='900'>
</p>

2. **View Information about the Book**:
<p align='center'>
   <img src='readme_files/images/book_info.gif' alt='main-page' width='900'>
</p>

3. **Book Search by Title**:
<p align='center'>
   <img src='readme_files/images/book_search_by_title.gif' alt='book-search-title' width='900'>
</p>

4. **Book Recommendations by Title**:
<p align='center'>
   <img src='readme_files/images/similar_books.gif' alt='book-recommendations' width='900'>
</p>

5. **Book Filtering by Author**:
<p align='center'>
   <img src='readme_files/images/book_filter_by_author.gif' alt='book-filter-author' width='900'>
</p>

6. **Additional Features**:
    - **Displaying the System's Currect State**:
   <p align='center'>
      <img src='readme_files/images/display_current_state.png' alt='book-filter-author' width='900'>
   </p>

   - **Responsive Web Design**:
   <p align='center'>
      <img src='readme_files/images/responsive_design_1.png' alt='book-filter-author' width='900'>
   </p><br>
   <p align='center'>
      <img src='readme_files/images/responsive_design_2.png' alt='book-filter-author' width='900'>
   </p>

   - **Non-Trivial Case Management**: 
   <p align='center'>
      <img src='readme_files/images/non_trivial_case_management.png' alt='non-trivial-case-management' width='900'>
   </p>