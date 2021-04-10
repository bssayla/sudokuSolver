var sudokuBoard = [
    [0,0,0,7,3,4,0,0,0],
    [9,3,0,5,0,6,7,0,2],
    [5,7,4,9,0,8,1,6,3],
    [0,5,3,1,4,0,0,9,7],
    [0,0,0,0,0,0,0,3,1],
    [6,1,7,8,9,3,0,0,4],
    [0,4,6,2,8,1,9,0,5],
    [0,9,0,4,6,0,3,2,8],
    [2,8,0,0,7,9,0,0,6]
    ];
    function squareIsValid(board,y,x,n){
        //search horizotal
        for(let i = 0 ; i < 9 ; i++ ){
            if ( board[y][i] == n ){return false}
        }
        //search vertical
        for (let i = 0 ; i < 9 ; i++ ){
            if (board[i][x] == n){return false}
        }
        //search in the square
         let x0 = Math.floor(x/3) * 3
         let y0 = Math.floor(y/3) * 3
         for (let i = 0; i < 3; i++) {
             for ( let j = 0; j < 3; j++ ) {
                if (board[y0+i][x0 + j] == n){return false}        
             }   
         }
         return true
    }
    function solveTheBoard(board){
        for ( let y = 0 ; y < 9 ; y++ ){
            for ( let x = 0 ; x < 9 ; x++ ){
                if (board[y][x] == 0 ){
                    for(let n = 1 ; n < 10 ; n++ ){
                        if (squareIsValid(board,y,x,n)){
                            board[y].splice(x,1,n);
                            solveTheBoard(board);
                            board[y].splice(x,1,0);
                        }
                    }
                    return
                }
            }
        }
       console.log(board);
    }
    solveTheBoard(sudokuBoard);