import React from "react";
import { LineChart, PieChart, ColumnChart } from "react-chartkick";
import "chart.js";

import ChartistGraph from "react-chartist";
import { log } from "util";

var temp = {
  labels: ["Bananas", "Apples", "Grapes"],
  series: [30, 20, 50]
};

var options = {
  labelInterpolationFnc: function(value) {
    return value[0];
  },
  width: "300px",
  height: "300px"
};

var responsiveOptions = [
  [
    "screen and (min-width: 640px)",
    {
      chartPadding: 30,
      labelOffset: 100,
      labelDirection: "explode",
      labelInterpolationFnc: function(value) {
        return value;
      }
    }
  ],
  [
    "screen and (min-width: 1024px)",
    {
      labelOffset: 80,
      chartPadding: 20
    }
  ]
];

const Chart = ({ type, series, labels }) => {
  let renderComponent;

  const data = labels.map((label, index) => {
    return [label, series[index]];
  });

  if (type === "Pie") {
    renderComponent = <PieChart data={data} />;
  }
  if (type === "Column") {
    renderComponent = <ColumnChart data={data} />;
  }

  return renderComponent;
};

export default Chart;
