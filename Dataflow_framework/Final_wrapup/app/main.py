import argparse
from app.processor import process_file
from app.watcher import watch_folder

def main():
    parser = argparse.ArgumentParser(description="Real-time File Processor")
    parser.add_argument("--input", help="Process a single file and exit")
    parser.add_argument("--watch", action="store_true", help="Watch folder continuously")

    args = parser.parse_args()

    if args.input:
        process_file(args.input)
    elif args.watch:
        watch_folder()
    else:
        print("Specify --input <file> or --watch")

if __name__ == "__main__":
    main()
