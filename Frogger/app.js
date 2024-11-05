// Dom Objects
const timeDisplay = document.querySelector('#time-left');
const resultDisplay = document.querySelector('#results');
const StartPause = document.querySelector('#start-pause');
// list of all usable squares on the grid
const squares = document.querySelectorAll('.grid div');
// Begin at the middle of the most bottome row
let currentPosition = (squares.length - 1) - 4
// left and right  bound squares
const leftSquares = [72,63,54,45,36,27,18,9,0]
const rightSquares = [8,17,26,35,44,53,62,71,80]
// Has the Game started?
let gameStarted = false;
// list of all logs
const logsLeft = document.querySelectorAll('.log-left');
const logsRight = document.querySelectorAll('.log-right');
// create lists of cars in both directions
const carsRight = document.querySelectorAll('.car-right');
const carsLeft = document.querySelectorAll('.car-left');
// timer ID & time left (seconds)
let time = 10;
let timerId;
// timerId for interval checking if you've won or lost
let resultTimerId;
// create function to move frog
function moveFrog(e) {
    console.log('move')
    switch (e.key){
        case 'a':
            if(leftSquares.includes(currentPosition)){
                console.log('Move out of bound!')
                break;
            } else{
                squares[currentPosition].classList.remove('frog')
                currentPosition -= 1;
                squares[currentPosition].classList.add('frog')
                console.log(`current postion: ${currentPosition}`)
                break;
            }
        case 'd':
            if(rightSquares.includes(currentPosition)){
                console.log('Move out of bound!')
                break;
            } else{
                squares[currentPosition].classList.remove('frog')
                currentPosition += 1;
                squares[currentPosition].classList.add('frog')
                console.log(`current postion: ${currentPosition}`)
                break;
            }
        case 'w':
            if(currentPosition <= 8){
                console.log('out of bound!!')
                break;
            } else{
                squares[currentPosition].classList.remove('frog')
                currentPosition -= 9;
                squares[currentPosition].classList.add('frog')
                console.log(`current postion: ${currentPosition}`)
                break;
            }
        case 's':
            if(currentPosition > 71){
                console.log('out of bound!!')
                break;
            } else{
                squares[currentPosition].classList.remove('frog')
                currentPosition += 9;
                squares[currentPosition].classList.add('frog')
                console.log(`current postion: ${currentPosition}`)
                break;
            }

        default:
            console.log('something went wrong lol')
    }
}
// auto move the logs
function autoMoveObj(){
    //this function gets executed every 1000ms
    //time--;
    timeDisplay.textContent = time
    logsLeft.forEach((logsLeft) => moveLogsLeft(logsLeft))
    logsRight.forEach((logsRight) => moveLogsRight(logsRight))
    carsLeft.forEach((carLeft) => moveCarsLeft(carLeft))
    carsRight.forEach((carRight) => moveCarsRight(carRight))
}

// function for moving logs
function moveLogsLeft(logsLeft){
    switch(true){
        case logsLeft.classList.contains('l5'):
            logsLeft.classList.remove('l5')
            logsLeft.classList.add('l1')
            break;

        case logsLeft.classList.contains('l1'):
            logsLeft.classList.remove('l1')
            logsLeft.classList.add('l2')
            break

        case logsLeft.classList.contains('l2'):
            logsLeft.classList.remove('l2')
            logsLeft.classList.add('l3')
            break

        case logsLeft.classList.contains('l3'):
            logsLeft.classList.remove('l3')
            logsLeft.classList.add('l4')
            break

        case logsLeft.classList.contains('l4'):
            logsLeft.classList.remove('l4')
            logsLeft.classList.add('l5')
            break
        default:
            console.log('something went wrong')
    }
}
function moveLogsRight(logsRight){
    switch(true){
        case logsRight.classList.contains('l1'):
            logsRight.classList.remove('l1')
            logsRight.classList.add('l5')
            break;

        case logsRight.classList.contains('l5'):
            logsRight.classList.remove('l5')
            logsRight.classList.add('l4')
            break

        case logsRight.classList.contains('l4'):
            logsRight.classList.remove('l4')
            logsRight.classList.add('l3')
            break

        case logsRight.classList.contains('l3'):
            logsRight.classList.remove('l3')
            logsRight.classList.add('l2')
            break

        case logsRight.classList.contains('l2'):
            logsRight.classList.remove('l2')
            logsRight.classList.add('l1')
            break
        default:
            console.log('something went wrong')
    }
}
// function that moves cars
function moveCarsLeft(carLeft){
    switch (true){
        case carLeft.classList.contains('c1'):
            carLeft.classList.remove('c1')
            carLeft.classList.add('c2')
            break;
        case carLeft.classList.contains('c2'):
            carLeft.classList.remove('c2')
            carLeft.classList.add('c3')
            break;
        case carLeft.classList.contains('c3'):
            carLeft.classList.remove('c3')
            carLeft.classList.add('c1')
            break;
    
        default:
            console.log('i did something wrong')
    }
}
function moveCarsRight(carRight){
    switch (true){
        case carRight.classList.contains('c1'):
            carRight.classList.remove('c1')
            carRight.classList.add('c3')
            break;
        case carRight.classList.contains('c3'):
            carRight.classList.remove('c3')
            carRight.classList.add('c2')
            break;
        case carRight.classList.contains('c2'):
            carRight.classList.remove('c2')
            carRight.classList.add('c1')
            break;
    
        default:
            console.log('i did something wrong')
    }
}
// check for collisions and for points
function checkLoss(){
    if(squares[currentPosition].classList.contains('c2') || (squares[currentPosition].classList.contains('l4')) || (squares[currentPosition].classList.contains('l5'))){
        console.log('haha you lost!!!')
        squares[currentPosition].classList.remove('frog')
        resultDisplay.textContent = 'Youre a bum!'
        clearInterval(timerId)
        clearInterval(resultTimerId)
        document.removeEventListener('keydown', moveFrog)
        document.removeEventListener('click', startGame)
    }
    if(time === 0){
        resultDisplay.textContent = "You lose!"
        clearInterval(timerId)
        clearInterval(resultTimerId)
        document.removeEventListener('keydown', moveFrog)
        document.removeEventListener('click', startGame)
    }
}
// check if you win
function checkWin(){
    if(squares[currentPosition].classList.contains('ending-block')){
        resultDisplay.textContent = 'You Win!!!'
        clearInterval(timerId)
        clearInterval(resultTimerId)
        document.removeEventListener('keydown', moveFrog)
        document.removeEventListener('click', startGame)
    }
}
function checkResult(){
    checkLoss();
    checkWin();
}
function startGame(){
    // if timer id has already been initialized, (start button intitial pressed)
    if(timerId){
        clearInterval(timerId)
        timerId = null
        clearInterval(resultTimerId)
        resultTimerId = null
        document.removeEventListener('keydown', moveFrog)
    }else{
        // if the button hasnt been already pressed, 
        // intialize your timers and display user (frog)
        document.addEventListener('keydown', moveFrog)
        resultTimerId = setInterval(checkResult,50)
        timerId = setInterval(autoMoveObj,1000);
        squares[currentPosition].classList.add('frog')
    }
}

// add a smurf on the start/pause button
StartPause.addEventListener('click',startGame)
