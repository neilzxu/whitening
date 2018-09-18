#!/usr/bin/env python3
from skimage import io
import argparse
import math

PIXEL_MAX = 255

def main():
    parser = argparse.ArgumentParser(description='Clean up white passport photo.')
    parser.add_argument(
            'image',
            type=str,
            help='Input image file location.')
    parser.add_argument(
            '--target',
            type=float,
            default=30.0,
            help='Percentile of white pixels that will be averaged.')
    parser.add_argument(
            '--threshold',
            type=float,
            default=30.0,
            help='Distance from white in the color space.')
    args = parser.parse_args()

    args.target = max(0.0 , min(args.target, 100.0))
    args.threshold = max(0.0, args.threshold)

    image = io.imread(args.image)

    coords = []
    for x in range(0, image.shape[0]):
        for y in range(0, image.shape[1]):
            coords.append((x,y))

    def white_dist(coord):
        pixel = image[coord[0], coord[1]]
        return math.sqrt(sum((PIXEL_MAX - pixel[x]) ** 2 for x in range(0, image.shape[2])))

    whites = sorted(list(filter(lambda x: white_dist(x) < args.threshold, coords)), key=white_dist)
    
    for coord in whites:
        for idx in range(0, image.shape[2]):
            image[coord[0], coord[1], idx] = PIXEL_MAX
  
    io.imsave('test.png', image)

if __name__ == '__main__':
    main()


