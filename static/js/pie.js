document.addEventListener( 'DOMContentLoaded', function () {
}, false );

var chart1;

var ctx1 = document.getElementById("pie-chartcanvas-1");
var data1 = {
      labels: ["Positive", "Negative"],
      datasets: [
          {
              label: "Positive and Negative",
              data: [1, 1],
              backgroundColor: [
                  "#62D2A2",
                  "#F19584"
              ],
              borderColor: [
                  "#62D2A2",
                  "#F19584"
              ],
              borderWidth: [1, 1, 1, 1, 1]
          }
      ]
  };
var options = {
     title: {
         display: true,
         position: "top",
         fontSize: 18,
         fontColor: "#111"
     },
     legend: {
         display: true,
         position: "bottom"
     },
     animation: {
      duration: 0,
      onComplete: function () {
        var self = this,
            chartInstance = this.chart,
            ctx = chartInstance.ctx;

        ctx.font = '18px Arial';
        ctx.textAlign = "center";
        ctx.fillStyle = "#ffffff";

        Chart.helpers.each(self.data.datasets.forEach((dataset, datasetIndex) => {
            var meta = self.getDatasetMeta(datasetIndex),
                total = 0, //total values to compute fraction
                labelxy = [],
                offset = Math.PI / 2, //start sector from top
                radius,
                centerx,
                centery,
                lastend = 0; //prev arc's end line: starting with 0

            for (var val of dataset.data) { total += val; }

            Chart.helpers.each(meta.data.forEach((element, index) => {
                radius = 0.9 * element._model.outerRadius - element._model.innerRadius;
                centerx = element._model.x;
                centery = element._model.y;
                var thispart = dataset.data[index],
                    arcsector = Math.PI * (2 * thispart / total);
                if (element.hasValue() && dataset.data[index] > 0) {
                  labelxy.push(lastend + arcsector / 2 + Math.PI + offset);
                }
                else {
                  labelxy.push(-1);
                }
                lastend += arcsector;
            }), self);

            var lradius = radius * 3 / 4;
            for (var idx in labelxy) {
              if (labelxy[idx] === -1) continue;
              var langle = labelxy[idx],
                  dx = centerx + lradius * Math.cos(langle),
                  dy = centery + lradius * Math.sin(langle),
                  val = Math.round(dataset.data[idx] / total * 100);
              ctx.fillText(val + '%', dx, dy);
            }

        }), self);
      }
    }
 };

chart1 = new Chart(ctx1, {
      type: "pie",
      data: data1,
      options: options
  });

chart1.update();
