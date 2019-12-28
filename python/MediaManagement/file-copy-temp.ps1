# Run on MonkeyCube
$Source = "\\norad\Movies" 
$Destination = "G:\movies"
$ReportDate = (Get-Date).tostring("MM-dd-yyyy-hh-mm-ss")
$Flags = "/xc /xn /xo"
$RoboCopyLog = $("\\NORAD\remote-logs\robocopy\RoboCopy_Grandma_"+ $ReportDate + ".log")

robocopy $Source $Destination /MAXAGE:15 /R:30 /W:10 /dcopy:DAT /Z /S /log:$RoboCopyLog



# Run on NORAD for NAS
$Source = "F:\Movies" 
$Destination = "\\192.168.2.146\Multimedia\Movies\Movies"
$ReportDate = (Get-Date).tostring("MM-dd-yyyy-hh-mm-ss")
$Flags = "/xc /xn /xo"
$RoboCopyLog = $("\\NORAD\remote-logs\robocopy\RoboCopy_Cheehahn_"+ $ReportDate + ".log")

robocopy $Source $Destination /MAXAGE:400 /R:30 /W:10 /dcopy:DAT /Z /S /log:$RoboCopyLog

