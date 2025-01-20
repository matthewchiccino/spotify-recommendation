const apiUrl = "http://127.0.0.1:8080/submit"

// Get references to the elements
const startButton = document.getElementById('startQuizButton');
const quizStartDiv = document.getElementById('quizStart');
const quizContentDiv = document.querySelector('.quiz-content');
const buttons = document.querySelectorAll('.quiz-button');  // Get all quiz buttons
const submitButton = document.getElementById('submitQuizButton');

let answers = {};  // Initialize the answers object to hold question answers
let answeredCount = 0;  // Counter to track how many questions have been answered

// Function to start the quiz
function startQuiz() {
    quizStartDiv.style.display = 'none';  // Hide the start quiz section
    quizContentDiv.style.display = 'block';  // Show the quiz questions
}

// Function to submit the quiz and output the JSON result
function submitQuiz() {
    const jsonString = JSON.stringify(answers);  // Convert the answers object to JSON string
    console.log(jsonString);  // You can display or send the JSON as needed
    if (Object.keys(answers).length === 7) {  // Adjust this based on the number of questions

        console.log("All answers are guessed:", answers);
        fetch(apiUrl, {
            method: 'POST',  // Change GET to POST
            headers: {
                'Content-Type': 'application/json',
            }, 
            body: JSON.stringify(answers),  // Send the answers in the request body
        })
        .then(response => response.json()) // Parse the JSON response
        .then(data => {
            processApiResponse(data); // Pass the data to the processing function
        })
        .catch(error => {
            console.error('Error:', error); // Handle any errors
            alert('There was an error with the API call');
        });
    } else {
        console.log("Not all answers are guessed. Current answers:", answers);
        alert('Make sure to answer every question');
    }
}

// Add click event to the start button
startButton.addEventListener('click', startQuiz);
submitButton.addEventListener('click', submitQuiz);

// Add keyboard event to start the quiz when Enter is pressed (but only once)
document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter' && !quizContentDiv.style.display) {  // Ensure quiz isn't already started
        startQuiz();
    }
});

// Event listener for each quiz button click to save the answer
buttons.forEach((button) => {
    button.addEventListener('click', () => {
        // Get the question number dynamically from the closest .question element
        const questionNumber = button.closest('.question').getAttribute('data-question-id');  // Assuming each .question has a unique data-question-id

        // Get the answer value from the button's data-answer attribute
        const answer = button.getAttribute('data-answer');  

        // If this is a new answer or someone is changing their answer, update the answers object
        if (!answers[questionNumber]) {
            answeredCount++;  // Increment counter only if the answer hasn't been recorded yet
        } else if (answers[questionNumber] !== answer) {
            // If the answer is changed, no need to increment `answeredCount`, just update it
            answers[questionNumber] = answer;
        }

        // Update the answer for the specific question
        answers[questionNumber] = answer;

        // Log the updated answers for debugging
        console.log(answers);
    });
});
