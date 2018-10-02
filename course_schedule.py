'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


'''

from collections import defaultdict

def course_schedule(num_courses, prereq):
    
    ## set up graph wit adj_list and status of vertices
    graph = defaultdict(list)
    status = defaultdict(int)

    for nxt, pre in prereq:
        graph[pre].append(nxt)

    for i in range(num_courses):
        status[i] = 0

    def dfs(v):
        if status[v] == -1:
            return True
        if status[v] == 1:
            return False
        
        status[v] = 1

        for u in graph[v]:
            if dfs(u) == False:
                return False
        
        status[v] = -1
        return True
    
    for v in range(num_courses):
        if dfs(v) == False:
            return False
    
    return True

num_courses = 2
prereq = [[0,1]]

print(course_schedule(num_courses, prereq))

num_courses_2 = 2
prereq_2 = [[1,0],[0,1]]

print(course_schedule(num_courses_2, prereq_2))

    
    
    
    