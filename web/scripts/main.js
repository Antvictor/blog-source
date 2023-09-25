let myHeading = document.querySelector("h1");
myHeading.textContent = "Hello World!";
// let x = 5;
function test() {
    if (true) {
        let y = 6;
    }
    var x = 5;
    // console.log(y);
    console.log(x);
}
function test1() {
    if (true) {
        let y = 6;
    }
    // var x = 7;
    // console.log(x);
}
// test();
// test1();
// console.log(x);


var all = 1;
let all2 = 2;

function test3() {
	// 整个test函数都生效
	var test = 3;
	let test2 = 4;
    const ss = 11;

	if (true) {
		// 整个test函数都生效
		var test3 = 5;
		// 只有if代码块中生效
		let test4 = 6;
        console.log(test4)
        console.log(all2)
	}
	console.log(all);
	console.log(all2);
	console.log(test);
	console.log(test2);
	console.log(test3);
	// console.log(test4); // 报错
}
// console.log(all2);
// 调用test函数
test3();