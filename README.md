# streamlit
============================================================
           SEMANTIC SEARCH WEB APPLICATION - STREAMLIT
============================================================

📌 Project Overview:
---------------------
This project is a simple and user-friendly semantic search tool
built with Streamlit and sentence-transformers.

It lets users type a natural sentence and then finds the most 
meaningfully similar sentence from a preset list using cosine 
similarity and embeddings.

============================================================

🚀 How to Set Up and Run the Application:
-----------------------------------------

1️⃣ Create a new folder on your computer for the project.

2️⃣ Inside that folder, create a file named: app.py  
    (This is where your Streamlit code will go.)

3️⃣ Create another file named: requirements.txt  
    (This file lists all the packages the app needs.)

4️⃣ In requirements.txt, include the following libraries:
    - streamlit
    - sentence-transformers
    - numpy
    - scikit-learn

5️⃣ Open your terminal (or command prompt) in the project folder.

6️⃣ Install the required packages by running:
    pip install -r requirements.txt

7️⃣ To start the app, run the command:
    streamlit run app.py

8️⃣ The app will open in your default web browser, usually at:
    http://localhost:8501

============================================================

🔁 How to Upload the Project to GitHub:
---------------------------------------

1️⃣ Go to GitHub and create a new empty repository.

2️⃣ In your terminal, make sure you're inside your project folder.

3️⃣ Initialize Git for your project:
    git init

4️⃣ Add all your project files:
    git add .

5️⃣ Commit your changes with a message:
    git commit -m "Initial commit"

6️⃣ Link your local project to your GitHub repo:
    git remote add origin https://github.com/your-username/your-repo-name.git

7️⃣ Push the code to GitHub:
    git push -u origin master

👉 Replace `your-username` and `your-repo-name` with your actual GitHub details.

============================================================

📁 Project Folder Structure (Recommended):
------------------------------------------
📄 app.py               → Main Streamlit app  
📄 requirements.txt     → Python dependencies  
📄 README.md            → Setup and usage instructions  
📁 data/ (optional)     → Folder for your custom input files or datasets  

============================================================

📊 What the Application Does:
------------------------------
✔ Accepts a sentence from the user  
✔ Finds the most semantically similar sentence from a given list  
✔ Shows the best match  
✔ Also displays a similarity matrix comparing all sentences  

============================================================

👥 Author:
------------
- Ushmitha Annapaneni  

============================================================

📄 License:
-----------
MIT License

============================================================
