var ec_right2 = echarts.init(document.getElementById('r2'), "vintage");

var ddd = [{'name': '肺炎', 'value': '12734670'}, {'name': '实时', 'value': '12734670'},
{'name': '新型', 'value': '12734670'}]
var ec_right2_option = {
                        // backgroundColor: '#515151',
						title : {
						    text : "今日疫情热搜",
						    textStyle : {
						        color : 'white',
						    },
						    left : 'left'
						},
                        tooltip: {
                            show: false
                        },
                        series: [{
                                type: 'wordCloud',
								// drawOutOfBound:true,
                                gridSize: 8,
                                sizeRange: [17, 60],
                                rotationRange: [-45, 0, 45, 90],
                                // maskImage: maskImage,
                                textStyle: {    //随机颜色
                                    normal: {
                                        color: function () {
                                            return 'rgb(' +
                                                    Math.round(Math.random() * 255) +
                                                    ', ' + Math.round(Math.random() * 255) +
                                                    ', ' + Math.round(Math.random() * 255) + ')'
                                        }
                                    }
                                },
                                // left: 'center',
                                // top: 'center',
                                // // width: '96%',
                                // // height: '100%',
                                right: null,
                                bottom: null,
                                // width: 300,
                                // height: 200,
                                // top: 20,
                                data:  []
                            }]
                    }

ec_right2.setOption(ec_right2_option);
