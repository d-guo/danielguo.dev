import frontmatter
import jinja2

from shutil import copyfile


templates_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('_templates'), extensions=['jinja_markdown.MarkdownExtension'])

def writeToSite(text, file_name):
    with open(f'_site/{file_name}', 'w+') as f:
        f.write(text)

def copyFileToSite(file_name, new_file_name=None):
    if not new_file_name:
        copyfile(file_name, f"_site/{file_name.split('/')[-1]}")
    else:
        copyfile(file_name, f"_site/{new_file_name}")

def renderTemplate(template_name, data):
    return templates_environment.get_template(template_name).render(data)

def splitFrontMatterContent(file_name):
    md_file = frontmatter.load(file_name)
    return md_file.metadata, md_file.content
