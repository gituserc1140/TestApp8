import streamlit as st
import pandas as pd
from datetime import datetime

# Sample data for blog posts
blog_posts = [
    {'id': 1, 'title': 'First Post', 'content': 'This is the first blog post.', 'date': '2023-10-01'},
    {'id': 2, 'title': 'Second Post', 'content': 'This is the second blog post.', 'date': '2023-10-02'}
]

def save_posts(posts):
    df = pd.DataFrame(posts)
    df.to_csv('blog_posts.csv', index=False)

def load_posts():
    try:
        df = pd.read_csv('blog_posts.csv')
        return df.to_dict('records')
    except FileNotFoundError:
        return []

st.title('Simple Blog App')

# Load existing posts
blog_posts = load_posts()

# Display all blog posts
st.header('Blog Posts')
for post in blog_posts:
    st.subheader(post['title'])
    st.write(f"Published on: {post['date']}")
    st.write(post['content'])
    st.write('---')

# Form to add a new blog post
st.header('Add a New Blog Post')
with st.form(key='blog_form'):
    title = st.text_input('Title')
    content = st.text_area('Content')
    submit_button = st.form_submit_button(label='Publish')

    if submit_button:
        new_post = {
            'id': len(blog_posts) + 1,
            'title': title,
            'content': content,
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        blog_posts.append(new_post)
        save_posts(blog_posts)
        st.success('Blog post published successfully!')
        st.experimental_rerun()