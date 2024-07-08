import webview, random
import webview.menu as wm
# Configuration settings
webview.settings = {
    'OPEN_DEVTOOLS_IN_DEBUG': True
}
def clone():
    v=(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    q=random.choice(v)
    w=random.choice(v)
    e=random.choice(v)
    r=random.choice(v)
    lk=input('url>')
    window_2 = webview.create_window('new', url=lk)
    window_2.title = f'tab {q}{w}{e}{r}'
def doitrang(window):
    url=input('url>')
    window.load_url(url)
    

if __name__ == '__main__':
    window = webview.create_window('toxicbrowser [debugging]',url='https://www.youtube.com', min_size=(200, 100))

    menu_items = [
        wm.Menu('new page',[wm.MenuAction('more tab', clone),wm.MenuAction('change url', doitrang)])]

print('starting....')
webview.start(debug=True, private_mode=False, storage_path=r'toxicdata', menu=menu_items)
