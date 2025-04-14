students = [
    ("Rahul", {"Math": 85, "English": 78, "Science": 92}),
    ("Anjali", {"Math": 45, "English": 88, "Science": 70}),
    ("Sneha", {"Math": 95, "English": 91, "Science": 89}),
    ("Rahul", {"Math": 85, "English": 78, "Science": 92}),  # Duplicate
]

# Step 1: Remove duplicates by converting dicts to frozensets
seen = set()
unique_students = []
for name, scores in students:
    key = (name, frozenset(scores.items()))
    if key not in seen:
        seen.add(key)
        unique_students.append((name, scores))

# Step 2: Calculate average marks
for name, scores in unique_students:
    avg = sum(scores.values()) / len(scores)
    print(f"{name}'s Average: {avg:.2f}")

# Step 3: Find all unique subjects
subjects = set()
for _, scores in unique_students:
    subjects.update(scores.keys())

print(f"\nUnique Subjects: {subjects}\n")

# Step 4: Students scoring >80 in Math
print("High scorers in Math:")
for name, scores in unique_students:
    if scores.get("Math", 0) > 80:
        print(f" - {name}")
