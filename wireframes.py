
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor

W, H = A4
PAD = 14 * mm

# Colour palette
C_BG       = HexColor("#F7F7F5")
C_WHITE    = HexColor("#FFFFFF")
C_BORDER   = HexColor("#E0DED6")
C_TEXT     = HexColor("#1A1A18")
C_MUTED    = HexColor("#6B6B68")
C_HINT     = HexColor("#A0A09C")
C_GREEN    = HexColor("#1D9E75")
C_GREEN_LT = HexColor("#E1F5EE")
C_GREEN_DK = HexColor("#085041")
C_WARN     = HexColor("#BA7517")
C_WARN_LT  = HexColor("#FAEEDA")
C_RED      = HexColor("#E24B4A")
C_RED_LT   = HexColor("#FCEBEB")
C_BLUE     = HexColor("#185FA5")
C_BLUE_LT  = HexColor("#E6F1FB")
C_SIDEBAR  = HexColor("#F2F2EF")

def new_page(c, title, subtitle="", page_num=1, total=17):
    c.showPage()
    c.setPageSize(A4)
    # header bar
    c.setFillColor(C_WHITE)
    c.rect(0, H - 11*mm, W, 11*mm, fill=1, stroke=0)
    c.setStrokeColor(C_BORDER)
    c.setLineWidth(0.4)
    c.line(0, H - 11*mm, W, H - 11*mm)
    # logo
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(C_TEXT)
    c.drawString(PAD, H - 7.5*mm, "Fuel")
    c.setFillColor(C_GREEN)
    c.drawString(PAD + 17, H - 7.5*mm, "Flow")
    c.setFillColor(C_MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(PAD + 42, H - 7.5*mm, "UI Wireframes")
    # page num
    c.setFont("Helvetica", 7.5)
    c.setFillColor(C_HINT)
    c.drawRightString(W - PAD, H - 7.5*mm, f"{page_num} / {total}")
    # page bg
    c.setFillColor(C_BG)
    c.rect(0, 0, W, H - 11*mm, fill=1, stroke=0)
    # screen label
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(C_TEXT)
    c.drawString(PAD, H - 21*mm, title)
    if subtitle:
        c.setFont("Helvetica", 8.5)
        c.setFillColor(C_MUTED)
        c.drawString(PAD, H - 26*mm, subtitle)

def card(c, x, y, w, h, fill=C_WHITE, radius=4, stroke=True):
    c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(C_BORDER)
        c.setLineWidth(0.4)
    else:
        c.setStrokeColor(fill)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)

def label(c, x, y, text, size=7.5, color=C_MUTED, font="Helvetica"):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawString(x, y, text)

def rlabel(c, x, y, text, size=7.5, color=C_MUTED, font="Helvetica"):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawRightString(x, y, text)

def pill(c, x, y, text, bg, fg, size=6.5):
    c.setFont("Helvetica", size)
    tw = c.stringWidth(text, "Helvetica", size)
    pw, ph = tw + 8, 9
    c.setFillColor(bg)
    c.setStrokeColor(bg)
    c.roundRect(x, y - 1.5, pw, ph, 4, fill=1, stroke=0)
    c.setFillColor(fg)
    c.drawString(x + 4, y + 4, text)
    return pw

def topbar(c, active_item=None, show_nav=True, role="owner"):
    bar_y = H - 11*mm - 9*mm
    c.setFillColor(C_WHITE)
    c.rect(PAD, bar_y, W - 2*PAD, 9*mm, fill=1, stroke=0)
    c.setStrokeColor(C_BORDER)
    c.setLineWidth(0.4)
    c.line(PAD, bar_y, W - PAD, bar_y)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(C_TEXT)
    c.drawString(PAD + 2, bar_y + 3.2*mm, "Fuel")
    c.setFillColor(C_GREEN)
    c.drawString(PAD + 16, bar_y + 3.2*mm, "Flow")
    if show_nav:
        nav_items = ["Dashboard","Stations","Reports","Credit","Inventory","Staff","Settings"]
        x = PAD + 45
        for item in nav_items:
            c.setFont("Helvetica", 7)
            tw = c.stringWidth(item, "Helvetica", 7)
            if item == active_item:
                c.setFillColor(C_BG)
                c.roundRect(x - 3, bar_y + 1.5*mm, tw + 6, 6*mm, 3, fill=1, stroke=0)
                c.setFillColor(C_TEXT)
                c.setFont("Helvetica-Bold", 7)
            else:
                c.setFillColor(C_MUTED)
            c.drawString(x, bar_y + 3.5*mm, item)
            x += tw + 12
    # avatar
    av_x = W - PAD - 10
    c.setFillColor(C_GREEN_LT)
    c.circle(av_x, bar_y + 4.5*mm, 4.5*mm, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 6)
    c.setFillColor(C_GREEN_DK)
    initials = "RK" if role == "owner" else "AK"
    c.drawCentredString(av_x, bar_y + 3*mm, initials)
    return bar_y

def sidebar(c, items, active, start_x, start_y, w=36*mm, item_h=7.5*mm):
    c.setFillColor(C_SIDEBAR)
    sidebar_h = len(items) * item_h + 6
    c.rect(start_x, start_y - sidebar_h, w, sidebar_h, fill=1, stroke=0)
    c.setStrokeColor(C_BORDER)
    c.setLineWidth(0.4)
    c.line(start_x + w, start_y - sidebar_h, start_x + w, start_y)
    for i, item in enumerate(items):
        iy = start_y - (i + 1) * item_h + 1
        if item == active:
            c.setFillColor(C_GREEN_LT)
            c.roundRect(start_x + 2, iy, w - 4, item_h - 2, 3, fill=1, stroke=0)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(C_GREEN_DK)
        else:
            c.setFont("Helvetica", 7)
            c.setFillColor(C_MUTED)
        c.drawString(start_x + 6, iy + 2.5*mm, item)
    return sidebar_h

def divider(c, x, y, w):
    c.setStrokeColor(C_BORDER)
    c.setLineWidth(0.3)
    c.line(x, y, x + w, y)

def metric_card(c, x, y, w, h, label_text, value, delta="", vcolor=C_TEXT):
    card(c, x, y, w, h)
    label(c, x + 5, y + h - 10, label_text, 6.5, C_MUTED)
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(vcolor)
    c.drawString(x + 5, y + 8, value)
    if delta:
        label(c, x + 5, y + 2, delta, 6, C_HINT)

def section_heading(c, x, y, text):
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(C_TEXT)
    c.drawString(x, y, text)

def cover_page(c):
    c.setPageSize(A4)
    c.setFillColor(C_WHITE)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    # green band top
    c.setFillColor(C_GREEN)
    c.rect(0, H - 60*mm, W, 60*mm, fill=1, stroke=0)
    # logo
    c.setFillColor(C_WHITE)
    c.setFont("Helvetica-Bold", 36)
    c.drawString(PAD, H - 28*mm, "FuelFlow")
    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#C8EEE0"))
    c.drawString(PAD, H - 40*mm, "ERP for petrol pumps")
    # title block
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(C_TEXT)
    c.drawString(PAD, H - 80*mm, "UI Wireframes")
    c.setFont("Helvetica", 11)
    c.setFillColor(C_MUTED)
    c.drawString(PAD, H - 92*mm, "Complete screen designs — web & mobile")
    # divider
    c.setStrokeColor(C_BORDER)
    c.setLineWidth(0.5)
    c.line(PAD, H - 100*mm, W - PAD, H - 100*mm)
    # index
    screens = [
        ("Web — Owner", [
            "01  Login",
            "02  Owner dashboard",
            "03  Stations list",
            "04  Station detail & nozzles",
            "05  Inventory & stock",
            "06  Shifts list",
            "07  Sales & transactions",
            "08  Credit customers",
            "09  Reports",
            "10  Settings & staff",
        ]),
        ("Web — Operator", [
            "11  Operator shift home",
            "12  New sale entry",
            "13  Close shift",
            "14  Expenses",
        ]),
        ("Mobile — Owner & Operator", [
            "15  Mobile owner screens",
            "16  Mobile operator screens",
            "17  Offline & AI copilot",
        ]),
    ]
    y = H - 112*mm
    for group, items in screens:
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(C_GREEN)
        c.drawString(PAD, y, group)
        y -= 6*mm
        for item in items:
            c.setFont("Helvetica", 8.5)
            c.setFillColor(C_TEXT)
            c.drawString(PAD + 4, y, item)
            y -= 5.5*mm
        y -= 3*mm
    # footer
    c.setFont("Helvetica", 7.5)
    c.setFillColor(C_HINT)
    c.drawString(PAD, 12*mm, "FuelFlow — Confidential. For internal use only.")
    c.drawRightString(W - PAD, 12*mm, "June 2025")

