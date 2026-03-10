from database import questions_collection

more_questions = [

{
"question": "If a number is increased by 15, the result is 40. What is the number?",
"options": {"A":"20","B":"25","C":"30","D":"35"},
"correct_answer": "B",
"difficulty": 0.2,
"topic": "Algebra",
"tags": ["linear equation"]
},

{
"question": "What is the value of 18 + 27?",
"options": {"A":"43","B":"44","C":"45","D":"46"},
"correct_answer": "C",
"difficulty": 0.2,
"topic": "Arithmetic",
"tags": ["addition"]
},

{
"question": "A shop gives a 10% discount on a ₹500 item. What is the final price?",
"options": {"A":"₹450","B":"₹460","C":"₹470","D":"₹480"},
"correct_answer": "A",
"difficulty": 0.3,
"topic": "Arithmetic",
"tags": ["percentage"]
},

{
"question": "Solve for x: 7x = 63",
"options": {"A":"7","B":"8","C":"9","D":"10"},
"correct_answer": "C",
"difficulty": 0.3,
"topic": "Algebra",
"tags": ["linear equation"]
},

{
"question": "Vocabulary: Meaning of 'benevolent'",
"options": {"A":"kind","B":"angry","C":"strict","D":"selfish"},
"correct_answer": "A",
"difficulty": 0.3,
"topic": "Vocabulary",
"tags": ["synonym"]
},

{
"question": "What is the average of 10, 20, and 30?",
"options": {"A":"18","B":"20","C":"22","D":"25"},
"correct_answer": "B",
"difficulty": 0.4,
"topic": "Arithmetic",
"tags": ["average"]
},

{
"question": "Solve: 2x + 5 = 17",
"options": {"A":"5","B":"6","C":"7","D":"8"},
"correct_answer": "B",
"difficulty": 0.4,
"topic": "Algebra",
"tags": ["equation"]
},

{
"question": "Vocabulary: Meaning of 'lucid'",
"options": {"A":"clear","B":"confusing","C":"dark","D":"slow"},
"correct_answer": "A",
"difficulty": 0.4,
"topic": "Vocabulary",
"tags": ["word meaning"]
},

{
"question": "If the perimeter of a square is 36, what is the length of one side?",
"options": {"A":"6","B":"7","C":"8","D":"9"},
"correct_answer": "D",
"difficulty": 0.5,
"topic": "Arithmetic",
"tags": ["geometry"]
},

{
"question": "Solve: x² = 64",
"options": {"A":"6","B":"7","C":"8","D":"9"},
"correct_answer": "C",
"difficulty": 0.5,
"topic": "Algebra",
"tags": ["quadratic"]
},

{
"question": "Vocabulary: Meaning of 'ambiguous'",
"options": {"A":"clear","B":"uncertain","C":"strong","D":"honest"},
"correct_answer": "B",
"difficulty": 0.5,
"topic": "Vocabulary",
"tags": ["synonym"]
},

{
"question": "A train travels 60 km in 1 hour. How far will it travel in 2.5 hours?",
"options": {"A":"120 km","B":"130 km","C":"140 km","D":"150 km"},
"correct_answer": "D",
"difficulty": 0.6,
"topic": "Arithmetic",
"tags": ["speed distance"]
},

{
"question": "Solve: 3x + 4 = 19",
"options": {"A":"3","B":"4","C":"5","D":"6"},
"correct_answer": "C",
"difficulty": 0.6,
"topic": "Algebra",
"tags": ["linear equation"]
},

{
"question": "Vocabulary: Meaning of 'resilient'",
"options": {"A":"fragile","B":"flexible","C":"weak","D":"silent"},
"correct_answer": "B",
"difficulty": 0.6,
"topic": "Vocabulary",
"tags": ["word meaning"]
},

{
"question": "What is 30% of 150?",
"options": {"A":"35","B":"40","C":"45","D":"50"},
"correct_answer": "C",
"difficulty": 0.7,
"topic": "Arithmetic",
"tags": ["percentage"]
},

{
"question": "Solve: x² + 5 = 30",
"options": {"A":"4","B":"5","C":"6","D":"7"},
"correct_answer": "B",
"difficulty": 0.7,
"topic": "Algebra",
"tags": ["quadratic"]
},

{
"question": "Vocabulary: Meaning of 'meticulous'",
"options": {"A":"careful","B":"careless","C":"lazy","D":"quick"},
"correct_answer": "A",
"difficulty": 0.7,
"topic": "Vocabulary",
"tags": ["synonym"]
},

{
"question": "Solve: √(x + 16) = 6",
"options": {"A":"20","B":"24","C":"30","D":"36"},
"correct_answer": "A",
"difficulty": 0.8,
"topic": "Algebra",
"tags": ["square root equation"]
},

{
"question": "Vocabulary: Meaning of 'altruistic'",
"options": {"A":"selfish","B":"generous","C":"lazy","D":"rude"},
"correct_answer": "B",
"difficulty": 0.8,
"topic": "Vocabulary",
"tags": ["advanced vocabulary"]
},

{
"question": "Solve: 2x² + 8 = 40",
"options": {"A":"4","B":"5","C":"6","D":"7"},
"correct_answer": "A",
"difficulty": 0.9,
"topic": "Algebra",
"tags": ["quadratic"]
}

]

questions_collection.insert_many(more_questions)

print("20 GRE questions inserted successfully.")