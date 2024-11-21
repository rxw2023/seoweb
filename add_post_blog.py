from bs4 import BeautifulSoup  
from datetime import datetime  

def add_blog_post(title, date, description, link):  
    # 打开 blog.html 文件  
    with open("blog.html", "r", encoding="utf-8") as file:  
        soup = BeautifulSoup(file, "html.parser")  
    
    # 找到博客文章容器  
    blog_posts_container = soup.find("div", class_="blog-posts")  
    
    # 创建新的博客文章元素  
    new_post = soup.new_tag("div", attrs={"class": "blog-post"})   
    
    # 创建博客标题  
    title_tag = soup.new_tag("h3")  
    title_tag.string = title  
    new_post.append(title_tag)  
    
    # 创建博客的元数据（日期）  
    meta_tag = soup.new_tag("div", attrs={"class": "blog-meta"})  
    date_tag = soup.new_tag("span", attrs={"class": "blog-date"})  
    
    # 创建 <i> 标签并插入日期  
    i_tag = soup.new_tag("i", attrs={"class": "fas fa-calendar-alt"})  
    i_tag.string = f" {date}"  
    
    # 将 <i> 标签添加到日期标签  
    date_tag.append(i_tag)  
    meta_tag.append(date_tag)  
    new_post.append(meta_tag)  
    
    # 创建博客描述  
    description_tag = soup.new_tag("p")  
    description_tag.string = description  
    new_post.append(description_tag)  
    
    # 创建“阅读更多”链接  
    read_more_tag = soup.new_tag("div", attrs={"class": "read-more"})  
    link_tag = soup.new_tag("a", href=link, attrs={"class": "read-more-btn"})  
    link_tag.string = "Read More"  
    read_more_tag.append(link_tag)  
    new_post.append(read_more_tag)  
    
    # 将新博客文章插入到博客文章容器的顶部  
    blog_posts_container.insert(0, new_post)  
    
    # 也将文章添加到最近博客列表  
    recent_blogs = soup.find("div", class_="recent-blogs")  
    recent_blog_list = recent_blogs.find("ul")  
    recent_blog_item = soup.new_tag("li")  
    recent_blog_link = soup.new_tag("a", href=link)  
    recent_blog_link.string = title  
    recent_blog_item.append(recent_blog_link)  
    recent_blog_list.append(recent_blog_item)  
    
    # 将更新后的 HTML 写回文件中  
    with open("blog.html", "w", encoding="utf-8") as file:  
        file.write(str(soup))  

# 输入接口  
def get_blog_input():  
    print("请输入博客文章的信息：")  
    title = input("请输入博客标题：")  
    date = input(f"请输入文章日期（默认格式：{datetime.now().strftime('%Y.%m.%d')}，按回车使用默认日期）：") or datetime.now().strftime("%Y.%m.%d")  
    description = input("请输入博客的简短描述：")  
    link = input("请输入文章的链接（例如：post1.html）：")  
    
    return title, date, description, link  

# 获取用户输入  
title, date, description, link = get_blog_input()  

# 添加博客文章  
add_blog_post(title, date, description, link)
