import json

users = {}        
current_user = None   

def save_data():
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

def load_data():
    global users
    try:
        with open("users.json", "r", encoding="utf-8") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

def register_user(username, password, is_admin=False):
    if username in users:
        print("⚠ 이미 존재하는 사용자입니다.")
        return False
    users[username] = {"password": password, "is_admin": is_admin}
    print(f"✅ {username} 님이 회원가입 완료되었습니다.")
    return True

def login_user(username, password):
    global current_user
    if username not in users:
        print("⚠ 존재하지 않는 사용자입니다.")
        return False
    if users[username]["password"] != password:
        print("⚠ 비밀번호가 틀렸습니다.")
        return False
    current_user = username
    print(f"👋 {username} 님 환영합니다!")
    return True

def logout_user():
    global current_user
    if current_user:
        print(f"👋 {current_user} 님이 로그아웃 되었습니다.")
        current_user = None
    else:
        print("⚠ 현재 로그인한 사용자가 없습니다.")

def is_admin():
    if current_user and users[current_user]["is_admin"]:
        return True
    return False
