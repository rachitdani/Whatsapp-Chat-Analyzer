# Whatsapp Chat Analyzer

A streamlit app used to analyze your whatsapp chat

## Project Structure

The project is organized as follows:

- `requirements.txt`: This file lists all the Python libraries and dependencies required to run the project.
  
- `.gitignore`: This file specifies which files and directories should be ignored by Git.

- `README.md`: This file is an outcome of displaying the projects documentation.

- `notebooks`: This directory contains Jupyter notebook file which has the rough code along with sample chat file which was created during the project implementation.
  
- `setup.sh and Procfile`: Files required for the code deployment in cloud.

- `preprocessor.py` : The file where the data preprocessing and cleaning is done.

- `utils.py` : The file where the functions are created and these functions are used in the app.py

- `app.py`: This is the main file for the analysis of whatsapp chats in web using streamlit.
  

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/rachitdani/Whatsapp-Chat-Analyzer.git
```

2. Navigate to the project directory:

```
cd Whatsapp-Chat-Analyzer.git
```

3. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

4. Run the Streamlit application:

```
streamlit run app.py
```

5. A web app pop-up will appear where you will upload your whatsapp chat file to be analyzed

## How to Export data from Whatsapp

For downloading your whatsapp file follow these steps :

1. Go to the chat you want to analyze it can be a group chat or a personal chat
2. Then go to chat info and scroll down until you see the `Export Chat` Option
3. Now Click on `Without Media` and download it
4. Now Extract the file and upload the file to the streamlit app and great you have just got your data analyzed.

## Screenshots

#### Main streamlit webpage
<img width="1438" alt="Screenshot 2024-01-07 at 12 28 16 AM" src="https://github.com/rachitdani/Whatsapp-Chat-Analyzer/assets/79761144/2bdef05f-b038-413f-b05a-ec698a36f859">

#### Upload Chat File and Select Overall for Overall Group Analysis or any user in the dropdown and Click on Show Analysis
<img width="1438" alt="Screenshot 2024-01-07 at 12 34 00 AM" src="https://github.com/rachitdani/Whatsapp-Chat-Analyzer/assets/79761144/4d91faa1-c4b0-4654-94a7-92d2a5472a86">

<img width="1438" alt="Screenshot 2024-01-07 at 12 28 40 AM" src="https://github.com/rachitdani/Whatsapp-Chat-Analyzer/assets/79761144/1f1af82c-9efd-4d2a-9655-78c23f2c7436">

<img width="1438" alt="Screenshot 2024-01-07 at 12 28 48 AM" src="https://github.com/rachitdani/Whatsapp-Chat-Analyzer/assets/79761144/39c42ed0-e305-4974-824a-0fed691b9e56">

<img width="1438" alt="Screenshot 2024-01-07 at 12 28 56 AM" src="https://github.com/rachitdani/Whatsapp-Chat-Analyzer/assets/79761144/67c9d386-ea91-4bff-a94d-17a2e6b2e3ce">

<img width="1438" alt="Screenshot 2024-01-07 at 12 29 02 AM" src="https://github.com/rachitdani/Whatsapp-Chat-Analyzer/assets/79761144/2d440e55-141f-453b-b11f-a5f8cb4c9b38">

<img width="1438" alt="Screenshot 2024-01-07 at 12 29 06 AM" src="https://github.com/rachitdani/Whatsapp-Chat-Analyzer/assets/79761144/2aac66df-1375-464e-bf3a-bdeebd084456">


## Contributing

Contributions are welcome !! I have only included the basic stopwords nltk library along with a few additional stopwords there are a lot more in our regular chatting language also a lot more features can be added to this project .
If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Description of your changes'`.
4. Push your changes to your fork: `git push origin feature-name`.
5. Create a pull request on the original repository.

