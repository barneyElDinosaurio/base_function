#-*-coding=utf-8-*-
import dash_core_components as dcc

dcc.Input(
    placeholder='Enter value',
    type='text',
    value=''
)
'''
import dash
import dash_core_components as dcc
import dash_html_components as html
# 实例化一个Dash对象
app = dash.Dash()
'''
'''
dash页面的布局结构为:
1 整个页面是一个div
2 div内设定一个h1型号的标题
3 div内包含一个子div,且内容为一行文本
'''
'''
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children=
        Dash: A web application framework for Python.
    ),
    dcc.Graph(
        # 唯一标识该图形，此属性并不显示在页面
        id='example-graph',
        # 图形的具体内容
        figure={
            # data是key,值为元素为字典的列表，即图形的具体数据，
            # 其中x为横轴数据链，y为与x相对应的纵轴数据链，
            # type为图形的类型，name为图形标识
            'data': [
                {'x': [1, 2, 3], 'y': [4, 10, 2], 'type': 'bar', 'name': 'AAPL'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'IBM'},
            ],
            # 图形的标题
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])
# 入口方法
if __name__ == '__main__':
    app.run_server(debug=True)
'''