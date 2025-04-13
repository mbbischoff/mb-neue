#!/usr/bin/env python3

import os
import re
import yaml
from pathlib import Path

# Path to Astro posts
POSTS_DIR = Path("src/content/posts")

# Regular expression to extract frontmatter from posts
FRONTMATTER_REGEX = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

# Custom YAML dumper to avoid anchors and maintain formatting
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

def should_remove_description(description, original_jekyll):
    """Determine if a description should be removed based on certain criteria."""
    if not description:
        return False
    
    # Check if description ends with ellipsis (likely auto-generated)
    ends_with_ellipsis = description.strip().endswith('...')
    
    # Check if description was from original Jekyll (we want to keep those)
    from_original = False
    if original_jekyll:
        from_original = (description == original_jekyll.get('description') or 
                         description == original_jekyll.get('excerpt'))
    
    # If it ends with ellipsis and wasn't from original Jekyll, it's likely auto-generated
    if ends_with_ellipsis and not from_original:
        return True
    
    # If description is just HTML tags or very short, also remove
    if re.match(r'^<[^>]+>.*<\/[^>]+>$', description) or len(description.strip()) < 20:
        return True
    
    return False

def process_post(post_path):
    """Process a single post file to clean up descriptions."""
    
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
    
    # Check if we need to update the frontmatter
    original_jekyll = frontmatter.get('original_jekyll', {})
    description = frontmatter.get('description')
    
    updated = False
    
    # Determine if we should remove the description
    if 'description' in frontmatter and should_remove_description(description, original_jekyll):
        del frontmatter['description']
        updated = True
        print(f"Removed auto-generated description from {post_path.name}")
    
    # If nothing was updated, no need to write
    if not updated:
        return
    
    # Generate new frontmatter text
    updated_frontmatter_text = yaml.dump(
        frontmatter, 
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
    
    print(f"Cleaned up descriptions in {len(processed_posts)} posts")

if __name__ == "__main__":
    process_all_posts()

