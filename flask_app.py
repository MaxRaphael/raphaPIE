from flask import Flask
import numpy as np
import ghhops_server as hs


app = Flask(__name__)
hops = hs.Hops(app)

@app.route('/StringMatch')
def hello_world():
    return 'Link Start'

@hops.component(
    "/StringMatch",
    name="StringMatch",
    description="This tool compares strings and returns a similarity score",
    inputs=[
        hs.HopsString("String_1", "String_1", "String_1"),
        hs.HopsString("String_2", "String_1", "String_1"),

        
    ],
    outputs=[
        hs.HopsString("Similarity_Ratio", "Similarity_Ratio", "Similarity_Ratio"),
        hs.HopsString("Match_closeness","Match_closeness", "Match_closeness"),
    ]
)

def StringMatch(String_1,String_2):
    str1 = str(String_1)
    str2 = str(String_2)
    
    def levenshtein_ratio_and_distance(s, t, ratio_calc = False):

        # Initialize matrix of zeros
        rows = len(s)+1
        cols = len(t)+1
        distance = np.zeros((rows,cols),dtype = int)

        # Populate matrix of zeros with the indeces of each character of both strings
        for i in range(1, rows):
            for k in range(1,cols):
                distance[i][0] = i
                distance[0][k] = k

        # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
        for col in range(1, cols):
            for row in range(1, rows):
                if s[row-1] == t[col-1]:
                    cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
                else:
                    # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                    # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                    if ratio_calc == True:
                        cost = 2
                    else:
                        cost = 1
                distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                        distance[row][col-1] + 1,          # Cost of insertions
                                        distance[row-1][col-1] + cost)     # Cost of substitutions
        if ratio_calc == True:
            # Computation of the Levenshtein Distance Ratio
            Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
            return Ratio
        else:
            # print(distance) 
            # insertions and/or substitutions
            # This is the minimum number of edits needed to convert string a to string b
            return "The strings are {} edits away from matching".format(distance[row][col])
    Distance = levenshtein_ratio_and_distance(str1.lower(),str2.lower())
    Ratio = levenshtein_ratio_and_distance(str1.lower(),str2.lower(),ratio_calc = True)
    match = 0
    if Ratio == 1:
        match = "The strings match!"
        Distance = match
    
    return Ratio, Distance

    
if __name__ == '__main__':
    app.run()
