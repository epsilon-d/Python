# https://aitrack.elice.io/courses/12015/lectures/100916/materials/14

# 클래스 Bbread(붕어빵)을 만들어봅시다.
# Bbread의 필드 taste를 생성하고, "밀가루"를 대입해봅시다.
# Bbread의 메서드 eat()를 생성해봅시다. 이 메서드는 taste, "맛이 나요!"를 출력합니다.
# taste의 값이 "밀가루"라면 "밀가루 맛이 나요!" 가 출력됩니다.
class Bdread:
    taste = "밀가루"
    def eat(self):
        print(self.taste, "맛이 나요!")

# 클래스 Bbread의 인스턴스 redBean과 choux를 만들어봅시다.
redBean = Bdread()
choux = Bdread()

# 객체 redBean의 필드 taste를 "팥"으로 바꿔줍시다
redBean.taste = "팥"

# 객체 choux의 필드 taste를 "슈크림"으로 바꿔줍시다
choux.taste = "슈크림"

# 객체 redBean의 메서드 eat()를 실행해봅시다
redBean.eat()

# 객체 choux의 메서드 eat()를 실행해봅시다
choux.eat()