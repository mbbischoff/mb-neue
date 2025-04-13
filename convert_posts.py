#!/usr/bin/env python3

import os
import re
import shutil
import yaml
from datetime import datetime
from pathlib import Path

# Paths
JEKYLL_POSTS_DIR = Path("../mbbbischoff.com/_posts")
ASTRO_POSTS_DIR = Path("src/content/posts")

# Create the destination directory if it doesn't exist
ASTRO_POSTS_DIR.mkdir(parents=True, exist_ok=True)

# Regular expression to extract frontmatter from Jekyll posts
FRONTMATTER_REGEX = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

# Custom YAML loader to avoid anchors
class NoAliasLoader(yaml.SafeLoader):
    def ignore_aliases(self, data):
        return True

# Custom YAML dumper to avoid anchors
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

def format_date(date_value):
    """Convert any date format to YYYY-MM-DD"""
    if isinstance(date_value, str):
        try:
            # Try to parse string date with time and timezone
            dt_parts = date_value.split()
            if len(dt_parts) > 0:
                # Just take the date part
                return dt_parts[0]
        except (ValueError, IndexError):
            return date_value
    elif isinstance(date_value, datetime):
        return date_value.strftime("%Y-%m-%d")
    return str(date_value)

def convert_post(jekyll_post_path):
    """Convert a Jekyll post to Astro format"""
    
    # Read the Jekyll post content
    with open(jekyll_post_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract frontmatter
    frontmatter_match = FRONTMATTER_REGEX.match(content)
    if not frontmatter_match:
        print(f"Warning: No frontmatter found in {jekyll_post_path}")
        return
    
    frontmatter_text = frontmatter_match.group(1)
    post_content = content[frontmatter_match.end():]
    
    # Parse frontmatter without aliases
    try:
        jekyll_frontmatter = yaml.load(frontmatter_text, Loader=NoAliasLoader)
    except yaml.YAMLError as e:
        print(f"Error parsing frontmatter in {jekyll_post_path}: {e}")
        return
    
    # Create new Astro frontmatter structure
    astro_frontmatter = {}
    
    # Extract and format essential fields for Astro
    if 'title' in jekyll_frontmatter:
        astro_frontmatter['title'] = jekyll_frontmatter['title']
    
    # Handle date conversion
    if 'date' in jekyll_frontmatter:
        date_value = jekyll_frontmatter['date']
        formatted_date = format_date(date_value)
        astro_frontmatter['pubDate'] = formatted_date
    
    # Copy description if available
    if 'description' in jekyll_frontmatter:
        astro_frontmatter['description'] = jekyll_frontmatter['description']
    elif 'excerpt' in jekyll_frontmatter:
        astro_frontmatter['description'] = jekyll_frontmatter['excerpt']
    
    # Create a deep copy of the original Jekyll metadata
    jekyll_metadata = jekyll_frontmatter.copy()
    
    # Remove fields that are already at the top level
    if 'title' in jekyll_metadata:
        del jekyll_metadata['title']
    
    # Store all remaining original Jekyll metadata
    astro_frontmatter['original_jekyll'] = jekyll_metadata
    
    # Generate new frontmatter text without anchors
    astro_frontmatter_text = yaml.dump(
        astro_frontmatter, 
        Dumper=NoAliasDumper,
        default_flow_style=False, 
        allow_unicode=True,
        sort_keys=False  # Preserve field order
    )
    
    # Build the new post content
    astro_content = f"---\n{astro_frontmatter_text}---\n\n{post_content}"
    
    # Generate the new filename
    jekyll_filename = jekyll_post_path.name
    astro_filename = jekyll_filename
    
    # Ensure .md extension
    if astro_filename.endswith('.markdown'):
        astro_filename = astro_filename[:-9] + '.md'
    
    # Create the destination path
    astro_post_path = ASTRO_POSTS_DIR / astro_filename
    
    # Write the Astro post
    with open(astro_post_path, 'w', encoding='utf-8') as file:
        file.write(astro_content)
    
    print(f"Converted {jekyll_post_path.name} -> {astro_post_path.name}")
    return astro_post_path

def convert_all_posts():
    """Convert all Jekyll posts to Astro format"""
    # Skip hidden files and non-Jekyll posts
    jekyll_posts = [f for f in JEKYLL_POSTS_DIR.glob('*.markdown') 
                  if not f.name.startswith('.')]
    
    # Also include .md files
    jekyll_posts.extend([f for f in JEKYLL_POSTS_DIR.glob('*.md') 
                        if not f.name.startswith('.')])
    
    print(f"Found {len(jekyll_posts)} Jekyll posts to convert")
    
    converted_posts = []
    for post in jekyll_posts:
        converted_post = convert_post(post)
        if converted_post:
            converted_posts.append(converted_post)
    
    print(f"Successfully converted {len(converted_posts)} posts")

if __name__ == "__main__":
    convert_all_posts()

