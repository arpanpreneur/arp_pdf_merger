import os
from pypdf import PdfMerger


def get_files_dict(directory):
    files_dict = {}

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Split filename into parts based on underscore
        parts = filename.split("_")

        if len(parts) >= 2:
            # Retrieve PAN and year from filename
            pan = parts[0]
            year = parts[-1].split(".")[0]

            merge_key = f"{pan}_{year}"

            # Determine if it's a PARTB file or not
            is_partb = "PARTB" in parts

            # Get the absolute file path
            file_path = os.path.join(directory, filename)

            # If PAN doesn't exist in dict, add it
            if merge_key not in files_dict:
                if is_partb:
                    files_dict[merge_key] = (None, file_path)
                else:
                    files_dict[merge_key] = (file_path, None)
            else:
                # If PAN exists, but is a PARTB file, replace second part
                if is_partb:
                    files_dict[merge_key] = (files_dict[merge_key][0], file_path)
                else:
                    # Else, replace the first part
                    files_dict[merge_key] = (file_path, files_dict[merge_key][1])

    return files_dict


def merge_pdfs(source_dir, dest_dir):
    files_dict = get_files_dict(source_dir)

    for pan_year, files in files_dict.items():
        merger = PdfMerger()

        # Check if first part exists and is a PDF file before merging
        if files[0] and files[0].endswith(".pdf"):
            merger.append(files[0])

        # Check if second part exists and is a PDF file before merging
        if files[1] and files[1].endswith(".pdf"):
            merger.append(files[1])

        # If the destination directory doesn't exist, create it
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Save the merged PDFs in the destination directory
        output_filename = f"{pan_year}_merged.pdf"
        merger.write(os.path.join(dest_dir, output_filename))
        merger.close()