def draw_row(c, x, y, w, col1, col2, col1_color=C_MUTED, col2_color=C_TEXT, bold2=True):
    label(c, x, y, col1, 7, col1_color)
    f = "Helvetica-Bold" if bold2 else "Helvetica"
    c.setFont(f, 7)
    c.setFillColor(col2_color)
    c.drawRightString(x + w, y, col2)
    divider(c, x, y - 1.5, w)

# ─── Build PDF ────────────────────────────────────────────────────────────────
c = canvas.Canvas("/mnt/user-data/outputs/FuelFlow_Wireframes.pdf", pagesize=A4)
c.setTitle("FuelFlow UI Wireframes")
c.setAuthor("FuelFlow")

cover_page(c)

TOTAL = 17
SI_ITEMS = ["Overview","Stations","Sales","Inventory","Shifts","Credit","Reports","Settings"]

# ── PAGE 1: LOGIN ──────────────────────────────────────────────────────────────
new_page(c, "Screen 01 — Login", "Authentication · Owner & operator entry point", 1, TOTAL)
# outer frame
card(c, PAD, 30*mm, W - 2*PAD, H - 11*mm - 9*mm - 36*mm - 30*mm, C_BG, 6)
# center login card
lw, lh = 70*mm, 88*mm
lx = (W - lw) / 2
ly = (H - lh) / 2 - 5*mm
card(c, lx, ly, lw, lh, C_WHITE, 6)
c.setFont("Helvetica-Bold", 14)
c.setFillColor(C_TEXT)
c.drawString(lx + 6, ly + lh - 14, "Fuel")
c.setFillColor(C_GREEN)
c.drawString(lx + 28, ly + lh - 14, "Flow")
label(c, lx + 6, ly + lh - 22, "Sign in to your account", 8, C_MUTED)
divider(c, lx + 6, ly + lh - 26, lw - 12)
for i, (lbl, val) in enumerate([("Email", "owner@sunrisepetrol.in"), ("Password", "••••••••")]):
    fy = ly + lh - 46 - i * 22
    label(c, lx + 6, fy + 11, lbl, 7, C_MUTED)
    c.setFillColor(C_WHITE)
    c.setStrokeColor(C_BORDER)
    c.setLineWidth(0.4)
    c.roundRect(lx + 6, fy, lw - 12, 9*mm, 3, fill=1, stroke=1)
    label(c, lx + 10, fy + 2.5*mm, val, 7.5, C_TEXT if i == 0 else C_HINT)
btn_y = ly + 16
c.setFillColor(C_GREEN)
c.roundRect(lx + 6, btn_y, lw - 12, 8.5*mm, 3, fill=1, stroke=0)
c.setFont("Helvetica-Bold", 8)
c.setFillColor(C_WHITE)
c.drawCentredString(lx + lw/2, btn_y + 2.8*mm, "Sign in")
label(c, lx + lw/2 - 15, ly + 7, "Forgot password?", 7, C_BLUE)

# ── PAGE 2: OWNER DASHBOARD ───────────────────────────────────────────────────
new_page(c, "Screen 02 — Owner dashboard", "Primary view · Revenue, alerts, top stations, stock summary", 2, TOTAL)
tb_y = topbar(c, "Dashboard")
content_top = tb_y - 9*mm
sb_h = sidebar(c, SI_ITEMS, "Overview", PAD, content_top, 36*mm)
cx = PAD + 38*mm
cw = W - PAD - cx - 2

# 4 metric cards
mw = (cw - 9) / 4
my = content_top - 26
for val, lbl, delta, col in [
    ("₹4,82,350","Today's revenue","↑ 6% vs yesterday", C_TEXT),
    ("₹4,82,350","Expected cash","Based on sales", C_TEXT),
    ("₹4,79,100","Actual cash","↓ ₹3,250 variance", C_WARN),
    ("₹1,24,500","Outstanding credit","14 customers", C_RED),
]:
    metric_card(c, cx, my - 18, mw, 18*mm, lbl, val, delta, col)
    cx += mw + 3

cx = PAD + 38*mm
cw = W - PAD - cx - 2
col_w = (cw - 6) / 2
gy = my - 22

# Left col: top stations
card(c, cx, gy - 52*mm, col_w, 54*mm)
section_heading(c, cx + 4, gy - 7, "Top stations today")
stations = [("Sunrise — Patna","₹72,400",100),("Highway — NH30","₹61,200",85),("City Centre","₹50,100",70),("Danapur Road","₹40,000",55)]
for i,(name,rev,pct) in enumerate(stations):
    sy = gy - 16 - i * 11
    c.setFont("Helvetica", 6.5); c.setFillColor(C_MUTED); c.drawString(cx+4, sy, str(i+1))
    label(c, cx+10, sy, name, 7, C_TEXT)
    c.setFillColor(C_BORDER); c.roundRect(cx+80, sy, 25*mm, 2.5, 2, fill=1, stroke=0)
    c.setFillColor(C_GREEN); c.roundRect(cx+80, sy, 25*mm*pct/100, 2.5, 2, fill=1, stroke=0)
    rlabel(c, cx+col_w-4, sy, rev, 7, C_TEXT)

# Left col: mini bar chart
card(c, cx, gy - 90*mm, col_w, 35*mm)
section_heading(c, cx + 4, gy - 58, "Revenue — last 7 days")
days = [("Mo",38),("Tu",52),("We",45),("Th",60),("Fr",48),("Sa",65),("Su",55)]
bw = 7; gap = (col_w - 20) / 7
for i,(d,v) in enumerate(days):
    bx = cx + 10 + i * gap
    bh = v * 0.35
    is_today = (d == "Su")
    c.setFillColor(C_GREEN if not is_today else HexColor("#9FE1CB"))
    c.rect(bx, gy - 86*mm, bw, bh, fill=1, stroke=0)
    lc = C_GREEN_DK if is_today else C_HINT
    label(c, bx, gy - 89*mm, d, 6, lc)

# Right col: alerts
rc = cx + col_w + 6
card(c, rc, gy - 52*mm, col_w, 54*mm)
section_heading(c, rc + 4, gy - 7, "Alerts")
alerts = [("Danapur — diesel low (320L left)", C_RED, "now"),
          ("NH30 — cash variance ₹1,400", C_WARN, "1h ago"),
          ("City Centre — shift not closed", C_WARN, "2h ago"),
          ("All nozzles calibrated", C_GREEN, "today")]
for i,(msg,dc,time) in enumerate(alerts):
    ay = gy - 17 - i * 10
    c.setFillColor(dc); c.circle(rc+7, ay+2.5, 2.5, fill=1, stroke=0)
    label(c, rc+13, ay, msg, 7, C_TEXT if i<3 else C_MUTED)
    rlabel(c, rc+col_w-4, ay, time, 6, C_HINT)

# Right col: fuel stock
card(c, rc, gy - 72*mm, col_w, 18*mm)
section_heading(c, rc + 4, gy - 56, "Fuel stock summary")
for i,(fuel,lvl,col) in enumerate([("Petrol","18,400 L",C_GREEN),("Diesel","4,200 L",C_WARN),("Premium","6,800 L",C_GREEN)]):
    ry = gy - 63 - i*7
    label(c, rc+4, ry, fuel, 7, C_MUTED)
    rlabel(c, rc+col_w-4, ry, lvl, 7, col, "Helvetica-Bold")

# ── PAGE 3: STATIONS LIST ─────────────────────────────────────────────────────
new_page(c, "Screen 03 — Stations list", "All stations · status, fuel levels, today's revenue", 3, TOTAL)
tb_y = topbar(c, "Stations")
ct = tb_y - 9*mm
sidebar(c, SI_ITEMS, "Stations", PAD, ct, 36*mm)
cx = PAD + 38*mm; cw = W - PAD - cx - 2
# 4 metrics
mw = (cw-9)/4; my = ct - 26
for val,lbl,col in [("10","Total stations",C_TEXT),("8","Active now",C_GREEN),("48,200 L","Today's volume",C_TEXT),("₹4,82,350","Revenue today",C_TEXT)]:
    metric_card(c, cx, my-18, mw, 18*mm, lbl, val, "", col)
    cx += mw+3
