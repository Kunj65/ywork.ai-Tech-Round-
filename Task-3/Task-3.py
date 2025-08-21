def maximalRectangleWithCoords(matrix):
    if not matrix:
        return 0, None
    
    n = len(matrix[0])
    heights = [0] * (n + 1)  # +1 sentinel
    max_area = 0
    rect_coords = None  # (top_row, left_col, bottom_row, right_col)

    for row_index, row in enumerate(matrix):
        # Build heights histogram
        for i in range(n):
            if row[i] == "1":
                heights[i] += 1
            else:
                heights[i] = 0
        
        stack = [-1]
        for i in range(n + 1):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                area = h * w
                if area > max_area:
                    max_area = area
                    # bottom row is row_index
                    bottom = row_index
                    top = row_index - h + 1
                    left = stack[-1] + 1
                    right = i - 1
                    rect_coords = (top, left, bottom, right)
            stack.append(i)

    return max_area, rect_coords


def printMatrixWithRectangle(matrix, coords):
    top, left, bottom, right = coords
    for i, row in enumerate(matrix):
        row_str = ""
        for j, val in enumerate(row):
            if top <= i <= bottom and left <= j <= right and val == "1":
                row_str += f"[{val}]"  # highlight rectangle 1's
            else:
                row_str += f" {val} "
        print(row_str)


# Example
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

max_area, coords = maximalRectangleWithCoords(matrix)
print("Max Area:", max_area)
print("Rectangle Coordinates (top, left, bottom, right):", coords)
print("\nMatrix with rectangle highlighted:")
printMatrixWithRectangle(matrix, coords)
