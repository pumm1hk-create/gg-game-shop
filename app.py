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
        .box { background:#1a1a1e; padding:20px; border-radius:8px; border:1px solid #2f2f35; margin-bottom:15px; overflow:hidden; }
        .product-img { width:100%; height:auto; border-radius:6px; margin-bottom:12px; display:block; }
        .btn { width:100%; background:#ff4757; color:#fff; padding:12px; border:none; border-radius:5px; font-weight:bold; cursor:pointer; text-align:center; display:block; text-decoration:none; margin-top:10px; }
        .price { color:#2ed573; font-weight:bold; margin:5px 0; font-size:1.2rem; }
        .pay-info { display:none; background:#222227; border-left:4px solid #ff4757; padding:15px; border-radius:4px; margin-top:15px; }
        .pay-info.active { display:block; }
        .input-angpao { width:100%; padding:10px; background:#121214; border:1px solid #2f2f35; border-radius:5px; color:#fff; margin-top:10px; outline:none; font-size:0.9rem; }
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
            <h3 style="margin-bottom:15px;">🛍️ ไอดีเกม</h3>
            
            <div class="box">
                <img src="https://i.imgur.com/B9O0Wsc.jpeg" class="product-img" alt="ID ROBLOX Grow a Garden 2">
                <h4>ID ROBLOX grow a garden 2</h4>
                <p style="color:#aaa; font-size:0.85rem;">ไก่แมพ grow a garden 2</p>
                <div class="price">49 บาท</div>
                <button class="btn" onclick="buyNow('ID ROBLOX grow a garden 2 (ราคา 49)', 49)">ซื้อสินค้า</button>
            </div>
            
            <div class="box">
                <img src="https://i.imgur.com/B9O0Wsc.jpeg" class="product-img" alt="ID ROBLOX Grow a Garden 2">
                <h4>ID ROBLOX grow a garden 2</h4>
                <p style="color:#aaa; font-size:0.85rem;">มีเงินในเกมเยอะ</p>
                <div class="price">29 บาท</div>
                <button class="btn" onclick="buyNow('ID ROBLOX grow a garden 2 (ราคา 29)', 29)">ซื้อสินค้า</button>
            </div>
        </div>
        
        <div id="page-checkout" class="page">
            <div class="box">
                <h3 style="margin-bottom:15px; color:#ff4757;">ชำระเงินค่าสินค้า</h3>
                <h4 id="checkout-title">ชื่อสินค้า</h4>
                <div class="price" style="margin-bottom:15px;">ยอดที่ต้องโอน: <span id="checkout-price">0</span> บาท</div>
                <button class="btn" style="background:#00a950;" onclick="showPay('kbank')">🟢 โอนผ่าน กสิกรไทย</button>
                <button class="btn" style="background:#ff8c00;" onclick="showPay('wallet')">🟠 จ่ายผ่าน ลิงก์ซองอั่งเปา</button>
                
                <div id="pay-kbank-info" class="pay-info">
                    <p style="color:#00a950; font-weight:bold;">ธนาคารกสิกรไทย</p>
                    <p style="font-size:1.4rem; font-weight:bold; margin:5px 0;">222-3-21925-3</p>
                    <p style="color:#ccc; font-size:0.85rem;">ชื่อบัญชี: ณัฐภูมิ</p>
                    <p style="color:#ff9f43; font-size:0.85rem; margin-top:10px; text-align:center;">⚠️ โอนเสร็จแล้ว ส่งภาพสลิปให้แอดมินในแชตได้เลย</p>
                    <a href="https://www.facebook.com/share/1NwmijHGB5/" target="_blank" class="btn" style="background:#2ed573;">📲 ส่งสลิปแจ้งแอดมิน</a>
                </div>

                <div id="pay-wallet-info" class="pay-info">
                    <p style="color:#ff8c00; font-weight:bold;">🧧 ชำระด้วยซองอั่งเปา TrueMoney</p>
                    <p style="color:#aaa; font-size:0.85rem; margin-top:5px;">วิธีจ่าย: สร้างซองอั่งเปาในแอปวอลเล็ทตามราคาสินค้า (เลือกแบบแบ่งเงินเท่ากัน ใส่จำนวนคนรับ 1 คน) แล้วคัดลอกลิงก์มาวางในช่องด้านล่างนี้ครับ</p>
                    <input type="text" id="angpao-link" class="input-angpao" placeholder="วางลิงก์ซองอั่งเปาที่นี่ (https://gift.truemoney.com/...)" required>
                    <button class="btn" style="background:#ff8c00;" onclick="sendAngpao()">📲 ส่งข้อมูลซองอั่งเปาให้แอดมิน</button>
                </div>
                
                <hr style="border:none; border-top:1px solid #2f2f35; margin:20px 0;">
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
        function sendAngpao() {
            const link = document.getElementById('angpao-link').value.trim();
            if(!link) { alert('กรุณาวางลิงก์ซองอั่งเปาก่อนครับ!'); return; }
            if(!link.includes('gift.truemoney.com')) { alert('ลิงก์ไม่ถูกต้อง! ต้องเป็นลิงก์ซองอั่งเปาจาก TrueMoney เท่านั้นครับ'); return; }
            
            navigator.clipboard.writeText(link).then(() => {
                alert('ระบบคัดลอกลิงก์ซองอั่งเปาแล้ว! กำลังพาท่านไปส่งแอดมินในเฟซบุ๊ก ให้กดวาง (Paste) ในแชตได้เลยครับ');
                window.open('https://www.facebook.com/share/1NwmijHGB5/', '_blank');
            }).catch(() => {
                window.open('https://www.facebook.com/share/1NwmijHGB5/', '_blank');
            });
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
    
