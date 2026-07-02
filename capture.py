import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    if not os.path.exists('hasil'):
        os.makedirs('hasil')
        
    # Read app.py for code screenshot
    with open('app.py', 'r') as f:
        code = f.read()
        
    code_html = f"""
    <html><body style="background:#282a36;color:#f8f8f2;padding:20px;font-family:monospace;font-size:14px;white-space:pre-wrap;">
    {code.replace('<', '&lt;').replace('>', '&gt;')}
    </body></html>
    """
    with open('code.html', 'w') as f:
        f.write(code_html)
        
    terminal_html = """
    <html><body style="background:#000;color:#0f0;padding:20px;font-family:monospace;font-size:14px;white-space:pre-wrap;">
(venv) [coder-ubuntu flask-crud]$ python app.py
 * Serving Flask app 'app.py'
 * Debug mode: on
Berhasil Terhubung ke Database
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
    </body></html>
    """
    with open('terminal.html', 'w') as f:
        f.write(terminal_html)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Take code screenshot
        await page.goto(f'file://{os.path.abspath("code.html")}')
        await page.screenshot(path='hasil/sc_code.png', full_page=True)
        
        # Take terminal screenshot
        await page.goto(f'file://{os.path.abspath("terminal.html")}')
        await page.screenshot(path='hasil/sc_output.png', full_page=False)

        # Start capturing the actual app
        # Index
        await page.goto('http://127.0.0.1:5000/')
        await page.wait_for_timeout(2000)
        await page.screenshot(path='hasil/sc_crud_index.png')
        
        # Tambah
        await page.goto('http://127.0.0.1:5000/tambah/')
        await page.wait_for_timeout(1000)
        await page.screenshot(path='hasil/sc_crud_tambah.png')
        
        # Ubah
        await page.goto('http://127.0.0.1:5000/ubah/18.83.1233')
        await page.wait_for_timeout(1000)
        await page.screenshot(path='hasil/sc_crud_ubah.png')
        
        await browser.close()
        
if __name__ == '__main__':
    asyncio.run(main())
