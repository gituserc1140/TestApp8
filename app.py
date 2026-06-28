import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configuration for file path
BLOG_POSTS_FILE = os.getenv('BLOG_POSTS_FILE', 'blog_posts.csv')

# Sample data for blog posts
blog_posts = []

def save_posts(posts):
    try:
        df = pd.DataFrame(posts)
        df.to_csv(BLOG_POSTS_FILE, index=False)
        st.success('Changes saved successfully!')
    except Exception as e:
        st.error(f"Failed to save posts: {e}")

def load_posts():
    try:
        df = pd.read_csv(BLOG_POSTS_FILE)
        return df.to_dict('records')
    except FileNotFoundError:
        return []
    except Exception as e:
        st.error(f"Failed to load posts: {e}")
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
        if not title or not content:
            st.error("Title and content cannot be empty.")
        else:
            new_post = {
                'id': len(blog_posts) + 1,
                'title': title,
                'content': content,
                'date': datetime.now().strftime('%Y-%m-%d')
            }
            blog_posts.append(new_post)
            save_posts(blog_posts)
            st.success('Blog post published successfully!')
            st.rerun()