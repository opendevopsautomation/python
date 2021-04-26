import heapq
class Solution:
    #TC: nlogn
    #SC: n
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        heapify(heap)
        flag=0
        for i in range(len(heights)-1):
            diff=heights[i+1] - heights[i]
            if heights[i+1] <= heights[i]: continue
            
            elif diff <= bricks:
                bricks-=diff
                heappush(heap, -1*(diff)) # multiply with -1 to make it work like max heap
                
            elif ladders > 0:
                if len(heap):
                    if (-1*heap[0]) > diff:
                        a=(-1*heappop(heap))
                        bricks+=a
                        heappush(heap,-1*(diff))
                        bricks-=diff
                ladders-=1
            else:
                flag=1
                break
        return i if flag==1 else len(heights)-1             