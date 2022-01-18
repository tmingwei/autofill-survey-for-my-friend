from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

web = webdriver.Chrome()
web.get("https://forms.office.com/pages/responsepage.aspx?id=jCy0E8_LPU6dIPVbe17jwQVdNjZG6yZEocD8ltfQNUpUQjVEMFlaRkNIM1RNREVBQ1VCMTdKR1ZOWi4u")
time.sleep(1)

for i in range(200):
	gender_range=random.randint(0,1)
	gender1 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	gender1[gender_range].click()

	age_range=random.randint(2,8)
	age2 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	age2[age_range].click()

	marital_range=random.randint(9,12)
	marital3 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	marital3[marital_range].click()

	employ_range=random.randint(13,17)#skip181920
	employ4 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	employ4[employ_range].click()	

	annual_range=random.randint(21,23)
	annual5 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	annual5[annual_range].click()

	interest_range=random.randint(24,25)
	interest6 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	interest6[interest_range].click()

	days_range=random.randint(26,28)
	days7 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	days7[days_range].click()

	loca_range=random.randint(29,32)
	loca8 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	loca8[loca_range].click()

	plat_range=random.randint(33,36)
	plat9 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	plat9[plat_range].click()

	consider_range=random.randint(37,39)
	consider10a = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	consider10a[consider_range].click()

	consider_range=random.randint(40,41)
	consider10b = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	consider10b[consider_range].click()

	consider_range=random.randint(42,43)
	consider10c = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	consider10c[consider_range].click()

	a=[0,10,15,20]
	q11_range=random.choice(a)
	q11a= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q11a[q11_range].click()

	a=[81,86,91,96]
	q11_range=random.choice(a)
	q11b= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q11b[q11_range].click()

	a=[62,67,72,77]
	q11_range=random.choice(a)
	q11c= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q11c[q11_range].click()

	a=[38,43,48,53,58]
	q11_range=random.choice(a)
	q11d= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q11d[q11_range].click()

	a=[29,34]
	q11_range=random.choice(a)
	q11e= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q11e[q11_range].click()

	a=[130,135,140,145,150]
	q12_range=random.choice(a)
	q12a= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q12a[q12_range].click()

	a=[101,106,171,176]
	q12_range=random.choice(a)
	q12b= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q12b[q12_range].click()

	a=[157,162,167,182,187]
	q12_range=random.choice(a)
	q12c= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q12c[q12_range].click()

	a=[113,118,123]
	q12_range=random.choice(a)
	q12d= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q12d[q12_range].click()

	a=[129,134,139,144,149,154]
	q12_range=random.choice(a)
	q12e= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q12e[q12_range].click()	

	q13_range=random.randint(44,46)
	q13 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	q13[q13_range].click()

	q13_range=random.randint(44,53)#skip54
	q13a = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	q13a[q13_range].click()

	q14_range=random.randint(55,60)
	q14 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	q14[q14_range].click()

	a=[230,235,260,265]
	q15_range=random.choice(a)
	q15a= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q15a[q15_range].click()	

	a=[201,206,291,296]
	q15_range=random.choice(a)
	q15b= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q15b[q15_range].click()

	a=[242,247,252,257]
	q15_range=random.choice(a)
	q15c= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q15c[q15_range].click()

	a=[213,218,228,223]
	q15_range=random.choice(a)
	q15d= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q15d[q15_range].click()

	a=[274,279,284,289]
	q15_range=random.choice(a)
	q15e= web.find_elements(By.CLASS_NAME,"office-form-matrix-cell.radio")
	q15e[q15_range].click()

	q16_range=random.randint(61,69)
	q16 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	q16[q16_range].click()

	q17_range=random.randint(70,73)
	q17 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	q17[q17_range].click()

	q18_range=random.randint(74,76)
	q18 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	q18[q18_range].click()

	q18_range=random.randint(77,79)
	q18a = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	q18a[q18_range].click()

	answer = web.find_element(By.XPATH,'//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[19]/div/div[2]/div/div/textarea')
	answer.click()
	answer.send_keys("NIL")	

	q20_range=random.randint(80,81)
	q20 = web.find_elements(By.CLASS_NAME,"office-form-question-choice-text-span")
	q20[q20_range].click()

	submit = web.find_element(By.XPATH,'//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div')
	submit.click()
	time.sleep(1)
	web.refresh()
	time.sleep(1)