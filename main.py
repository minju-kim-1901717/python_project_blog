import student1
import student2
import student3

def main():
    students = {
        1: student1.student1,
        2: student2.student2,
        3: student3.student3
    }

    while True:
        try:
            command = int(input("작동 코드를 실행해주세요 : (0:종료/1~3:수강생 호출) ").strip())
        except ValueError:
            print("⚠ 숫자만 입력해주세요.")
            continue

        if command == 0:
            print("프로그램을 종료합니다.")
            break
        elif command in students:
            students[command]()   # 해당 함수 실행
        else:
            print("⚠ 잘못된 명령어입니다. (1~3 입력 가능)")

if __name__ == "__main__":
    main()
