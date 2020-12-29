# -*- mode: python -*-
import sys
sys.path.append("./libs")

block_cipher = None
import sys
sys.setrecursionlimit(5000)

import os
import sklearn
datas = [
  (os.path.join(os.path.dirname(sklearn.__file__), '.libs/*'), 'sklearn/.libs/')
]

a = Analysis(['D:\\python\\SEV_Venv\\CheckColor.py'],
             pathex=['D:\\python\\py2exe'],
             binaries=[],
             datas=datas,
             hiddenimports=['sklearn.utils._cython_blas','sklearn.neighbors.typedefs','sklearn.neighbors.quad_tree','sklearn.tree._utils'],
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
          name='CheckSimColor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
