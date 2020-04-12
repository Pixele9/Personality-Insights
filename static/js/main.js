let getResultBtn = document.querySelector("#getResultBtn")
let textArea = document.querySelector("#textToAnalyze")
let spinner = document.querySelector(".spinner") // show animation
let detailViewBtn = document.querySelector("#detailViewBtn")

detailViewBtn.addEventListener("click", () => {
	window.location = "/detail"
})

getResultBtn.addEventListener("click", function(e) {
	e.preventDefault()
	if(textArea.value == null || textArea.value == "" || textArea.textLength <= 1000) {
		alert("Plese enter a text bigger then 100 characters to analyze")
	} else {
		const textContent = textArea.value
		let formData = new FormData();
		formData.append("textToAnalyze", textContent)

		postAjax(formData)
	}
})

// Set options
Chart.defaults.global.responsive = false
Chart.defaults.scale.scaleLabel.display = true 

const chartOptions = {
	legend: {
		display: true,
		labels: {
			fontColor: 'rgb(38, 38, 38)',
			padding: 10,
		}
	}
}

function postAjax(formData) {
	$.ajax({
		type: "POST",
		url: "/analyze",
		data: formData,
		processData: false,
		contentType: false,
		success: (result , textStatus, xhr) => {
			console.log("ajax in JS")
			let res = JSON.parse(result)
			
			localStorage.setItem("resp", JSON.stringify(res))

			let ctx = document.getElementById('chart').getContext('2d');
			let myChart = new Chart(ctx, {
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
				options: chartOptions,
			});
		}
	})
}

$(document).ready(function() { 

	// Setup the ajax indicator
	$('.activityIndicator').append('<div class="spinner loader10"></div>');

	$('.spinner').css({
		display:"none",
		margin:"0px",
		position:"absolute",
		right:"275px",
		top:"200px",
		transform:"scale(0.7)",
	});
	});

	// Ajax activity indicator bound to ajax start/stop document events
	$(document).ajaxStart(function(){ 
	$('.spinner').show(); 
	}).ajaxStop(function(){ 
	$('.spinner').hide();
});

// var ctx = document.getElementById('chart');
// var myChart = new Chart(ctx, {
//     type: 'radar',
// 	data: {
// 		labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
// 		datasets: [
// 			{
// 			label: "1950",
// 			fill: true,
// 			backgroundColor: "rgba(179,181,198,0.2)",
// 			borderColor: "rgba(179,181,198,1)",
// 			pointBorderColor: "#fff",
// 			pointBackgroundColor: "rgba(179,181,198,1)",
// 			data: [8.77,55.61,21.69,6.62,6.82]
// 			}, {
// 			label: "2050",
// 			fill: true,
// 			backgroundColor: "rgba(255,99,132,0.2)",
// 			borderColor: "rgba(255,99,132,1)",
// 			pointBorderColor: "#fff",
// 			pointBackgroundColor: "rgba(255,99,132,1)",
// 			pointBorderColor: "#fff",
// 			data: [25.48,54.16,7.61,8.06,4.45]
// 			}
// 		]
//     },
//     options: {
//         scale: {
// 			angleLines: {
// 				display: false
// 			},
// 			ticks: {
// 				suggestedMin: 50,
// 				suggestedMax: 100
// 			}
// 		}
//     }
// });