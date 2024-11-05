
const gridDisplay = document.querySelector('.grid')
const scoreDisplay = document.querySelector('#score')
const blockWidth = 100
const blockHeight = 20
const boardWidth = 600
const boardHeight = 300
const ballDiameter = 20
const userStart = [230,10]
const ballStart = [300,35]
let currentPostion = userStart
let currentBallPosition = ballStart
let ballTimerId;
let xDirection = -2;
let yDirection = 2;
let score = 0;



//create my blocks
class Block{
    constructor(xAxis,yAxis){
        this.bottomLeft = [xAxis,yAxis]
        this.bottomRight = [xAxis + blockWidth,yAxis]
        this.topRight = [xAxis + blockWidth, yAxis + blockHeight]
        this.topLeft = [xAxis,yAxis + blockHeight]
    }
}
// instantiate all my blocks
const myBlocks = [
    new Block(10,250),
    new Block(120,250),
    new Block(230,250),
    new Block(340,250),
    new Block(450,250),
    new Block(10,220),
    new Block(120,220),
    new Block(230,220),
    new Block(340,220),
    new Block(450,220),
    new Block(10,190),
    new Block(120,190),
    new Block(230,190),
    new Block(340,190),
    new Block(450,190),
]
//draw all my blocks
function addBlock(){
    for(let i = 0; i < myBlocks.length; i++){
        const block = document.createElement('div')
        block.classList.add('block')
        block.style.bottom = myBlocks[i].bottomLeft[1] + 'px'
        block.style.left = myBlocks[i].bottomLeft[0] + 'px'
        gridDisplay.appendChild(block)
    }
}
addBlock()

// Add user
const user = document.createElement('div')
user.classList.add('user')
gridDisplay.appendChild(user)

//Draw User
function drawUser(){
    user.style.bottom = currentPostion[1] + 'px';
    user.style.left = currentPostion[0] + 'px';
}
drawUser()

//Move User


document.querySelector('html').addEventListener('keydown', e =>{
    if(e.key == 'a') {
        if (currentPostion[0] > 0){
            currentPostion[0] -= 10;
        }
        
    } else if(e.key == 'd') {
        if (currentPostion[0] < 500){
            currentPostion[0] += +10;
        }
        
    }
    drawUser()
})
//create Ball
const ball = document.createElement('div');
ball.classList.add('ball')
gridDisplay.appendChild(ball)

//Draw Ball
function drawBall(){
    ball.style.left = currentBallPosition[0] + 'px';
    ball.style.bottom = currentBallPosition[1] + 'px';
}
drawBall()

//Make ball move
function moveBall(){
    currentBallPosition[0] += xDirection;
    currentBallPosition[1] += yDirection;
    drawBall();
    checkForCollisions()
}
//Make ball move continuosly
ballTimerId = setInterval(moveBall,30);

//Check for when a ball hits a wall
function checkForCollisions(){
    // check for block collisions
    for (let i = 0; i < myBlocks.length; i++){
        if (
            (currentBallPosition[0] > myBlocks[i].bottomLeft[0] && currentBallPosition[0] < myBlocks[i].bottomRight[0]) && 
            ((currentBallPosition[1] + ballDiameter) > myBlocks[i].bottomLeft[1] && currentBallPosition[1] < myBlocks[i].topLeft[1])
            ) {
            const allBlocks = Array.from(document.querySelectorAll('.block'))
            allBlocks[i].classList.remove('block');
            myBlocks.splice(i,1)
            changeDirection();
            score++
            scoreDisplay.innerHTML = score
        }
    }
    //check for user collision
    if (
        (currentBallPosition[0] > currentPostion[0] && currentBallPosition[0] < currentPostion[0]+ blockWidth) &&
        (currentBallPosition[1] > currentPostion[1] && currentBallPosition[1] < currentPostion[1]+ blockHeight)
    ){
        changeDirection();
    }

    //check for right corner wall
    if (currentBallPosition[0] >= (boardWidth-ballDiameter) ||
        currentBallPosition[1] >= (boardHeight - ballDiameter) ||
        currentBallPosition[0] <=0) {
        changeDirection();
    
    }

    if(currentBallPosition[1] <= 0) {
        clearInterval(ballTimerId)
        scoreDisplay.innerHTML = `You Lose! your score was ${score}`
    }
}

//Change Direction
function changeDirection(){
    //if ball is moving positively (x) and touches right wall
    if (xDirection == 2 && yDirection == 2){
        yDirection = -2;
        return  
        //if ball is moving positively (y) and hits upper wall
    } else if(xDirection == 2 && yDirection == -2){
        xDirection = -2;
        return
        //if ball is moving in the negative (x) direction and touches wall
    } else if (xDirection == -2 && yDirection == -2){
        yDirection = 2;
        return
        //if ball is moving in the negative (y) direction and touches wall
    } else if(xDirection == -2 && yDirection ==2){
        xDirection = 2
    }
}
