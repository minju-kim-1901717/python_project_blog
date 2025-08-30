# 포스팅하면 텍스트 파일이 한 파일에 모이고
# 포스팅 하는 포멧이 고정되어 있다는 전제로 코드를 만들었습니다.
# 코드에 주석처리 해놨으니 읽어주세요.

import os
import datetime

folder_path = 'member2/test_posts' # 포스팅한 글을 모아둔 기본 폴더주소

class BoardManager:

    def get_titles_from_post(): # 포스팅한 글을 가져오는 함수
        i = 0
        for filename in os.listdir(folder_path): # 폴더 안에 있는 파일을의 이름을 가져와서 위의 기본 폴더 주소와 합쳐 파일을 열 수 있게 했습니다.
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        if line.startswith('제목:'):  # '제목:'으로 시작하는 줄을 찾아서 제목 추출
                            title = line.split(':', 1)[1].strip()# 콜론(:) 뒤의 문자열을 가져와 공백 제거
                            print (f'{i+1}.{title}')
                            i += 1
                            break
            except:
                pass
    
    def Category_search_titles(Category): # 카테고리를 입력하면 그 카테고리를 가지고 있는 포스트들을 긁어오는 함수입니다.
        found = False
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        if line.startswith("제목: "): # 제목을 먼저 title로 가져오는 코드입니다.
                            title = line.split(':', 1)[1].strip()
                        elif line.startswith(f'카테고리: {Category}'): # 이후에 적어 놓은 카테고리와 같은 카테고리를 가진 포스트면 밑의 프린트를 출력합니다.
                                print (f'제목: {title} 카테고리:{Category}')
                                found = True
                                break
            except:
                pass
        if not found: # 모든 파일을 다 확인한 후 카테고리에 해당하는 글이 없으면 출력됩니다.
            print('찾으시는 카테고리에 해당하는 글이 없습니다.')

    def Latest_post(): # 글을 최신순으로 정렬하는 함수
        posts = {} # 글안에 제목과 시간을 딕셔너리 형태로 가져옵니다.
        i = 0
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        if line.startswith("제목: "): # 제목을 가져와 title로 가져옵니다.
                            title = line.split(':', 1)[1].strip()
                        elif line.startswith("시간: "): # 시간:으로 시작하는 라인을 찾아옵니다.
                            time = line.split(':', 1)[1].strip()
                            post_time = datetime.datetime.strptime(time, "%Y.%m.%d %H:%M:%S") # 시간을 datetime.datetime.strptime를 사용해 객체로 만들어 뒤에 sorted로 비교할 수 있게 만들었습니다. 
                            posts[title] = post_time # 제목과 시간을 posts로 딕셔너리 형태로 넣습니다.
            except:
                pass

        sorted_items_by_value = sorted(posts.items(), key=lambda item: item[1]) #posts안의 item[1]즉 시간을 기준으로 정렬하라는 내용입니다.

        for title, time in sorted_items_by_value:
            date_string = time.strftime("%Y.%m.%d %H:%M:%S") # 시간을 다시 strftime로 지정한 포멧을 바꾸어 str로 바꿉니다.
            print(f'{i + 1}.{title} 시간: {date_string}')
            i += 1



BoardManager.get_titles_from_post()
BoardManager.Category_search_titles("매우좋음")
BoardManager.Latest_post()