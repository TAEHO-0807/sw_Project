
# coding: utf-8

# In[1]:


import random

# 학생 데이터 생성
def student_data():  # 학생 데이터 함수
    students = []
    for _ in range(30):
        name = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 선택 정렬
def selection_sort_modify(A, key):  # key는 정렬 기준
    n = len(A)
    
    for i in range(0, n - 1):
        least = i # 현재 최소값 인덱스
        for j in range(i + 1, n):
            
            if A[j][key] < A[least][key]:
                least = j
                
        if i != least: # 최소값을 현재 위치로 이동하는 부분 
            A[i], A[least] = A[least], A[i]
            
    return A

# 삽입 정렬
def insertion_sort_modify(A, key):
    n = len(A)
    
    for i in range(1, n):
        key_item = A[i]
        j = i - 1
        
        while j >= 0 and A[j][key] > key_item[key]:
            A[j + 1] = A[j] # 데이터를 뒤로 이동
            j -= 1
        A[j + 1] = key_item
        
    return A

# 퀵 정렬
def quick_sort_modify(A, left, right, key):
    if left < right:
        q = partition(A, left, right, key) # 분할 과정
        quick_sort_modify(A, left, q - 1, key) # 왼쪽 리스트 정렬
        quick_sort_modify(A, q + 1, right, key)    # 오른쪽 리스트 정렬

def partition(A, left, right, key):
    low = left + 1
    high = right
    pivot = A[left]
    
    while low <= high:
        while low <= right and A[low][key] <= pivot[key]:
            low += 1
            
        while high >= left and A[high][key] > pivot[key]:
            high -= 1
            
        if low < high:
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]
    
    return high

# 기수 정렬 + 계수 정렬
def counting_sort_with_radix(A, exp):
    n = len(A)
    output = [0] * n
    count = [0] * 10

    for student in A:
        index = (student["성적"] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (A[i]["성적"] // exp) % 10
        output[count[index] - 1] = A[i]
        count[index] -= 1

    return output

def radix_sort_with_counting(A):
    max_score = max(student["성적"] for student in A)
    exp = 1
    
    while max_score // exp > 0:
        A = counting_sort_with_radix(A, exp)
        exp *= 10
        
    return A

# 정렬 실행 함수
def sort_students(students, algorithm, key):
    if algorithm == 1:  # 선택 정렬
        return selection_sort_modify(students, key)
    elif algorithm == 2:  # 삽입 정렬
        return insertion_sort_modify(students, key)
    elif algorithm == 3:  # 퀵 정렬
        quick_sort_modify(students, 0, len(students) - 1, key)
        return students
    elif algorithm == 4 and key == "성적":  # 기수 정렬
        return radix_sort_with_counting(students)
    else:
        print("잘못된 정렬 알고리즘 또는 키입니다.")
        return students

# 사용자 인터페이스
def menu():  # 사용자 메뉴 출력 함수
    
    print("===== 성적 관리 프로그램 =====")
    print("1. 이름을 기준으로 정렬")
    print("2. 나이를 기준으로 정렬")
    print("3. 성적을 기준으로 정렬")
    print("4. 프로그램 종료")
    print("==============================")

def main():  # 프로그램의 메인 실행 함수
    students = student_data()
    print("생성된 학생 정보:")
    for student in students:
        print(student)

    while True:
        menu()
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            key = "이름"
        elif choice == "2":
            key = "나이"
        elif choice == "3":
            key = "성적"
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")
            continue

        print("\n정렬 알고리즘을 선택하세요:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬 (성적 기준만 가능)")
        algorithm = int(input("알고리즘 번호를 선택하세요 (1/2/3/4): "))

        if algorithm == 4 and key != "성적":
            print("기수 정렬은 성적 기준 정렬만 가능합니다.")
            continue

        sorted_students = sort_students(students, algorithm, key)
        print("\n정렬된 결과:")
        for student in sorted_students:
            print(student)

if __name__ == "__main__":
    main()

