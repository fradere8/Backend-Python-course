def check_winners(scores, student_score):
    if student_score in sorted(scores, reverse=True)[:3]:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


check_winners([20, 48, 52, 53, 54, 67, 72, 30, 10, 84, 41], 67)
check_winners([20, 48, 52, 53, 54, 67, 72, 30, 10, 84, 41], 48)
