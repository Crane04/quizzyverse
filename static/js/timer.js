var countdownTime = "{{ exam.duration }}" * 60;

// Get the countdown element from the HTML
var countdownElement = document.querySelector(".time-left");

// Set an interval to update the countdown every second
var countdownInterval = setInterval(function() {
// Convert the countdown time to hours and minutes
var hours = Math.floor(countdownTime / 60);
var minutes = countdownTime % 60;

// Format the countdown display
var countdownDisplay = hours.toString().padStart(2, "0") + " : " + minutes.toString().padStart(2, "0");

// Update the countdown element with the display text
countdownElement.innerHTML = countdownDisplay;

// Decrease the countdown time by 1 minute
countdownTime--;

// Stop the countdown when it reaches 0
if (countdownTime < 0) {
    clearInterval(countdownInterval);
    countdownElement.innerHTML = "00 : 00";
    document.querySelector("#hide_submit").click()
}
}, 1000);