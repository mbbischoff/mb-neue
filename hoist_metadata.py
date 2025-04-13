#!/usr/bin/env python3

import os
import re
import yaml
from pathlib import Path
import textwrap

# Path to Astro posts
POSTS_DIR = Path("src/content/posts")

# Regular expression to extract frontmatter from posts
FRONTMATTER_REGEX = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

# Custom YAML dumper to avoid anchors and maintain formatting
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

def extract_first_paragraph(content, max_length=160):
    """Extract first paragraph from content as description."""
    # Find the first paragraph that's not empty
    paragraphs = content.split('\n\n')
    for para in paragraphs:
        if para.strip() and not para.strip().startswith('#') and not para.strip().startswith('!'):
            # Clean up markdown elements
            clean_para = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', para)  # Replace links with text
            clean_para = re.sub(r'[\*_`]', '', clean_para)  # Remove emphasis markers
            clean_para = re.sub(r'\n', ' ', clean_para)  # Replace newlines with spaces
            
            # Truncate if needed and add ellipsis
            if len(clean_para) > max_length:
                clean_para = clean_para[:max_length].rstrip() + '...'
                
            return clean_para
    
    # Fallback to a generic description
    return "A post from the blog archive."

def process_post(post_path):
    """Process a single post file to hoist metadata."""
    
    with open(post_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract frontmatter
    frontmatter_match = FRONTMATTER_REGEX.match(content)
    if not frontmatter_match:
        print(f"Warning: No frontmatter found in {post_path}")
        return
    
    frontmatter_text = frontmatter_match.group(1)
    post_content = content[frontmatter_match.end():]
    
    # Parse frontmatter
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as e:
        print(f"Error parsing frontmatter in {post_path}: {e}")
        return
    
    # Initialize updated frontmatter with existing top-level fields
    updated_frontmatter = {k: v for k, v in frontmatter.items() if k != 'original_jekyll'}
    
    # Get original Jekyll data
    original_jekyll = frontmatter.get('original_jekyll', {})
    if not original_jekyll:
        print(f"Warning: No original_jekyll data found in {post_path}")
        original_jekyll = {}
    
    # Copy remaining original Jekyll data
    remaining_jekyll = original_jekyll.copy()
    
    # Handle description (required field)
    if 'description' not in updated_frontmatter:
        if 'description' in original_jekyll:
            updated_frontmatter['description'] = original_jekyll['description']
            remaining_jekyll.pop('description', None)
        elif 'excerpt' in original_jekyll:
            updated_frontmatter['description'] = original_jekyll['excerpt']
            remaining_jekyll.pop('excerpt', None)
        else:
            # Extract from content as fallback
            updated_frontmatter['description'] = extract_first_paragraph(post_content)
    
    # Handle image field
    if 'image' in original_jekyll:
        updated_frontmatter['image'] = original_jekyll['image']
        remaining_jekyll.pop('image', None)
    elif 'picture' in original_jekyll and 'png_image' in original_jekyll['picture']:
        updated_frontmatter['image'] = original_jekyll['picture']['png_image']
        # Keep picture data for reference
    
    # Handle tags
    if 'tags' in original_jekyll:
        updated_frontmatter['tags'] = original_jekyll['tags']
        remaining_jekyll.pop('tags', None)
    
    # Handle categories
    if 'categories' in original_jekyll:
        updated_frontmatter['categories'] = original_jekyll['categories']
        remaining_jekyll.pop('categories', None)
    
    # Keep the rest of the original_jekyll data
    updated_frontmatter['original_jekyll'] = remaining_jekyll
    
    # Generate new frontmatter text
    updated_frontmatter_text = yaml.dump(
        updated_frontmatter, 
        Dumper=NoAliasDumper,
        default_flow_style=False, 
        allow_unicode=True,
        sort_keys=False
    )
    
    # Build the updated post content
    updated_content = f"---\n{updated_frontmatter_text}---\n\n{post_content}"
    
    # Write the updated post
    with open(post_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"Updated {post_path.name}")
    return post_path

def process_all_posts():
    """Process all posts in the content directory."""
    
    # Get all markdown files
    posts = list(POSTS_DIR.glob('*.md'))
    
    print(f"Found {len(posts)} posts to process")
    
    processed_posts = []
    for post in posts:
        processed_post = process_post(post)
        if processed_post:
            processed_posts.append(processed_post)
    
    print(f"Successfully processed {len(processed_posts)} posts")

if __name__ == "__main__":
    process_all_posts()

