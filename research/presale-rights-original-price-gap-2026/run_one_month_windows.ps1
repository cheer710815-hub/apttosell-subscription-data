param(
  [Parameter(Mandatory=$true)][ValidatePattern('^\d{5}$')][string]$Region,
  [Parameter(Mandatory=$true)][ValidatePattern('^\d{6}$')][string]$Month
)
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$collector = Join-Path $here 'collect_molit_presale_rights.py'
if (!(Test-Path $collector)) { throw 'Collector script not found in the same folder.' }
$secure = Read-Host 'Enter the DECODING (non-URL-encoded) data.go.kr API key (input hidden)' -AsSecureString
$ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
try {
  $env:MOLIT_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr)
  & py -3 $collector --region $Region --month $Month --outdir (Join-Path $here 'private_raw')
  if ($LASTEXITCODE -ne 0) { throw ('Collector failed, exit code ' + $LASTEXITCODE) }
}
finally {
  Remove-Item Env:MOLIT_API_KEY -ErrorAction SilentlyContinue
  [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr)
  $secure.Dispose()
}
