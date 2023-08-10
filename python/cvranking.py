import PyPDF2
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    return text

# Example usage
if __name__ == "__main__":
    pdf_files = [
           r"resume.pdf",r"resume(1).pdf"
        #r"C:\Users\palep\OneDrive\Desktop\madhu resumes\harshini.pdf",
    # Add paths for other PDF files here
    ]

    for pdf_file_path in pdf_files:
        extracted_text = extract_text_from_pdf(pdf_file_path)
        print(f"Text extracted from {pdf_file_path}:")
        print(extracted_text)
        print("-" * 30)


def search_word_in_text(text, word_to_search, case_sensitive=True):
    if not case_sensitive:
        text = text.lower()
        word_to_search = word_to_search.lower()
    return word_to_search in text

def calculate_score(text, keywords_weight):
    total_score = 0
    matched_keywords = {}
    for keyword, weight in keywords_weight.items():
        if search_word_in_text(text, keyword):
            total_score += weight
            matched_keywords[keyword] = weight
    return total_score, matched_keywords

def send_email(recipient_email, subject, message):
    # Replace these placeholders with your actual email settings
    sender_email = "satyavinayak2002@gmail.com"
    sender_password = "zdefpqbdxdqrmcie"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Change this to the appropriate port

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", e)


if __name__ == "__main__":
    resume_files = [
        r"resume.pdf",r"resume(1).pdf"
        #r"C:\Users\palep\OneDrive\Desktop\madhu resumes\harshini.pdf",
        # Add paths for 10 resumes here
    ]
    
    design_keywords_weight = {
        "header": 5,
        "bullet points": 3,
        "bold text": 2,
        "italic text": 2
    }
    
    experience_keywords_weight = {
        "experience": 5,
        "education": 3,
        "achievements": 2,
        "contact information": 1
    }
    
    skills_keywords_weight = {
        "Java": 5,
        "Python": 8,
        "HTML": 4,
        "CSS": 4,
        "JavaScript": 5,
        "problem-solving": 4,
        "teamwork": 3
    }
    
    projects_keywords_weight = {
        "project": 5
    }
    
    overall_keywords_weight = {
        "resume": 5,
        "communication": 2
    }
    
    resume_scores = []
    
    for pdf_file_path in resume_files:
        extracted_text = extract_text_from_pdf(pdf_file_path)
        design_score, design_matched_keywords = calculate_score(extracted_text, design_keywords_weight)
        experience_score, experience_matched_keywords = calculate_score(extracted_text, experience_keywords_weight)
        skills_score, skills_matched_keywords = calculate_score(extracted_text, skills_keywords_weight)
        projects_score, projects_matched_keywords = calculate_score(extracted_text, projects_keywords_weight)
        overall_score, overall_matched_keywords = calculate_score(extracted_text, overall_keywords_weight)
        
        total_possible_score = sum(list(design_keywords_weight.values()) +
                                  list(experience_keywords_weight.values()) +
                                  list(skills_keywords_weight.values()) +
                                  list(projects_keywords_weight.values()) +
                                  list(overall_keywords_weight.values()))
        
        percentage_score = (overall_score / total_possible_score) * 100
        
        resume_scores.append((pdf_file_path, design_score, experience_score, skills_score, projects_score, overall_score, percentage_score))
    
    # Sort the resumes based on overall score or 1st rank and print the resume scores
    print("Resume Scores:")
    for i, (pdf_file_path, design_score, experience_score, skills_score, projects_score, overall_score, percentage_score) in enumerate(resume_scores):
        print(f"\nResume {i+1}")
        print(f"Experience Score: {experience_score} out of {sum(experience_keywords_weight.values())}")
        print(f"Skills Score: {skills_score} out of {sum(skills_keywords_weight.values())}")
        print(f"Projects Score: {projects_score} out of {sum(projects_keywords_weight.values())}")
        print(f"Design Score: {design_score} out of {sum(design_keywords_weight.values())}")
        print(f"Education and Certifications Score: {experience_matched_keywords.get('education', 0)} out of {experience_keywords_weight['education']}")
        print(f"Achievements Score: {experience_matched_keywords.get('achievements', 0)} out of {experience_keywords_weight['achievements']}")
        print(f"Contact Information Score: {experience_matched_keywords.get('contact information', 0)} out of {experience_keywords_weight['contact information']}")
        print(f"Overall Score: {overall_score} out of {total_possible_score}")
        print(f"Percentage of matched keywords: {percentage_score:.2f}%")

    # Sort the resumes based on overall score or 1st rank and print the rankings with resume names
    print("\nResume Rankings:")
    ranked_resumes = sorted(resume_scores, key=lambda x: (x[5], x[0]), reverse=True)
    for i, (pdf_file_path, _, _, _, _, overall_score, _) in enumerate(ranked_resumes):
        resume_name = pdf_file_path.split('\\')[-1]
        print(f"{i+1}. {resume_name} - Overall Score: {overall_score}")

    # Check if the top candidate is shortlisted based on overall score or 1st rank
    top_candidate_score = ranked_resumes[0][5]
    threshold = 60
    if top_candidate_score >= threshold:
        print("\nTop candidate is Shortlisted")
        top_candidate_email = "satyavinayak431@gmail.com"  # Replace with the actual email address of the top candidate
        email_subject = "Congratulations! You've been shortlisted for the position"
        email_message = "Dear Candidate,\n\nCongratulations! We are pleased to inform you that you have been shortlisted for the position based on your impressive resume.\n\nBest regards,\nThe Hiring Team"
        send_email(top_candidate_email, email_subject, email_message)
    else:
        print("\nTop candidate is not shortlisted. Better luck next time for the top candidate.")
