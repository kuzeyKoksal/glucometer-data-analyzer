THRESHOLD = 200

def fileReader(filename):
    patientInfo = {}  # store all exceedances per patient

    with open(filename, "r") as file:
        for line in file:
            fields = line.strip().split()
            if len(fields) != 5:
                continue  # skip malformed lines

            patientId, date, bloodSugar, bodyTemp, heartRate = fields

            try:
                bloodSugar = int(bloodSugar)
            except ValueError:
                print(f"Invalid blood sugar '{bloodSugar}' for patient {patientId}, skipping")
                continue

            if bloodSugar >= THRESHOLD:
                if patientId not in patientInfo:
                    patientInfo[patientId] = []
                patientInfo[patientId].append((date, bloodSugar))

    # Sort patients by number of exceedances, descending
    sortedPatients = sorted(patientInfo.items(), key=lambda x: len(x[1]), reverse=True)

    # Print each exceedance in order
    for patientId, exceedances in sortedPatients:
        for date, sugar in exceedances:
            print(f"{patientId} {date} {sugar}")

def main():
    fileReader('glucometers.txt')

main()
