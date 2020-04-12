function randomColor() {
	const colors = [
		'rgba(255, 99, 132, 0.2)',
		'rgba(54, 162, 235, 0.2)',
		'rgba(255, 206, 86, 0.2)',
		'rgba(75, 192, 192, 0.2)',
		'rgba(153, 102, 255, 0.2)',
	]

	const randInt = Math.floor(Math.random() * Math.floor(5));

	return colors[randInt]
}

const options = {
	scales: {
		yAxes: [{
			ticks: {
				suggestedMin: 0,
				suggestedMax: 100,
				stepSize: 10,
			}
		}]
	},
	legend: {
		display: true,
		labels: {
			fontColor: 'rgb(38, 38, 38)',
			padding: 10,
		}
	}
}

// Set Options
Chart.defaults.global.responsive = true
Chart.defaults.scale.ticks.beginAtZero = true
Chart.defaults.scale.scaleLabel.display = true // display numbers on y axis
Chart.defaults.global.tooltips.bodySpacing = 4

const res = JSON.parse(localStorage.getItem("resp"))
console.log(res)


let personalityChart = document.getElementById('personalityChart');
let chart1 = new Chart(personalityChart, {
	tooltipFontSize: 10,
	tooltipTemplate: "<%if (label){%><%=label%>: <%}%><%= value %>hrs",
	percentageInnerCutout : 70,
	type: 'bar',
	data: {
		labels: [
			res.personality[0].name, 
			res.personality[1].name,
			res.personality[2].name, 
			res.personality[3].name, 
			res.personality[4].name, 
		],
		datasets: [{
			label: 'Personality',
			data: [
				(res.personality[0].percentile)*100,
				(res.personality[1].percentile)*100,
				(res.personality[2].percentile)*100, 
				(res.personality[3].percentile)*100, 
				(res.personality[4].percentile)*100, 
			],
			backgroundColor: [
				'rgba(255, 99, 132, 0.2)',
				'rgba(54, 162, 235, 0.2)',
				'rgba(255, 206, 86, 0.2)',
				'rgba(75, 192, 192, 0.2)',
				'rgba(153, 102, 255, 0.2)',
				// 'rgba(255, 159, 64, 0.2)'
			],
			borderColor: [
				'rgba(255, 99, 132, 1)',
				'rgba(54, 162, 235, 1)',
				'rgba(255, 206, 86, 1)',
				'rgba(75, 192, 192, 1)',
				'rgba(153, 102, 255, 1)',
				// 'rgba(255, 159, 64, 1)'
			],
			borderWidth: 1
		}]
	},
	options: options,
});

var needsChart = document.getElementById('needsChart');
var chart2 = new Chart(needsChart, {
	type: 'bar',
	data: {
		labels: [
			res.needs[0].name,
			res.needs[1].name,
			res.needs[2].name,
			res.needs[3].name,
			res.needs[4].name,
			res.needs[5].name,
			res.needs[6].name,
			res.needs[7].name,
			res.needs[8].name,
			res.needs[9].name,
			res.needs[10].name,
			res.needs[11].name,
		],
		datasets: [
			{
			label: "Needs",
			fill: true,
			// backgroundColor: "rgba(255,99,132,0.2)",
			backgroundColor: [
				randomColor(),
				randomColor(),
				randomColor(),
				randomColor(),
				randomColor(),
				randomColor(),
				randomColor(),
				randomColor(),
				randomColor(),
				randomColor(),
				randomColor(),
				randomColor(),
			],
			// borderColor: "rgba(255,99,132,1)",
			borderWidth: 1,
			pointBorderColor: "#fff",
			pointBackgroundColor: "rgba(255,99,132,1)",
			pointBorderColor: "#fff",
			data: [
				res.needs[0].percentile*100,
				res.needs[1].percentile*100,
				res.needs[2].percentile*100,
				res.needs[3].percentile*100,
				res.needs[4].percentile*100,
				res.needs[5].percentile*100,
				res.needs[6].percentile*100,
				res.needs[7].percentile*100,
				res.needs[8].percentile*100,
				res.needs[9].percentile*100,
				res.needs[10].percentile*100,
				res.needs[11].percentile*100,
			]},
		]
	},
	options: options,
});

let valuesChart = document.getElementById('valuesChart');
let chart3 = new Chart(valuesChart, {
	tooltipFontSize: 10,
	tooltipTemplate: "<%if (label){%><%=label%>: <%}%><%= value %>hrs",
	percentageInnerCutout : 70,
	type: 'bar',
	data: {
		labels: [
			res.values[0].name, 
			res.values[1].name,
			res.values[2].name, 
			res.values[3].name, 
			res.values[4].name, 
		],
		datasets: [{
			label: 'Values',
			data: [
				(res.values[0].percentile)*100,
				(res.values[1].percentile)*100,
				(res.values[2].percentile)*100, 
				(res.values[3].percentile)*100, 
				(res.values[4].percentile)*100, 
			],
			backgroundColor: [
				'rgba(255, 99, 132, 0.2)',
				'rgba(54, 162, 235, 0.2)',
				'rgba(255, 206, 86, 0.2)',
				'rgba(75, 192, 192, 0.2)',
				'rgba(153, 102, 255, 0.2)',
			],
			borderColor: [
				'rgba(255, 99, 132, 1)',
				'rgba(54, 162, 235, 1)',
				'rgba(255, 206, 86, 1)',
				'rgba(75, 192, 192, 1)',
				'rgba(153, 102, 255, 1)',
			],
			borderWidth: 1
		}]
	},
	options: options,
});