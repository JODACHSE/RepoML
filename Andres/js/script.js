const questions = [
  {
    question: "¿Cuál es la capital de España?",
    answers: [
      { text: "Madrid", correct: true },
      { text: "París", correct: false },
      { text: "Londres", correct: false },
      { text: "Roma", correct: false },
    ],
  },
  {
    question: "¿Quién pintó la Mona Lisa?",
    answers: [
      { text: "Vincent van Gogh", correct: false },
      { text: "Pablo Picasso", correct: false },
      { text: "Leonardo da Vinci", correct: true },
      { text: "Salvador Dalí", correct: false },
    ],
  },
  {
    question: "¿Cuál es el río más largo del mundo?",
    answers: [
      { text: "Amazonas", correct: true },
      { text: "Nilo", correct: false },
      { text: "Yangtsé", correct: false },
      { text: "Misisipi", correct: false },
    ],
  },
  {
    question: "¿En qué año comenzó la Segunda Guerra Mundial?",
    answers: [
      { text: "1939", correct: true },
      { text: "1945", correct: false },
      { text: "1914", correct: false },
      { text: "1950", correct: false },
    ],
  },
  // Puedes seguir agregando más preguntas aquí
];

const questionElement = document.getElementById("question");
const answerButton = document.getElementById("answer-buttons");
const nextButton = document.getElementById("next-btn");

let currentQuestionIndex = 0;
let score = 0;

function starQuiz() {
  currentQuestionIndex = 0;
  score = 0;
  nextButton.innerHTML = "Next";
  showQuestion();
}

function showQuestion() {
  resetState(); 
  let currentQuestion = questions[currentQuestionIndex];
  let questionNo = currentQuestionIndex + 1;
  questionElement.innerHTML = questionNo + ". " + currentQuestion.question;

  currentQuestion.answers.forEach((answer) => {
    const button = document.createElement("button");
    button.innerHTML = answer.text;
    button.classList.add("btn");
    answerButton.appendChild(button);
    if (answer.correct) {
      button.dataset.correct = answer.correct;
    }
    button.addEventListener("click", selectAnswer);
  });
}

function resetState() {
  nextButton.style.display = "none";
  while (answerButton.firstChild) {
    answerButton.removeChild(answerButton.firstChild);
  }
}

function selectAnswer(e) {
  const selectBtn = e.target;
  const isCorrect = selectBtn.dataset.correct === "true";
  if (isCorrect) {
    selectBtn.classList.add("correct");
    score++;
  } else {
    selectBtn.classList.add("incorrect");
  }
  Array.from(answerButton.children).forEach((button) => {
    if (button.dataset.correct === "true") {
      button.classList.add("correct");
    }
    button.disabled = true;
  });
  nextButton.style.display = "block";
}

function showScore() {
  resetState();
  questionElement.innerHTML = `you scored ${score} out of ${questions.length}!`;
  nextButton.innerHTML = "Play Again";
  nextButton.style.display = "block";
}

function handleNextButton() {
  currentQuestionIndex++;
  if (currentQuestionIndex < questions.length) {
    showQuestion();
  } else {
    showScore();
  }
}
nextButton.addEventListener("click", () => {
  if (currentQuestionIndex < questions.length) {
    handleNextButton();
  } else {
    starQuiz();
  }
});

starQuiz();