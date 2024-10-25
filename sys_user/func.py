import traceback

from django.http import QueryDict

# from django.db.models.query import QuerySet


from django.core import serializers
from pymysql.connections import Connection
from django.conf import settings
from pymysql.cursors import DictCursor


def mydict(GET: QueryDict):
    """
    处理get/post请求参数
    """
    print(
        "In MyDict: ",
    )
    print(len(GET))
    res = {name: v if len(v) > 1 else v[0] for name, v in dict(GET).items()}
    print(len(res))
    return res


def mymeta(_cls, condition=None):
    """
    用于首页数据内容展示
    """
    try:
        # if not isinstance(_cls, MyModal):
        #     return None

        total = _cls.objects.count()
        if condition is None:
            records = _cls.objects.all()
        else:
            records = _cls.objects.filter(**condition)
        meta = _cls().toMeta()
        meta["statistic"] = {
            f"{field.verbose_name}({field.name})": len(
                list(set([getattr(record, field.name) for record in records]))
            )
            for field in meta.get("field")
        }
        meta["field_list"] = _cls().toParams_zh()
        meta["field"] = _cls().toParams_en()
        meta["implement"] = _cls().toImplement()
        meta["field_count_list"] = list(meta["statistic"].values())
        meta["total"] = total
        # del meta["field"]

        return meta
    except Exception as e:
        print(e)
    return None


def color(data):
    """
    将数据值分 颜色展示
    """

    def _color(r):
        r = int(r / 100 * 255)
        g = r % 100
        b = 0
        return (r, g, b)

    # return ["#{:02x}{:02x}{:02x}".format(*_color((i + 1) / (1 + len(data)) * 100)) for i in range(len(data))]

    return [_color(i / len(data) * 100) for i in range(len(data))]
    # return  '#F0FFFF'


def get_connection_from():
    """
    默认链接本系统 配置 数据库.
    """
    return Connection(
        port=settings.DATABASE_PORT,
        host=settings.DATABASE_HOST,
        user=settings.DATABASE_USER,
        password=settings.DATABASE_PSW,
        database=settings.DATABASE_NAME,
    )


def get_data(sql):
    conn = get_connection_from()
    records = []
    with conn.cursor(DictCursor) as cursor:
        try:
            cursor.execute(sql)
            records = cursor.fetchall()
        except Exception as e:
            traceback.print_exc()
            print("error: ", sql)
        finally:
            cursor.close()
            conn.close()
    return records


"""
根据 展示需要逐步扩展支持的图表类型
"""


def get_pie(sql, mcfieldnamezh):
    res = dict()
    data = get_data(sql)

    _total = sum(record.get("y") for record in data)
    res["color"] = color(data)
    res["title"] = mcfieldnamezh
    # res["legend"] = [record.get("x") for record in data]

    res["legend"] = []
    res["series"] = [
        {
            "name": mcfieldnamezh,
            "type": "pie",
            "label": {
                "show": "true",
                "position": "top",
            },
            "data": [
                {
                    "value": f"{record.get('y') / _total * 100:.2f}",
                    "name": record.get("x"),
                }
                for record in data
            ],
        },
    ]
    res["interval"] = int(len(data) / 14)
    return res


def get_pie_v1(sql, mcfieldnamezh):
    res = dict()
    data = get_data(sql)

    _total = sum(record.get("y") for record in data)
    res["color"] = color(data)
    res["title"] = mcfieldnamezh
    # res["legend"] = [record.get("x") for record in data]

    res["legend"] = []
    res["series"] = [
        {
            "name": mcfieldnamezh,
            "type": "pie",
            "radius": ["40%", "70%"],
            "avoidLabelOverlap": "false",
            "label": {
                "show": "false",
                "position": "center",
            },
            "emphasis": {"label": {}},
            "labelLine": {"show": "false"},
            "data": [
                {
                    "value": f"{record.get('y') / _total * 100:.2f}",
                    "name": record.get("x"),
                }
                for record in data
            ],
        },
    ]
    res["interval"] = int(len(data) / 14)
    return res


