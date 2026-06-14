import os
from flask import Flask

app = Flask(__name__)

html_content = """<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GG GAME SHOP</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; font-family:sans-serif; }
        body { background:#121214; color:#fff; padding:15px; }
        header { background:#1a1a1e; text-align:center; padding:15px; border-bottom:2px solid #ff4757; position:relative; }
        header h1 { color:#ff4757; font-size:1.8rem; }
        .menu-btn { background:#ff9f43; color:#fff; border:2px solid rgba(255,255,255,0.4); padding:8px 16px; border-radius:12px; font-size:1rem; font-weight:bold; cursor:pointer; display:inline-flex; align-items:center; gap:8px; margin-top:10px; }
        nav { display:none; background:#222227; margin-top:10px; border-radius:8px; overflow:hidden; border:1px solid #2f2f35; }
        nav a { display:block; color:#fff; text-decoration:none; padding:12px; font-weight:bold; border-bottom:1px solid #2f2f35; cursor:pointer; }
        nav a:hover { background:#ff4757; }
        .container { max-width:500px; margin:20px auto; }
        .page { display:none; } .page.active { display:block; }
        .box { background:#1a1a1e; padding:20px; border-radius:8px; border:1px solid #2f2f35; margin-bottom:15px; }
        .btn { width:100%; background:#ff4757; color:#fff; padding:12px; border:none; border-radius:5px; font-weight:bold; cursor:pointer; text-align:center; display:block; text-decoration:none; margin-top:10px; }
        .price { color:#2ed573; font-weight:bold; margin:5px 0; font-size:1.2rem; }
        .pay-info { display:none; background:#222227; border-left:4px solid #ff4757; padding:15px; border-radius:4px; margin-top:15px; }
        .pay-info.active { display:block; }
    </style>
</head>
<body>
    <header>
        <h1>GG GAME SHOP</h1>
        <button class="menu-btn" onclick="toggleMenu()"><span>☰</span> เมนู</button>
        <nav id="main-nav">
            <a onclick="switchPage('home')">🛍️ หน้าร้านค้า</a>
            <a href="https://www.facebook.com/share/1NwmijHGB5/" target="_blank">📞 ติดต่อเรา</a>
        </nav>
    </header>
    
    <div class="container">
        <div id="page-home" class="page active">
            <h3 style="margin-bottom:15px;">🛍️ ไอดีเกมแนะนำ</h3>
            <div class="box">
                <h4>ID ROBLOX - สายฟาร์มโหด</h4>
                <p style="color:#aaa; font-size:0.85rem;">เลเวลตัน มีดาบในตำนานครบ พร้อมเล่น</p>
                <div class="price">350 บาท</div>
                <button class="btn" onclick="buyNow('ID ROBLOX - สายฟาร์มโหด', 350)">ซื้อสินค้า</button>
            </div>
            <div class="box">
                <h4>ID ROBLOX - สายสุ่มผล</h4>
                <p style="color:#aaa; font-size:0.85rem;">มีเงินในเกมเยอะ มีผลเสือ ผลโมจิในคลัง</p>
                <div class="price">150 บาท</div>
                <button class="btn" onclick="buyNow('ID ROBLOX - สายสุ่มผล', 150)">ซื้อสินค้า</button>
            </div>
        </div>
        
        <div id="page-checkout" class="page">
            <div class="box">
                <h3 style="margin-bottom:15px; color:#ff4757;">ชำระเงินค่าสินค้า</h3>
                <h4 id="checkout-title">ชื่อสินค้า</h4>
                <div class="price" style="margin-bottom:15px;">ยอดที่ต้องโอน: <span id="checkout-price">0</span> บาท</div>
                <button class="btn" style="background:#00a950;" onclick="showPay('kbank')">🟢 โอนผ่าน กสิกรไทย</button>
                <button class="btn" style="background:#ff8c00;" onclick="showPay('wallet')">🟠 โอนผ่าน ทูมันนี่ วอลเล็ท</button>
                
                <div id="pay-kbank-info" class="pay-info">
                    <p style="color:#00a950; font-weight:bold;">ธนาคารกสิกรไทย</p>
                    <p style="font-size:1.4rem; font-weight:bold; margin:5px 0;">222-3-21925-3</p>
                    <p style="color:#ccc; font-size:0.85rem;">ชื่อบัญชี: ณัฐภูมิ</p>
                </div>
                <div id="pay-wallet-info" class="pay-info">
                    <p style="color:#ff8c00; font-weight:bold;">ทูมันนี่ วอลเล็ท</p>
                    <p style="font-size:1.4rem; font-weight:bold; margin:5px 0;">090-946-5370</p>
                    <p style="color:#ccc; font-size:0.85rem;">ชื่อบัญชี: ณัฐภูมิ เขียววารี</p>
                </div>
                
                <hr style="border:none; border-top:1px solid #2f2f35; margin:20px 0;">
                <p style="color:#ff9f43; font-size:0.85rem; text-align:center; margin-bottom:10px;">⚠️ โอนเสร็จแล้ว ส่งสลิปมาที่เฟซบุ๊กได้เลย!</p>
                <a href="https://www.facebook.com/share/1NwmijHGB5/" target="_blank" class="btn" style="background:#2ed573;">📲 ส่งสลิปแจ้งแอดมิน</a>
                <button class="btn" style="background:#444;" onclick="switchPage('home')">กลับหน้าร้าน</button>
            </div>
        </div>
    </div>
    
    <script>
        function toggleMenu() {
            const nav = document.getElementById('main-nav');
            nav.style.display = (nav.style.display === 'block') ? 'none' : 'block';
        }
        function switchPage(p) {
            document.querySelectorAll('.page').forEach(e => e.classList.remove('active'));
            document.getElementById('page-' + p).classList.add('active');
            document.getElementById('main-nav').style.display = 'none';
        }
        function buyNow(name, price) {
            document.getElementById('checkout-title').innerText = name;
            document.getElementById('checkout-price').innerText = price;
            document.querySelectorAll('.pay-info').forEach(e => e.classList.remove('active'));
            switchPage('checkout');
        }
        function showPay(type) {
            document.querySelectorAll('.pay-info').forEach(e => e.classList.remove('active'));
            document.getElementById('pay-' + type + '-info').classList.add('active');
        }
    </script>
</body>
</html>"""

@app.route('/')
def home():
    return html_content

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