cx = PAD+38*mm; col_w=(cw-6)/2; gy=my-22
# Station cards
for si,(name,loc,pct_p,pct_d,nozzles,rev,op) in enumerate([
    ("Sunrise Petrol Pump","Boring Road, Patna",78,22,8,"₹72,400","Amit Kumar"),
    ("Highway Pump — NH30","NH30, Patna Bypass",62,55,12,"₹61,200","Suresh Mehta"),
]):
    sx = cx + si*(col_w+6)
    card(c, sx, gy-72*mm, col_w, 74*mm)
    c.setFont("Helvetica-Bold",8.5); c.setFillColor(C_TEXT)
    c.drawString(sx+5, gy-8, name)
    label(c, sx+5, gy-16, loc, 7, C_MUTED)
    pill(c, sx+col_w-22, gy-14, "Active", C_GREEN_LT, C_GREEN_DK)
    # fuel bars
    for j,(fuel,pct,fc) in enumerate([("Petrol",pct_p,C_GREEN),("Diesel",pct_d,C_WARN if pct_d<30 else C_GREEN)]):
        fy = gy-28-j*14
        label(c, sx+5, fy, fuel, 6.5, C_MUTED)
        c.setFillColor(C_BORDER); c.roundRect(sx+5, fy-5, col_w-30, 3, 1, fill=1, stroke=0)
        c.setFillColor(fc); c.roundRect(sx+5, fy-5, (col_w-30)*pct/100, 3, 1, fill=1, stroke=0)
        warn = " ⚠" if (fuel=="Diesel" and pct_d<30) else ""
        rlabel(c, sx+col_w-5, fy, f"{pct}%{warn}", 6.5, fc)
    divider(c, sx+5, gy-56, col_w-10)
    for k,(lbl,val) in enumerate([("Nozzles",f"{nozzles} active"),("Revenue",rev),("Operator",op)]):
        ry = gy-62-k*8
        label(c, sx+5, ry, lbl, 7, C_MUTED)
        rlabel(c, sx+col_w-5, ry, val, 7, C_TEXT)

# ── PAGE 4: STATION DETAIL ────────────────────────────────────────────────────
new_page(c, "Screen 04 — Station detail & nozzles", "Sunrise Petrol Pump · nozzle grid, tanks, active shift", 4, TOTAL)
tb_y = topbar(c)
ct = tb_y-9*mm
sidebar(c, SI_ITEMS, "Stations", PAD, ct, 36*mm)
cx=PAD+38*mm; cw=W-PAD-cx-2
my=ct-26; mw=(cw-9)/4
for val,lbl,col in [("₹72,400","Today's revenue",C_TEXT),("4,820 L","Volume sold",C_TEXT),("−₹450","Cash variance",C_WARN),("Open","Shift status",C_GREEN)]:
    metric_card(c, cx, my-18, mw, 18*mm, lbl, val, "", col)
    cx+=mw+3
cx=PAD+38*mm; gy=my-22
# nozzle grid
card(c, cx, gy-46*mm, cw, 48*mm)
section_heading(c, cx+4, gy-7, "Nozzles")
nozzles=[("N-01","Petrol","82,441 L",True),("N-02","Petrol","74,209 L",True),
         ("N-03","Diesel","63,108 L",True),("N-04","Diesel","58,440 L",True),
         ("N-05","Premium","22,310 L",True),("N-06","Premium","Inactive",False),
         ("N-07","Petrol","41,002 L",True),("N-08","Petrol","38,771 L",True)]
