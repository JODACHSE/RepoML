// Obtén el canvas usando el ID "gameCanvas"
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const gridSize = 20;
const canvasSize = canvas.width;

// Variables globales
let snake = [
  { x: 160, y: 200 },
  { x: 140, y: 200 },
  { x: 120, y: 200 },
];
let direction = { x: gridSize, y: 0 };
let food = { x: 0, y: 0 };
let score = 0;  // Variable para el puntaje

// Genera posición aleatoria para la comida
function randomFood() {
  food.x = Math.floor(Math.random() * (canvasSize / gridSize)) * gridSize;
  food.y = Math.floor(Math.random() * (canvasSize / gridSize)) * gridSize;
}

// Actualiza el texto del score en el HTML
function updateScore() {
  document.getElementById("scoreValue").innerText = score;
}

// Dibuja la serpiente
function drawSnake() {
  ctx.fillStyle = "green";
  snake.forEach(part => {
    ctx.fillRect(part.x, part.y, gridSize, gridSize);
  });
}

// Dibuja la comida
function drawFood() {
  ctx.fillStyle = "red";
  ctx.fillRect(food.x, food.y, gridSize, gridSize);
}

// Actualiza la posición de la serpiente y maneja colisiones
function updateSnake() {
  const head = { x: snake[0].x + direction.x, y: snake[0].y + direction.y };

  // Verifica colisiones con los límites del canvas
  if (head.x < 0 || head.x >= canvasSize || head.y < 0 || head.y >= canvasSize) {
    return gameOver();
  }

  // Verifica colisiones con el cuerpo
  for (let i = 0; i < snake.length; i++) {
    if (head.x === snake[i].x && head.y === snake[i].y) {
      return gameOver();
    }
  }

  snake.unshift(head);

  // Comprueba si la serpiente ha comido la comida
  if (head.x === food.x && head.y === food.y) {
    score++;       // Incrementa el score
    updateScore(); // Actualiza el texto del score en el HTML
    randomFood();  // Genera nueva posición de la comida
  } else {
    snake.pop();
  }
}

// Función de fin de juego
function gameOver() {
  alert("¡Game Over!");
  document.location.reload();
}

// Control de teclas para mover la serpiente
document.addEventListener("keydown", function(event) {
  switch(event.key) {
    case "ArrowUp":
      if (direction.y === 0) direction = { x: 0, y: -gridSize };
      break;
    case "ArrowDown":
      if (direction.y === 0) direction = { x: 0, y: gridSize };
      break;
    case "ArrowLeft":
      if (direction.x === 0) direction = { x: -gridSize, y: 0 };
      break;
    case "ArrowRight":
      if (direction.x === 0) direction = { x: gridSize, y: 0 };
      break;
  }
});

// Bucle principal del juego
function gameLoop() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawFood();
  updateSnake();
  drawSnake();
}

// Inicializa la comida y el score, luego inicia el bucle
randomFood();
updateScore();
setInterval(gameLoop, 100);
