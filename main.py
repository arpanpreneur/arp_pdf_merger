from merger.merger import merge_pdfs
import argparse


def main():
    parser = argparse.ArgumentParser(description="Merge Form16 PDFs.")
    parser.add_argument("source_dir", help="Source directory containing the PDFs")
    parser.add_argument("dest_dir", help="Destination directory for the merged PDFs")

    args = parser.parse_args()

    merge_pdfs(args.source_dir, args.dest_dir)


if __name__ == "__main__":
    main()
