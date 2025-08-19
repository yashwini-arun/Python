
def my_filter(func, items):
    result = []
    for item in items:
        if func(item):
            result.append(item)
    return result

def is_eligible(candidate):
    return candidate["experience"] >= 2 and candidate["skills"].count("Python") > 0


print("=== Job Applicants Filter System ===")

applicants = [
    {"name": "Ravi", "experience": 3, "skills": ["Python", "Django"]},
    {"name": "Meera", "experience": 1, "skills": ["C", "C++"]},
    {"name": "Arjun", "experience": 2, "skills": ["Python", "Flask"]},
    {"name": "Kavya", "experience": 4, "skills": ["Java", "Spring"]},
    {"name": "Neha", "experience": 2, "skills": ["Python", "ML"]}
]

print("All Applicants:", [c["name"] for c in applicants])

eligible = my_filter(is_eligible, applicants)

print("\nEligible Applicants for Interview:")
for c in eligible:
    print(f"{c['name']} → {c['experience']} yrs, Skills: {', '.join(c['skills'])}")
