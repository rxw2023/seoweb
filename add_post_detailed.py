from datetime import datetime  
from jinja2 import Environment, FileSystemLoader  

def generate_blog_post(title, date, description, previous_link, next_link, recent_posts, file_name, image_path):  
    # 设置模板环境  
    env = Environment(loader=FileSystemLoader(searchpath="./"))  
    template = env.get_template("blog_template.html")  

    # 用用户输入的数据填充模板  
    output = template.render(  
        title=title,  
        date=date,  
        description=description,  
        previous_link=previous_link,  
        next_link=next_link,  
        recent_posts=recent_posts,  # 传递最近博客的列表  
        image_path=image_path  # 添加图片路径  
    )  

    # 将输出写入新的HTML文件，使用用户指定的文件名  
    output_file = f"{file_name}.html"  
    with open(output_file, "w", encoding="utf-8") as f:  
        f.write(output)  
    
    print(f"博客文章 '{title}' 已生成，文件名为 '{output_file}'。")  

def get_blog_input():  
    print("请输入博客文章的详细信息：")  
    title = input("请输入博客标题：")  
    date = input(f"请输入文章日期（默认格式: {datetime.now().strftime('%Y.%m.%d')}，按回车使用默认日期）：") or datetime.now().strftime("%Y.%m.%d")  
    description = input("请输入您的博客内容：")  
    previous_link = input("请输入上一篇文章的链接（例如：post1.html）：")  
    next_link = input("请输入下一篇文章的链接（例如：post2.html）：")  
    file_name = input("请输入生成的文件名（不带扩展名，例如 'new_blog'）：")  
    image_path = input("请输入图片路径（例如：img/bg2.jpg），或按回车表示没有图片：") or ""  

    # 最近博客的列表  
    recent_posts = [  
        {"title": "More Space for Water Shoes Stock & Easier Transportation", "link": "post1.html"},  
        {"title": "Organizing The Water Shoes Sample Room", "link": "post2.html"},  
        {"title": "What Are Water Shoes Made Of?", "link": "post3.html"},  
    ]  
    
    return title, date, description, previous_link, next_link, recent_posts, file_name, image_path  

if __name__ == "__main__":  
    # 获取用户输入  
    title, date, description, previous_link, next_link, recent_posts, file_name, image_path = get_blog_input()  

    # 生成博客文章  
    generate_blog_post(title, date, description, previous_link, next_link, recent_posts, file_name, image_path)
