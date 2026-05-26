#!/usr/bin/env python3
"""
Bitcoin Natal Chart (Doğum Haritası)
======================================
Genesis Block: 3 Ocak 2009, 18:15:05 UTC
Konum: 0°N 0°E (Satoshi Nakamoto'nun konumu bilinmediği için)

Flatlib kütüphanesi kullanılarak hesaplanmıştır.
"""

from flatlib import const, aspects as asp_module
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.dignities import essential

# ─── Semboller ────────────────────────────────────────────────────────────────

PLANET_SYMBOLS = {
    const.SUN:        '☉  Güneş   ',
    const.MOON:       '☽  Ay      ',
    const.MERCURY:    '☿  Merkür  ',
    const.VENUS:      '♀  Venüs   ',
    const.MARS:       '♂  Mars    ',
    const.JUPITER:    '♃  Jüpiter ',
    const.SATURN:     '♄  Satürn  ',
    const.URANUS:     '♅  Uranüs  ',
    const.NEPTUNE:    '♆  Neptün  ',
    const.PLUTO:      '♇  Plüton  ',
    const.NORTH_NODE: '☊  K.Node  ',
}

SIGN_SYMBOLS = {
    'Aries':       '♈ Koç      ',
    'Taurus':      '♉ Boğa     ',
    'Gemini':      '♊ İkizler  ',
    'Cancer':      '♋ Yengeç   ',
    'Leo':         '♌ Aslan    ',
    'Virgo':       '♍ Başak    ',
    'Libra':       '♎ Terazi   ',
    'Scorpio':     '♏ Akrep    ',
    'Sagittarius': '♐ Yay      ',
    'Capricorn':   '♑ Oğlak    ',
    'Aquarius':    '♒ Kova     ',
    'Pisces':      '♓ Balık    ',
}

SIGN_SYMBOLS_SHORT = {
    'Aries': '♈', 'Taurus': '♉', 'Gemini': '♊', 'Cancer': '♋',
    'Leo': '♌', 'Virgo': '♍', 'Libra': '♎', 'Scorpio': '♏',
    'Sagittarius': '♐', 'Capricorn': '♑', 'Aquarius': '♒', 'Pisces': '♓',
}

ASPECT_SYMBOLS = {
    const.CONJUNCTION:  '☌  Konjunksiyon (0°) ',
    const.SEXTILE:      '⚹  Sextil      (60°)',
    const.SQUARE:       '□  Kare        (90°)',
    const.TRINE:        '△  Trigon     (120°)',
    const.OPPOSITION:   '☍  Karşıt     (180°)',
}

ELEMENT_TR = {
    'Fire': '🔥 Ateş', 'Earth': '🌍 Toprak',
    'Air': '💨 Hava', 'Water': '💧 Su',
}

MODE_TR = {
    'Cardinal': 'Öncü', 'Fixed': 'Sabit', 'Mutable': 'Değişken',
}

MOVEMENT_TR = {
    'Direct': '→ İlerleyen',
    'Retrograde': '℞ Gerileyen',
    'Stationary': '• Durağan',
}

DIGNITY_TR = {
    'ruler': 'Yönetici',
    'exalted': 'Yüceltilmiş',
    'dayTrip': 'Gündüz Tril.',
    'nightTrip': 'Gece Tril.',
    'partTrip': 'Katıl. Tril.',
    'term': 'Terim',
    'face': 'Yüz',
    'peregrine': 'Yolcu',
    'detriment': 'Sürgün',
    'fall': 'Düşüş',
    'exile': 'Sürgün',
}


def sign_tr(sign):
    return SIGN_SYMBOLS.get(sign, sign)


def sign_short(sign):
    return SIGN_SYMBOLS_SHORT.get(sign, sign[:3])


def format_deg(signlon):
    """Derece°dakika'saniye\" formatı"""
    deg = int(signlon)
    min_f = (signlon - deg) * 60
    mins = int(min_f)
    secs = int((min_f - mins) * 60)
    return f"{deg:2d}°{mins:02d}'{secs:02d}\""


def separator(char='─', width=65):
    print(char * width)


def header(title):
    separator('═')
    pad = (65 - len(title) - 2) // 2
    print('║' + ' ' * pad + title + ' ' * (65 - pad - len(title) - 2) + '║')
    separator('═')


