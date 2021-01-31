import React, {useRef, useCallback} from 'react'; 
import produce from 'immer';

const NUM_ROW = 3;
const NUM_COL = 3;

const generateEmptyGrid = () => {
  const rows = []; 
  for (var i = 0; i < NUM_ROW; i++) {
    rows.push(Array.from(Array(NUM_COL), ()=> 0 ))
  }
  return rows
}

function App() {
  const {useEffect, useState} = React;
  const [grid, setGrid] = useState(() => {
    return generateEmptyGrid();
  });
  const [isXNext, setIsXNext] = useState(true);
  const [winner, setWinner] = useState(0);
  const clear = () => {
    setGrid(generateEmptyGrid());
    setIsXNext(true);
  }
  const checkWinner = useCallback(
    () => {
      for(var i = 0; i < NUM_ROW; i++){
        var sum = grid[i].reduce((a, b) => {return a + b;}, 0)
        if (sum === 3){
          setWinner(1);
          console.log("Player 2 Won");
          clear();
          
        }
        else if (sum === -3){
          setWinner(2);
          console.log("Player 1 Won");
          clear();
        }
      }
    },
    [isXNext],
  )

  useEffect(() => {
    checkWinner()
  }, [isXNext]
  )

  return (
    <>
      <button onClick = {clear}>Clear</button>
      <hr></hr>
      <div 
          style={{
            display:"grid",
            gridTemplateColumns: `repeat(${NUM_COL}, 100px)`
          }}
        >
          {grid.map((rows, i) => 
            rows.map((col, k) => (
              <div 
              key = {`${i}-${k}`}
              onClick={()=>{
                const newGrid = produce(grid, gridCopy => {
                  if (grid[i][k] === 0){
                    gridCopy[i][k] = isXNext ? -1:1;
                    setIsXNext(!isXNext);
                  }
                  
                })
                setGrid(newGrid);
              }}
                style={{
                  width: 100, 
                  height: 100, 
                  color: "white",
                  backgroundColor: grid[i][k] ? grid[i][k] === -1 ? "blue":"red":undefined,
                  //content: grid[i][k] ? 'x': 'o',
                  border: "2px solid black",
                }}
              />
            ))
          )}
        </div>
      </>
  );
}

export default App;
