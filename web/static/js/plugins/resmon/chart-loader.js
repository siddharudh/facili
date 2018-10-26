var drawDoughnutCenterText = function (chart, option) {
    var width = chart.width,
    height = chart.height,
    ctx = chart.ctx;

    ctx.restore();
    var fontSize = (height / 114).toFixed(2);
    ctx.font = fontSize + "em sans-serif";
    ctx.textBaseline = "middle";
    ctx.fillStyle = 'black';

    var text = chart.options.centertext,
        textX = Math.round((width - ctx.measureText(text).width) / 2),
        textY = height / 2;

    ctx.fillText(text, textX, textY);
    ctx.save();
}


var liveCPUChart = new Chart("live-cpu-chart", {
    type: 'doughnut',

    data: {
        labels: ['Used', 'Free'],
        datasets: [{
            data: [0, 100],
            backgroundColor: ['green', 'lightgrey']
        }]
    },

    options: {
        cutoutPercentage: 75,
        maintainAspectRatio: false,
        legend: { display: false },
        tooltips: { enabled: false },
        centertext: "0%"
    },
    plugins: [{
        id: 'doughnut-center-text',
        beforeDraw: drawDoughnutCenterText
    }]
});



var liveLoadChart = new Chart("live-load-chart", {
    type: 'bar',

    data: {
        labels: ['1min', '5min', '15min'],
        datasets: [{
            data: [0, 0, 0],
            backgroundColor: ['#66f', '#44b', '#228']
        }]
    },
    options: {
        maintainAspectRatio: false,
        legend: { display: false },
        tooltips: { enabled: false },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});



var liveMemoryChart = new Chart("live-mem-chart", {
    type: 'doughnut',

    data: {
        labels: ['Used', 'Free'],
        datasets: [{
            data: [0, 100],
            backgroundColor: ['green', 'lightgrey']
        }]
    },

    options: {
        cutoutPercentage: 75,
        maintainAspectRatio: false,
        legend: { display: false },
        tooltips: { enabled: false },
        centertext: "0%"
    },
    plugins: [{
        id: 'doughnut-center-text',
        beforeDraw: drawDoughnutCenterText
    }]
});


function percentUsageColor(pct) {
    var green = pct <= 50 ? 220 : (100 - pct) * 220 / 50;
    var red = pct >= 50 ? 220 : pct * 220 / 50;
    return 'rgb(' + red + ', ' + green + ', 0)';
}

function updateLiveDoughnetChart(chart, pct) {
    chart.data.datasets[0].data = [pct, 100 - pct];
    chart.options.centertext = pct + "%";
    chart.data.datasets[0].backgroundColor[0] = percentUsageColor(pct);
    chart.update();
}

function updateLiveBarChart(chart, values, labels) {
    chart.data.datasets[0].data = values;
    if (labels != undefined) {
        chart.data.labels = labels;
    }
    chart.update();
}


setInterval(function() {
    $.ajax({
        url: "/data?k=resmon.live",
        success: function(result){
            var cpu = result['resmon.live.cpu'];
            updateLiveDoughnetChart(liveCPUChart, Math.round(cpu.avg));

            var mem = result['resmon.live.mem'];
            updateLiveDoughnetChart(liveMemoryChart, Math.round(mem.percent));

            var load = result['resmon.live.load'];
            updateLiveBarChart(liveLoadChart, load);
    }});
}, 1000);


