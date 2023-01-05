import os

import markdown2
import yaml

import utils

from shutil import rmtree


# load data from _config.yml
with open("_config.yml", 'r') as stream:
    data = yaml.load(stream, Loader=yaml.FullLoader)
print('succesfully loaded site config from _config.yml')

# delete all files in _site
rmtree('_site')
os.makedirs('_site')
print('deleted previous files in _site')

# copy styling into _site
for styling in os.listdir('_styles'):
    utils.copyFileToSite(f'_styles/{styling}')
print('copied styling into _site')

# render main index into _site
text = utils.renderTemplate('index.html', data)
utils.writeToSite(text, 'index.html')
print('rendered index into _site')

# create blog section of _site
os.makedirs('_site/blog')

# create blog archive section of _site
os.makedirs('_site/blog/archive')

# copy styling into blog and archive section
for styling in os.listdir('_styles'):
    utils.copyFileToSite(f'_styles/{styling}', f'blog/{styling}')
    utils.copyFileToSite(f'_styles/{styling}', f'blog/archive/{styling}')
print('copied styling into blog and archive section')

# render main index into blog section
blogdata = {'blogs': [utils.splitFrontMatterContent(f'_blogposts/{blogpost}')[0] | {'url': f'{"".join(blogpost.split(".")[:-1])}.html'} for blogpost in os.listdir('_blogposts') if blogpost[-3:] == '.md']}
blogdata['blogs'].sort(key=lambda x: x['order'], reverse=True)
blogdata['blog_template_title'] = 'Blog Posts'
text = utils.renderTemplate('blog-index.html', blogdata)
utils.writeToSite(text, 'blog/index.html')
print('rendered blog index into blog')

# render main index into blog archive section
blogdata = {'blogs': [utils.splitFrontMatterContent(f'_blogposts/archive/{blogpost}')[0] | {'url': f'{"".join(blogpost.split(".")[:-1])}.html'} for blogpost in os.listdir('_blogposts/archive') if blogpost[-3:] == '.md']}
blogdata['blogs'].sort(key=lambda x: x['order'], reverse=True)
blogdata['blog_template_title'] = 'Archived Blog Posts'
text = utils.renderTemplate('blog-index.html', blogdata)
utils.writeToSite(text, 'blog/archive/index.html')
print('rendered archive index into blog/archive')

# render blogpages into blog
for blogpost in [blogpost for blogpost in os.listdir('_blogposts') if blogpost[-3:] == '.md']:
    front_matter, content = utils.splitFrontMatterContent(f'_blogposts/{blogpost}')

    blogpost_data = front_matter
    blogpost_data['content'] = markdown2.markdown(content, extras=["tables", "cuddled-lists", "code-friendly", "fenced-code-blocks"])

    template = 'blogpage.html'
    text = utils.renderTemplate(template, blogpost_data)
    utils.writeToSite(text, f'blog/{"".join(blogpost.split(".")[:-1])}.html')
print('rendered blogposts into blog')

# render blogpages into blog archive
for blogpost in [blogpost for blogpost in os.listdir('_blogposts/archive') if blogpost[-3:] == '.md']:
    front_matter, content = utils.splitFrontMatterContent(f'_blogposts/archive/{blogpost}')

    blogpost_data = front_matter
    blogpost_data['content'] = markdown2.markdown(content, extras=["tables", "cuddled-lists", "code-friendly", "fenced-code-blocks"])

    template = 'blogpage.html'
    text = utils.renderTemplate(template, blogpost_data)
    utils.writeToSite(text, f'blog/archive/{"".join(blogpost.split(".")[:-1])}.html')
print('rendered blogposts into blog archive')

print('success')