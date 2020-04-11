import sys
import os


if os.environ:
    print('Environment variables:')
    for k, v in os.environ.items():
        print(f'\t{k:16}: {v}')

if 'Content-Length' in os.environ:
    print('Request body:')
    request_body = sys.stdin.read(int(os.environ['Content-Length'])).strip()
    print(f'\t{request_body}')

if len(sys.argv) > 1:
    print('Command line arguments:')
    print(f'\t{", ".join(sys.argv[1:])}')