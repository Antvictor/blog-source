const customename = document.getElementById("customname");
const randomize = document.querySelector(".randomize");
const story = document.querySelector(".story");

/**
 * @param {Object} array 数组
 * 随机返回数组中的内容
 */
function randomValueFromArray(array) {
	return array[Math.floor(Math.random() * array.length)];
}

let storyText = "今天气温 :temperature: ，:inserta:出去遛弯。当走到:insertb:门前时，突然就:insertc:。人们都惊呆了，李雷全程目睹但并没有慌，因为:inserta:是一个 :weigth: 的胖子，天气又辣么热。";
let insertX = ["怪兽威利", "大老爹", "圣诞老人"];
let insertY = ["肯德基", "迪士尼", "白宫"];
let insertZ = ["自燃了", "在人行道化成了一坨泥", "变成一条鼻涕虫爬走了"];


randomize.addEventListener("click", result);

function result() {
	let newStroy = storyText;
	let weigth = Math.floor(Math.random() * 140 + 140);
	let temperature  = 34;
	if (customename.value !== '') {
		let name = customename.value;
		newStroy = newStroy.replace("李雷", name);
	}
	
	if (document.getElementById("american").checked) {
		 weigth = Math.round(weigth * 2.20462262) + " 磅";
		 temperature = Math.round(32 + temperature * 1.8) + " 华氏度";
	} else {
		weigth += " 公斤";
		temperature += " 摄氏度";
	}
	newStroy = newStroy.replace(":temperature:", temperature);
	newStroy = newStroy.replace(":weigth:", weigth);
	newStroy = newStroy.replaceAll(":inserta:", randomValueFromArray(insertX));
	newStroy = newStroy.replace(":insertb:", randomValueFromArray(insertY));
	newStroy = newStroy.replace(":insertc:", randomValueFromArray(insertZ));
	
	story.textContent = newStroy;
	story.style.visibility = 'visible';
	
}