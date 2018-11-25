[Byte[]] $powerOn  = 0xA0, 0x01, 0x01, 0xA2
[Byte[]] $powerOff = 0xA0, 0x01, 0x00, 0xA1
$robojax = new-Object System.IO.Ports.SerialPort COM8,9600,None,8,one
$robojax.Open()
$robojax.Write($powerOff, 0, $powerOff.Count)
$robojax.Close() 
