import markdown
from . import mdx_downheader
from . import mdx_math
from django.shortcuts import HttpResponse


def convert(text):
    md = markdown.Markdown(
        extensions=[mdx_downheader.makeExtension(levels=3),
                    mdx_math.makeExtension(enable_dollar_delimiter=True, add_preview=False),
                    'codehilite',
                    'nl2br',
                    ]
    )
    return md.convert(text)


def markdown_convert_api(request):
    return HttpResponse(convert(request.body.decode()))
