const apiUrl = "https://spotify-recommendation-plsf.onrender.com/submit"

// Get references to the elements
const startButton = document.getElementById('startQuizButton');
const quizStartDiv = document.getElementById('quizStart');
const quizContentDiv = document.querySelector('.quiz-content');
const buttons = document.querySelectorAll('.quiz-button');  // Get all quiz buttons
const submitButton = document.getElementById('submitQuizButton');
const resultsDiv = document.getElementById('results');
const resultsContentDiv = document.getElementById('resultsContent');

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
            method: 'POST',  
            headers: {
                'Content-Type': 'application/json',
            }, 
            body: JSON.stringify(answers),  // Send the answers in the request body
        })
        .then(response => response.json()) // Parse the JSON response
        .then(data => {
            console.log('API Response:', data); // Log the response for debugging
            displayArtistInfo(data); // Display the results
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


        // Get the question element
        const questionElement = button.closest('.question');
        
        // Remove the 'selected' class from all buttons within the same question
        const allButtonsInQuestion = questionElement.querySelectorAll('.quiz-button');
        allButtonsInQuestion.forEach(btn => btn.classList.remove('selected'));

        // Add the 'selected' class to the clicked button
        button.classList.add('selected');


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

// Function to display artist info
const displayArtistInfo = (artistData) => {
    // Get the artist data from the response
    const artist = artistData.message; // Adjust to match the structure of your API response

    // Check if artist data is valid
    if (!artist || !artist.name || !artist.external_urls || !artist.images) {
        console.error('Invalid artist data:', artistData);
        alert('No valid artist data found');
        return;
    }

    // Update the artist name
    const artistNameElement = document.getElementById("artist-name");
    artistNameElement.textContent = artist.name;

    // Update the Spotify link
    const spotifyLink = document.getElementById("spotify-link");
    spotifyLink.href = artist.external_urls.spotify;

    // Update the artist image
    const artistImage = document.getElementById("artist-image");
    const imageUrl = artist.images[0]?.url || ''; // Use the first image, or fallback to an empty string
    artistImage.src = imageUrl;
    artistImage.alt = `${artist.name} image`;

    // Show the results section
    const resultsDiv = document.getElementById("results");
    quizContentDiv.style.display = 'none'; // Hide the quiz section
    resultsDiv.style.display = 'block'; // Make the results section visible
};

document.getElementById('spotify-link').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default behavior of the link if needed
    const spotifyLink = document.getElementById('spotify-link');
    const linkHref = spotifyLink.href; // Access the href property
    console.log('Spotify link:', linkHref); // Log the link to the console
    window.open(linkHref, '_blank'); // Open the link in a new tab
});

document.getElementById('homeButton').addEventListener('click', function() {
    resultsDiv.style.display = 'none';
    quizStartDiv.style.display = 'block';
});