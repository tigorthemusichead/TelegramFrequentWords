import make
print("where can I find your result.json file?")
json_adr = input()
print("OK, where to put the image?")
res_adr = input()
make.make(json_adr, res_adr)
