import csv
import random
import pyttsx3
import speech_recognition as sr
import datetime
import pandas as pd

def rcsv(csv_file):
    df = pd.read_csv(csv_file)
    a = random.randint(0, 100)
    return df['Questions'].loc[a]

def switch(selected_language):
    counter = 0
    while counter < 10:
        question = rcsv(f"{selected_language}.csv")
        display_question(question)
        user_answer = record_user_answer()
        save_user_answer(question, user_answer, selected_language)
        counter += 1

    change_language = input("Do you want to change language? (yes/no): ")
    if change_language.lower() == "yes":
        print("Please choose a programming language (Java, Python, AI, ML, C, C++):")
        selected_language = input("Language: ").upper()
        switch(selected_language)
    else:
        print("Thank you, it's completed. Please exit.")

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Display the question on the screen
def display_question(question):
    print(f"Question: {question}")

# Record user's speech answer
def record_user_answer():
    recording_duration = 5  # You can adjust the recording duration as needed
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak your answer...")
        audio = recognizer.listen(source, timeout=recording_duration)

    # Convert the recorded speech to text
    try:
        user_answer = recognizer.recognize_google(audio)
        return user_answer
    except sr.UnknownValueError:
        print("Sorry, I could not understand your answer.")
        return None
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return None

# Save the user's answer and question to a CSV file
def save_user_answer(question, user_answer, selected_language):
    file_name = f"user_answers.csv"

    with open(file_name, mode="a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([question, user_answer])

# Main function
def main():
    
    print("Choose a Programming Language (Java, Python, AI, ML, C, C++):")
    selected_language = input("Language: ").upper()
    switch(selected_language)
    
            

if __name__ == "__main__":
    main()
