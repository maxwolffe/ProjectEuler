import heapq


triangle = """75
                         95 64
                       17 47 82
                     18 35 87 10
                   20 04 82 47 65
                 19 01 23 75 03 34
                88 02 77 73 07 63 67
              99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


tree = [[int(n) for n in line.split()] 
		   for line in triangle.split('\n')]

class PriorityQueue:
   """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.

      Note that this PriorityQueue does not allow you to change the priority
      of an item.  However, you may insert the same item multiple times with
      different priorities.
    """
   def  __init__(self):
       	self.heap = []
        self.count = 0

   def push(self, item, priority):
       # FIXME: restored old behaviour to check against old results better
        # FIXED: restored to stable behaviour
        entry = (priority, self.count, item)
        # entry = (priority, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

   def pop(self):
       (_, _, item) = heapq.heappop(self.heap)
        #  (_, item) = heapq.heappop(self.heap)
       return item

   def isEmpty(self):
       return len(self.heap) == 0


def uniformCostSearch():
   total_depth = len(tree) - 1
   depth = 0
   lateral_position = 0
   previously_visited = set()
   stack = PriorityQueue()
   position = (depth, lateral_position)
   previously_visited.add(position)
   total_cost = 0
   plan = []

   while depth != total_depth - 1:
       possibilities = ([(depth + 1, lateral_position), tree[depth + 1][lateral_position]], [(depth + 1, lateral_position + 1), tree[depth + 1][lateral_position + 1]])
       visitable = False

       for fringenode in possibilities:
           fringe_name = fringenode[0]
           if fringe_name not in previously_visited:
               visitable = True
               fringe_cost = 100 - fringenode[1]
               if depth != total_depth:
                   previously_visited.add(fringe_name)
               stack.push((fringenode, plan + [fringenode[1],], total_cost + fringe_cost), total_cost + fringe_cost)

       popped = stack.pop()
       print(popped)
       lateral_position = popped[0][0][1]
       depth = popped[0][0][0]
       total_cost = popped[2]
       plan = popped[1]

   plan.append(tree[0][0])
   return plan

print(uniformCostSearch())