ncol=4; nw=(cw-16)/ncol; nh=16*mm
for i,(nid,fuel,reading,active) in enumerate(nozzles):
    nx=cx+6+(i%ncol)*(nw+2); ny=gy-22-(i//ncol)*(nh+2)
    bg=C_GREEN_LT if active else C_BG
    c.setFillColor(bg); c.setStrokeColor(C_GREEN if active else C_BORDER)
    c.setLineWidth(0.5 if active else 0.3)
    c.roundRect(nx, ny, nw, nh, 3, fill=1, stroke=1)
    label(c, nx+3, ny+nh-7, nid, 6, C_HINT)
    c.setFont("Helvetica-Bold",7.5); c.setFillColor(C_GREEN_DK if active else C_HINT)
    c.drawString(nx+3, ny+5, fuel)
    label(c, nx+3, ny+1, reading, 6, C_MUTED if active else C_HINT)

col_w=(cw-6)/2
card(c, cx, gy-70*mm, col_w, 22*mm)
section_heading(c, cx+4, gy-50, "Tanks")
for k,(t,v,col) in enumerate([("Tank 1 — Petrol","18,400 L",C_GREEN),("Tank 2 — Diesel","4,200 L ⚠",C_WARN),("Tank 3 — Premium","6,800 L",C_GREEN)]):
    draw_row(c, cx+4, gy-57-k*7, col_w-8, t, v, C_MUTED, col)

rc=cx+col_w+6
card(c, rc, gy-70*mm, col_w, 22*mm)
section_heading(c, rc+4, gy-50, "Current shift")
for k,(l,v,vc) in enumerate([("Operator","Amit Kumar",C_TEXT),("Shift","Morning (6AM–2PM)",C_TEXT),("Opening reading","82,000 L",C_TEXT),("Sales so far","₹38,200",C_GREEN)]):
    draw_row(c, rc+4, gy-57-k*7, col_w-8, l, v, C_MUTED, vc)

# ── PAGE 5: INVENTORY ─────────────────────────────────────────────────────────
new_page(c, "Screen 05 — Inventory & stock", "Live fuel levels across all stations · delivery management", 5, TOTAL)
tb_y = topbar(c, "Inventory")
ct = tb_y-9*mm
sidebar(c, SI_ITEMS, "Inventory", PAD, ct, 36*mm)
cx=PAD+38*mm; cw=W-PAD-cx-2
my=ct-26; mw=(cw-9)/4
for val,lbl,col in [("92,400 L","Total petrol",C_GREEN),("28,100 L","Total diesel",C_WARN),("2","Low stock alerts",C_RED),("Tomorrow","Next delivery",C_TEXT)]:
    metric_card(c, cx, my-18, mw, 18*mm, lbl, val, "", col)
    cx+=mw+3
cx=PAD+38*mm; gy=my-22
card(c, cx, gy-80*mm, cw, 82*mm)
section_heading(c, cx+4, gy-7, "Stock levels by station")
# table header
hcols=[(cx+4,"Station",40),(cx+60,"Petrol",28),(cx+95,"Diesel",28),(cx+130,"Premium",28),(cx+162,"Status",30),(cx+196,"Last delivery",40)]
c.setFont("Helvetica-Bold",6.5); c.setFillColor(C_MUTED)
for hx,ht,_ in hcols: c.drawString(hx, gy-16, ht)
divider(c, cx+4, gy-18, cw-8)
rows=[
    ("Sunrise — Patna","18,400 L","4,200 L","6,800 L","Diesel low","3 days ago",C_WARN),
    ("Highway — NH30","12,000 L","9,800 L","—","Normal","Yesterday",C_GREEN),
    ("City Centre","9,200 L","1,800 L","2,400 L","Critical","5 days ago",C_RED),
    ("Danapur Road","14,200 L","8,100 L","—","Normal","2 days ago",C_GREEN),
]
for i,(sn,pt,di,pr,st,ld,sc) in enumerate(rows):
    ry=gy-27-i*12
    c.setFont("Helvetica",7); c.setFillColor(C_TEXT); c.drawString(cx+4,ry,sn)
    c.setFillColor(C_GREEN if pt!="—" else C_HINT); c.drawString(cx+60,ry,pt)
    dc=C_WARN if di=="4,200 L" else (C_RED if di=="1,800 L" else (C_GREEN if di!="—" else C_HINT))
    c.setFillColor(dc); c.drawString(cx+95,ry,di)
    c.setFillColor(C_GREEN if pr!="—" else C_HINT); c.drawString(cx+130,ry,pr)
    bg=C_RED_LT if sc=="Critical" else (C_WARN_LT if sc=="Diesel low" else C_GREEN_LT)
    fg=C_RED if sc=="Critical" else (C_WARN if sc=="Diesel low" else C_GREEN_DK)
    pill(c, cx+162, ry-1, st, bg, fg, 6)
    label(c, cx+196, ry, ld, 7, C_MUTED)
    divider(c, cx+4, ry-3, cw-8)

# ── PAGE 6: SHIFTS LIST ───────────────────────────────────────────────────────
new_page(c, "Screen 06 — Shifts list", "All shifts today · operator, station, variance, status", 6, TOTAL)
tb_y = topbar(c, "Staff")
ct = tb_y-9*mm
sidebar(c, SI_ITEMS, "Shifts", PAD, ct, 36*mm)
cx=PAD+38*mm; cw=W-PAD-cx-2; gy=ct-10
card(c, cx, gy-90*mm, cw, 90*mm)
section_heading(c, cx+4, gy-8, "Today's shifts")
hdrs=["Operator","Station","Shift","Sales","Cash collected","Variance","Status"]
hx=[cx+4,cx+42,cx+82,cx+112,cx+145,cx+180,cx+210]
c.setFont("Helvetica-Bold",6.5); c.setFillColor(C_MUTED)
for hxi,ht in zip(hx,hdrs): c.drawString(hxi,gy-18,ht)
divider(c, cx+4, gy-20, cw-8)
shift_rows=[
    ("Amit Kumar","Sunrise","Morning","₹38,200","₹38,200","₹0","Open",C_GREEN,C_GREEN_LT),
    ("Suresh Mehta","NH30","Day","₹29,400","₹28,000","−₹1,400","Open",C_GREEN,C_GREEN_LT),
    ("—","City Centre","Day","—","—","—","Unassigned",C_WARN,C_WARN_LT),
    ("Ramesh Yadav","Sunrise","Night","₹44,100","₹44,100","₹0","Closed",C_MUTED,C_BG),
    ("Priya Singh","Danapur","Morning","₹18,900","₹19,200","+₹300","Open",C_GREEN,C_GREEN_LT),
]
for i,row in enumerate(shift_rows):
    op,st,sh,sa,cc,va,status,sc,sbg = row
    ry=gy-30-i*13
    vals=[op,st,sh,sa,cc,va]
    c.setFont("Helvetica",7)
    for xi,v in zip(hx,vals):
        col = C_WARN if "−" in v else (C_GREEN if "+" in v else (C_MUTED if v=="—" else C_TEXT))
        c.setFillColor(col); c.drawString(xi,ry,v)
    pill(c, hx[-1], ry-1, status, sbg, sc, 6)
    divider(c, cx+4, ry-4, cw-8)

# ── PAGE 7: SALES ─────────────────────────────────────────────────────────────
new_page(c, "Screen 07 — Sales & transactions", "All transactions · filter by station, fuel type, payment", 7, TOTAL)
tb_y = topbar(c, "Reports")
ct = tb_y-9*mm
sidebar(c, SI_ITEMS, "Sales", PAD, ct, 36*mm)
cx=PAD+38*mm; cw=W-PAD-cx-2; my=ct-26; mw=(cw-9)/4
for val,lbl,col in [("₹4,82,350","Total sales",C_TEXT),("₹2,84,100","Petrol",C_TEXT),("₹1,62,800","Diesel",C_TEXT),("₹35,450","Credit sales",C_WARN)]:
    metric_card(c, cx, my-18, mw, 18*mm, lbl, val, "", col)
    cx+=mw+3
cx=PAD+38*mm; gy=my-22
card(c, cx, gy-88*mm, cw, 90*mm)
section_heading(c, cx+4, gy-7, "Transactions")
hdrs=["Time","Station","Nozzle","Fuel","Volume","Amount","Payment","Vehicle"]
hx=[cx+4,cx+32,cx+72,cx+94,cx+116,cx+140,cx+165,cx+195]
c.setFont("Helvetica-Bold",6.5); c.setFillColor(C_MUTED)
for hxi,ht in zip(hx,hdrs): c.drawString(hxi,gy-18,ht)
divider(c, cx+4, gy-20, cw-8)
txns=[
    ("10:42 AM","Sunrise","N-01","Petrol","32 L","₹3,104","Cash","BR01AB1234"),
    ("10:38 AM","NH30","N-04","Diesel","80 L","₹7,200","Credit","BR07CD5678"),
    ("10:35 AM","Sunrise","N-02","Petrol","15 L","₹1,455","UPI","—"),
    ("10:30 AM","Danapur","N-03","Diesel","50 L","₹4,500","Cash","BR09EF9012"),
    ("10:24 AM","NH30","N-07","Petrol","40 L","₹3,880","Cash","BR03GH3456"),
]
for i,row in enumerate(txns):
    ry=gy-30-i*13
    t,st,nz,fu,vo,am,pay,ve=row
    vals=[t,st,nz,fu,vo,am,None,ve]
    c.setFont("Helvetica",7)
    for xi,v in zip(hx,vals):
        if v is None: continue
        col=C_MUTED if v in [t,st,nz,fu,vo,ve] else C_TEXT
        if v==am: col=C_TEXT
        c.setFillColor(col); c.drawString(xi,ry,v)
    pbg=C_WARN_LT if pay=="Credit" else C_GREEN_LT
    pfg=C_WARN if pay=="Credit" else C_GREEN_DK
    pill(c, hx[6], ry-1, pay, pbg, pfg, 6)
    divider(c, cx+4, ry-4, cw-8)

# ── PAGE 8: CREDIT ────────────────────────────────────────────────────────────
new_page(c, "Screen 08 — Credit customers", "Outstanding balances · overdue tracking · payment history", 8, TOTAL)
tb_y = topbar(c, "Credit")
ct = tb_y-9*mm
sidebar(c, SI_ITEMS, "Credit", PAD, ct, 36*mm)
cx=PAD+38*mm; cw=W-PAD-cx-2; my=ct-26; mw=(cw-9)/4
for val,lbl,col in [("₹1,24,500","Total outstanding",C_RED),("₹44,200","Overdue (30d+)",C_RED),("₹82,000","Collected this month",C_GREEN),("68%","Credit limit used",C_WARN)]:
    metric_card(c, cx, my-18, mw, 18*mm, lbl, val, "", col)
    cx+=mw+3
cx=PAD+38*mm; gy=my-22
card(c, cx, gy-88*mm, cw, 90*mm)
section_heading(c, cx+4, gy-7, "Credit customers")
hdrs=["Customer","Type","Outstanding","Credit limit","Last payment","Status"]
hx=[cx+4,cx+68,cx+100,cx+132,cx+168,cx+210]
c.setFont("Helvetica-Bold",6.5); c.setFillColor(C_MUTED)
for hxi,ht in zip(hx,hdrs): c.drawString(hxi,gy-18,ht)
divider(c, cx+4, gy-20, cw-8)
cr_rows=[
    ("Patna Transport Co.","Fleet","₹38,400","₹50,000","12 days ago","Overdue",C_RED,C_RED_LT),
    ("Bihar Roadways","Fleet","₹22,100","₹30,000","3 days ago","Due soon",C_WARN,C_WARN_LT),
    ("Ravi Kumar","Individual","₹8,200","₹10,000","1 week ago","Normal",C_GREEN,C_GREEN_LT),
    ("Sunrise Logistics","Fleet","₹18,600","₹40,000","2 days ago","Normal",C_GREEN,C_GREEN_LT),
    ("Krishna Travels","Fleet","₹5,800","₹15,000","Today","Normal",C_GREEN,C_GREEN_LT),
]
for i,row in enumerate(cr_rows):
    cu,ty,ou,cl,lp,st,sc,sbg=row
    ry=gy-30-i*13
    c.setFont("Helvetica",7); c.setFillColor(C_TEXT); c.drawString(hx[0],ry,cu)
    c.setFillColor(C_MUTED); c.drawString(hx[1],ry,ty)
    oc=C_RED if "38" in ou else (C_WARN if "22" in ou else C_TEXT)
    c.setFillColor(oc); c.drawString(hx[2],ry,ou)
    c.setFillColor(C_TEXT); c.drawString(hx[3],ry,cl)
    c.setFillColor(C_MUTED); c.drawString(hx[4],ry,lp)
    pill(c, hx[5], ry-1, st, sbg, sc, 6)
    divider(c, cx+4, ry-4, cw-8)

# ── PAGE 9: REPORTS ───────────────────────────────────────────────────────────
new_page(c, "Screen 09 — Reports", "Generate, export and schedule all report types", 9, TOTAL)
tb_y = topbar(c, "Reports")
ct = tb_y-9*mm
sidebar(c, SI_ITEMS, "Reports", PAD, ct, 36*mm)
cx=PAD+38*mm; cw=W-PAD-cx-2; gy=ct-10
reps=[
    ("Daily sales report","Sales by station, fuel type, shift. Variance summary.","Ready",C_GREEN,C_GREEN_LT),
    ("Shift summary","Opening/closing readings, cash collected, operator breakdown.","Ready",C_GREEN,C_GREEN_LT),
    ("Inventory report","Stock levels, deliveries, daily consumption rate.","Last run 2d ago",C_WARN,C_WARN_LT),
    ("Credit ledger","Outstanding balances, payment history, overdue summary.","2 overdue",C_RED,C_RED_LT),
    ("Staff performance","Shifts per operator, variance history, attendance.","Ready",C_GREEN,C_GREEN_LT),
    ("Multi-station compare","Side-by-side revenue, volume, efficiency across stations.","Ready",C_GREEN,C_GREEN_LT),
]
ncols=3; rw=(cw-ncols*4)/ncols
for i,(title,desc,status,sc,sbg) in enumerate(reps):
    rx=cx+(i%ncols)*(rw+6)
    ry=gy-10-(i//ncols)*46
    card(c, rx, ry-38, rw, 40)
    c.setFont("Helvetica-Bold",8); c.setFillColor(C_TEXT); c.drawString(rx+5,ry-10,title)
    # wrapped desc
    words=desc.split(); line=""; lines_out=[]
    for w in words:
        test=line+" "+w if line else w
        if c.stringWidth(test,"Helvetica",7)>rw-12: lines_out.append(line); line=w
        else: line=test
    if line: lines_out.append(line)
    for j,ln in enumerate(lines_out[:3]):
        label(c, rx+5, ry-18-j*8, ln, 7, C_MUTED)
    pill(c, rx+5, ry-36, status, sbg, sc, 6)

# ── PAGE 10: SETTINGS ─────────────────────────────────────────────────────────
new_page(c, "Screen 10 — Settings & staff", "Staff roles, fuel prices, notifications, subscription plan", 10, TOTAL)
tb_y = topbar(c, "Settings")
ct = tb_y-9*mm
sidebar(c, SI_ITEMS, "Settings", PAD, ct, 36*mm)
cx=PAD+38*mm; cw=W-PAD-cx-2; col_w=(cw-6)/2; gy=ct-10
# Left: staff
card(c, cx, gy-60*mm, col_w, 62*mm)
section_heading(c, cx+4, gy-8, "Staff & roles")
staff=[("Amit Kumar","Sunrise · Operator","Operator",C_BLUE,C_BLUE_LT),
       ("Suresh Mehta","NH30 · Operator","Operator",C_BLUE,C_BLUE_LT),
       ("Priya Singh","All stations · Manager","Manager",C_WARN,C_WARN_LT),
       ("Rajesh Kumar","Owner","Owner",C_GREEN,C_GREEN_LT)]
for i,(name,role_sub,badge,bc,bbg) in enumerate(staff):
    sy=gy-18-i*13
    c.setFont("Helvetica-Bold",7.5); c.setFillColor(C_TEXT); c.drawString(cx+4,sy,name)
    label(c, cx+4, sy-7, role_sub, 6.5, C_MUTED)
    pill(c, cx+col_w-30, sy-3, badge, bbg, bc, 6)
# Fuel prices
card(c, cx, gy-88*mm, col_w, 26*mm)
section_heading(c, cx+4, gy-64, "Fuel prices")
for k,(fuel,price) in enumerate([("Petrol","₹97.00 / L"),("Diesel","₹90.00 / L"),("Premium","₹108.00 / L")]):
    draw_row(c, cx+4, gy-73-k*8, col_w-8, fuel, price)
# Right: notifications
rc=cx+col_w+6
card(c, rc, gy-60*mm, col_w, 62*mm)
section_heading(c, rc+4, gy-8, "Notifications")
notifs=["Low stock alert","Cash variance alert","Shift not closed","Daily summary (WhatsApp)","Credit overdue"]
for i,n in enumerate(notifs):
    ny=gy-18-i*11
    label(c, rc+4, ny, n, 7, C_TEXT)
    pill(c, rc+col_w-18, ny-1, "On", C_GREEN_LT, C_GREEN_DK, 6.5)
# Subscription
card(c, rc, gy-88*mm, col_w, 26*mm)
section_heading(c, rc+4, gy-64, "Subscription")
c.setFillColor(C_GREEN_LT); c.roundRect(rc+4, gy-76, col_w-8, 10, 3, fill=1, stroke=0)
c.setFont("Helvetica-Bold",7.5); c.setFillColor(C_GREEN_DK); c.drawString(rc+7, gy-70, "Growth plan — ₹4,999 / month")
draw_row(c, rc+4, gy-80, col_w-8, "Next renewal", "1 Jul 2025")

# ── PAGE 11: OPERATOR HOME ────────────────────────────────────────────────────
OP_SI = ["My shift","New sale","Sales log","Expenses","Close shift"]
new_page(c, "Screen 11 — Operator shift home", "Operator view · shift stats, nozzle readings, recent sales", 11, TOTAL)
tb_y = topbar(c, show_nav=False, role="operator")
ct = tb_y-9*mm
sidebar(c, OP_SI, "My shift", PAD, ct, 36*mm)
cx=PAD+38*mm; cw=W-PAD-cx-2; my=ct-26; mw=(cw-9)/4
for val,lbl,col in [("₹38,200","Sales today",C_TEXT),("₹38,200","Cash collected",C_GREEN),("2,410 L","Volume dispensed",C_TEXT),("₹0","Variance",C_GREEN)]:
    metric_card(c, cx, my-18, mw, 18*mm, lbl, val, "", col)
    cx+=mw+3
cx=PAD+38*mm; gy=my-22; col_w=(cw-6)/2
card(c, cx, gy-50*mm, col_w, 52*mm)
section_heading(c, cx+4, gy-7, "My nozzles")
for k,(nz,fuel,op,now) in enumerate([("N-01","Petrol","82,000","82,441"),("N-02","Petrol","73,800","74,209"),("N-03","Diesel","62,600","63,108"),("N-05","Premium","22,000","22,310")]):
    ry=gy-17-k*10
    label(c, cx+4, ry, f"{nz} · {fuel}", 7, C_MUTED)
    rlabel(c, cx+col_w-4, ry, f"{op} L → {now} L", 7, C_TEXT)
    divider(c, cx+4, ry-2, col_w-8)
rc=cx+col_w+6
card(c, rc, gy-50*mm, col_w, 52*mm)
section_heading(c, rc+4, gy-7, "Recent sales")
for k,(t,d,a) in enumerate([("10:42 AM","N-01 · 32L Petrol","₹3,104"),("10:35 AM","N-02 · 15L Petrol","₹1,455"),("10:28 AM","N-03 · 50L Diesel","₹4,500"),("10:15 AM","N-01 · 20L Petrol","₹1,940")]):
    ry=gy-17-k*10
    label(c, rc+4, ry, f"{t} · {d}", 7, C_MUTED)
    rlabel(c, rc+col_w-4, ry, a, 7, C_TEXT)
    divider(c, rc+4, ry-2, col_w-8)

# ── PAGE 12: NEW SALE ─────────────────────────────────────────────────────────
new_page(c, "Screen 12 — New sale entry", "Nozzle select · payment type · numpad amount entry", 12, TOTAL)
tb_y = topbar(c, show_nav=False, role="operator")
ct = tb_y-9*mm
sidebar(c, OP_SI, "New sale", PAD, ct, 36*mm)
cx=PAD+38*mm; cw=W-PAD-cx-2; gy=ct-10; col_w=(cw-6)/2

# Left: nozzle + payment + vehicle
card(c, cx, gy-40*mm, col_w, 42*mm)
section_heading(c, cx+4, gy-7, "1. Select nozzle")
nw2=(col_w-14)/4
for i,(nid,fuel,active) in enumerate([("N-01","Petrol",True),("N-02","Petrol",True),("N-03","Diesel",True),("N-05","Premium",True)]):
    nx=cx+5+i*(nw2+2); ny=gy-24
    sel=(i==0)
    bg=C_GREEN_LT; bc=C_GREEN if sel else C_BORDER; lw=1.2 if sel else 0.4
    c.setFillColor(bg if sel else C_BG); c.setStrokeColor(bc); c.setLineWidth(lw)
    c.roundRect(nx, ny, nw2, 14*mm, 3, fill=1, stroke=1)
    label(c, nx+2, ny+12*mm, nid, 6, C_HINT)
    c.setFont("Helvetica-Bold",7); c.setFillColor(C_GREEN_DK if sel else C_TEXT)
    c.drawString(nx+2, ny+5*mm, fuel)

card(c, cx, gy-56*mm, col_w, 14*mm)
section_heading(c, cx+4, gy-43, "2. Payment type")
for i,pt in enumerate(["Cash","UPI","Credit","Card"]):
    pbx=cx+4+i*30; pby=gy-54*mm
    if i==0:
        c.setFillColor(C_GREEN); c.roundRect(pbx,pby+1,26,8,3,fill=1,stroke=0)
        c.setFont("Helvetica-Bold",6.5); c.setFillColor(C_WHITE); c.drawString(pbx+3,pby+3.5,pt)
    else:
        c.setFillColor(C_WHITE); c.setStrokeColor(C_BORDER); c.setLineWidth(0.4)
        c.roundRect(pbx,pby+1,26,8,3,fill=1,stroke=1)
        label(c, pbx+3, pby+3.5, pt, 6.5, C_MUTED)

card(c, cx, gy-70*mm, col_w, 12*mm)
section_heading(c, cx+4, gy-58, "3. Vehicle (optional)")
c.setFillColor(C_WHITE); c.setStrokeColor(C_BORDER); c.setLineWidth(0.4)
c.roundRect(cx+4, gy-69*mm, col_w-8, 8*mm, 3, fill=1, stroke=1)
label(c, cx+8, gy-66*mm, "BR01AB1234", 7.5, C_TEXT)

# Right: display + numpad
rc=cx+col_w+6
card(c, rc, gy-80*mm, col_w, 82*mm)
# Amount display
c.setFillColor(C_BG); c.roundRect(rc+4, gy-24, col_w-8, 22, 3, fill=1, stroke=0)
label(c, rc+6, gy-9, "Petrol · N-01 · Cash", 6.5, C_MUTED)
c.setFont("Helvetica-Bold",18); c.setFillColor(C_TEXT); c.drawRightString(rc+col_w-8, gy-20, "₹3,104")
label(c, rc+6, gy-22, "32.00 L dispensed", 6.5, C_HINT)
# Numpad
keys=[["1","2","3"],["4","5","6"],["7","8","9"],["⌫","0","."]]
kw=(col_w-14)/3; kh=10*mm; kg=2
for r,row in enumerate(keys):
    for ci,k in enumerate(row):
        kx=rc+5+ci*(kw+kg); ky=gy-38-r*(kh+kg)
        if k=="⌫":
            c.setFillColor(C_RED_LT); c.setStrokeColor(HexColor("#F7C1C1"))
        else:
            c.setFillColor(C_WHITE); c.setStrokeColor(C_BORDER)
        c.setLineWidth(0.4); c.roundRect(kx,ky,kw,kh,3,fill=1,stroke=1)
        c.setFont("Helvetica-Bold",11)
        c.setFillColor(C_RED if k=="⌫" else C_TEXT)
        c.drawCentredString(kx+kw/2, ky+kh/2-4, k)
# Confirm button
c.setFillColor(C_GREEN); c.roundRect(rc+5,gy-82*mm,col_w-10,9*mm,3,fill=1,stroke=0)
c.setFont("Helvetica-Bold",8); c.setFillColor(C_WHITE)
c.drawCentredString(rc+col_w/2, gy-79*mm, "Confirm sale  ₹3,104")

# ── PAGE 13: CLOSE SHIFT ──────────────────────────────────────────────────────
new_page(c, "Screen 13 — Close shift", "Meter readings · cash reconciliation · variance check", 13, TOTAL)
tb_y = topbar(c, show_nav=False, role="operator")
ct = tb_y-9*mm
sidebar(c, OP_SI, "Close shift", PAD, ct, 36*mm)
cx=PAD+38*mm; cw=W-PAD-cx-2; gy=ct-10; col_w=(cw-6)/2
# Left: meter readings
card(c, cx, gy-70*mm, col_w, 72*mm)
section_heading(c, cx+4, gy-7, "Closing meter readings")
for k,(nid,fuel,op,cl) in enumerate([("N-01","Petrol","82,000","82,441"),("N-02","Petrol","73,800","74,209"),("N-03","Diesel","62,600","63,108"),("N-05","Premium","22,000","22,310")]):
    fy=gy-20-k*16
    label(c, cx+4, fy, f"{nid} · {fuel} — opening: {op}", 6.5, C_MUTED)
    c.setFillColor(C_WHITE); c.setStrokeColor(C_BORDER); c.setLineWidth(0.4)
    c.roundRect(cx+4, fy-10, col_w-8, 8*mm, 3, fill=1, stroke=1)
    label(c, cx+8, fy-6, cl, 7.5, C_TEXT)
# Right: cash summary
rc=cx+col_w+6
card(c, rc, gy-48*mm, col_w, 50*mm)
section_heading(c, rc+4, gy-7, "Cash summary")
for k,(lbl,val,vc) in enumerate([("Total sales (system)","₹38,200",C_TEXT),("Cash sales","₹28,400",C_TEXT),("UPI received","₹7,400",C_TEXT),("Credit sales","₹2,400",C_TEXT)]):
    draw_row(c, rc+4, gy-17-k*8, col_w-8, lbl, val, C_MUTED, vc)
label(c, rc+4, gy-47, "Actual cash in hand", 6.5, C_MUTED)
c.setFillColor(C_WHITE); c.setStrokeColor(C_BORDER); c.setLineWidth(0.4)
c.roundRect(rc+4, gy-60, col_w-8, 8*mm, 3, fill=1, stroke=1)
label(c, rc+8, gy-56, "28,400", 7.5, C_TEXT)
c.setFillColor(C_GREEN_LT); c.roundRect(rc+4, gy-72, col_w-8, 9, 3, fill=1, stroke=0)
c.setFont("Helvetica-Bold",7.5); c.setFillColor(C_GREEN_DK)
c.drawString(rc+8, gy-67, "Variance: ₹0 — Balanced")
# Expenses summary
card(c, rc, gy-72*mm, col_w, 18*mm)
section_heading(c, rc+4, gy-52, "Expenses this shift")
for k,(e,a) in enumerate([("Cleaning supplies","₹240"),("Generator diesel","₹800")]):
    draw_row(c, rc+4, gy-60-k*8, col_w-8, e, a)
# Submit button
c.setFillColor(C_RED); c.roundRect(rc+4, gy-80*mm, col_w-8, 8*mm, 3, fill=1, stroke=0)
c.setFont("Helvetica-Bold",8); c.setFillColor(C_WHITE)
c.drawCentredString(rc+col_w/2, gy-77*mm, "Submit and close shift")

# ── PAGE 14: EXPENSES ─────────────────────────────────────────────────────────
new_page(c, "Screen 14 — Expenses entry", "Log shift expenses · categories · cash or reimbursement", 14, TOTAL)
tb_y = topbar(c, show_nav=False, role="operator")
ct = tb_y-9*mm
sidebar(c, OP_SI, "Expenses", PAD, ct, 36*mm)
cx=PAD+38*mm; cw=W-PAD-cx-2; gy=ct-10; col_w=(cw-6)/2
card(c, cx, gy-76*mm, col_w, 78*mm)
section_heading(c, cx+4, gy-7, "Add new expense")
for k,(lbl,val) in enumerate([("Category","Cleaning & maintenance"),("Description","Cleaning supplies"),("Amount (₹)","240"),("Paid by","Cash from till")]):
    fy=gy-20-k*18
    label(c, cx+4, fy, lbl, 6.5, C_MUTED)
    c.setFillColor(C_WHITE); c.setStrokeColor(C_BORDER); c.setLineWidth(0.4)
    c.roundRect(cx+4, fy-10, col_w-8, 8*mm, 3, fill=1, stroke=1)
    label(c, cx+8, fy-6, val, 7.5, C_TEXT)
c.setFillColor(C_GREEN); c.roundRect(cx+4, gy-76*mm, col_w-8, 8*mm, 3, fill=1, stroke=0)
c.setFont("Helvetica-Bold",8); c.setFillColor(C_WHITE)
c.drawCentredString(cx+col_w/2, gy-73*mm, "Save expense")
rc=cx+col_w+6
card(c, rc, gy-50*mm, col_w, 52*mm)
section_heading(c, rc+4, gy-7, "Expenses this shift")
for k,(e,a) in enumerate([("Cleaning supplies","₹240"),("Generator diesel","₹800")]):
    draw_row(c, rc+4, gy-17-k*10, col_w-8, e, a)
c.setFillColor(C_BG); c.roundRect(rc+4, gy-43, col_w-8, 9, 3, fill=1, stroke=0)
c.setFont("Helvetica-Bold",8); c.setFillColor(C_TEXT)
c.drawString(rc+8, gy-38, "Total  ₹1,040")
label(c, rc+4, gy-47, "Deducted from cash handover at close.", 6.5, C_HINT)

# ── PAGE 15: MOBILE OWNER ────────────────────────────────────────────────────
def phone_frame(c, x, y, w=48*mm, h=88*mm):
    c.setFillColor(C_WHITE)
    c.setStrokeColor(C_BORDER)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 6, fill=1, stroke=1)
    # status bar
    c.setFillColor(C_WHITE)
    c.roundRect(x, y+h-7*mm, w, 7*mm, 6, fill=1, stroke=0)
    c.setStrokeColor(C_BORDER); c.setLineWidth(0.3)
    c.line(x, y+h-7*mm, x+w, y+h-7*mm)
    c.setFont("Helvetica-Bold",6); c.setFillColor(C_TEXT)
    c.drawString(x+3, y+h-4.5*mm, "Fuel")
    c.setFillColor(C_GREEN); c.drawString(x+14, y+h-4.5*mm, "Flow")
    # bottom nav
    c.setFillColor(C_WHITE)
    c.roundRect(x, y, w, 9*mm, 6, fill=1, stroke=0)
    c.setStrokeColor(C_BORDER); c.setLineWidth(0.3)
    c.line(x, y+9*mm, x+w, y+9*mm)
    return x, y+9*mm, w, h-16*mm

def phone_metric(c, x, y, w, h, lbl, val, col=C_TEXT):
    c.setFillColor(C_BG); c.setStrokeColor(C_BORDER); c.setLineWidth(0.3)
    c.roundRect(x, y, w, h, 2, fill=1, stroke=1)
    label(c, x+2, y+h-7, lbl, 5.5, C_MUTED)
    c.setFont("Helvetica-Bold",8); c.setFillColor(col); c.drawString(x+2, y+2, val)

new_page(c, "Screen 15 — Mobile owner app", "Home dashboard · station detail · credit customers", 15, TOTAL)
phones = [
    ("Owner — home", 0),
    ("Owner — station detail", 1),
    ("Owner — credit", 2),
]
phone_w = 48*mm; gap = (W - 2*PAD - 3*phone_w) / 2
base_y = 35*mm; phone_h = 112*mm

for pi,(title,_) in enumerate(phones):
    px = PAD + pi*(phone_w+gap)
    phone_frame(c, px, base_y, phone_w, phone_h)
    bx, by, bw, bh = px, base_y+9*mm, phone_w, phone_h-16*mm
    label(c, px, base_y-5, title, 7, C_MUTED, "Helvetica-Bold")
    if pi==0:
        label(c, bx+3, by+bh-5, "Good morning, Rajesh", 7.5, C_TEXT, "Helvetica-Bold")
        label(c, bx+3, by+bh-12, "Today · All 10 stations", 6, C_MUTED)
        mw2=(bw-8)/2; mh2=14
        for mi,(ml,mv,mc) in enumerate([("Revenue","₹4.8L",C_TEXT),("Variance","−₹3.2k",C_WARN),("Credit","₹1.2L",C_RED),("Shifts","8 active",C_GREEN)]):
            mx=bx+2+(mi%2)*(mw2+3); my2=by+bh-32-(mi//2)*(mh2+3)
            phone_metric(c, mx, my2, mw2, mh2, ml, mv, mc)
        # alerts
        c.setFillColor(C_BG); c.roundRect(bx+2,by+bh-72,bw-4,32,2,fill=1,stroke=0)
        label(c, bx+4, by+bh-58, "Alerts", 6.5, C_TEXT, "Helvetica-Bold")
        for ai,(amsg,adc) in enumerate([("Danapur diesel low (320L)",C_RED),("NH30 variance ₹1,400",C_WARN),("City Centre unassigned",C_WARN)]):
            ay2=by+bh-66-ai*7
            c.setFillColor(adc); c.circle(bx+6,ay2+2.5,2,fill=1,stroke=0)
            label(c, bx+10, ay2, amsg, 6, C_TEXT)
    elif pi==1:
        label(c, bx+3, by+bh-5, "Sunrise Petrol Pump", 7.5, C_TEXT, "Helvetica-Bold")
        label(c, bx+3, by+bh-12, "Boring Road, Patna", 6, C_MUTED)
        mw2=(bw-8)/2
        for mi,(ml,mv,mc) in enumerate([("Revenue","₹72,400",C_TEXT),("Variance","₹0",C_GREEN)]):
            mx=bx+2+mi*(mw2+3)
            phone_metric(c, mx, by+bh-32, mw2, 14, ml, mv, mc)
        c.setFillColor(C_BG); c.roundRect(bx+2,by+bh-72,bw-4,36,2,fill=1,stroke=0)
        label(c, bx+4, by+bh-58, "Fuel levels", 6.5, C_TEXT, "Helvetica-Bold")
        for fi,(fuel,pct,fc) in enumerate([("Petrol",78,C_GREEN),("Diesel",22,C_WARN),("Premium",60,C_GREEN)]):
            fy2=by+bh-67-fi*9
            label(c, bx+4, fy2, fuel, 6, C_MUTED)
            c.setFillColor(C_BORDER); c.roundRect(bx+22,fy2,bw-26,2.5,1,fill=1,stroke=0)
            c.setFillColor(fc); c.roundRect(bx+22,fy2,(bw-26)*pct/100,2.5,1,fill=1,stroke=0)
    elif pi==2:
        label(c, bx+3, by+bh-5, "Credit customers", 7.5, C_TEXT, "Helvetica-Bold")
        label(c, bx+3, by+bh-12, "₹1,24,500 outstanding", 6, C_MUTED)
        c.setFillColor(C_BG); c.roundRect(bx+2,by+bh-40,bw-4,24,2,fill=1,stroke=0)
        label(c, bx+4, by+bh-26, "Overdue", 6.5, C_RED, "Helvetica-Bold")
        label(c, bx+4, by+bh-33, "Patna Transport", 6, C_TEXT)
        rlabel(c, bx+bw-6, by+bh-33, "₹38,400", 6, C_RED)
        label(c, bx+4, by+bh-40, "Bihar Roadways", 6, C_TEXT)
        rlabel(c, bx+bw-6, by+bh-40, "₹22,100", 6, C_WARN)
        c.setFillColor(C_BG); c.roundRect(bx+2,by+bh-76,bw-4,32,2,fill=1,stroke=0)
        label(c, bx+4, by+bh-62, "Normal", 6.5, C_GREEN, "Helvetica-Bold")
        for ci,(cust,amt) in enumerate([("Ravi Kumar","₹8,200"),("Sunrise Logistics","₹18,600"),("Krishna Travels","₹5,800")]):
            ry2=by+bh-70-ci*7
            label(c, bx+4, ry2, cust, 6, C_TEXT)
            rlabel(c, bx+bw-6, ry2, amt, 6, C_TEXT)

# ── PAGE 16: MOBILE OPERATOR ──────────────────────────────────────────────────
new_page(c, "Screen 16 — Mobile operator app", "Shift home · new sale with numpad · close shift", 16, TOTAL)
op_phones=[("Operator — shift home",0),("Operator — new sale",1),("Operator — close shift",2)]
for pi,(title,_) in enumerate(op_phones):
    px=PAD+pi*(phone_w+gap)
    phone_frame(c, px, base_y, phone_w, phone_h)
    bx,by,bw,bh=px,base_y+9*mm,phone_w,phone_h-16*mm
    label(c, px, base_y-5, title, 7, C_MUTED, "Helvetica-Bold")
    if pi==0:
        label(c, bx+3, by+bh-5, "Good morning, Amit", 7.5, C_TEXT, "Helvetica-Bold")
        label(c, bx+3, by+bh-12, "Sunrise · Morning · 06:02 AM", 6, C_MUTED)
        mw2=(bw-8)/2
        for mi,(ml,mv,mc) in enumerate([("Sales","₹38.2k",C_TEXT),("Txns","48",C_TEXT),("Volume","2,410L",C_TEXT),("Variance","₹0",C_GREEN)]):
            mx=bx+2+(mi%2)*(mw2+3); my2=by+bh-32-(mi//2)*(14+3)
            phone_metric(c, mx, my2, mw2, 14, ml, mv, mc)
        c.setFillColor(C_BG); c.roundRect(bx+2,by+bh-72,bw-4,32,2,fill=1,stroke=0)
        label(c, bx+4, by+bh-58, "Last sales", 6.5, C_TEXT, "Helvetica-Bold")
        for si2,(st2,am2) in enumerate([("10:42 · N-01 · 32L","₹3,104"),("10:35 · N-02 · 15L","₹1,455"),("10:28 · N-03 · 50L","₹4,500")]):
            sy2=by+bh-66-si2*7
            label(c, bx+4, sy2, st2, 6, C_MUTED)
            rlabel(c, bx+bw-6, sy2, am2, 6, C_TEXT)
        c.setFillColor(C_GREEN); c.roundRect(bx+2,by+3,bw-4,7,2,fill=1,stroke=0)
        c.setFont("Helvetica-Bold",6); c.setFillColor(C_WHITE); c.drawCentredString(bx+bw/2,by+5.5,"+ New sale")
    elif pi==1:
        label(c, bx+3, by+bh-5, "Select nozzle", 7.5, C_TEXT, "Helvetica-Bold")
        nw3=(bw-8)/2
        for ni,(nid2,fuel2,sel2) in enumerate([("N-01","Petrol",True),("N-02","Petrol",False),("N-03","Diesel",False),("N-05","Premium",False)]):
            nx2=bx+2+(ni%2)*(nw3+3); ny2=by+bh-32-(ni//2)*(14+3)
            bg2=C_GREEN_LT if sel2 else C_BG
            bc2=C_GREEN if sel2 else C_BORDER
            c.setFillColor(bg2); c.setStrokeColor(bc2); c.setLineWidth(1.2 if sel2 else 0.3)
            c.roundRect(nx2,ny2,nw3,14,2,fill=1,stroke=1)
            label(c, nx2+2, ny2+10, nid2, 5.5, C_HINT)
            c.setFont("Helvetica-Bold",7); c.setFillColor(C_GREEN_DK if sel2 else C_TEXT)
            c.drawString(nx2+2, ny2+2, fuel2)
        # display
        c.setFillColor(C_BG); c.roundRect(bx+2,by+bh-72,bw-4,20,2,fill=1,stroke=0)
        label(c, bx+4, by+bh-60, "Petrol · N-01 · Cash", 6, C_MUTED)
        c.setFont("Helvetica-Bold",12); c.setFillColor(C_TEXT); c.drawRightString(bx+bw-5,by+bh-68,"₹3,104")
        # mini keypad
        kw3=(bw-10)/3; kh3=7
        for ki,k3 in enumerate(["1","2","3","4","5","6","7","8","9","⌫","0","."]):
            kx3=bx+2+(ki%3)*(kw3+1.5); ky3=by+bh-82-(ki//3)*(kh3+1.5)
            bg3=C_RED_LT if k3=="⌫" else C_WHITE
            c.setFillColor(bg3); c.setStrokeColor(C_BORDER); c.setLineWidth(0.3)
            c.roundRect(kx3,ky3,kw3,kh3,2,fill=1,stroke=1)
            c.setFont("Helvetica-Bold",6.5); c.setFillColor(C_RED if k3=="⌫" else C_TEXT)
            c.drawCentredString(kx3+kw3/2,ky3+2,k3)
        c.setFillColor(C_GREEN); c.roundRect(bx+2,by+3,bw-4,7,2,fill=1,stroke=0)
        c.setFont("Helvetica-Bold",6); c.setFillColor(C_WHITE); c.drawCentredString(bx+bw/2,by+5.5,"Confirm  ₹3,104")
    elif pi==2:
        label(c, bx+3, by+bh-5, "Close shift", 7.5, C_TEXT, "Helvetica-Bold")
        label(c, bx+3, by+bh-12, "Enter closing readings", 6, C_MUTED)
        c.setFillColor(C_BG); c.roundRect(bx+2,by+bh-44,bw-4,28,2,fill=1,stroke=0)
        label(c, bx+4, by+bh-30, "Meter readings", 6.5, C_TEXT, "Helvetica-Bold")
        for ri2,(nid3,val3) in enumerate([("N-01 Petrol","82,441"),("N-02 Petrol","74,209"),("N-03 Diesel","63,108")]):
            ry3=by+bh-38-ri2*7; label(c, bx+4,ry3,nid3,6,C_MUTED); rlabel(c, bx+bw-6,ry3,val3,6,C_TEXT)
        c.setFillColor(C_BG); c.roundRect(bx+2,by+bh-76,bw-4,28,2,fill=1,stroke=0)
        label(c, bx+4, by+bh-62, "Cash summary", 6.5, C_TEXT, "Helvetica-Bold")
        for ri3,(lbl3,val3,vc3) in enumerate([("Expected","₹38,200",C_TEXT),("Collected","₹38,200",C_TEXT),("Variance","₹0",C_GREEN)]):
            ry4=by+bh-70-ri3*7; label(c, bx+4,ry4,lbl3,6,C_MUTED); rlabel(c, bx+bw-6,ry4,val3,6,vc3)
        c.setFillColor(C_GREEN_LT); c.roundRect(bx+2,by+11,bw-4,7,2,fill=1,stroke=0)
        c.setFont("Helvetica-Bold",6); c.setFillColor(C_GREEN_DK); c.drawCentredString(bx+bw/2,by+13.5,"Balanced — no discrepancy")
        c.setFillColor(C_RED); c.roundRect(bx+2,by+3,bw-4,7,2,fill=1,stroke=0)
        c.setFont("Helvetica-Bold",6); c.setFillColor(C_WHITE); c.drawCentredString(bx+bw/2,by+5.5,"Submit & close shift")

# ── PAGE 17: OFFLINE + AI ─────────────────────────────────────────────────────
new_page(c, "Screen 17 — Offline mode & AI copilot", "Operator offline sync · owner AI copilot · alert feed", 17, TOTAL)
sp_phones=[("Operator — offline",0),("Owner — AI copilot",1),("Owner — alerts",2)]
for pi,(title,_) in enumerate(sp_phones):
    px=PAD+pi*(phone_w+gap)
    phone_frame(c, px, base_y, phone_w, phone_h)
    bx,by,bw,bh=px,base_y+9*mm,phone_w,phone_h-16*mm
    label(c, px, base_y-5, title, 7, C_MUTED, "Helvetica-Bold")
    if pi==0:
        # Offline banner
        c.setFillColor(C_WARN_LT); c.roundRect(bx+2,by+bh-16,bw-4,12,2,fill=1,stroke=0)
        c.setFont("Helvetica-Bold",6); c.setFillColor(C_WARN)
        c.drawString(bx+4,by+bh-9,"No internet — working offline")
        label(c, bx+3, by+bh-23, "Offline mode", 7.5, C_TEXT, "Helvetica-Bold")
        label(c, bx+3, by+bh-30, "Data saved locally", 6, C_MUTED)
        c.setFillColor(C_BG); c.roundRect(bx+2,by+bh-56,bw-4,22,2,fill=1,stroke=0)
        label(c, bx+4, by+bh-42, "Pending sync", 6.5, C_TEXT, "Helvetica-Bold")
        for si3,(lbl4,v4) in enumerate([("Sales recorded","12"),("Expenses","2"),("Readings","4")]):
            ry5=by+bh-50-si3*7; label(c, bx+4,ry5,lbl4,6,C_MUTED); rlabel(c, bx+bw-6,ry5,v4,6,C_TEXT)
        c.setFillColor(C_BG); c.roundRect(bx+2,by+bh-84,bw-4,24,2,fill=1,stroke=0)
        label(c, bx+4, by+bh-70, "Available offline", 6.5, C_TEXT, "Helvetica-Bold")
        for ai2,(feat,avail,fc2) in enumerate([("New sale entry","Yes",C_GREEN),("Meter readings","Yes",C_GREEN),("Expenses","Yes",C_GREEN),("Live dashboard","No",C_RED)]):
            ay3=by+bh-78-ai2*7; label(c, bx+4,ay3,feat,6,C_MUTED); rlabel(c, bx+bw-6,ay3,avail,6,fc2)
        c.setFillColor(C_GREEN); c.roundRect(bx+2,by+3,bw-4,7,2,fill=1,stroke=0)
        c.setFont("Helvetica-Bold",6); c.setFillColor(C_WHITE); c.drawCentredString(bx+bw/2,by+5.5,"Continue offline")
    elif pi==1:
        label(c, bx+3, by+bh-5, "AI Copilot", 7.5, C_TEXT, "Helvetica-Bold")
        label(c, bx+3, by+bh-12, "Ask anything about your stations", 6, C_MUTED)
        chats=[
            ("You","Why did diesel sales drop this week?",C_BG,C_TEXT,False),
            ("AI","Diesel dropped 18% — Danapur ran low Mon-Tue, NH30 had no operator Wednesday. Impact: ₹28,400.",C_GREEN_LT,C_GREEN_DK,True),
            ("You","When should I order fuel?",C_BG,C_TEXT,False),
            ("AI","Order diesel for Danapur today — 2 days left. Petrol is fine for 8 days.",C_GREEN_LT,C_GREEN_DK,True),
        ]
        cy2=by+bh-16
        for who,msg,cbg,cfg,is_ai in chats:
            words2=msg.split(); ln2=""; lns2=[]
            for w2 in words2:
                test2=ln2+" "+w2 if ln2 else w2
                if c.stringWidth(test2,"Helvetica",6)>bw-12: lns2.append(ln2); ln2=w2
                else: ln2=test2
            if ln2: lns2.append(ln2)
            ch2=len(lns2)*8+8
            c.setFillColor(cbg); c.roundRect(bx+2,cy2-ch2,bw-4,ch2,2,fill=1,stroke=0)
            c.setFont("Helvetica-Bold",5.5); c.setFillColor(C_GREEN if is_ai else C_HINT)
            c.drawString(bx+4,cy2-7,who)
            for li2,ln3 in enumerate(lns2):
                label(c, bx+4, cy2-14-li2*7, ln3, 6, cfg)
            cy2-=ch2+3
        # input box
        c.setFillColor(C_WHITE); c.setStrokeColor(C_BORDER); c.setLineWidth(0.3)
        c.roundRect(bx+2,by+3,bw-4,8,2,fill=1,stroke=1)
        label(c, bx+5, by+5.5, "Ask anything...", 6, C_HINT)
    elif pi==2:
        label(c, bx+3, by+bh-5, "Alerts", 7.5, C_TEXT, "Helvetica-Bold")
        label(c, bx+3, by+bh-12, "Today · 3 unread", 6, C_MUTED)
        alert_data=[
            ("Danapur — diesel critical","320L remaining. Order now.",C_RED),
            ("NH30 — variance ₹1,400","Suresh Mehta shift shortfall.",C_WARN),
            ("City Centre unassigned","Day shift has no operator.",C_WARN),
            ("Daily summary ready","Yesterday: ₹4,54,100.",C_GREEN),
        ]
        ay4=by+bh-18
        for amsg2,asub,ac in alert_data:
            c.setFillColor(C_WHITE); c.setStrokeColor(C_BORDER); c.setLineWidth(0.3)
            c.roundRect(bx+2+3,ay4-16,bw-4-3,16,2,fill=1,stroke=1)
            c.setFillColor(ac); c.rect(bx+2,ay4-16,3,16,fill=1,stroke=0)
            c.setFont("Helvetica-Bold",6); c.setFillColor(C_TEXT); c.drawString(bx+8,ay4-8,amsg2)
            label(c, bx+8, ay4-14, asub, 5.5, C_MUTED)
            ay4-=20

c.save()
print("PDF saved successfully")



