class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dict = {}
        rows = len(wall)
        for cur_row in wall:
            cur_boundary = 0
            for cur_brick in cur_row[:-1]:
                cur_boundary += cur_brick
                if cur_boundary in dict.keys():
                    dict[cur_boundary] += 1
                else:
                    dict[cur_boundary] = 1
        boundary_occ = dict.values()
        if boundary_occ:
            min_crossing = rows - max(boundary_occ)
        else:
            min_crossing = rows
        return min_crossing        