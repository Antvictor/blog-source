const name1 = document.querySelector("#name");
const delay = document.querySelector("#delay");

const setAlarm = document.querySelector("#set-alarm");
const output = document.querySelector("#output");

function alarm(person, delay) {
    return new Promise((resolve, reject) => {
        if (delay < 0 ) {
            throw new Error("Alarm delay must not be negative");
        }
        window.setTimeout(() => {
            resolve(`Wake up, ${person}`)
        }, delay);
    });
}

setAlarm.addEventListener("click", () => {
    alarm(name1.value, delay.value)
        .then((message) => {
            output.textContent = message;
        })
        .catch((error) => {
            output.textContent = `Error info : ${error}`;
        });
});