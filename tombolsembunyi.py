impor  os
dari  waktu  tidur impor 


a  = ' \ 033 [92m'
b  = ' \ 033 [91m'
c  = ' \ 033 [0m'

 penyiapan def ():
    coba :
        os . mkdir ( '/data/data/com.termux/files/home/.termux' )
    kecuali :
        lulus
    key  =  "extra-keys = [['ESC', '/', '-', 'HOME', 'UP', 'END', 'PGUP'], ['TAB', 'CTRL', 'ALT' , 'LEFT', 'DOWN', 'RIGHT', 'PGDN']] "
    buka ( '/data/data/com.termux/files/home/.termux/termux.properties' , 'w' ). tulis ( kunci )
    os . sistem ( 'termux-reload-settings' )


def  spanduk ():
    os . sistem ( 'jelas' )
    print ( a + 'Shortcut for help you' . center ( 40 ))
    print ( b + 'Yt-Real Videos' . center ( 40 ))
    cetak ( "" . gabung ([ i  untuk  saya  dalam  " \ n " * 3 ]))

jika  __name__ == '__main__' :
    spanduk ()
    dari  threading,  import  Thread  sebagai  td
    t  =  td ( target = setup )
    t . mulai ()
    sementara  t . is_alive ():
        untuk  saya  di  "- \ | / - \ | /" :
            print ( ' \ r Please wait' + i + '' , end = "" , flush = True )
            tidur ( 0.1 )
    spanduk ()
    | _     _  _    ___                  _      
( )   ( )( )_ |  _`\               (_ )    
`\`\_/'/'| ,_)| (_) )   __     _ _  | |    
  `\ /'  | |  | ,  /  /'__`\ /'_` ) | |    
   | |   | |_ | |\ \ (  ___/( (_| | | |    
   (_)   `\__)(_) (_)`\____)`\__,_)(___)   
                                           
                                           |

cetak ( '' ' \ 033 [95m
+ -------------------------------------- +
| jangan lupa like and subscribe nya |
+ -------------------------------------- +
| Terimakasih | Yt-Real videos |
+ -------------------------------------- + '' ' )
