from bs4 import BeautifulSoup
from datetime import datetime

def add_blog_post(title, date, description, link):
    # Open the blog.html file
    with open("blog.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    # Find the parent container of the pagination element
    pagination_container = soup.find("div", class_="pagination")
    
    # Find the blog post container
    blog_posts_container = soup.find("div", class_="blog-posts")
    
    # Create a new blog post element
    new_post = soup.new_tag("div", attrs={"class": "blog-post"}) 
    
    # Create blog title
    title_tag = soup.new_tag("h3")
    title_tag.string = title
    new_post.append(title_tag)
    
    # Create blog metadata (date)
    meta_tag = soup.new_tag("div", attrs={"class": "blog-meta"})
    date_tag = soup.new_tag("span", attrs={"class": "blog-date"})
    
    # Create an <i> tag and insert the date
    i_tag = soup.new_tag("i", attrs={"class": "fas fa-calendar-alt"})
    i_tag.string = f" {date}"
    
    # Add <i> tag to date tag
    date_tag.append(i_tag)
    meta_tag.append(date_tag)
    new_post.append(meta_tag)
    
    # Create a description for your blog
    description_tag = soup.new_tag("p")
    description_tag.string = description
    new_post.append(description_tag)
    
    # Create a "Read More" link
    read_more_tag = soup.new_tag("div", attrs={"class": "read-more"})
    link_tag = soup.new_tag("a", href=link, attrs={"class": "read-more-btn"})
    link_tag.string = "Read More"
    read_more_tag.append(link_tag)
    new_post.append(read_more_tag)
    
    # Insert new blog post before pagination element
    pagination_container.insert_before(new_post)
    
    # Also adds the article to the list of recent blogs
    recent_blogs = soup.find("div", class_="recent-blogs")
    recent_blog_list = recent_blogs.find("ul")
    recent_blog_item = soup.new_tag("li")
    recent_blog_link = soup.new_tag("a", href=link)
    recent_blog_link.string = title
    recent_blog_item.append(recent_blog_link)
    recent_blog_list.append(recent_blog_item)
    
    # Write updated HTML back to file
    with open("blog.html", "w", encoding="utf-8") as file:
        file.write(str(soup))

# Input interface
def get_blog_input():
    print("Please enter the block information for the blog post：")
    title = input("Please enter blog title：")
    date = input(f"Please enter the article date（Default format：{datetime.now().strftime('%Y.%m.%d')}，Press enter to use the default date）：") or datetime.now().strftime("%Y.%m.%d")
    description = input("Please enter a short description of your blog：")
    link = input("Please enter the link to the article（For example：post1.html）：")
    
    return title, date, description, link

# Get user input
title, date, description, link = get_blog_input()

# Add blog post
add_blog_post(title, date, description, link)
