from datetime import datetime
from jinja2 import Environment, FileSystemLoader

def generate_blog_post(title, date, description, previous_link, next_link, recent_posts, file_name, image_path):
    # Set up template environment
    env = Environment(loader=FileSystemLoader(searchpath="./"))
    template = env.get_template("blog_template.html")

    # Populate the template with user-entered data
    output = template.render(
        title=title,
        date=date,
        description=description,
        previous_link=previous_link,
        next_link=next_link,
        recent_posts=recent_posts,  # Pass a list of recent blogs
        image_path=image_path  # Add image path
    )

    # 
    output_file = f"{file_name}.html"  # Output to a new HTML file, using a user-specified file name
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output)
    
    print(f"Blog post '{title}' generated as '{output_file}'.")

def get_blog_input():
    print("Please enter blog post details：")
    title = input("Please enter blog title：")
    date = input(f"Please enter the date of the article (default format: {datetime.now().strftime('%Y.%m.%d')}, press Enter to use the default date):") or datetime.now ().strftime("%Y.%m.%d")
    description = input("Please enter your blog:")
    previous_link = input("Please enter the link to the previous article (for example: post1.html):")
    next_link = input("Please enter the next article link (for example: post2.html):")
    file_name = input("Please enter the generated file name (no extension required, such as 'new_blog'):")
    image_path = input("Please enter the image path (for example: img/bg2.jpg):")
    
   # List of recent blogs (enter manually, or dynamically load from file or database)
    recent_posts = [
        {"title": "More Space for Water Shoes Stock & Easier Transportation", "link": "post1.html"},
        {"title": "Organizing The Water Shoes Sample Room", "link": "post2.html"},
        {"title": "Title", "link": "post3.html"},
    ]
    
    return title, date, description, previous_link, next_link, recent_posts, file_name, image_path

if __name__ == "__main__":
    # Get user input
    title, date, description, previous_link, next_link, recent_posts, file_name, image_path = get_blog_input()

    # Generate blog posts
    generate_blog_post(title, date, description, previous_link, next_link, recent_posts, file_name, image_path)
