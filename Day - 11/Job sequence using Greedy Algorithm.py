def job_sequencing_with_deadlines(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    time_slots = [False] * max_deadline
    job_sequence = []

    for job in jobs:
        deadline = job[1]
        for i in range(deadline - 1, -1, -1):
            if not time_slots[i]:
                time_slots[i] = True
                job_sequence.append(job[0])
                break

    return job_sequence

# Example Usage
jobs = [("J1", 2, 3), ("J2", 1, 2), ("J3", 2, 5), ("J4", 1, 4), ("J5", 3, 7)]
print(job_sequencing_with_deadlines(jobs))
3