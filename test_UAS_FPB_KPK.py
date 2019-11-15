import pandas as pd
import math
# https://sebentarsaja.com/kpk-dan-fpb/
def fpb_kpk(datas):
	angka = pd.DataFrame(columns=['angka', 'pangkat'])
	for data in datas:
		tmp = pd.DataFrame(columns=['angka'])
		for i in range(2,data+1):
			check_is_smaller = False
			for angka_i in tmp["angka"]:
				if i%angka_i == 0:
					check_is_smaller = True
			if(not check_is_smaller and data%i==0):
				tmp_pangkat = 0
				devide = i
				while data/devide > 0 and data%devide ==0 :
					devide*=i
					tmp_pangkat += 1
				# pangkat.append(tmp_pangkat)
				angka = angka.append({"angka":i,"pangkat":tmp_pangkat},ignore_index=True)
				tmp = tmp.append({"angka":i},ignore_index=True)
	angka["max"] = pd.DataFrame(columns=['max'])
	angka["min"] = pd.DataFrame(columns=['min'])

	for q in angka.index:
		angka.loc[q]["max"] = 1
		angka.loc[q]["min"] = 1

	for i in angka.index:
		for j in angka.index:
			if angka.loc[i]["angka"] == angka.loc[j]["angka"] and i != j:
				if angka.loc[i]["pangkat"] > angka.loc[j]["pangkat"]:
					angka.loc[j]["max"] = 0
					angka.loc[i]["min"] = 0

	# KPK semuanya tapi terkecil
	kpk = []
	kpk_value = 1
	for i in angka.index:
		# print(angka.loc[i]["angka"], kpk)
		if angka.loc[i]["angka"] not in kpk:
			kpk.append(angka.loc[i]["angka"])
			kpk_value *= math.pow(angka.loc[i]["angka"],angka.loc[i]["pangkat"])
	return kpk_value

# if __name__ == "__main__":
# 	print(fpb_kpk([6,25,16,30,60,2]))

def test_R1():
	assert fpb_kpk([1,2]) == 2