from pyzbar.pyzbar import decode
from PIL import Image
from appJar import gui
from pathlib import Path

def QRcode_decoder():
  def Qrcode_decode(input_file):
    text=decode(Image.open(input_file))
    message=str(text)
    message=message.split('\'')
    if(app.infoBox("Displaying Decoded Message","Message= "+message[1])):
          app.stop()
          
    

  def validate_inputs(src_file):

       errors = False
       error_msgs = []
       if Path(src_file).suffix.upper() != ".png":
          errors = False
          error_msgs.append("Please select a Qrcode image file")
          
       return(errors, error_msgs)  



  def press(button):
      if button=="Process":
          src_file = app.getEntry("Input_File")

          errors, error_msg = validate_inputs(src_file)
          if errors:
              app.errorBox("Error", "\n".join(error_msg), parent=None)
          else:
             Qrcode_decode(src_file)
      else:
          app.stop()

  app=gui("QR code Message decoder", useTtk=True)
  app.setTtkTheme('alt')
  app.setSize(500, 200)

  # Add the interactive components
  app.addLabel("Choose Source of Qr code image")
  app.addFileEntry("Input_File")

  app.addButtons(["Process", "Quit"],press)
  app.go()

QRcode_decoder()
