document.addEventListener("DOMContentLoaded", function() {
    var counterTens = new Counter(document.querySelector('[data-js="counter-tens"]')),
        counterOnes = new Counter(document.querySelector('[data-js="counter-ones"]'));

    function Counter(el) {
        var current = el.querySelector('[data-js="current"]'),
            next = el.querySelector('[data-js="next"]'),
            count,
            timeout;

        function update(value) {
            if (count === value) { return; }
            count = value;
            next.innerHTML = count;
            el.classList.add('is-changing');
            window.clearTimeout(timeout);
            timeout = window.setTimeout(function() {
                current.innerHTML = next.innerHTML;
                el.classList.remove('is-changing');
            }, 210);
        }

        return {
            update: update
        };
    }

    var evtSource = new EventSource("/counter");
    evtSource.onmessage = function(event) {
        EventSource.prototype.withCredentials = true;
        console.log("Received data:", event.data); 
        var count = parseInt(event.data, 10);  // Convert the received data to an integer

        var tens = Math.floor(count / 10);
        var ones = count % 10;

        counterTens.update(tens);
        counterOnes.update(ones);
    }
});
