# Ask for the user's age
symptoms = []
symptoms_answers = []
scoring_weight = [3,1,2,3,2,2,3]
total_weight = sum(scoring_weight)
results_qualitative = 0
chest_pain = input(" Did you have any chest pains last month ? ")
chest_pain_sport = input(" Did you have any chest pains last month during effort ? ")

if chest_pain == "yes" or chest_pain_sport == "yes":
    chest_pain_scale = int(input("On a scale of 1 to 10, what is your level of chest pain?"))
    symptoms_answers.append("yes")

else :
    chest_pain_scale = 0
    symptoms_answers.append("no")


scoring_weight[0] = float(scoring_weight[0]*chest_pain_scale/10)
fatigue = input(" Did you feel tired for any particular reasons lately ? ")
symptoms_answers.append(fatigue)
fluttering = input("Did you feel pounding lately ?")
symptoms_answers.append(fluttering)
vertiges = input ("Did you feel dizzy lately ?")
symptoms_answers.append(vertiges)
fainting = input("Have you fainted last month ?")
symptoms_answers.append(fainting)
breath = input("Have you been out of breath lately?")
symptoms_answers.append(breath)
feet_swelling = input("Have your feet swollen recently?")
symptoms_answers.append(feet_swelling)

def transform(question, symptoms):
    if question == "yes":
        symptoms.append(1)
    else :
        symptoms.append(0)

    return symptoms





for i in range(len(symptoms_answers)):
    transform(symptoms_answers[i], symptoms)


print(symptoms_answers)
print(symptoms)


def qualitative_compute(symtoms, scoring_weight, total_weight):
    
    results_qualitative = 0
    for i in range(len(symptoms)):
               results_qualitative = results_qualitative+ symptoms[i]*scoring_weight[i]
    
    results_qualitative = results_qualitative/total_weight
    return results_qualitative


results_qualitative = qualitative_compute(symptoms, scoring_weight, total_weight)
print(results_qualitative)

model_training = 0.7
diagnostics = 0.7*model_training+ 0.3*results_qualitative
print(diagnostics)