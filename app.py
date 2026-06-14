import os
from flask import Flask, send_from_directory

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
        .input-field { width:100%; padding:12px; background:#121214; border:1px solid #2f2f35; border-radius:5px; color:#fff; margin-top:8px; margin-bottom:15px; outline:none; font-size:1rem; }
        .input-angpao { width:100%; padding:10px; background:#121214; border:1px solid #2f2f35; border-radius:5px; color:#fff; margin-top:10px; outline:none; font-size:0.9rem; }
        .link-text { color:#ff4757; cursor:pointer; text-decoration:underline; font-weight:bold; }
        .line-box { background:rgba(0, 185, 0, 0.1); border:1px solid #00b900; color:#00b900; padding:12px; border-radius:6px; font-size:0.9rem; margin-top:15px; text-align:center; }
    </style>
</head>
<body>
    <header>
        <h1>GG GAME SHOP</h1>
        <button id="menu-toggle-btn" class="menu-btn" style="display:none;" onclick="toggleMenu()"><span>☰</span> เมนู</button>
        <nav id="main-nav">
            <a onclick="switchPage('home')">🛍️ หน้าร้านค้า</a>
            <a onclick="goToLine()">💬 ติดต่อทาง LINE</a>
            <a href="https://www.facebook.com/share/1NwmijHGB5/" target="_blank">📞 ติดต่อทาง Facebook</a>
            <a onclick="logout()">🚪 ออกจากระบบ</a>
        </nav>
    </header>
    
    <div class="container">
        <div id="page-login" class="page active">
            <div class="box">
                <h3 style="margin-bottom:15px; color:#ff4757; text-align:center;">🔑 เข้าสู่ระบบ</h3>
                <label>ชื่อผู้ใช้งาน (Username)</label>
                <input type="text" id="login-user" class="input-field" placeholder="กรอกชื่อผู้ใช้งาน">
                <label>รหัสผ่าน (Password)</label>
                <input type="password" id="login-pass" class="input-field" placeholder="กรอกรหัสผ่าน">
                <button class="btn" onclick="handleLogin()">เข้าสู่ระบบ</button>
                <p style="text-align:center; margin-top:15px; font-size:0.9rem; color:#aaa;">
                    ยังไม่มีบัญชีใช่ไหม? <span class="link-text" onclick="switchPage('register')">สมัครสมาชิกที่นี่</span>
                </p>
            </div>
        </div>

        <div id="page-register" class="page">
            <div class="box">
                <h3 style="margin-bottom:15px; color:#ff9f43; text-align:center;">📝 สมัครสมาชิก</h3>
                <label>ตั้งชื่อผู้ใช้งาน (Username)</label>
                <input type="text" id="reg-user" class="input-field" placeholder="ภาษาอังกฤษหรือตัวเลข">
                <label>ตั้งรหัสผ่าน (Password)</label>
                <input type="password" id="reg-pass" class="input-field" placeholder="อย่างน้อย 4 ตัวขึ้นไป">
                <button class="btn" style="background:#ff9f43;" onclick="handleRegister()">ยืนยันการสมัครสมาชิก</button>
                <p style="text-align:center; margin-top:15px; font-size:0.9rem; color:#aaa;">
                    มีบัญชีอยู่แล้ว? <span class="link-text" onclick="switchPage('login')">เข้าสู่ระบบตรงนี้</span>
                </p>
            </div>
        </div>

        <div id="page-home" class="page">
            <h3 style="margin-bottom:15px;">🛍️ ไอดีเกมแนะนำ</h3>
            
            <div class="box">
                <img src="/get_image/pic.jpg" class="product-img" alt="ID ROBLOX Grow a Garden 2">
                <h4>ID ROBLOX grow a garden 2</h4>
                <p style="color:#aaa; font-size:0.85rem;">ไก่แมพ grow a garden 2</p>
                <div class="price">49 บาท</div>
                <button class="btn" onclick="buyNow('ID ROBLOX grow a garden 2 (ราคา 49)', 49)">ซื้อสินค้า</button>
            </div>
            
            <div class="box">
                <img src="/get_image/pic.jpg" class="product-img" alt="ID ROBLOX Grow a Garden 2">
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
                    <div class="line-box">
                        💬 โอนเงินเสร็จแล้ว กดปุ่มด้านล่างเพื่อส่งสลิปให้แอดมินทาง LINE เพื่อตรวจสอบและรับไอดีเกมได้เลยครับ
                    </div>
                    <button class="btn" style="background:#00b900;" onclick="redirectToLineWithAlert()">📲 ส่งสลิปแจ้งแอดมินใน LINE</button>
                </div>

                <div id="pay-wallet-info" class="pay-info">
                    <p style="color:#ff8c00; font-weight:bold;">🧧 ชำระด้วยซองอั่งเปา TrueMoney</p>
                    <p style="color:#aaa; font-size:0.85rem; margin-top:5px;">วิธีจ่าย: สร้างซองอั่งเปาในแอปวอลเล็ทตามราคาสินค้า (เลือกแบบแบ่งเงินเท่ากัน ใส่จำนวนคนรับ 1 คน) แล้วคัดลอกลิงก์มาวางในช่องด้านล่างนี้ครับ</p>
                    <input type="text" id="angpao-link" class="input-angpao" placeholder="วางลิงก์ซองอั่งเปาที่นี่ (https://gift.truemoney.com/...)" required>
                    <button class="btn" style="background:#00b900;" onclick="sendAngpaoToLine()">📲 ส่งลิงก์อั่งเปาให้แอดมินใน LINE</button>
                </div>
                
                <hr style="border:none; border-top:1px solid #2f2f35; margin:20px 0;">
                <button class="btn" style="background:#444;" onclick="switchPage('home')">กลับหน้าร้าน</button>
            </div>
        </div>
    </div>
    
    <script>
        // เชื่อมต่อเข้ากับลิงก์ LINE จริงของภูมิเรียบร้อยแล้ว
        let lineLink = "https://line.me/ti/p/LNcNfKnZgQ"; 

        if(!localStorage.getItem('users')) {
            localStorage.setItem('users', JSON.stringify({"admin":"1234"}));
        }

        function toggleMenu() {
            const nav = document.getElementById('main-nav');
            nav.style.display = (nav.style.display === 'block') ? 'none' : 'block';
        }

        function switchPage(p) {
            document.querySelectorAll('.page').forEach(e => e.classList.remove('active'));
            document.getElementById('page-' + p).classList.add('active');
            document.getElementById('main-nav').style.display = 'none';
            
            const menuBtn = document.getElementById('menu-toggle-btn');
            if(p === 'login' || p === 'register') {
                menuBtn.style.display = 'none';
            } else {
                menuBtn.style.display = 'inline-flex';
            }
        }

        function handleRegister() {
            const u = document.getElementById('reg-user').value.trim();
            const p = document.getElementById('reg-pass').value.trim();
            if(!u || !p) { alert('กรุณากรอกข้อมูลให้ครบถ้วนครับ!'); return; }
            if(p.length < 4) { alert('รหัสผ่านต้องมีความยาว 4 ตัวขึ้นไปครับ'); return; }

            let db = JSON.parse(localStorage.getItem('users'));
            if(db[u]) { alert('ชื่อผู้ใช้งานนี้มีคนใช้แล้วครับ!'); return; }

            db[u] = p;
            localStorage.setItem('users', JSON.stringify(db));
            alert('🎉 สมัครสมาชิกสำเร็จแล้ว! ระบบจะพาท่านไปหน้าเข้าสู่ระบบ');
            document.getElementById('reg-user').value = '';
            document.getElementById('reg-pass').value = '';
            switchPage('login');
        }

        function handleLogin() {
            const u = document.getElementById('login-user').value.trim();
            const p = document.getElementById('login-pass').value.trim();
            let db = JSON.parse(localStorage.getItem('users'));

            if(db[u] && db[u] === p) {
                alert('🔓 เข้าสู่ระบบสำเร็จ ยินดีต้อนรับสู่ร้านค้าครับ!');
                document.getElementById('login-user').value = '';
                document.getElementById('login-pass').value = '';
                switchPage('home');
            } else {
                alert('❌ ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง ลองอีกครั้งครับ!');
            }
        }

        function logout() {
            alert('🚪 ออกจากระบบเรียบร้อยแล้ว');
            switchPage('login');
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

        function goToLine() {
            window.open(lineLink, '_blank');
        }

        function redirectToLineWithAlert() {
            alert('กำลังพาท่านไปที่ LINE ของแอดมิน... กรุณาส่งหลักฐานการโอนเงินในแชตเพื่อรับไอดีเกมตัวจริงจากแอดมินครับ');
            window.open(lineLink, '_blank');
        }

        function sendAngpaoToLine() {
            const link = document.getElementById('angpao-link').value.trim();
            if(!link) { alert('กรุณาวางลิงก์ซองอั่งเปาก่อนครับ!'); return; }
            if(!link.includes('gift.truemoney.com')) { alert('ลิงก์ไม่ถูกต้อง! ต้องเป็นลิงก์ซองอั่งเปาจาก TrueMoney เท่านั้นครับ'); return; }
            
            navigator.clipboard.writeText(link).then(() => {
                alert('ระบบคัดลอกลิงก์ซองอั่งเปาเรียบร้อยแล้ว! กำลังพาท่านไปที่ LINE ของแอดมิน กรุณากดวาง (Paste) ลิงก์ลงในแชตเพื่อรับไอดีเกมครับ');
                window.open(lineLink, '_blank');
            }).catch(() => {
                window.open(lineLink, '_blank');
            });
            document.getElementById('angpao-link').value = '';
        }
    </script>
</body>
</html>"""

@app.route('/')
def home():
    return html_content

@app.route('/get_image/<filename>')
def get_image(filename):
    return send_from_directory(os.getcwd(), filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
