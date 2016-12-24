#!/usr/bin/python3

from moviepy.editor import *
from pysubs2 import *
import argparse
import sys


class GIFGenerator:
    """
    Class to convert video and subtitle file into GIF with subtitles
    """
    def __init__(self):
        self.args = None

        self.sub_file = None
        self.subtitle = None
        self.subtitle_num = None

    def run(self):
        """
        Main function that calls all other class methods
        """

        # Call class methods to initialize class variables
        self.init_arguments()
        self.sub_file = load(self.args.subtitles)
        self.init_subtitles()

        # Get output filename
        gif_filename = self.get_output_file()

        # Get start and end times for subtitle
        start_time = self.sub_file[self.subtitle_num].start / 1000.0
        end_time = self.sub_file[self.subtitle_num].end / 1000.0

        # Create sub-clip from main video clip
        clip = (VideoFileClip(self.args.video)
                .subclip(start_time, end_time)
                .resize(self.args.resize[0]))

        # Create subtitle to be added to sub-clip
        text = (TextClip(self.subtitle,
                         fontsize=float(self.args.font_size[0]),
                         color=self.args.font_color[0],
                         font=self.args.font[0],
                         stroke_color=self.args.stroke_color[0],
                         stroke_width=float(self.args.stroke_width[0]))
                .set_position(('center', 'bottom'))
                .set_duration(clip.duration))

        # Merge sub-clip and subtitle
        composition = CompositeVideoClip([clip, text])
        # If fps passed by user write .gif using fps
        if self.args.fps is not None:
            composition.write_gif(gif_filename, fps=self.args.fps[0])
        else:
            composition.write_gif(gif_filename)

    def init_subtitles(self):
        """
        Check if subtitle information passed via command line is usable.
        Initialize class variables using command line parameters
        """
        if self.args.display_text is not None:
            self.subtitle = self.args.display_text[0]

        if self.args.sub_number is not None:
            self.subtitle_num = self.args.sub_number[0]
            if self.subtitle is None:
                self.subtitle = self.get_subtitle()
        elif self.subtitle is not None:
            self.subtitle_num = self.get_subtitle_num()
            if self.subtitle_num is None:
                print('display_text not found in subtitle file.'
                      + '\nCheck if these were correct:\n\t--display-text=SUBTITLE or\n\t--sub-number=SUBTITLE_NUMBER')
                sys.exit(2)
        else:
            print('No subtitles found.\nUse:\n\t--display-text=SUBTITLE or\n\t--sub-number=SUBTITLE_NUMBER')
            sys.exit(2)

    def get_subtitle(self):
        """
        Returns subtitle from subtitle file using subtitle number
        """
        return self.sub_file[self.subtitle_num].text

    def get_subtitle_num(self):
        """
        Returns subtitle number where subtitle from command line was found
        """
        for i in range(len(self.sub_file)):
            if self.subtitle in self.sub_file[i].text:
                print(self.subtitle)
                print(self.sub_file[i].text)
                return i
        # if subtitle not found in file
        return None

    def get_output_file(self):
        """
        Returns output filename
        """

        # If filename is passed via command line, use that
        if self.args.gif is not None:
            filename = self.args.gif[0]
            # Append .gif if needed
            if '.gif' not in filename:
                filename += '.gif'
        # Else use name of video file with .gif extension
        else:
            filename = self.args.video[:-3] + 'gif'

        return filename

    def init_arguments(self):
        """
        Initialize command line argument parser and define acceptable arguments
        """
        parser = argparse.ArgumentParser(description='Generate GIFs with subtitles from video and subtitle file.')
        parser.add_argument('video',
                            help='Video file to use for GIF.')
        parser.add_argument('subtitles',
                            help='Subtitles file to get GIF subtitles from.')
        parser.add_argument('--display-text=',
                            dest='display_text',
                            nargs=1,
                            help='Text to display as subtitle on GIF.')
        parser.add_argument('--sub-number=',
                            dest='sub_number',
                            type=int,
                            nargs=1,
                            help='Subtitle number to search.')
        parser.add_argument('--gif=',
                            dest='gif',
                            nargs=1,
                            help='Output GIF filename (default is video filename).')
        parser.add_argument('--resize=',
                            dest='resize',
                            type=float,
                            nargs=1,
                            default=[1.0],
                            help='Size of output GIF, based on 1.0 as 100%% of original (default is 1.0).')
        parser.add_argument('--fps=',
                            dest='fps',
                            type=int,
                            nargs=1,
                            help='Fps rate to export GIF with (default is fps of video file).')
        parser.add_argument('--font=',
                            dest='font',
                            nargs=1,
                            default=['arial'],
                            help='Subtitle font (default is Arial).')
        parser.add_argument('--font-size=',
                            dest='font_size',
                            type=int,
                            nargs=1,
                            default=[45],
                            help='Subtitle font size (default is 45).')
        parser.add_argument('--font-color=',
                            dest='font_color',
                            nargs=1,
                            default=['white'],
                            help='Subtitle color (default is white).')
        parser.add_argument('--stroke-width=',
                            dest='stroke_width',
                            type=int,
                            nargs=1,
                            default=[1],
                            help='Subtitle stroke width (default is 1).')
        parser.add_argument('--stroke-color=',
                            dest='stroke_color',
                            nargs=1,
                            default=['black'],
                            help='Subtitle stroke color (default is white).')
        parser.add_argument('--capital=',
                            dest='capital',
                            type=bool,
                            nargs=1,
                            default=[False],
                            help='Capitalize every letter in subtitle (default is False).')

        # Assign command line arguments to class variable
        self.args = parser.parse_args()


def main():
    generator = GIFGenerator()
    generator.run()

if __name__ == "__main__":
    main()
