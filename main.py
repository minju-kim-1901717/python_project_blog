import member1
import member2
import member3

def main():
    while True:
        print("\n===== 메인 메뉴 =====")
        print("1. 게시글 작성")
        print("2. 게시글 목록 보기")
        print("3. 회원 관리 (로그인/회원가입)")
        print("0. 종료")
        
        command = input("👉 메뉴 선택: ").strip()
        
        if command == "0":
            print("프로그램을 종료합니다.")
            break
        elif command == "1":
            member1.create_post()
        elif command == "2":
            member1.show_posts()
        elif command == "3":
            manage_user()
        else:
            print("⚠ 잘못된 명령어입니다.")

def manage_user():
    while True:
        print("\n--- 회원 관리 ---")
        print("1. 회원가입")
        print("2. 로그인")
        print("3. 로그아웃")
        print("0. 메인으로 돌아가기")
        
        choice = input("👉 선택: ").strip()
        
        if choice == "1":
            username = input("아이디 입력: ")
            password = input("비밀번호 입력: ")
            member3.register_user(username, password)
        elif choice == "2":
            username = input("아이디 입력: ")
            password = input("비밀번호 입력: ")
            member3.login_user(username, password)
        elif choice == "3":
            member3.logout_user()
        elif choice == "0":
            break
        else:
            print("⚠ 잘못된 선택입니다.")

if __name__ == "__main__":
    member3.load_data()
    main()
    member3.save_data()