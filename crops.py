def crop(crop_name):
    crop_data = {
    "wheat":["/static/images/wheat.jpg", "Rift-valley, Uasin Gishu, Trans-Nzoia, Nakuru", "Wheat","Uganda, Tanzania, Rwanda"],
    "paddy":["/static/images/paddy.jpg", "Mwea in Kirinyaga, Ahero in Kisumu, Bunyala in Busia", "Rice","South Sudan Uganda, Rwanda"],
    "barley":["/static/images/barley.jpg", "Rift-valler region like Nakuru and Narok", "Barley","Rwanda, Sudan"],
    "maize":["/static/images/maize.jpg", "Nakuru, Kakamega, Murang`a, Kiambu, Embu, Meru, Nandi", "Corn", "Tanzania, Uganda"],
    "bajra":["/static/images/bajra.jpg", "Malindi, Mombasa, Kilifi, Lamu", "Bajra", "Uganda Tanzania"],
    "Copra":["/static/images/copra.jpg", "Kilifi, Kwale, Mombasa, Malindi", "Coconuts", "India, China, UAE"],
    "cotton":["/static/images/cotton.jpg", "Busia, Siaya, Kisumu, Homabay, Kitui, Meru", "Uganda, Tanzania, Rwanda"],
    "masoor":["/static/images/masoor.jpg", "Aberdare range, Mount Kenya parts, Rift valley parts", "Lentils", "India, Sri lanka, UAE"],
    "gram":["/static/images/gram.jpg", "Eastern Kenya, Rift valley", "Chickpeas", "Tanznia, Uganda, Rwanda"],
    "groundnut":["/static/images/groundnut.jpg", "Busia, Siaya, Limuru, Meru, Makueni", "Ground Nuts", "Uganda, Tanzania, Ethiopia"],
    "arhar":["/static/images/arhar.jpg", "Coastal Regions, Eastern Kenya", "Pigeon Peas", "Sri lanka, Uganda India"],
    "sesamum":["/static/images/sesamum.jpg", "Eastern and coastal Kenya", "Sesame", "Iraq, China, Sudan, China"],
    "jowar":["/static/images/jowar.jpg", "Rift Valley, Eastern Kenya", "Sorghum", "Torronto, Uganda, Rwanda, Tanzania"],
    "moong":["/static/images/moong.jpg", "Kitui, Makueni, Machacos", "Green Grams", "UAE, Tanzania, Canada"],
    "niger":["/static/images/niger.jpg", "Highlands of Rift Valley", "Niger", ",Argentina, Somalia, Belgium"],
    "rape":["/static/images/rape.jpg", "Rift Valley Regions", "Canola", "Veitnam, Malaysia, South Africa"],
    "jute":["/static/images/jute.jpg", "Embu, Meru", "Jutte", "Jordan, Taiwan"],
    "safflower":["/static/images/safflower.jpg",  "Eastern parts only", "Flower", " Philippines, Rwanda, Tanzania"],
    "soyabean":["/static/images/soyabean.jpg",  "Kisumu, Busia, Meru, Rift Valley", "Soya", "South Sudan, Uganda, Singapore"],
    "urad":["/static/images/urad.jpg",  "Homabay, Kisumu, eldoret, Kitale", "Black Gram", "Morocco, India, Congo"],
    "ragi":["/static/images/ragi.jpg",  "Kisii, Kakamega, Nyeri, Murang`a", "Finger Millet", "Tanzania, Uganda, Ethiopia"],
    "sunflower":["sunflower.jpg",  " Bungoma, Homa Bay, Kakamega, Meru, Kajiado", "Flower", "South Sudan, Angola, Tanzania"],
    "sugarcane":["sugarcane.jpg","Bungoma, Busia, Kakamega, Kisumu, Homabay" , "Sugar", "South Sudan, Tanzania, Mozambique"]
    }
    return crop_data[crop_name]