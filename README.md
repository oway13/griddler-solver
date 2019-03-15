# griddler-solver

Proposed First Algorithm (Expensive)
    
    -While not solved
        
        --For each row and column
            
            ---find all possible permutations of spaces with runs of the required length in the required order
                
                ----if there are spaces already marked, only use the combinations that contain that mark
            
            ---Mark all unmarked spaces that exist in every permutation that was used
    
Storing Griddlers Row/Col Required Lengths 
    
    Ordering of values will be the required ordering of runs
    
    Two 2D Matrices
    
    val1, val2
    
    val1, val2, val3
    
    val1, val2
    
    val1, val2, val3, val4
    
    val1
    
    ...

    
    One 2D Matrix
    1 = marked
    0 = unmarked