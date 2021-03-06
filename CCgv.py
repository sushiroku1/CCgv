import argparse
import random
from sys import argv, exit


def aer(m):
    print('Error ! %s' % m)
    print('Ketik "%s -h" untuk informasi lebih' % argv[0])
    exit()


def imagin():
    f = '%-*s%*s'
    print('\n\n')
    print('     	 ' + '=' * 60)
    print('     	 ' + '|' + ' '*58 + '|')
    print('     	 ' + '|  ' + '_' * 54 + '  |')
    print('     	 ' + '| |' + ' ' * 54 + '| |')
    print('     	 ' + f % (30, '| | Dibuat oleh', 30, '[M]iZun0 | |'))
    print('     	 ' + f % (30, '| | Nama app', 30, 'CCgv | |'))
    print('     	 ' + f % (30, '| | Terima kasih  ', 30, 'DedSecTL | |'))
    print('     	 ' + f % (30, '| | ', 30, ' | |'))
    print('     	 ' + f % (30, '| | ', 30, ' | |'))
    print('     	 ' + f % (30, '| | ', 30, ' | |'))
    print('     	 ' + f %
          (15, '| | CCgv', 45, 'CC Generator and validator | |'))
    print('         ' + f % (30, '| | ', 30, ' | |'))
    print('         ' + f %
          (55, '| | CCgv dibuat berdasarkan algoritma MOD 10', 5, ' | |'))
    print('     	 ' + f %
          (55, '| | yang dimana MOD 10 ini adalah rumus checksum', 5, ' | |'))
    print('     	 ' + f %
          (55, '| | (deteksi kesalahan) yang merupakan nama umum', 5, ' | |'))
    print('     	 ' + f % (55, '| | dari algoritma Luhn.', 5, ' | |'))
    print('     	 ' + f % (55, '| | ', 5, ' | |'))
    print('     	 ' + f % (30, '| | ', 30, 'Version : 1.0 | |'))
    print('     	 | |' + '_' * 54 + '| |')
    print('     	 |  ' + ' ' * 54 + '  |')
    print('     	 ' + f %
          (55, '|   ON OFF    Vol/Up  Vol/Down    TV/AV    MENU', 5, '  |'))
    print('        ' + ' |' + '=' * 58 + '|')
    print('\n\n')


def cvl(t):
    cr = ""
    for i in list(t):
        cr += str(i)
    return cr


def gene(digi=None, mcd=None):

    digo = []
    c = 0
    c0 = 0
    if digi is None:
        digi = []
        for i in range(mcd):
            digi.append(random.randrange(0, 9))

    dd = len(digi) - 1
    diga = digi[:dd]
    for i in diga[::-1]:
        if c == c0:
            a = int(i + i)

            if len(str(a)) != 1:
                a = int(int(str(a)[0]) + int(str(a)[1]))

            digo.append(a)
            c += 2
        else:
            digo.append(i)
            c0 += 1
            c -= 1
    return {'digi': cvl(digi), 'digo': cvl(digo)}


def gin(pin, tidig):
    indah = ""
    for i in pin:
        indah += str(i) + '+'
    kan = len(indah) - 1
    kita = eval(indah[:kan])
    cinta = int(kita * 9)
    kamu = tidig[int(len(str(tidig)) - 1)]
    aku = str(cinta)[int(len(str(cinta)) - 1)]
    if str(aku) == str(kamu):
        beruntung = 'Valid'
    else:
        beruntung = 'Invalid'
    return beruntung


pars = argparse.ArgumentParser(imagin(),
                               description="""
CC Palsu generator ( Lulus Validasi ) dan
Validasi CC
""")
pars.error = aer
CE = pars.add_argument_group('Validasi CC')
CR = pars.add_argument_group('Membuat CC palsu')
CR.add_argument('--create',
                help='Membuat CC palsu.',
                action='store_true',
                default=None)
CR.add_argument('--jumlah',
                type=int,
                help='Jumlah CC yang akan dibuat, default 1.',
                default=1)
CE.add_argument('--file',
                default=None,
                help='File berisi list CC untuk di cek.',
                type=argparse.FileType('r'))
pars.add_argument('--output',
                  help='Simpan output ke file.',
                  type=argparse.FileType('w+'),
                  default=None)
arg = pars.parse_args()

bwt = arg.create
tot = arg.jumlah
li = arg.file
outp = arg.output
hari = 0
if __name__ == "__main__":
    forever = ""
    if bwt:
        while (hari < int(tot)):
            yd = gene(None, random.randrange(13, 16))
            loveyou = gin(yd['digo'], yd['digi'])
            if loveyou == 'Valid':
                forever += "%s\n" % (yd['digi'])
                hari += 1
        if outp:
            outp.write(str(forever) + '\n')
            print('Saved to %s' % outp.name)
        else:
            print(forever)

    elif li:
        for i in li.read().split():
            yd = gene(i)
            loveyou = gin(yd['digo'], yd['digi'])
            forever += "%s : %s\n" % (yd['digi'], loveyou)

        if outp:
            outp.write(str(forever) + '\n')
            print('Saved to %s' % outp.name)
        else:
            print(forever)

