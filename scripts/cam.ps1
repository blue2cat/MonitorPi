#go to the home directory - otherwise we can't write the file
Set-location ~

#functinon to gather data and take a picture if the door is open
function Get-Images {

  #run the python script
  $doorStatus = python3 ~/door.py | convertfrom-json

  #check to make sure the image dir exists
  if (!$(test-path ~/img)) {
    mkdir -p ./img
  }

  #if the front door is open, take a picure with the Raspi camera
  if ($doorStatus[0][-1] -eq "n") {
    raspistill -o 'current_image.jpg'
  }

  # if the back door is open, take a picture with the USB camera
  elseif ($doorStatus[1][-1] -eq "n") {
    fswebcam -r 'current_image.jpg'
  }

  #if there is a extra image, move it to the img directory. This is needed becase
  #bash does not like using powershell variables to name files directly, so we essentially
  #just rename them with powershell to get around this problem.
  if ($(test-path current_image.jpg)) {
    Copy-Item current_image.jpg "img/door-open-$($(get-date -UFormat %m-%d-%y@%H.%M).ToString() + ".jpg")"

    #remove the old copy
    Remove-item current_image.jpg
  }

  #wait
  Start-Sleep 5
}

#infinite loop to check for door status and take pictures if the door is open
do {
  Get-Images
} while (1 -ne 2)
