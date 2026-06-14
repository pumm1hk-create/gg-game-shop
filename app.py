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
        .form-group { margin-bottom:15px; }
        .form-group label { display:block; margin-bottom:5px; color:#ccc; font-size:0.9rem; }
        .form-group input { width:100%; padding:10px; background:#121214; border:1px solid #2f2f35; border-radius:5px; color:#fff; outline:none; }
        .btn { width:100%; background:#ff4757; color:#fff; padding:10px; border:none; border-radius:5px; font-weight:bold; cursor:pointer; }
        .link { text-align:center; margin-top:15px; font-size:0.85rem; color:#aaa; }
        .link span { color:#ff4757; cursor:pointer; text-decoration:underline; }
        .price { color:#2ed573; font-weight:bold; margin:5px 0; }
    </style>
</head>
<body>
    <header>
        <h1>GG GAME SHOP</h1>
        <button id="menu-toggle-btn" class="menu-btn" style="display:none;" onclick="toggleMenu()"><span>☰</span> เมนู</button>
        <nav id="main-nav">
            <a onclick="switchPage('home')">🛍️ ไอดีพร้อมขาย (สินค้า)</a>
            <a href="https://www.facebook.com/share/1NwmijHGB5/" target="_blank">📞 ติดต่อเรา</a>
        </nav>
    </header>
    <div class="container">
        <div id="page-register" class="page active">
            <div class="box">
                <h3 style="margin-bottom:15px;">สมัครสมาชิกใหม่</h3>
                <form onsubmit="handleRegister(event)">
                    <div class="form-group"><label>ชื่อผู้ใช้งาน (Username)</label><input type="text" id="reg-user" required></div>
                    <div class="form-group"><label>รหัสผ่าน (Password)</label><input type="password" id="reg-pass" required></div>
                    <div class="form-group"><label>ยืนยันรหัสผ่าน</label><input type="password" id="reg-confirm" required></div>
                    <button type="submit" class="btn">สร้างบัญชีผู้ใช้</button>
                    <div class="link">มีบัญชีอยู่แล้ว? <span onclick="switchPage('login')">เข้าสู่ระบบที่นี่</span></div>
                </form>
            </div>
        </div>
        <div id="page-login" class="page">
            <div class="box">
                <h3 style="margin-bottom:15px;">เข้าสู่ระบบ</h3>
                <form onsubmit="handleLogin(event)">
                    <div class="form-group"><label>ชื่อผู้ใช้งาน (Username)</label><input type="text" id="login-user" required></div>
                    <div class="form-group"><label>รหัสผ่าน (Password)</label><input type="password" id="login-pass" required></div>
                    <button type="submit" class="btn">เข้าสู่ระบบ</button>
                    <div class="link">ยังไม่มีบัญชี? <span onclick="switchPage('register')">สมัครสมาชิกที่นี่</span></div>
                </form>
            </div>
        </div>
        <div id="page-home" class="page">
            <h3 style="margin-bottom:15px;">ไอดีเกมแนะนำ</h3>
            <div class="box">
                <h4>ID ROBLOX - สายฟาร์มโหด</h4>
                <p style="color:#aaa; font-size:0.85rem;">เลเวลตัน มีดาบในตำนานครบ พร้อมเล่น</p>
                <div class="price">350 บาท</div>
                <button class="btn" onclick="addToCart('ID สายฟาร์ม', 350)">ใส่ตะกร้า</button>
            </div>
            <div class="box">
                <h4>ID ROBLOX - สายสุ่มผล</h4>
                <p style="color:#aaa; font-size:0.85rem;">มีเงินในเกมเยอะ มีผลเสือ ผลโมจิ</p>
                <div class="price">150 บาท</div>
                <button class="btn" onclick="addToCart('ID สายสุ่มผล', 150)">ใส่ตะกร้า</button>
            </div>
            <div class="box" style="border-color:#2ed573;">
                <h4>ตะกร้าสินค้าของคุณ</h4>
                <div id="cart-list" style="margin:10px 0; color:#aaa; font-size:0.9rem;"><p>ยังไม่มีสินค้าในตะกร้า</p></div>
                <div style="font-weight:bold; color:#2ed573; margin-bottom:10px;">รวมทั้งหมด: <span id="total-price">0</span> บาท</div>
                <button class="btn" style="background:#2ed573;" onclick="checkoutLine()">สั่งซื้อผ่าน LINE</button>
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
        function handleRegister(e) {
            e.preventDefault();
            const u = document.getElementById('reg-user').value.trim();
            const p = document.getElementById('reg-pass').value;
            const c = document.getElementById('reg-confirm').value;
            if(p !== c) { alert('รหัสผ่านไม่ตรงกันครับ!'); return; }
            if(p.length < 6) { alert('รหัสผ่านต้องมี 6 ตัวขึ้นไปครับ!'); return; }
            localStorage.setItem('user_data', u);
            localStorage.setItem('pass_data', p);
            alert('สมัครสมาชิกสำเร็จแล้ว!');
            switchPage('login');
        }
        function handleLogin(e) {
            e.preventDefault();
            const u = document.getElementById('login-user').value.trim();
            const p = document.getElementById('login-pass').value;
            if(u === localStorage.getItem('user_data') && p === localStorage.getItem('pass_data')) {
                alert('เข้าสู่ระบบสำเร็จ!');
                document.getElementById('menu-toggle-btn').style.display = 'inline-flex';
                switchPage('home');
            } else {
                alert('ชื่อผู้ใช้งาน หรือ รหัสผ่านไม่ถูกต้อง!');
            }
        }
        let cart = []; let total = 0;
        function addToCart(n, pr) {
            cart.push({name:n, price:pr}); total += pr;
            const l = document.getElementById('cart-list'); l.innerHTML = '';
            cart.forEach(i => { l.innerHTML += `<div style="display:flex; justify-content:space-between; margin-bottom:5px;"><span>` + i.name + `</span><span>` + i.price + ` บ.</span></div>`; });
            document.getElementById('total-price').innerText = total;
        }
        function checkoutLine() {
            if(cart.length === 0) { alert('กรุณาเลือกสินค้าก่อนครับ!'); return; }
            let m = "ต้องการซื้อไอดีเกม:\\n";
            cart.forEach((i, x) => { m += (x+1) + ". " + i.name + " (" + i.price + " บาท)\\n"; });
            m += "ยอดรวม: " + total + " บาท";
            window.open("https://line.me/R/msg/text/?" + encodeURIComponent(m), '_blank');
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
  
