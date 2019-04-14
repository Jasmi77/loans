#example of python script
def count_performance_rows():
    """
    A function to count the number of rows that deal with performance for each loan.
    Each row in the source text file is a loan_id and date.
    If there's a date, it means the loan was foreclosed on.
    We'll return a dictionary that indicates if each loan was foreclosed on, along with the number of performance events per loan.
    """

    counts = {}

    # Read the data file.
    with open(os.path.join(settings.PROCESSED_DIR, "Performance.txt"), 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                # Skip the header row
                continue
            # Each row is a loan id and a date, separated by a |
            loan_id, date = line.split("|")
            # Convert to integer
            loan_id = int(loan_id)
            # Add the loan to the counts dictionary, so we can count the number of performance events.
            if loan_id not in counts:
                counts[loan_id] = {
                    "foreclosure_status": False,
                    "performance_count": 0
                }
            # Increment the counter.
            counts[loan_id]["performance_count"] += 1
            # If there's a date, it indicates that the loan was foreclosed on
            if len(date.strip()) > 0:
                counts[loan_id]["foreclosure_status"] = True
    return counts
