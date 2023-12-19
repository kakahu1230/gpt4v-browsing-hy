const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

const url = process.argv[2];
const timeout = 8000;

(async () => {
    const browser = await puppeteer.launch( {
        headless: "new",
    } );

    const page = await browser.newPage();

    await page.setViewport( {
        width: 1200,
        height: 200,
        deviceScaleFactor: 1,
    } );

    await page.goto( url, {
        waitUntil: "domcontentloaded",
        timeout: timeout,
    } );
    console.log('visit url page');

    // await page.waitForTimeout(timeout);
    try{
        await page.screenshot( {
            path: "screenshot.jpg",
            fullPage: true,
        } );
    } catch(err) {
        console.log('Error: ${err.message}');
    } finally{
        await browser.close();
    }
    
})();
