def number_for_vertex(n):
  return int(n)-1

class Node:
  
  def __init__(self, gender_num, fav_number):
    self.gender = gender_num
    self.F = fav_number 
    self.neighboorhood = list()

if __name__ == '__main__':

  num_houses = int(input())
  people_gender = list(map(int, input().split()))
  people_F = list(map(int, input().split()))
  houses = list()

  for gender, F in zip(people_gender, people_F):
    house = Node(gender, F)
    houses.append(house)
    
  for i in range(num_houses-1):
    vertex = list(map(number_for_vertex, input().split()))
    houses[vertex[0]].neighboorhood.append(vertex[1])
    houses[vertex[1]].neighboorhood.append(vertex[0])
    
  num_questions = int(input())

  for i in range(num_questions):
    count = 0
    pair = list(map(number_for_vertex, input().split()))
    pointer = pair[0]
    while pointer != pair[1] + 1:
      for n in houses[pointer].neighboorhood:
        if houses[pointer].gender != houses[n].gender and houses[pointer].F == houses[n].F:
          count += 1
      if pointer + 1 == len(houses):
        pointer = 0
      else:
        pointer += 1
    
    print(count)