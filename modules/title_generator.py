def generate_title(summary):

    words = summary.split()

    if len(words) > 7:

        return " ".join(words[:7]) + "..."

    return summary