import img2pdf
from glob import glob
import argparse
import os

current_dir = os.getcwd()

parser = argparse.ArgumentParser(
    prog='img2pdf.py',
    description='Some images in a directory to PDF file.\n')
parser.add_argument('-od', '--output_dir', type=str, default=current_dir, help='Default is current directory')
parser.add_argument('-id', '--input_dir', type=str, default=current_dir, help='Default is current directory')
parser.add_argument('-o', '--output_name', type=str, default='', help='Default is input directory name, Set file name, Not path')
parser.add_argument('-e', '--extention', type=str, default='jpg', help='Default is \'jpg\', Set file extention without \'.\'')
parser.add_argument('-q', '--quiet', default=False, action='store_true', help='Not print')
args = parser.parse_args()

def imageToPDF(image_dir, output_path):
    '''
    image_dir: string , source image's directory path
    output_path: string, output file path
    '''
    image_path = os.path.join(image_dir, '*.' + args.extention)
    image_list = glob(image_path)
    if image_list == list():
        print('[!] Error: image not Found.')
        return False
    #image_list.sort()
    if args.quiet:
        print('[3] convert image list')
        for i in range(len(image_list)):
            image_name = image_list[i].split(os.path.sep)[-1]
            if i == 0:
                print('\t', image_name, '  ', end='', flush=True)
            elif i%5 == 0:
                if i == len(image_list)-1:
                    print('\n\t', image_name)
                else:
                    print('\n\t', image_name, '  ', end='', flush=True)
            elif i == len(image_list)-1:
                print(image_name)
            else:
                print(image_name, '  ', end='', flush=True)

    with open(output_path, 'wb') as f:
        f.write(img2pdf.convert( [_ for _ in image_list] ))

    if args.quiet:
        print('[*] Converted to pdf file.')

# Main
out_name = args.input_dir.split(os.path.sep)[-1] + '.pdf'
if args.output_name != '':
    out_name = os.path.join(args.output_dir, args.output_name)
out_path = os.path.join(args.output_dir, out_name)

if not (os.path.exists(args.output_dir)):
    if args.quiet:
        print(args.output_dir, ' not Found.\n Make the Directory.')
    os.makedirs(args.output_dir)

input_dir = args.input_dir

# Convert image to PDF
if args.quiet:
    print('[1] input directory  |  ', input_dir)
    print('[2] output path      |  ', out_path)
if os.path.exists(input_dir):
    imageToPDF(input_dir, out_path)
else:
    print('[!] Error: ', input_dir, ' not Found.')
