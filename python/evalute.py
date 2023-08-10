def evaluateJobDescription(job_title, job_description):
    job_title_keywords = {
        'software engineer': ['software', 'developer', 'programming', 'coding'],
        'data analyst': ['data', 'analysis', 'statistics', 'reporting'],
        'marketing manager': ['marketing', 'strategy', 'campaigns'],
        'Advocate' : ['law']
    }
    
    job_title_lower = job_title.lower()
    keywords = job_title_keywords.get(job_title_lower, [])
    
    # Evaluate job description based on keyword matching
    count_match_keywords = sum(10 for keyword in keywords if keyword in job_description.lower())*10
    total_keywords = len(keywords)
    
    if total_keywords == 0:
        # No keywords for this job title, unable to evaluate properly
        score = 0.0
    else:
        score = count_match_keywords / total_keywords
        
    return score

# Example usage:
job_title = 'Software Engineer'
job_description = 'We are looking for a skilled software developer with strong coding skills.'
evaluation_score = evaluateJobDescription(job_title, job_description)
print(f'Evaluation Score for {job_title}: {evaluation_score} percentage ')
print(f'You have been succesfully fit for the {job_title} role in our company')