# ─── Harita Oluştur ────────────────────────────────────────────────────────────

date = Datetime('2009/01/03', '18:15:05', '+00:00')
pos  = GeoPos('0n00', '0e00')

ALL_PLANETS = [
    const.SUN, const.MOON, const.MERCURY, const.VENUS, const.MARS,
    const.JUPITER, const.SATURN, const.URANUS, const.NEPTUNE, const.PLUTO,
    const.NORTH_NODE,
]

chart = Chart(
    date, pos,
    hsys=const.HOUSES_PLACIDUS,
    IDs=ALL_PLANETS + [const.SYZYGY, const.PARS_FORTUNA],
)

# ─── BAŞLIK ───────────────────────────────────────────────────────────────────
print()
header('₿  BİTCOIN NATAL (DOĞUM) HARİTASI  ₿')
print()
print('  📅 Tarih  : 3 Ocak 2009')
print('  🕕 Saat   : 18:15:05 UTC')
print('  📍 Konum  : 0°N 0°E (Satoshi bilinmiyor → Null Island)')
print('  🏠 Ev Sys.: Placidus')
print()

# ─── YÜKSELEN / MC ────────────────────────────────────────────────────────────
separator()
print('  ACI NOKTALAR')
separator()
asc = chart.get(const.ASC)
mc  = chart.get(const.MC)
dsc = chart.get(const.DESC)
ic  = chart.get(const.IC)

print(f"  ↑  Yükselen (ASC)  : {sign_tr(asc.sign)} {format_deg(asc.signlon)}")
print(f"  ↓  Alçalan  (DSC)  : {sign_tr(dsc.sign)} {format_deg(dsc.signlon)}")
print(f"  ↑  MC              : {sign_tr(mc.sign)}  {format_deg(mc.signlon)}")
print(f"  ↓  IC              : {sign_tr(ic.sign)}  {format_deg(ic.signlon)}")
print()

# ─── GEZEGENLER ───────────────────────────────────────────────────────────────
separator()
print('  GEZEGENLER  (Burç  Derece   Hareket  Element  Hız/gün)')
separator()

for pid in ALL_PLANETS:
    try:
        obj = chart.get(pid)
    except Exception:
        continue

    sym    = PLANET_SYMBOLS.get(pid, f'  {pid:<12}')
    sign   = sign_tr(obj.sign)
    deg    = format_deg(obj.signlon)
    mov    = MOVEMENT_TR.get(obj.movement(), obj.movement())
    try:
        elem = ELEMENT_TR.get(obj.element(), obj.element())
    except Exception:
        elem = '     —    '
    speed  = f'{obj.lonspeed:+.4f}°'

    print(f"  {sym}  {sign}  {deg}  {mov}  {elem}  {speed}")

# Part of Fortune
try:
    pof = chart.get(const.PARS_FORTUNA)
    print(f"  ⊕  Şans Burcu  {sign_tr(pof.sign)} {format_deg(pof.signlon)}")
except Exception:
    pass

print()

# ─── EVLER ────────────────────────────────────────────────────────────────────
separator()
print('  12 EV (Placidus)')
separator()

house_ids = [getattr(const, f'HOUSE{i}') for i in range(1, 13)]
house_names = [
    '1. Ev  (Benlik)',     '2. Ev  (Mal-Mülk)',   '3. Ev  (İletişim)',
    '4. Ev  (Ev/Kök)',     '5. Ev  (Yaratıcılık)', '6. Ev  (Sağlık)',
    '7. Ev  (Ortaklık)',   '8. Ev  (Dönüşüm)',    '9. Ev  (Felsefe)',
    '10. Ev (Kariyer)',    '11. Ev (Topluluk)',    '12. Ev (Gizem)',
]

for hid, hname in zip(house_ids, house_names):
    try:
        house = chart.get(hid)
        print(f"  {hname:<22}  {sign_tr(house.sign)}  {format_deg(house.signlon)}")
    except Exception:
        pass

print()

# ─── AÇILAR (ASPECTS) ─────────────────────────────────────────────────────────
separator()
print('  MAJÖR AÇILAR')
separator()

