def create_document_schema(
    source_file,
    file_type,
    text,
    page_number=None
):
    return {
        "source_file": source_file,
        "file_type": file_type,
        "page_number": page_number,
        "text": text
    }


def build_document_records(
    source_file,
    file_type,
    text=None,
    pages=None
):

    records = []

    if file_type == "txt":

        records.append(
            create_document_schema(
                source_file=source_file,
                file_type=file_type,
                page_number=None,
                text=text
            )
        )

    else:

        for page in pages:

            records.append(
                create_document_schema(
                    source_file=source_file,
                    file_type=file_type,
                    page_number=page.get("page_number"),
                    text=page.get("text", "")
                )
            )

    return records
