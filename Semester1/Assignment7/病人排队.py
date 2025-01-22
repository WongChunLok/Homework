n = int(input())

#收集病人数据
patients = []
for _ in range(n):
    patient_info = input().strip().split()
    patient_id = patient_info[0]
    age = int(patient_info[1])
    patients.append((patient_id, age, _))  

sorted_patients = sorted(
    patients,
    key=lambda x: (-1 if x[1] >= 60 else 1, -x[1] if x[1] >= 60 else x[2])
)

for patient in sorted_patients:
    print(patient[0])
