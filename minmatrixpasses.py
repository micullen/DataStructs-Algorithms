from structs import Queue

# Function to check whether given coordinates is a valid cell or not
def is_valid(i, j):
    return (0 <= i < M) and (0 <= j < N)

# Below lists details all 4 possible movements from a cell
# (top, right, bottom, and left)
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

# Returns true if the matrix contains at least one negative value
def has_negative(matrix):
    for i in range(M):
        for j in range(N):
            z = matrix[i][j]
            if matrix[i][j] < 0:
                return True
    return False

def convert(matrix):
    queue = Queue()

    # Populate queue with positive numbers
    for i in range(M):
        for j in range(N):
            if matrix[i][j] > 0:
                queue.enqueue([i, j])

    passes = 0
    while True:

        queue_copy = queue

        temp = []
        for i in range(queue_copy.length()):
            x, y = queue_copy.dequeue()

            # Add all new positive numbers within the matrix to the queue
            for k in range(4):
                p = is_valid(x+row[k], y + col[k])
                if is_valid(x + row[k], y + col[k]):
                    q = matrix[x + row[k]][y + col[k]]
                if is_valid(x+row[k], y + col[k]) and matrix[x + row[k]][y + col[k]] < 0:
                    temp.append([x+row[k], y + col[k]])
                    matrix[x + row[k]][y + col[k]] *= -1

        # So we don't repeat over the values changed in one pass
        for val in temp:
            queue.enqueue(val)
        passes += 1
        bo = has_negative(matrix)
        if not has_negative(matrix):
            break

    return passes


matrix = [
    [-1, -9, 0, -1, 0],
    [-8, -3, -2, 9, -7],
    [2, 0, 0, -6, 0],
    [0, -7, -3, 5, -4]
]

(M, N) = (len(matrix), len(matrix[0]))
passes = convert(matrix)
print(passes)
