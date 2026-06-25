import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    if not os.path.exists("assets"):
        os.makedirs("assets")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        # Navigate to Streamlit app
        await page.goto("http://localhost:8501")
        # Wait for Streamlit to load completely (wait for the analyze button)
        await page.wait_for_selector("button:has-text('Analyze Logs')", timeout=10000)
        # Give it a second to render
        await asyncio.sleep(2)
        
        # Take dashboard screenshot
        await page.screenshot(path="assets/dashboard.png", full_page=True)
        print("Captured dashboard.png")
        
        # Click the Analyze button
        await page.click("button:has-text('Analyze Logs')")
        
        # Wait for the results to load (wait for the alert text)
        await page.wait_for_selector("text=Critical Security Threats", timeout=10000)
        # Give it a second to render expanders
        await asyncio.sleep(2)
        
        # Take alert panel screenshot
        await page.screenshot(path="assets/alert_panel.png", full_page=True)
        print("Captured alert_panel.png")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
