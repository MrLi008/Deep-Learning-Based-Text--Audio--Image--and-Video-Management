//第一个图
    var myChart = echarts.init(document.getElementById('demo1'));
      var option = {
        color: ['#3398DB'],
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {},
        xAxis: [
          {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            axisLabel: {
                textStyle: {
                    color: '#7da1d3' // 设置 X 轴数据颜色为红色
                }
            },
          }
        ],
        yAxis: [
          {
            type: 'value',
            axisLabel: {
                textStyle: {
                    color: '#7da1d3' // 设置 y轴数据颜色为红色
                }
            },
          }
        ],
        series: [
          {
            name: '训练频率',
            type: 'bar',
            barWidth: '60%',
            data: [10, 52, 200, 334, 390, 330, 220]
          }
        ]
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);




//第二个图
      var myChart2 = echarts.init(document.getElementById('demo2'));
      var option2 = {
        legend: {
            left: "left",
            data: ["累计训练指数", "累计评估指数"],
            textStyle: {
                color: '#7da1d3' 
            }
          },
          xAxis: {
            type: "category",
            name: "x",
            splitLine: {
              show: false
            },
            axisLabel: {
                textStyle: {
                    color: '#7da1d3' // 设置 X 轴数据颜色
                }
            },
            data: ["一", "二", "三", "四", "五", "六", "七", "八", "九"]
          },
          grid: {
            left: "3%",
            right: "4%",
            bottom: "3%",
            containLabel: true
          },
          yAxis: {
            type: "log",
            name: "y",
            minorTick: {
              show: true
            },
            axisLabel: {
                textStyle: {
                    color: '#7da1d3' // 设置 y 轴数据颜色
                }
            },
            minorSplitLine: {
              show: true
            }
          },
          series: [{
            name: "累计训练指数",
            type: "line",
            data: [1, 3, 9, 27, 81, 247, 741, 2223, 6669]
          }, {
            name: "累计评估指数",
            type: "line",
            data: [1, 2, 4, 8, 16, 32, 64, 128, 256]
          }, 
      };
      // 使用刚指定的配置项和数据显示图表。
      myChart2.setOption(option2);

//第三个图
var myChart3 = echarts.init(document.getElementById('demo3'));
var option3 = {
    toolbox: {
        show: true,
        feature: {
          dataZoom: {
            yAxisIndex: "none"
          },
          dataView: {
            readOnly: false
          },
          magicType: {
            type: ["line", "bar"]
          },
          restore: {},
          saveAsImage: {}
        }
      },
      xAxis: {
        type: "category",
        boundaryGap: false,
        data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        axisLabel: {
            textStyle: {
                color: '#7da1d3' // 设置 X 轴数据颜色为红色
            }
        }
      },
      yAxis: {
        type: "value",
        axisLabel: {
          formatter: "{value} 热度",
          textStyle: {
            color: '#7da1d3' // 设置 y轴数据颜色为红色
            }
        }
      },
      series: [{
        name: "最高气温",
        type: "line",
        data: [11, 11, 15, 13, 12, 13, 10],
        markPoint: {
          data: [{
            type: "max",
            name: "Max"
          }, {
            type: "min",
            name: "Min"
          }]
        },
        markLine: {
          data: [{
            type: "average",
            name: "Avg"
          }]
        }
      }, {
        name: "最低气温",
        type: "line",
        data: [1, -2, 2, 5, 3, 2, 0],
        markPoint: {
          data: [{
            name: "周最低",
            value: -2,
            xAxis: 1,
            yAxis: -1.5
          }]
        },
        markLine: {
          data: [{
              type: "average",
              name: "Avg"
            },
            [{
              symbol: "none",
              x: "90%",
              yAxis: "max"
            }, {
              symbol: "circle",
              label: {
                position: "start",
                formatter: "Max"
              },
              type: "max",
              name: "Top"
            }]
          ]
        }
      }]
};
// 使用刚指定的配置项和数据显示图表。
myChart3.setOption(option3);



//第四个图
var myChart4 = echarts.init(document.getElementById('demo4'));
var data4 = [
    {
      name: 'Flora',
      itemStyle: {
        color: '#da0d68'
      },
      children: [
        {
          name: 'Black Tea',
          value: 1,
          itemStyle: {
            color: '#975e6d'
          }
        },
        {
          name: 'Floral',
          itemStyle: {
            color: '#e0719c'
          },
          children: [
            {
              name: 'Chamomile',
              value: 1,
              itemStyle: {
                color: '#f99e1c'
              }
            },
            {
              name: 'Rose',
              value: 1,
              itemStyle: {
                color: '#ef5a78'
              }
            },
            {
              name: 'Jasmine',
              value: 1,
              itemStyle: {
                color: '#f7f1bd'
              }
            }
          ]
        }
      ]
    },
    {
      name: 'Fruity',
      itemStyle: {
        color: '#da1d23'
      },
      children: [
        {
          name: 'Berry',
          itemStyle: {
            color: '#dd4c51'
          },
          children: [
            {
              name: 'Blackberry',
              value: 1,
              itemStyle: {
                color: '#3e0317'
              }
            },
            {
              name: 'Raspberry',
              value: 1,
              itemStyle: {
                color: '#e62969'
              }
            },
            {
              name: 'Blueberry',
              value: 1,
              itemStyle: {
                color: '#6569b0'
              }
            },
            {
              name: 'Strawberry',
              value: 1,
              itemStyle: {
                color: '#ef2d36'
              }
            }
          ]
        },
        {
          name: 'Dried Fruit',
          itemStyle: {
            color: '#c94a44'
          },
          children: [
            {
              name: 'Raisin',
              value: 1,
              itemStyle: {
                color: '#b53b54'
              }
            },
            {
              name: 'Prune',
              value: 1,
              itemStyle: {
                color: '#a5446f'
              }
            }
          ]
        },
        {
          name: 'Other Fruit',
          itemStyle: {
            color: '#dd4c51'
          },
          children: [
            {
              name: 'Coconut',
              value: 1,
              itemStyle: {
                color: '#f2684b'
              }
            },
            {
              name: 'Cherry',
              value: 1,
              itemStyle: {
                color: '#e73451'
              }
            },
            {
              name: 'Pomegranate',
              value: 1,
              itemStyle: {
                color: '#e65656'
              }
            },
            {
              name: 'Pineapple',
              value: 1,
              itemStyle: {
                color: '#f89a1c'
              }
            },
            {
              name: 'Grape',
              value: 1,
              itemStyle: {
                color: '#aeb92c'
              }
            },
            {
              name: 'Apple',
              value: 1,
              itemStyle: {
                color: '#4eb849'
              }
            },
            {
              name: 'Peach',
              value: 1,
              itemStyle: {
                color: '#f68a5c'
              }
            },
            {
              name: 'Pear',
              value: 1,
              itemStyle: {
                color: '#baa635'
              }
            }
          ]
        },
        {
          name: 'Citrus Fruit',
          itemStyle: {
            color: '#f7a128'
          },
          children: [
            {
              name: 'Grapefruit',
              value: 1,
              itemStyle: {
                color: '#f26355'
              }
            },
            {
              name: 'Orange',
              value: 1,
              itemStyle: {
                color: '#e2631e'
              }
            },
            {
              name: 'Lemon',
              value: 1,
              itemStyle: {
                color: '#fde404'
              }
            },
            {
              name: 'Lime',
              value: 1,
              itemStyle: {
                color: '#7eb138'
              }
            }
          ]
        }
      ]
    },
    {
      name: 'Sour/\nFermented',
      itemStyle: {
        color: '#ebb40f'
      },
      children: [
        {
          name: 'Sour',
          itemStyle: {
            color: '#e1c315'
          },
          children: [
            {
              name: 'Sour Aromatics',
              value: 1,
              itemStyle: {
                color: '#9ea718'
              }
            },
            {
              name: 'Acetic Acid',
              value: 1,
              itemStyle: {
                color: '#94a76f'
              }
            },
            {
              name: 'Butyric Acid',
              value: 1,
              itemStyle: {
                color: '#d0b24f'
              }
            },
            {
              name: 'Isovaleric Acid',
              value: 1,
              itemStyle: {
                color: '#8eb646'
              }
            },
            {
              name: 'Citric Acid',
              value: 1,
              itemStyle: {
                color: '#faef07'
              }
            },
            {
              name: 'Malic Acid',
              value: 1,
              itemStyle: {
                color: '#c1ba07'
              }
            }
          ]
        },
        {
          name: 'Alcohol/\nFremented',
          itemStyle: {
            color: '#b09733'
          },
          children: [
            {
              name: 'Winey',
              value: 1,
              itemStyle: {
                color: '#8f1c53'
              }
            },
            {
              name: 'Whiskey',
              value: 1,
              itemStyle: {
                color: '#b34039'
              }
            },
            {
              name: 'Fremented',
              value: 1,
              itemStyle: {
                color: '#ba9232'
              }
            },
            {
              name: 'Overripe',
              value: 1,
              itemStyle: {
                color: '#8b6439'
              }
            }
          ]
        }
      ]
    },
    {
      name: 'Green/\nVegetative',
      itemStyle: {
        color: '#187a2f'
      },
      children: [
        {
          name: 'Olive Oil',
          value: 1,
          itemStyle: {
            color: '#a2b029'
          }
        },
        {
          name: 'Raw',
          value: 1,
          itemStyle: {
            color: '#718933'
          }
        },
        {
          name: 'Green/\nVegetative',
          itemStyle: {
            color: '#3aa255'
          },
          children: [
            {
              name: 'Under-ripe',
              value: 1,
              itemStyle: {
                color: '#a2bb2b'
              }
            },
            {
              name: 'Peapod',
              value: 1,
              itemStyle: {
                color: '#62aa3c'
              }
            },
            {
              name: 'Fresh',
              value: 1,
              itemStyle: {
                color: '#03a653'
              }
            },
            {
              name: 'Dark Green',
              value: 1,
              itemStyle: {
                color: '#038549'
              }
            },
            {
              name: 'Vegetative',
              value: 1,
              itemStyle: {
                color: '#28b44b'
              }
            },
            {
              name: 'Hay-like',
              value: 1,
              itemStyle: {
                color: '#a3a830'
              }
            },
            {
              name: 'Herb-like',
              value: 1,
              itemStyle: {
                color: '#7ac141'
              }
            }
          ]
        },
        {
          name: 'Beany',
          value: 1,
          itemStyle: {
            color: '#5e9a80'
          }
        }
      ]
    },
    {
      name: 'Other',
      itemStyle: {
        color: '#0aa3b5'
      },
      children: [
        {
          name: 'Papery/Musty',
          itemStyle: {
            color: '#9db2b7'
          },
          children: [
            {
              name: 'Stale',
              value: 1,
              itemStyle: {
                color: '#8b8c90'
              }
            },
            {
              name: 'Cardboard',
              value: 1,
              itemStyle: {
                color: '#beb276'
              }
            },
            {
              name: 'Papery',
              value: 1,
              itemStyle: {
                color: '#fefef4'
              }
            },
            {
              name: 'Woody',
              value: 1,
              itemStyle: {
                color: '#744e03'
              }
            },
            {
              name: 'Moldy/Damp',
              value: 1,
              itemStyle: {
                color: '#a3a36f'
              }
            },
            {
              name: 'Musty/Dusty',
              value: 1,
              itemStyle: {
                color: '#c9b583'
              }
            },
            {
              name: 'Musty/Earthy',
              value: 1,
              itemStyle: {
                color: '#978847'
              }
            },
            {
              name: 'Animalic',
              value: 1,
              itemStyle: {
                color: '#9d977f'
              }
            },
            {
              name: 'Meaty Brothy',
              value: 1,
              itemStyle: {
                color: '#cc7b6a'
              }
            },
            {
              name: 'Phenolic',
              value: 1,
              itemStyle: {
                color: '#db646a'
              }
            }
          ]
        },
        {
          name: 'Chemical',
          itemStyle: {
            color: '#76c0cb'
          },
          children: [
            {
              name: 'Bitter',
              value: 1,
              itemStyle: {
                color: '#80a89d'
              }
            },
            {
              name: 'Salty',
              value: 1,
              itemStyle: {
                color: '#def2fd'
              }
            },
            {
              name: 'Medicinal',
              value: 1,
              itemStyle: {
                color: '#7a9bae'
              }
            },
            {
              name: 'Petroleum',
              value: 1,
              itemStyle: {
                color: '#039fb8'
              }
            },
            {
              name: 'Skunky',
              value: 1,
              itemStyle: {
                color: '#5e777b'
              }
            },
            {
              name: 'Rubber',
              value: 1,
              itemStyle: {
                color: '#120c0c'
              }
            }
          ]
        }
      ]
    },
    {
      name: 'Roasted',
      itemStyle: {
        color: '#c94930'
      },
      children: [
        {
          name: 'Pipe Tobacco',
          value: 1,
          itemStyle: {
            color: '#caa465'
          }
        },
        {
          name: 'Tobacco',
          value: 1,
          itemStyle: {
            color: '#dfbd7e'
          }
        },
        {
          name: 'Burnt',
          itemStyle: {
            color: '#be8663'
          },
          children: [
            {
              name: 'Acrid',
              value: 1,
              itemStyle: {
                color: '#b9a449'
              }
            },
            {
              name: 'Ashy',
              value: 1,
              itemStyle: {
                color: '#899893'
              }
            },
            {
              name: 'Smoky',
              value: 1,
              itemStyle: {
                color: '#a1743b'
              }
            },
            {
              name: 'Brown, Roast',
              value: 1,
              itemStyle: {
                color: '#894810'
              }
            }
          ]
        },
        {
          name: 'Cereal',
          itemStyle: {
            color: '#ddaf61'
          },
          children: [
            {
              name: 'Grain',
              value: 1,
              itemStyle: {
                color: '#b7906f'
              }
            },
            {
              name: 'Malt',
              value: 1,
              itemStyle: {
                color: '#eb9d5f'
              }
            }
          ]
        }
      ]
    },
    {
      name: 'Spices',
      itemStyle: {
        color: '#ad213e'
      },
      children: [
        {
          name: 'Pungent',
          value: 1,
          itemStyle: {
            color: '#794752'
          }
        },
        {
          name: 'Pepper',
          value: 1,
          itemStyle: {
            color: '#cc3d41'
          }
        },
        {
          name: 'Brown Spice',
          itemStyle: {
            color: '#b14d57'
          },
          children: [
            {
              name: 'Anise',
              value: 1,
              itemStyle: {
                color: '#c78936'
              }
            },
            {
              name: 'Nutmeg',
              value: 1,
              itemStyle: {
                color: '#8c292c'
              }
            },
            {
              name: 'Cinnamon',
              value: 1,
              itemStyle: {
                color: '#e5762e'
              }
            },
            {
              name: 'Clove',
              value: 1,
              itemStyle: {
                color: '#a16c5a'
              }
            }
          ]
        }
      ]
    },
    {
      name: 'Nutty/\nCocoa',
      itemStyle: {
        color: '#a87b64'
      },
      children: [
        {
          name: 'Nutty',
          itemStyle: {
            color: '#c78869'
          },
          children: [
            {
              name: 'Peanuts',
              value: 1,
              itemStyle: {
                color: '#d4ad12'
              }
            },
            {
              name: 'Hazelnut',
              value: 1,
              itemStyle: {
                color: '#9d5433'
              }
            },
            {
              name: 'Almond',
              value: 1,
              itemStyle: {
                color: '#c89f83'
              }
            }
          ]
        },
        {
          name: 'Cocoa',
          itemStyle: {
            color: '#bb764c'
          },
          children: [
            {
              name: 'Chocolate',
              value: 1,
              itemStyle: {
                color: '#692a19'
              }
            },
            {
              name: 'Dark Chocolate',
              value: 1,
              itemStyle: {
                color: '#470604'
              }
            }
          ]
        }
      ]
    },
    {
      name: 'Sweet',
      itemStyle: {
        color: '#e65832'
      },
      children: [
        {
          name: 'Brown Sugar',
          itemStyle: {
            color: '#d45a59'
          },
          children: [
            {
              name: 'Molasses',
              value: 1,
              itemStyle: {
                color: '#310d0f'
              }
            },
            {
              name: 'Maple Syrup',
              value: 1,
              itemStyle: {
                color: '#ae341f'
              }
            },
            {
              name: 'Caramelized',
              value: 1,
              itemStyle: {
                color: '#d78823'
              }
            },
            {
              name: 'Honey',
              value: 1,
              itemStyle: {
                color: '#da5c1f'
              }
            }
          ]
        },
        {
          name: 'Vanilla',
          value: 1,
          itemStyle: {
            color: '#f89a80'
          }
        },
        {
          name: 'Vanillin',
          value: 1,
          itemStyle: {
            color: '#f37674'
          }
        },
        {
          name: 'Overall Sweet',
          value: 1,
          itemStyle: {
            color: '#e75b68'
          }
        },
        {
          name: 'Sweet Aromatics',
          value: 1,
          itemStyle: {
            color: '#d0545f'
          }
        }
      ]
    }
  ];
var option4 = {
        title: {
          textStyle: {
            fontSize: 14,
            align: 'center'
          },
          subtextStyle: {
            align: 'center'
          },
          sublink: 'https://worldcoffeeresearch.org/work/sensory-lexicon/'
        },
        series: {
          type: 'sunburst',
          data: data4,
          radius: [0, '95%'],
          sort: undefined,
          emphasis: {
            focus: 'ancestor'
          },
          levels: [
            {},
            {
              r0: '15%',
              r: '35%',
              itemStyle: {
                borderWidth: 2
              },
              label: {
                rotate: 'tangential'
              }
            },
            {
              r0: '35%',
              r: '70%',
              label: {
                align: 'right'
              }
            },
            {
              r0: '70%',
              r: '72%',
              label: {
                position: 'outside',
                padding: 3,
                silent: false
              },
              itemStyle: {
                borderWidth: 3
              }
            }
          ]
        }
};
// 使用刚指定的配置项和数据显示图表。
myChart4.setOption(option4);



//第五个图
var myChart5 = echarts.init(document.getElementById('demo5'));
var option5 = {
    
color: ["#c23531", "#91c7ae", "#dd8668"],
legend: {
  top: 10,
  data: ["北京", "上海", "广州"],
  itemGap: 20,
  textStyle: {
    color: '#7da1d3' 
}

},
parallelAxis: [{
  dim: 0,
  name: "日期",
  inverse: true,
  max: 31,
  nameLocation: "start"
}, {
  dim: 1,
  name: "AQI"
}, {
  dim: 2,
  name: "PM2.5"
}, {
  dim: 3,
  name: "PM10"
}, {
  dim: 4,
  name: " CO"
}, {
  dim: 5,
  name: "NO2"
}, {
  dim: 6,
  name: "SO2"
}, {
  dim: 7,
  name: "等级",
  type: "category",
  data: ["优", "良", "轻度污染", "中度污染", "重度污染", "严重污染"]
}],
parallel: {
  left: "5%",
  right: "13%",
  bottom: "10%",
  top: "20%",
  parallelAxisDefault: {
    type: "value",
    name: "AQI指数",
    nameLocation: "end",
    nameGap: 20,
    nameTextStyle: {
      fontSize: 12
    }
  }
},
series: [{
  name: "北京",
  type: "parallel",
  data: [
    [1, 55, 9, 56, 0.46, 18, 6, "良"],
    [2, 25, 11, 21, 0.65, 34, 9, "优"],
    [3, 56, 7, 63, 0.3, 14, 5, "良"],
    [4, 33, 7, 29, 0.33, 16, 6, "优"],
    [5, 42, 24, 44, 0.76, 40, 16, "优"],
    [6, 82, 58, 90, 1.77, 68, 33, "良"],
    [7, 74, 49, 77, 1.46, 48, 27, "良"],
    [8, 78, 55, 80, 1.29, 59, 29, "良"],
    [9, 267, 216, 280, 4.8, 108, 64, "重度污染"],
    [10, 185, 127, 216, 2.52, 61, 27, "中度污染"],
    [11, 39, 19, 38, 0.57, 31, 15, "优"],
    [12, 41, 11, 40, 0.43, 21, 7, "优"],
    [13, 64, 38, 74, 1.04, 46, 22, "良"],
    [14, 108, 79, 120, 1.7, 75, 41, "轻度污染"],
    [15, 108, 63, 116, 1.48, 44, 26, "轻度污染"],
    [16, 33, 6, 29, 0.34, 13, 5, "优"],
    [17, 94, 66, 110, 1.54, 62, 31, "良"],
    [18, 186, 142, 192, 3.88, 93, 79, "中度污染"],
    [19, 57, 31, 54, 0.96, 32, 14, "良"],
    [20, 22, 8, 17, 0.48, 23, 10, "优"],
    [21, 39, 15, 36, 0.61, 29, 13, "优"],
    [22, 94, 69, 114, 2.08, 73, 39, "良"],
    [23, 99, 73, 110, 2.43, 76, 48, "良"],
    [24, 31, 12, 30, 0.5, 32, 16, "优"],
    [25, 42, 27, 43, 1, 53, 22, "优"],
    [26, 154, 117, 157, 3.05, 92, 58, "中度污染"],
    [27, 234, 185, 230, 4.09, 123, 69, "重度污染"],
    [28, 160, 120, 186, 2.77, 91, 50, "中度污染"],
    [29, 134, 96, 165, 2.76, 83, 41, "轻度污染"],
    [30, 52, 24, 60, 1.03, 50, 21, "良"],
    [31, 46, 5, 49, 0.28, 10, 6, "优"]
  ]
}, {
  name: "上海",
  type: "parallel",
  data: [
    [1, 91, 45, 125, 0.82, 34, 23, "良"],
    [2, 65, 27, 78, 0.86, 45, 29, "良"],
    [3, 83, 60, 84, 1.09, 73, 27, "良"],
    [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [8, 89, 65, 78, 0.86, 51, 26, "良"],
    [9, 53, 33, 47, 0.64, 50, 17, "良"],
    [10, 80, 55, 80, 1.01, 75, 24, "良"],
    [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"],
    [12, 99, 71, 142, 1.1, 62, 42, "良"],
    [13, 95, 69, 130, 1.28, 74, 50, "良"],
    [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"],
    [15, 108, 80, 121, 1.3, 85, 37, "轻度污染"],
    [16, 134, 83, 167, 1.16, 57, 43, "轻度污染"],
    [17, 79, 43, 107, 1.05, 59, 37, "良"],
    [18, 71, 46, 89, 0.86, 64, 25, "良"],
    [19, 97, 71, 113, 1.17, 88, 31, "良"],
    [20, 84, 57, 91, 0.85, 55, 31, "良"],
    [21, 87, 63, 101, 0.9, 56, 41, "良"],
    [22, 104, 77, 119, 1.09, 73, 48, "轻度污染"],
    [23, 87, 62, 100, 1, 72, 28, "良"],
    [24, 168, 128, 172, 1.49, 97, 56, "中度污染"],
    [25, 65, 45, 51, 0.74, 39, 17, "良"],
    [26, 39, 24, 38, 0.61, 47, 17, "优"],
    [27, 39, 24, 39, 0.59, 50, 19, "优"],
    [28, 93, 68, 96, 1.05, 79, 29, "良"],
    [29, 188, 143, 197, 1.66, 99, 51, "中度污染"],
    [30, 174, 131, 174, 1.55, 108, 50, "中度污染"],
    [31, 187, 143, 201, 1.39, 89, 53, "中度污染"]
  ]
}, {
  name: "广州",
  type: "parallel",
  data: [
    [1, 26, 37, 27, 1.163, 27, 13, "优"],
    [2, 85, 62, 71, 1.195, 60, 8, "良"],
    [3, 78, 38, 74, 1.363, 37, 7, "良"],
    [4, 21, 21, 36, 0.634, 40, 9, "优"],
    [5, 41, 42, 46, 0.915, 81, 13, "优"],
    [6, 56, 52, 69, 1.067, 92, 16, "良"],
    [7, 64, 30, 28, 0.924, 51, 2, "良"],
    [8, 55, 48, 74, 1.236, 75, 26, "良"],
    [9, 76, 85, 113, 1.237, 114, 27, "良"],
    [10, 91, 81, 104, 1.041, 56, 40, "良"],
    [11, 84, 39, 60, 0.964, 25, 11, "良"],
    [12, 64, 51, 101, 0.862, 58, 23, "良"],
    [13, 70, 69, 120, 1.198, 65, 36, "良"],
    [14, 77, 105, 178, 2.549, 64, 16, "良"],
    [15, 109, 68, 87, 0.996, 74, 29, "轻度污染"],
    [16, 73, 68, 97, 0.905, 51, 34, "良"],
    [17, 54, 27, 47, 0.592, 53, 12, "良"],
    [18, 51, 61, 97, 0.811, 65, 19, "良"],
    [19, 91, 71, 121, 1.374, 43, 18, "良"],
    [20, 73, 102, 182, 2.787, 44, 19, "良"],
    [21, 73, 50, 76, 0.717, 31, 20, "良"],
    [22, 84, 94, 140, 2.238, 68, 18, "良"],
    [23, 93, 77, 104, 1.165, 53, 7, "良"],
    [24, 99, 130, 227, 3.97, 55, 15, "良"],
    [25, 146, 84, 139, 1.094, 40, 17, "轻度污染"],
    [26, 113, 108, 137, 1.481, 48, 15, "轻度污染"],
    [27, 81, 48, 62, 1.619, 26, 3, "良"],
    [28, 56, 48, 68, 1.336, 37, 9, "良"],
    [29, 82, 92, 174, 3.29, 0, 13, "良"],
    [30, 106, 116, 188, 3.628, 101, 16, "轻度污染"],
    [31, 118, 50, 0, 1.383, 76, 11, "轻度污染"]
  ]
}]

};
// 使用刚指定的配置项和数据显示图表。
myChart5.setOption(option5);



//第六个图


var myChart6 = echarts.init(document.getElementById('demo6'));
var option6 = {
    legend: {
        data: ["Display", "Click", "Visit", "Consulting", "Order"]
      },
      series: [{
        name: "漏斗图",
        type: "funnel",
        data: [{
          value: 60,
          name: "Visit"
        }, {
          value: 40,
          name: "Consulting"
        }, {
          value: 20,
          name: "Order"
        }, {
          value: 80,
          name: "Click"
        }, {
          value: 100,
          name: "Display"
        }]
      }]

}

// 使用刚指定的配置项和数据显示图表。
myChart6.setOption(option6);





//显示时间

function showCurrentTime() {
    var date = new Date() // 创建一个Date对象，获取当前日期和时间
    var year = date.getFullYear() // 获取年份
    var month = date.getMonth() + 1 // 获取月份（注意月份是从0开始的，所以要加1）
    var day = date.getDate() // 获取日期
    var hours = date.getHours() // 获取小时数
    var minutes = date.getMinutes() // 获取分钟数
    var seconds = date.getSeconds() // 获取秒数
  
    // 格式化月份、日期、小时、分钟和秒数
    month = month < 10 ? '0' + month : month
    day = day < 10 ? '0' + day : day
    hours = hours < 10 ? '0' + hours : hours
    minutes = minutes < 10 ? '0' + minutes : minutes
    seconds = seconds < 10 ? '0' + seconds : seconds
  
    // 拼接成完整的日期时间字符串
    var currentTime = year + '-' + month + '-' + day + ' ' + hours + ':' + minutes + ':' + seconds
  
    // 将日期时间显示在页面上
    document.getElementById('time_show').innerHTML = currentTime
  }
  
  // 页面加载时显示当前时间，之后每秒更新一次时间
  var timer  = null;
  window.onload = function () {
    clearInterval(timer);
    showCurrentTime()
    timer = setInterval(showCurrentTime, 1000)
  }