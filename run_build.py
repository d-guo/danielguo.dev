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

# copy styling into blog section
for styling in os.listdir('_styles'):
    utils.copyFileToSite(f'_styles/{styling}', f'blog/{styling}')
print('copied styling into blog section')

# render main index into blog section
blogdata = {'blogs': [utils.splitFrontMatterContent(f'_blogposts/{blogpost}')[0] | {'url': f'{"".join(blogpost.split(".")[:-1])}.html'} for blogpost in os.listdir('_blogposts')]}
blogdata['blogs'].sort(key=lambda x: x['order'], reverse=True)
text = utils.renderTemplate('blog-index.html', blogdata)
utils.writeToSite(text, 'blog/index.html')
print('rendered index into _site')

# render blogpages into _site
for blogpost in os.listdir('_blogposts'):
    front_matter, content = utils.splitFrontMatterContent(f'_blogposts/{blogpost}')

    blogpost_data = front_matter
    blogpost_data['content'] = markdown2.markdown(content, extras=["tables", "cuddled-lists", "code-friendly", "fenced-code-blocks"])

    template = 'blogpage.html'
    text = utils.renderTemplate(template, blogpost_data)
    utils.writeToSite(text, f'blog/{"".join(blogpost.split(".")[:-1])}.html')

print('success')