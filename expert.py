def evaluate_performance(name, productivity, teamwork, communication):
    performance_score = 0
   
    if productivity >= 90:
        performance_score += 5
    elif 80 <= productivity < 90:
        performance_score += 4
    elif 70 <= productivity < 80:
        performance_score += 3
    elif 60 <= productivity < 70:
        performance_score += 2
    else:
        performance_score += 1
    
    # Evaluate teamwork
    if teamwork >= 4:
        performance_score += 4
    elif 3 <= teamwork < 4:
        performance_score += 3
    elif 2 <= teamwork < 3:
        performance_score += 2
    else:
        performance_score += 1
    
    # Evaluate communication
    if communication >= 4:
        performance_score += 4
    elif 3 <= communication < 4:
        performance_score += 3
    elif 2 <= communication < 3:
        performance_score += 2
    else:
        performance_score += 1
    
    # Determine performance label
    if performance_score >= 12:
        performance_label = "Excellent"
    elif 9 <= performance_score < 12:
        performance_label = "Good"
    else:
        performance_label = "Poor"
    return performance_label

k=evaluate_performance("John", 95, 4.5, 4)
print(k)