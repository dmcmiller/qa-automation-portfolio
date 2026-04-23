test_scores = [85, 42, 91, 60, 78, 11, 69, 65]

def grade_checker(grades, passing_grade):
    passed = 0
    failed = 0
    for grade in grades:
        if grade >= passing_grade:
            print(f'{grade} - PASS')
            passed += 1
        else:
            print(f'{grade} - FAIL')
            failed += 1

    print(f"Results: {passed} passed, {failed} failed")

grade_checker(test_scores, 70)
