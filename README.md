# streamlit
SEMANTIC SEARCH WEB APPLICATION - STREAMLIT

📌 Project Description:
------------------------
This project is a simple and intuitive semantic search engine developed using Streamlit and sentence-transformers.

The application allows users to enter a sentence or question in natural language and returns the most semantically similar sentence from a predefined list using cosine similarity on sentence embeddings.

🚀 Steps to Create and Run the Application:
-------------------------------------------

1️⃣ Create a new folder for the project.

2️⃣ Inside the folder, create a file named: app.py  
    (This file will contain your main Streamlit application code.)

3️⃣ Create another file named: requirements.txt  
    (This file will list all the necessary Python packages.)

4️⃣ Add the following libraries in requirements.txt:
    - streamlit  
    - sentence-transformers  
    - numpy  
    - scikit-learn

5️⃣ Open a terminal (or command prompt) in your project folder.

6️⃣ Install all required packages by running the command:
    pip install -r requirements.txt

7️⃣ To launch the Streamlit application, use:
    streamlit run app.py

8️⃣ The app will open in your browser at the following address:
    http://localhost:8501

🔁 Steps to Push the Project to GitHub:
---------------------------------------

1️⃣ Go to GitHub and create a new repository.

2️⃣ On your computer, navigate to your project folder using the terminal.

3️⃣ Initialize Git in the project folder:
    git init

4️⃣ Add your project files to the repository:
    git add .

5️⃣ Commit the changes with a message:
    git commit -m "Add Streamlit app and requirements"

6️⃣ Link your local folder to the GitHub repository:
    git remote add origin https://github.com/your-username/your-repo-name.git

7️⃣ Push your code to GitHub:
    git push -u origin main

(Replace 'your-username' and 'your-repo-name' with your actual GitHub details.)

📂 Recommended Project Structure:
---------------------------------
app.py               → Main Streamlit application  
requirements.txt     → List of required Python packages  
README.md            → Setup instructions and usage guide  
data/ (optional)     → Folder for input files or sample datasets  

📊 What the Application Does:
-----------------------------
✔ Allows users to input a sentence or query  
✔ Calculates semantic similarity with a predefined sentence list  
✔ Displays the closest matching sentence  
✔ Shows a similarity matrix for reference  

👩‍💻 Author:
-------------
Ushmitha Annapaneni  
📄 License:
-----------
MIT License
