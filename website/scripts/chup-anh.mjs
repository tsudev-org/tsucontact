// Chụp trang chủ Sáng + Tối để đính vào PR (ảnh trước/sau). Cách dùng:
//   node scripts/chup-anh.mjs <thư-mục-ra> [url-gốc]   - bỏ url-gốc thì phục vụ dist/ cục bộ
import { mkdirSync } from 'node:fs';
import { chromium } from 'playwright';
import { moMayChu } from './may-chu-tinh.mjs';

const [ra = 'anh-chup', goc] = process.argv.slice(2);
mkdirSync(ra, { recursive: true });
const mayChu = goc ? null : await moMayChu();
const base = goc ?? mayChu.base;
const browser = await chromium.launch();
for (const cheDo of ['light', 'dark']) {
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  await context.addInitScript((c) => { try { localStorage.setItem('tsudev-theme', c); } catch { /* bỏ qua */ } }, cheDo);
  const page = await context.newPage();
  await page.goto(`${base}/`, { waitUntil: 'networkidle' });
  await page.screenshot({ path: `${ra}/trang-chu-${cheDo}.png` });
  await context.close();
}
await browser.close();
mayChu?.dong();
console.log(`[chup-anh] đã lưu vào ${ra}`);
