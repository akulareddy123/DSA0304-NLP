import re

# Sample resumes
resumes = [
    """
    Name: Rahul Kumar
    Email: rahul.kumar@gmail.com
    Mobile: +91-9876543210
    Skills: Python, Java, SQL, Machine Learning, NLP
    Experience: 3 years
    """,

    """
    Name: Priya Sharma
    Email: priya.sharma@yahoo.com
    Mobile: 9876543211
    Skills: Java, SQL, NLP
    Experience: 4 years
    """,

    """
    Name: Arjun Reddy
    Email: arjun.reddy@gmail.com
    Mobile: +91 9123456789
    Skills: Python, SQL, Machine Learning
    Experience: 1 year
    """
]

# Regular expressions
name_pattern = r"Name\s*:\s*([A-Za-z ]+)"
email_pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
mobile_pattern = r"(?:\+91[-\s]?)?[6-9]\d{9}"
experience_pattern = r"Experience\s*:\s*(\d+(?:\.\d+)?)\s*years?"

skills_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]


def extract_resume_info(resume):
    # Extract name
    name_match = re.search(name_pattern, resume, re.IGNORECASE)
    name = name_match.group(1).strip() if name_match else "Not Found"

    # Extract email
    email_match = re.search(email_pattern, resume)
    email = email_match.group() if email_match else "Not Found"

    # Extract mobile number
    mobile_match = re.search(mobile_pattern, resume)
    mobile = mobile_match.group() if mobile_match else "Not Found"

    # Extract experience
    exp_match = re.search(experience_pattern, resume, re.IGNORECASE)
    experience = float(exp_match.group(1)) if exp_match else 0

    # Detect technical skills
    detected_skills = []
    for skill in skills_list:
        if re.search(r"\b" + re.escape(skill) + r"\b", resume, re.IGNORECASE):
            detected_skills.append(skill)

    return {
        "Name": name,
        "Email": email,
        "Mobile": mobile,
        "Skills": detected_skills,
        "Experience": experience
    }


# Process resumes
eligible_candidates = []

for resume in resumes:
    candidate = extract_resume_info(resume)

    print("\n----- Candidate Profile -----")
    print("Name       :", candidate["Name"])
    print("Email      :", candidate["Email"])
    print("Mobile     :", candidate["Mobile"])
    print("Skills     :", ", ".join(candidate["Skills"]))
    print("Experience :", candidate["Experience"], "years")

    # Eligibility criteria
    if candidate["Experience"] >= 2 and "Python" in candidate["Skills"]:
        print("Eligibility : ELIGIBLE")
        eligible_candidates.append(candidate)
    else:
        print("Eligibility : NOT ELIGIBLE")


# Display eligible candidates
print("\n========== ELIGIBLE CANDIDATES ==========")

for candidate in eligible_candidates:
    print("\nName       :", candidate["Name"])
    print("Email      :", candidate["Email"])
    print("Mobile     :", candidate["Mobile"])
    print("Skills     :", ", ".join(candidate["Skills"]))
    print("Experience :", candidate["Experience"], "years")