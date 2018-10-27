// facili - easy info tool web frotend

// Copyright (C) 2018 Siddharudh P T

// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 2.1 of the License, or
// (at your option) any later version.

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.

// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>


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
                },
                gridLines: {
                    display:false
                }
            }],
            xAxes: [{
                gridLines: {
                    display:false
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


var liveDiskIOChart = new Chart("live-dio-chart", {
    type: 'line',

    data: {
        labels: ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        datasets: [
            {
                data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                label: 'read',

                borderColor: 'blue',
                backgroundColor: 'rgba(0,0,255,0.2)',
                pointRadius: 0,
                borderWidth: 1
            },
            {
                data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                label: 'write',
                borderColor: 'red',
                backgroundColor: 'rgba(255,0,0,0.2)',
                pointRadius: 0,
                borderWidth: 1
            }
        ]
    },
    options: {
        maintainAspectRatio: false,
        // legend: { display: false },
        tooltips: { enabled: false },
        scales: {
            xAxes: [{
                    gridLines: {
                        display:false
                    }
                }],
            yAxes: [{
                    gridLines: {
                        display:false
                    }
                }]
        }
    }
});


var liveNetworkChart = new Chart("live-net-chart", {
    type: 'line',

    data: {
        labels: ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        datasets: [
            {
                data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                label: 'recv',

                borderColor: '#4a0',
                backgroundColor: 'rgba(150,255,0,0.3)',
                pointRadius: 0,
                borderWidth: 1
            },
            {
                data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                label: 'send',
                borderColor: '#d0f',
                backgroundColor: 'rgba(200,0,255,0.3)',
                pointRadius: 0,
                borderWidth: 1
            }
        ]
    },
    options: {
        maintainAspectRatio: false,
        // legend: { display: false },
        tooltips: { enabled: false },
        scales: {
            xAxes: [{
                    gridLines: {
                        display:false
                    }
                }],
            yAxes: [{
                    gridLines: {
                        display:false
                    }
                }]
        }
    }
});


function percentUsageColor(pct) {
    var green = Math.round(pct <= 50 ? 220 : (100 - pct) * 220 / 50);
    var red = Math.round(pct >= 50 ? 220 : pct * 220 / 50);
    return 'rgba(' + red + ', ' + green + ', 0, 255)';
}

function updateLiveDoughnetChart(chart, pct) {
    chart.data.datasets[0].data = [pct, 100 - pct];
    chart.options.centertext = pct + "%";
    chart.data.datasets[0].backgroundColor[0] = percentUsageColor(pct);
    chart.update();
}

function updateLiveBarChart(chart, labels, series1, series2) {
    chart.data.labels = labels;
    chart.data.datasets[0].data = series1;
    if (series2 != undefined) {
        chart.data.datasets[1].data = series2;
    }
    chart.update();
}


function updateLiveCharts(result) {
    var cpu = result['resmon.live.cpu'];
    updateLiveDoughnetChart(liveCPUChart, Math.round(cpu.avg));

    var mem = result['resmon.live.mem'];
    updateLiveDoughnetChart(liveMemoryChart, Math.round(mem.percent));

    var load = result['resmon.live.load'];
    updateLiveBarChart(liveLoadChart, ['1min', '5min', '15min'], load);

    var disk_io = result['resmon.live.disk_io']['total'];
    labels = liveDiskIOChart.data.labels;
    read_speeds = liveDiskIOChart.data.datasets[0].data;
    write_speeds = liveDiskIOChart.data.datasets[1].data;;
    if (disk_io != undefined) {
        labels.push('');
        read_speeds.push(disk_io.read_speed / (1024 * 1024));
        write_speeds.push(disk_io.write_speed / (1024 * 1024));
    }
    if (labels.length >= 30) {
        labels.shift();
        read_speeds.shift();
        write_speeds.shift();
    }
    updateLiveBarChart(liveDiskIOChart, labels, read_speeds, write_speeds);

    var net_io = result['resmon.live.net_io']['total'];
    labels = liveNetworkChart.data.labels;
    recv_speeds = liveNetworkChart.data.datasets[0].data;
    send_speeds = liveNetworkChart.data.datasets[1].data;;
    if (disk_io != undefined) {
        labels.push('');
        recv_speeds.push(net_io.recv_speed / 1024);
        send_speeds.push(net_io.send_speed / 1024);
    }
    if (labels.length >= 30) {
        labels.shift();
        recv_speeds.shift();
        send_speeds.shift();
    }
    updateLiveBarChart(liveNetworkChart, labels, recv_speeds, send_speeds);
}
