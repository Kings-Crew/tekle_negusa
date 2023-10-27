// Listens for the document's content to be fully loaded.
document.addEventListener("DOMContentLoaded", function() {

    // Creates a counter for the tens' place and assigns it to the variable.
    const counterTens = createCounter('[data-js="counter-tens"]');
    
    // Creates a counter for the ones' place and assigns it to the variable.
    const counterOnes = createCounter('[data-js="counter-ones"]');

    // A function that initializes and returns a counter object.
    function createCounter(selector) {

        // Selects the main counter element based on the provided selector.
        const el = document.querySelector(selector);
        
        // Selects the element showing the current value of the counter.
        const current = el.querySelector('[data-js="current"]');
        
        // Selects the element showing the next value of the counter.
        const next = el.querySelector('[data-js="next"]');
        
        // Declares a variable to keep track of the current count.
        let count;

        // A function to update the counter's value.
        function update(value) {
            
            // If the new value is the same as the old, do nothing.
            if (count === value) return;
            
            // Update the count variable and display the new value.
            count = value;
            next.innerHTML = count;
            
            // Add a CSS class to animate the changing of the counter's value.
            el.classList.add('is-changing');

            // After 210ms, update the displayed value and remove the animation class.
            setTimeout(() => {
                current.innerHTML = next.innerHTML;
                el.classList.remove('is-changing');
            }, 210);
        }

        // Return the update function so it can be used outside the createCounter function.
        return { update };
    }

    // Establishes a connection to the server using Server-Sent Events (SSE) to the specified endpoint.
    const evtSource = new EventSource("/counter-increment");

    // Defines a callback for when a new message is received from the server.
    evtSource.onmessage = function(event) {
        
        // Parses the received data as an integer.
        const data = parseInt(event.data, 10);
        
        // Logs the received data to the console.
        console.log("Received data:", data); 

        // Updates the tens' place of the counter.
        counterTens.update(Math.floor(data / 10));
        
        // Updates the ones' place of the counter.
        counterOnes.update(data % 10);
    };
});
