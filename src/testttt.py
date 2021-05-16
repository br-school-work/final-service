# write-html-2-mac.py
import webbrowser
import os

f = open('helloworld.html','w')

message = """<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSd7kPTVHy8y7jVi25GXdS04K4LX1z3epg2E4cZ5zJgFyG6Siw/viewform?embedded=true" width="640" height="403" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>"""

f.write(message)
f.close()

#Change path to reflect file location
filename = f'{os.getcwd()}' + 'helloworld.html'
webbrowser.open_new_tab(filename)
