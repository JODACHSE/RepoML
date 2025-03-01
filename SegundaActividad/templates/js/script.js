// Obtén el canvas y el contexto
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const gridSize = 20;
const canvasSize = canvas.width;

// Variables globales del juego
let snake, direction, food, score, paused, gameStarted, gameInterval;

// Inicializa las variables del juego
function initializeGameVariables() {
  snake = [
    { x: 160, y: 200 },
    { x: 140, y: 200 },
    { x: 120, y: 200 },
  ];
  direction = { x: gridSize, y: 0 };
  food = { x: 0, y: 0 };
  score = 0;
  paused = false;
  updateScore();
  randomFood();
}

// Actualiza el puntaje en el DOM
function updateScore() {
  document.getElementById("scoreValue").innerText = score;
}

// Genera posición aleatoria para la comida
function randomFood() {
  food.x = Math.floor(Math.random() * (canvasSize / gridSize)) * gridSize;
  food.y = Math.floor(Math.random() * (canvasSize / gridSize)) * gridSize;
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

  // Colisión con los límites del canvas
  if (head.x < 0 || head.x >= canvasSize || head.y < 0 || head.y >= canvasSize) {
    return gameOver();
  }
  // Colisión con el cuerpo de la serpiente
  for (let i = 0; i < snake.length; i++) {
    if (head.x === snake[i].x && head.y === snake[i].y) {
      return gameOver();
    }
  }

  snake.unshift(head);

  // Si la serpiente come la comida
  if (head.x === food.x && head.y === food.y) {
    score++;
    updateScore();
    randomFood();
  } else {
    snake.pop();
  }
}

// Bucle principal del juego
function gameLoop() {
  if (paused) return;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawFood();
  updateSnake();
  drawSnake();
}

// Inicia el juego (oculta overlay y arranca el loop)
function startGame() {
  initializeGameVariables();
  document.getElementById("gameOverOverlay").style.display = "none";
  gameInterval = setInterval(gameLoop, 100);
}

// Detiene el juego
function stopGame() {
  clearInterval(gameInterval);
}

// Se llama cuando ocurre un Game Over
function gameOver() {
  stopGame();
  document.getElementById("gameOverOverlay").style.display = "flex";
}

// Reinicia el juego sin recargar la página
function restartGame() {
  stopGame();
  initializeGameVariables();
  document.getElementById("gameOverOverlay").style.display = "none";
  gameInterval = setInterval(gameLoop, 100);
}

// Control de teclas:
// Inicia el juego al presionar Space y permite mover la serpiente una vez iniciado
document.addEventListener("keydown", function (event) {
  if (!gameStarted && event.code === "Space") {
    gameStarted = true;
    startGame();
    return;
  }
  
  if (gameStarted && !paused) {
    switch (event.key) {
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
  }
});

// Botón de pausa/reanudar
document.getElementById("pauseBtn").addEventListener("click", function () {
  if (!gameStarted) return;
  paused = !paused;
  this.innerText = paused ? "Reanudar" : "Pausar";
});
