

frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
backend_skills = {"Python", "JavaScript", "SQL", "React"}

print("Union:", frontend_skills | backend_skills)
print("Intersection:", frontend_skills & backend_skills)
print("Frontend-only Difference:", frontend_skills - backend_skills)
print("Symmetric Difference:", frontend_skills ^ backend_skills)