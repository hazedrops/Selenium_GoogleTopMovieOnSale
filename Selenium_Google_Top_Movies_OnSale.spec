# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Selenium_Google_Top_Movies_OnSale.py'],
             pathex=['C:\\Users\\WSYJ\\Desktop\\Study_YJ\\Python\\PythonPortfolio\\WebScraping\\Selenium_GoogleTopMovieOnSale'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Selenium_Google_Top_Movies_OnSale',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
