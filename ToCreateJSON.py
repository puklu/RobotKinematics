import json


solution = {} 

solution["q1"] = [[0.707106781186548], [0.707106781186548], [0], [0]]
solution["q2"] = [[0.707106781186548], [0], [0.707106781186548], [0]]
solution["q21"]=[[0.5], [0.5], [0.5], [-0.5]]

solution["R1"] = [[1.0, 0, 0], [0, 0, -1.0], [0, 1.0, 0]]
solution["R2"] = [[0, 0, 1.0], [0, 1.0, 0], [-1.0, 0, 0]]
solution["R21"]=[[0, 1.0, 0], [0, 0, -1.0], [-1.0, 0, 0]]


j = json.dumps(solution)
with open("hw06.json", "w") as outfile:
    outfile.write(j)
    outfile.close()