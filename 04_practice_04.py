#연습문제 #4: 졸업학점 검사

credit = int(input("이수한 학점수를 입력하시오: "))
grade = float(input("평점을 입력하시오: "))

if credit>=140 and grade>=2.0:
    print("졸업 가능")
else:
    print("졸업이 힘듭니다!")