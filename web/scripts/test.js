var t = document.querySelector('h1');
    t.textContent = "red";
    alert(t);
    console.log(t);

function updateColor() {
    var t = document.querySelector('h1');
    t.textContent = "red";
    alert(t);
    console.log(t);
}

function step1(init, callback) {
	const result = init + 1;
	callback(result);
}
function step2(init, callback) {
	const result = init + 2;
	callback(result);
}
function step3(init, callback) {
	const result = init + 3;
	callback(result);
}

function doOperation() {
	step1(0, (result1) => {
		step2(result1, (result2) => {
			step3(result2, (reslut3) => {
				console.log(`结果${reslut3}`)
			})
		})
	})
}

doOperation();


fetch("http://localhost:8081/promise/test", {
    headers: {"Access-Control-Allow-Origin": '*'},
    method: "POST",
	body: {"test":"test"}
}).then((response) => {
    console.log(`${response.status}`)
})