planet_pairs_done = set()
aspect_list = []

for i, p1_id in enumerate(ALL_PLANETS[:10]):  # node hariç
    for p2_id in ALL_PLANETS[i+1:10]:
        key = (p1_id, p2_id)
        if key in planet_pairs_done:
            continue
        planet_pairs_done.add(key)

        try:
            obj1 = chart.get(p1_id)
            obj2 = chart.get(p2_id)
            aspect = asp_module.getAspect(obj1, obj2, const.MAJOR_ASPECTS)
            if aspect.type != const.NO_ASPECT:
                aspect_list.append((aspect, p1_id, p2_id))
        except Exception:
            pass

if aspect_list:
    for aspect, p1_id, p2_id in aspect_list:
        sym1 = PLANET_SYMBOLS.get(p1_id, p1_id).strip()
        sym2 = PLANET_SYMBOLS.get(p2_id, p2_id).strip()
        asp_sym = ASPECT_SYMBOLS.get(aspect.type, aspect.type)
        orb = f"orb: {aspect.orb:.1f}°"
        try:
            mov = aspect.active.movement
            mov_tr = {'applicative': '→ Yaklaşıyor', 'separative': '← Uzaklaşıyor', 'exact': '• Tam'}.get(mov, mov)
        except Exception:
            mov_tr = ''
        print(f"  {sym1:<14}  {asp_sym}  {sym2:<14}  {orb:<10}  {mov_tr}")
else:
    print('  Majör açı bulunamadı.')

print()

# ─── TEMEL ONURLAR ────────────────────────────────────────────────────────────
separator()
print('  TEMEL ONURLAR (Essential Dignities)')
separator()

trad_planets = [const.SUN, const.MOON, const.MERCURY, const.VENUS,
                const.MARS, const.JUPITER, const.SATURN]

for pid in trad_planets:
    try:
        obj = chart.get(pid)
        score = essential.score(obj.id, obj.sign, obj.signlon)
        sym = PLANET_SYMBOLS.get(pid, pid).strip()
        info = essential.EssentialInfo(obj)
        # dignities list
        digs = []
        for attr in ['ruler', 'exalted', 'dayTrip', 'nightTrip', 'partTrip', 'term', 'face']:
            try:
                if getattr(info, attr):
                    digs.append(DIGNITY_TR.get(attr, attr))
            except Exception:
                pass
        for attr in ['peregrine', 'detriment', 'fall']:
            try:
                if getattr(info, attr):
                    digs.append('⚠ ' + DIGNITY_TR.get(attr, attr))
            except Exception:
                pass
        dig_str = ', '.join(digs) if digs else 'Yolcu (Gurbetçi)'
        print(f"  {sym:<16}  Skor: {score:+3d}   {dig_str}")
    except Exception as e:
        pass

print()

# ─── AY FAZI & GECE/GÜNDÜZ ────────────────────────────────────────────────────
separator()
print('  HARITA ÖZELLİKLERİ')
separator()

try:
    moon_phase = chart.getMoonPhase()
    phase_tr = {
        'First Quarter': '🌒 Birinci Çeyrek',
        'Second Quarter': '🌔 İkinci Çeyrek',
        'Third Quarter': '🌖 Üçüncü Çeyrek',
        'Last Quarter': '🌘 Son Çeyrek',
    }
    print(f"  🌙 Ay Fazı     : {phase_tr.get(moon_phase, moon_phase)}")
except Exception:
    pass

try:
    diurnal = chart.isDiurnal()
    print(f"  ☀️  Harita Tipi : {'Gündüz Haritası ☀️' if diurnal else 'Gece Haritası 🌙'}")
except Exception:
    pass

# Yükselen yöneticisi
try:
    ruler_id = essential.ruler(asc.sign)
    ruler_obj = chart.get(ruler_id)
    print(f"  👑 ASC Yönetici: {PLANET_SYMBOLS.get(ruler_id, ruler_id).strip()} "
          f"({sign_tr(ruler_obj.sign)} {format_deg(ruler_obj.signlon)})")
except Exception:
    pass

print()
separator('═')
print('  ₿  Bitcoin — \"Vires in Numeris\" (Güç Sayılardadır)')
separator('═')
print()
