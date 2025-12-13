# Cloudinary Upload Script
# Uploads spiritual-enlightenment.mov to Cloudinary Pro

$cloudName = "dzegofdgp"
$apiKey = "283632349543287"
$apiSecret = "dm_7xFvraZI-IwcvAxnWGTeNrWM"
$videoPath = "d:\projelerim\siber-isik-portal\assets\videos\spiritual-enlightenment.mov"

# Upload URL
$uploadUrl = "https://api.cloudinary.com/v1_1/$cloudName/video/upload"

Write-Host "Starting upload..." -ForegroundColor Green
Write-Host "File: $videoPath" -ForegroundColor Cyan
Write-Host "Size: $([math]::Round((Get-Item $videoPath).Length/1MB, 2)) MB" -ForegroundColor Cyan

# Prepare form data
$boundary = [System.Guid]::NewGuid().ToString()
$LF = "`r`n"

# Read file as bytes
$fileBytes = [System.IO.File]::ReadAllBytes($videoPath)
$fileName = [System.IO.Path]::GetFileName($videoPath)

# Build multipart form data
$bodyLines = @(
    "--$boundary",
    "Content-Disposition: form-data; name=`"file`"; filename=`"$fileName`"",
    "Content-Type: video/quicktime",
    "",
    [System.Text.Encoding]::GetEncoding("iso-8859-1").GetString($fileBytes),
    "--$boundary",
    "Content-Disposition: form-data; name=`"api_key`"",
    "",
    $apiKey,
    "--$boundary",
    "Content-Disposition: form-data; name=`"timestamp`"",
    "",
    [string]([int](Get-Date -UFormat %s)),
    "--$boundary",
    "Content-Disposition: form-data; name=`"public_id`"",
    "",
    "spiritual-enlightenment",
    "--$boundary--"
)

$body = $bodyLines -join $LF

# Upload
try {
    $response = Invoke-RestMethod -Uri $uploadUrl -Method Post -ContentType "multipart/form-data; boundary=$boundary" -Body $body
    
    Write-Host "`nUpload successful!" -ForegroundColor Green
    Write-Host "URL: $($response.secure_url)" -ForegroundColor Yellow
    Write-Host "`nCopy this URL:" -ForegroundColor Cyan
    Write-Host $response.secure_url -ForegroundColor White
    
    # Save URL to file
    $response.secure_url | Out-File "cloudinary-video-url.txt"
    Write-Host "`nURL saved to: cloudinary-video-url.txt" -ForegroundColor Green
    
} catch {
    Write-Host "`nUpload failed: $_" -ForegroundColor Red
    Write-Host "Error details: $($_.Exception.Message)" -ForegroundColor Red
}
