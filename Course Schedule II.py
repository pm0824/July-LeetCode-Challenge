'''
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
 Hint #1  
This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
 Hint #2  
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
 Hint #3  
Topological sort could also be done via BFS.
'''

#Solution:
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        zero_in_degree_queue, in_degree, out_degree = collections.deque(), {}, {}
        
        for i, j in prerequisites:
            if i not in in_degree:
                in_degree[i] = set()
            if j not in out_degree:
                out_degree[j] = set()
            in_degree[i].add(j)
            out_degree[j].add(i)
        
        
      
        for i in range(numCourses):
            if i not in in_degree:
                zero_in_degree_queue.append(i)
       
        res=[]
        while zero_in_degree_queue:
           
            prerequisite = zero_in_degree_queue.popleft()
            res.append(prerequisite)
            if prerequisite in out_degree:
                for course in out_degree[prerequisite]:
                    in_degree[course].discard(prerequisite)
                    if not in_degree[course]:
                        zero_in_degree_queue.append(course)
            
                del out_degree[prerequisite]
            
                
        if out_degree:
            return []
        return res
        
        
        
        
