from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv
import pickle

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

class lenovoResult:
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, value):
		self._name = value

	@property
	def partNumber(self):
		return self._partNumber
	@partNumber.setter
	def partNumber(self, value):
		self._partNumber = value

	@property
	def processor(self):
		return self._processor
	@processor.setter
	def processor(self, value):
		self._processor = value

	@property
	def OS(self):
		return self._OS
	@OS.setter
	def OS(self, value):
		self._OS = value

	@property
	def memory(self):
		return self._memory
	@memory.setter
	def memory(self, value):
		self._memory = value

	@property
	def hardDrive(self):
		return self._hardDrive
	@hardDrive.setter
	def hardDrive(self, value):
		self._hardDrive = value

	@property
	def warranty(self):
		return self._warranty
	@warranty.setter
	def warranty(self, value):
		self._warranty = value

	@property
	def gfx(self):
		return self._gfx
	@gfx.setter
	def gfx(self, value):
		self._gfx = value

	@property
	def battery(self):
		return self._battery
	@battery.setter
	def battery(self, value):
		self._battery = value

	@property
	def stock(self):
		return self._stock
	@stock.setter
	def stock(self, value):
		self._stock = value

	@property
	def price(self):
		return self._price
	@price.setter
	def price(self, value):
		self._price = value

	@property
	def itemStock(self):
		return self._itemStock
	@itemStock.setter
	def itemStock(self, value):
		self._itemStock = value


browser = webdriver.Chrome(chrome_options=option)
browser.get("https://www.lenovo.com/us/en/outletus/laptops/c/LAPTOPS?q=%3Aprice-desc%3AfacetSys-Brand%3AThink&page=0")

items=[]
while True:
	try:
		#browser.find_element_by_xpath("//*[contains(text(), 'Next Page')]")
		deals = browser.find_elements_by_css_selector(".facetedResults-item")
		for deal in deals:
			lr = lenovoResult()
			lr.name = deal.find_element_by_css_selector(".facetedResults-title").text
			lr.partNumber = deal.find_element_by_css_selector(".facetedResults-feature-list").find_element_by_xpath("//*[contains(text(), 'Part number')]/following-sibling::*[1]")
			lr.processor = deal.find_element_by_css_selector(".facetedResults-feature-list").find_element_by_xpath("//*[contains(text(), 'Processor')]/following-sibling::*[1]")
			lr.OS = deal.find_element_by_css_selector(".facetedResults-feature-list").find_element_by_xpath("//*[contains(text(), 'Operating System')]/following-sibling::*[1]")
			lr.memory = deal.find_element_by_css_selector(".facetedResults-feature-list").find_element_by_xpath("//*[contains(text(), 'Memory')]/following-sibling::*[1]")
			lr.harddrive = deal.find_element_by_css_selector(".facetedResults-feature-list").find_element_by_xpath("//*[contains(text(), 'Hard Drive')]/following-sibling::*[1]")
			lr.warranty = deal.find_element_by_css_selector(".facetedResults-feature-list").find_element_by_xpath("//*[contains(text(), 'Warranty')]/following-sibling::*[1]")
			lr.gfx = deal.find_element_by_css_selector(".facetedResults-feature-list").find_element_by_xpath("//*[contains(text(), 'Graphics')]/following-sibling::*[1]")
			lr.battery = deal.find_element_by_css_selector(".facetedResults-feature-list").find_element_by_xpath("//*[contains(text(), 'Battery')]/following-sibling::*[1]")
			lr.price = deal.find_element_by_css_selector(".pricingSummary-details-final-price").text
			lr.itemStock = deal.find_element_by_css_selector(".pricingSummary-secondary-details").text
			items.append(lr)
			print("%s | %s | %s" % (lr.name, lr.price, lr.itemStock))
		browser.find_element_by_xpath("//*[contains(text(), 'Next Page')]").click()
	except NoSuchElementException:
		break

#pickle just in case
#backupFile = open("pickle.obj", "wb")
#pickle.dump(items, backupFile)
#backupFile.close()


#show your work?

with open("products.csv", 'wb') as csvfile:
	outfile = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	outfile.writerow(['name', 'Part Number', 'Processor', 'Operting System', 'Memory', 'Hard Drive', 'Warranty', 'Graphics Card', 'Battery', 'Price'])
	for item in items:
		outfile.writerow([item.name, item.partNumber, item.processor, item.OS, item.memory, item.harddrive, item.warranty, item.gfx, item.battery, item.price])
