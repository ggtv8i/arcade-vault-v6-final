#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arcade Vault — ROM Scanner
ضع ألعابك في مجلدات systems/*/roms/ ثم شغّل هذا الملف
"""
import os, json, sys

BASE = os.path.dirname(os.path.abspath(__file__))
SYSTEMS_DIR = os.path.join(BASE, 'systems')

EXT_MAP = {
    'nes':   ['.nes'],
    'snes':  ['.smc','.sfc','.zip'],
    'n64':   ['.n64','.z64','.v64'],
    'gc':    ['.iso','.gcm','.gcz','.rvz'],
    'gb':    ['.gb'],
    'gbc':   ['.gbc'],
    'gba':   ['.gba'],
    'nds':   ['.nds'],
    'md':    ['.md','.gen','.smd','.bin'],
    'sms':   ['.sms'],
    'gg':    ['.gg'],
    'scd':   ['.bin','.cue','.iso','.chd'],
    's32x':  ['.32x','.bin'],
    'psx':   ['.bin','.cue','.img','.pbp','.chd'],
    'psp':   ['.iso','.cso','.pbp'],
    'fbneo': ['.zip'],
    'mame':  ['.zip'],
    'a2600': ['.a26','.bin','.rom'],
    'a7800': ['.a78','.bin'],
    'lynx':  ['.lnx'],
    'pce':   ['.pce','.zip'],
    'ngp':   ['.ngp'],
    'ngpc':  ['.ngc','.ngpc'],
    'ws':    ['.ws'],
    'wsc':   ['.wsc'],
    'dos':   ['.zip','.exe'],
}

def scan():
    if not os.path.isdir(SYSTEMS_DIR):
        print("❌ مجلد systems/ غير موجود!"); sys.exit(1)
    total = 0
    for sid in sorted(os.listdir(SYSTEMS_DIR)):
        sdir  = os.path.join(SYSTEMS_DIR, sid)
        rdir  = os.path.join(sdir, 'roms')
        if not os.path.isdir(sdir): continue
        os.makedirs(rdir, exist_ok=True)
        exts = EXT_MAP.get(sid, [])
        roms = []
        if os.path.isdir(rdir):
            for fn in sorted(os.listdir(rdir)):
                fp = os.path.join(rdir, fn)
                if not os.path.isfile(fp): continue
                ext = os.path.splitext(fn)[1].lower()
                if ext not in exts: continue
                name = os.path.splitext(fn)[0]
                roms.append({"name": name, "file": fn, "size": os.path.getsize(fp)})
        with open(os.path.join(sdir, 'roms.json'), 'w', encoding='utf-8') as f:
            json.dump(roms, f, ensure_ascii=False, indent=2)
        status = f"✅ {sid:10s} — {len(roms):3d} لعبة" if roms else f"  ⬜ {sid:10s} — فارغ"
        print(status)
        total += len(roms)
    print(f"\n{'='*38}\n  المجموع: {total} لعبة\n{'='*38}")
    print("\n✅ تم توليد roms.json لجميع الأنظمة")
    print("   ارفع كل الملفات إلى هوستك ثم اضغط 'مسح الألعاب' في التطبيق")

if __name__ == '__main__':
    print("🎮 Arcade Vault — ROM Scanner\n" + "="*38)
    scan()
    input("\nاضغط Enter للإغلاق...")