def get_pie_v2(sql, mcfieldnamezh):
    res = dict()
    data = get_data(sql)

    _total = sum(record.get("y") for record in data)
    res["color"] = color(data)
    res["title"] = mcfieldnamezh
    # res["legend"] = [record.get("x") for record in data]

    res["legend"] = []
    res["series"] = [
        {
            "name": mcfieldnamezh,
            "type": "pie",
            "radius": [50, 250],
            "center": ["50%", "50%"],
            "roseType": "area",
            "label": {},
            "data": [
                {
                    "value": f"{record.get('y') / _total * 100:.2f}",
                    "name": record.get("x"),
                }
                for record in data
            ],
        },
    ]
    res["interval"] = int(len(data) / 14)
    return res


def get_line(sql, mcfieldnamezh):
    res = dict()
    data = get_data(sql)
    # print(data)

    res["color"] = color(data)
    res["title"] = mcfieldnamezh
    res["legend"] = [
        mcfieldnamezh,
    ]
    res["series"] = [
        {
            "name": mcfieldnamezh,
            "type": "line",
            "label": {},
            "data": [item["y"] for item in data],
        },
        {
            "name": mcfieldnamezh,
            "type": "bar",
            "label": {},
            "data": [item["y"] for item in data],
        },
    ]
    res["xaxis"] = [str(item["x"]) for item in data]
    res["interval"] = int(len(data) / 14)
    return res


def get_bar(sql, mcfieldnamezh):
    res = dict()
    data = get_data(sql)
    # print(data)

    res["color"] = color(data)
    res["title"] = mcfieldnamezh
    res["legend"] = [
        mcfieldnamezh,
    ]
    res["series"] = [
        {
            "name": mcfieldnamezh,
            "type": "bar",
            "label": {},
            "data": [item["y"] for item in data],
        },
    ]
    res["xaxis"] = [str(item["x"]) for item in data]
    res["interval"] = int(len(data) / 14)
    return res


def get_bar_v1(sql, mcfieldnamezh):
    res = dict()
    data = get_data(sql)
    # print(data)

    res["color"] = color(data)
    res["title"] = mcfieldnamezh
    res["legend"] = [
        mcfieldnamezh,
    ]
    res["series"] = [
        {
            "name": mcfieldnamezh,
            "type": "bar",
            "label": {},
            "data": [item["y"] for item in data],
        },
    ]
    res["xaxis"] = [str(item["x"]) for item in data]
    res["interval"] = int(len(data) / 14)
    return res


def get_line_2(sql, mcfieldnamezh):
    res = dict()
    data = get_data(sql)
    print(data)
    res["color"] = color(data)
    res["title"] = mcfieldnamezh
    res["legend"] = [
        mcfieldnamezh,
    ]
    res["series"] = [
        {
            "name": mcfieldnamezh,
            "type": "line",
            "label": {},
            "data": [item["y"] for item in data],
        },
    ]
    res["xaxis"] = [str(item["x"]) for item in data]
    res["interval"] = int(len(data) / 14)
    return res


def get_bar_2(sql, mcfieldnamezh):
    res = dict()
    data = get_data(sql)
    print(data)
    res["color"] = color(data)
    res["title"] = mcfieldnamezh
    res["legend"] = [
        mcfieldnamezh,
    ]
    res["series"] = [
        {
            "name": mcfieldnamezh,
            "type": "bar",
            "label": {},
            "data": [item["y"] for item in data],
        },
    ]
    res["xaxis"] = [str(item["x"]) for item in data]
    res["interval"] = int(len(data) / 14)
    return res


def get_options():
    return {
        "title": {
            "text": "ECharts 入门示例",
            "subtext": "副标题",
            "left": "center",
        },
        "tooltip": {
            "trigger": "item",
            "formatter": "{a} <br/>{b} : {c} ({d}%)",
        },
        "legend": {
            "orient": "vertical",
            "left": "left",
            "data": ["直接访问", "邮件营销", "联盟广告", "视频广告", "搜索引擎"],
        },
        "series": [
            {
                "name": "访问来源",
            }
        ],
    }
