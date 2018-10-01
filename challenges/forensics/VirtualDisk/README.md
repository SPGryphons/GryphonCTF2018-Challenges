# VirtualDisk

## Question Text

Analyzing a virtual disk is more convenient than a physical disk

*Creator - PotatoDrug*

## Distribution
- VirtualDisk.vmdk
    - SHA1: `c9418b836ec5cf95eeaccb376650a9454155c084`

## Solution
Mount the vmdk on a windows virtual machine. Then extract the flag out from ADS.

```powershell
PS D:\> Get-Item -Path .\secret.txt -Stream *


PSPath        : Microsoft.PowerShell.Core\FileSystem::D:\secret.txt::$DATA
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::D:\
PSChildName   : secret.txt::$DATA
PSDrive       : D
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : D:\secret.txt
Stream        : :$DATA
Length        : 140818

PSPath        : Microsoft.PowerShell.Core\FileSystem::D:\secret.txt:secret
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::D:\
PSChildName   : secret.txt:secret
PSDrive       : D
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : D:\.txt
Stream        : secret
Length        : 47

PS D:\> Get-Content -Path .\secret.txt -Stream 'secret'
GCTF{D1D_y0u_90_d0wN_7H3_RU5514N_r48817_h0l3}
```

### Flag
`GCTF{D1D_y0u_90_d0wN_7H3_RU5514N_r48817_h0l3}`
