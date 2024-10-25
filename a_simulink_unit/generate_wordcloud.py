import io
import os
from PIL import Image
from wordcloud import WordCloud
import base64
import jieba

r = os.path.dirname(os.path.abspath(__file__))
font_path = f"{r}/simhei.ttf"


def generate_wordcloud_base64(
    text, width=800, height=400, background_color=None, min_font_size=10
):
    """
    生成词云图并将其转换为base64编码的字符串。

    :param text: 用于生成词云图的文本数据
    :param width: 词云图的宽度（默认800）
    :param height: 词云图的高度（默认400）
    :param background_color: 词云图的背景颜色（默认白色）
    :param min_font_size: 词云图中最小的字体大小（默认10）
    :return: 词云图的base64编码字符串
    """
    if len(text) == 0:
        return ""
    # 停用词

    stopwords_example = [
        "的",
        "了",
        "在",
        "是",
        "我",
        "有",
        "和",
        "人",
        "这",
        "中",
        "大",
        "为",
        "上",
        "个",
        "国",
        "你",
        "们",
        "说",
        "要",
        "他",
        "也",
        "就",
        "去",
        "都",
        "好",
        "看",
        "到",
        "不",
        "一",
        "来",
        "会",
        "没有",
        "着",
        "了",
        "过",
        "得",
        # ... (此处可以继续添加)
    ]
    text = " ".join([word for word in jieba.cut(text) if word not in stopwords_example])

    # 创建WordCloud对象并生成词云图

    wordcloud = WordCloud(
        font_path=font_path,
        width=width,
        height=height,
        background_color=background_color,
        min_font_size=min_font_size,
        mode="RGBA",
    ).generate(text)

    # 将词云图转换为PIL Image对象

    image = Image.fromarray(wordcloud.to_array())

    # 创建一个BytesIO对象，并将PIL Image对象保存为PNG格式的字节流

    byte_array = io.BytesIO()
    image.save(byte_array, format="PNG")

    # 将字节流编码为base64字符串并返回

    return f"data:image/png;base64,{base64.b64encode(byte_array.getvalue()).decode()}"


if __name__ == "__main__":
    # 示例用法

    text = "Python programming language is popular among developers. It is used for web development, data analysis, artificial intelligence, and more."
    base64_encoded_image = generate_wordcloud_base64(text)
    print(base64_encoded_image)
