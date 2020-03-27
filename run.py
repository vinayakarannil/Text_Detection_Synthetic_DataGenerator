import os
import argparse

from generator import ImageGenerator

def parse_arguments():

    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--output_dir",
        type=str,
        nargs="?",
        help="The output directory",
        default="output/",
    )
    parser.add_argument(
        "--font_dir",
        type=str,
        nargs="?",
        help="The font directory",
        default="fonts/latin/"
    )
    parser.add_argument(
        "--img_size",
        type=tuple,
        nargs="?",
        help="size of generated image",
        default=(1000, 1000)
    )
    parser.add_argument(
        "--bg_color",
        nargs="?",
        help="background colour of generated image. Default is white",
        default=(255,255,255,255)
    )
    parser.add_argument(
        "--fs_min",
        type=int,
        nargs="?",
        help="minimum font size of the genearted text",
        default=10
    )
    parser.add_argument(
        "--fs_max",
        type=int,
        nargs="?",
        help="maximum font size of the genearted text",
        default=26
    )
    parser.add_argument(
        "--text_corpus",
        type=str,
        nargs="?",
        help="path to the text corpus file",
        default="dicts/en.txt"
    )
    parser.add_argument(
        "--date_corpus",
        type=str,
        nargs="?",
        help="path to the text corpus file",
        default="dicts/dates.txt"
    )
    
    return parser.parse_args()

def main():

    args = parse_arguments()
    
    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)
        
    img_generator = ImageGenerator(args.font_dir, args.output_dir,args.fs_min, args.fs_max, args.text_corpus, args.date_corpus, args.img_size,args.bg_color)
    img_generator.generateImages(1, 100, draw_rectangle=True)

if __name__ == '__main__':
    main()