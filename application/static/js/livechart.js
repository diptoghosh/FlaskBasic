function getchartdata() {
    const config1 = {
        type: 'line',
        data: {
            labels: [],
            datasets: [
            {
                label: "Temperature",
                backgroundColor: 'purple',
                borderColor: 'purple',
                data: [],
                fill: false,
            }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            title: {
                display: true,
                text: 'Temperature'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    }
                }],
                yAxes: [{
                    display: true,
                    ticks : {
                        max : 1,    
                        min : -1
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                }]
            }
        }
    };

    const config2 = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: "Humidity",
                backgroundColor: 'green',
                borderColor: 'green',
                data: [],
                fill: false,
            }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            title: {
                display: false,
                text: 'Humidity Sensor Data'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                }]
            }
        }
    };


    const context1 = document.getElementById('canvas-temperature');
    const context2 = document.getElementById('canvas-humidity');

    context1.height = 200;
    context2.height = 200;

    context1.width = 200;
    context2.width = 200;

    const lineChart1 = new Chart(context1, config1);
    const lineChart2 = new Chart(context2, config2);

    var socket = io.connect('http://' + document.domain + ':' + location.port);  
    socket.on( 'mqtt_message', function( msg ) {
      console.log(msg);
      let today = new Date();
      let timenow = today.toLocaleTimeString('it-IT');
      const pldata = JSON.parse(msg["payload"]);
      $('#temperature').text(pldata.temperature + "\u2103");
      $('#humidity').text(pldata.humidity + "%");
      //Chart 1 data
      if (config1.data.labels.length === 100) {
        config1.data.labels.shift();
        config1.data.datasets[0].data.shift();
        config1.data.datasets[1].data.shift();
      }
      config1.data.labels.push(timenow);
      config1.data.datasets[0].data.push(pldata.temperature);

      lineChart1.update();


      //Chart 2 data
       if (config2.data.labels.length === 100) {
           config2.data.labels.shift();
           config2.data.datasets[0].data.shift();
       };
       config2.data.labels.push(timenow);
       config2.data.datasets[0].data.push(pldata.humidity);

       lineChart2.update();  
    });

}