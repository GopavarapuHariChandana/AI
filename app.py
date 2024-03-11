from flask import Flask,render_template,session,flash,redirect,request,send_from_directory,url_for,jsonify
# import jsonify
import mysql.connector, os
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from datetime import datetime
from sklearn.tree import DecisionTreeClassifier
import datetime
import time,requests
app=Flask(__name__)
app.config['SECRET_KEY']='attendance system'

def data_bace():
    db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dermatology")
    cur=db.cursor()
    return db,cur


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/admin', methods=['POST','GET'])
def admin():
    if request.method=='POST':
        useremail = request.form['userEmail'] 
        password = request.form['userPassword']

       
        if useremail=="admin@gmail.com" and password=="admin":
            flash("Welcome Admin","success")
            return render_template('admindash.html')
        else:
            flash("Invalid data entered","danger")
            return render_template('admin.html')
    return render_template('admin.html')


@app.route('/signin', methods=['POST','GET'])
def signin():
    if request.method=='POST':
        useremail = request.form['userEmail'] 
        password = request.form['userPassword']

        db,cur=data_bace()
        sql="select * from users where user_Email='"+useremail+"' and Password='"+password+"'"
        cur.execute(sql)
        data=cur.fetchall()
        db.commit()
        if data==[]:
            flash("Invalid data entered","danger")
            return render_template('signin.html')
        else:
           
            session['useremail']=useremail
            session['username']=data[0][1]
            flash("welcome ","success")
            return render_template('upload.html')
    return render_template('signin.html')

@app.route('/contact',methods=["POST","GET"])
def contact():
    if request.method=='POST':
        username=request.form['userName']
        useremail = request.form['userEmail']       
        password = request.form['userPassword']
        mobile = request.form['userPhone']
        address = request.form['userAddr']
        db,cur=data_bace()
        sql="select * from users where user_Email='%s' "%(useremail)
        cur.execute(sql)
        data=cur.fetchall()
        db.commit()
        if data==[]:
            sql = "insert into users(user_Name,user_Email,Password,user_Phone,user_Addr) values(%s,%s,%s,%s,%s)"
            val=(username,useremail,password,mobile,address)
            cur.execute(sql,val)
            db.commit()
            flash("User registered Successfully","success")
            return render_template("contact.html")
        else:
            flash("Details already Exists","warning")
            return render_template("contact.html")
        
    return render_template('contact.html')

@app.route('/userdash')
def userdash():
    return render_template('admindash.html')

import pickle 
@app.route("/upload", methods=["POST","GET"])
def upload():
    print('a')
    if request.method=='POST':
        myfile=request.files['file']
        age=float(request.form['age'])
        gender=float(request.form['gender'])
        days=float(request.form['day'])
        bmi=float(request.form['bmi'])
        smoking=float(request.form['smoking'])
        infection=float(request.form['infection'])
        fn=myfile.filename
        mypath=os.path.join('static/disease/', fn)
        myfile.save(mypath)
        print(mypath)
        lee=[age,gender,days,bmi,smoking,infection]
        filename = (r'models/LinearDiscriminantAnalysis.sav')
        model = pickle.load(open(filename, 'rb'))
        result =model.predict([lee])
        result=result[0]
        if result==0:
            msg1 = 'High'
        elif result==1:
            msg1= 'Low'
        else:
            msg1= 'Medium'
        accepted_formated=['jpg','png','jpeg','jfif','JPG']
        if fn.split('.')[-1] not in accepted_formated:
            flash("Image formats only Accepted","Danger")
            return render_template("upload.html")
        new_model = load_model(r"models\my_model1 (2).h5")
        test_image = image.load_img(mypath, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = new_model.predict(test_image)
        print(np.argmax(result))
        classes= ['Acne and Rosacea Photos','Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions','Atopic Dermatitis Photos' 'Bullous Disease Photos','Cellulitis Impetigo and other Bacterial Infections','Eczema Photos','Exanthems and Drug Eruptions','Hair Loss Photos Alopecia and other Hair Diseases','Herpes HPV and other STDs Photos','Light Diseases and Disorders of Pigmentation','Lupus and other Connective Tissue diseases','Melanoma Skin Cancer Nevi and Moles','Nail Fungus and other Nail Disease','Poison Ivy Photos and other Contact Dermatitis','Psoriasis pictures Lichen Planus and related diseases','Scabies Lyme Disease and other Infestations and Bites','Seborrheic Keratoses and other Benign Tumors','Systemic Disease','Tinea Ringworm Candidiasis and other Fungal Infections','Urticaria Hives','Vascular Tumors','Vasculitis Photos','Warts Molluscum and other Viral Infections']
        prediction=classes[np.argmax(result)]
        print(prediction)
        if prediction=="Acne and Rosacea":
            msg="Rosacea is a chronic skin condition characterized by facial redness, visible blood vessels, and acne-like bumps. It may affect the eyes and is often challenging to detect on brown and Black skin, causing symptoms like swelling and stinging."
            remedy="Treatment involves topical products (e.g., brimonidine for flushing, azelaic acid for bumps), oral antibiotics (for more severe cases), and laser therapy to reduce blood vessels. Self-care includes gentle skin care, identifying triggers, and sun protection. Regular follow-up is crucial, as symptoms may recur."
        elif prediction=="Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions":
            msg="Actinic Keratosis (AK) is a precancerous skin condition caused by sun exposure, presenting as rough, scaly patches. Basal Cell Carcinoma (BCC) is a common skin cancer, appearing as raised, pearly bumps with visible blood vessels. Malignant Lesions encompass various cancers, displaying abnormal growths that may metastasize." 
            remedy="Treatment for Actinic Keratosis involves cryotherapy or topical medications. Basal Cell Carcinoma is typically removed surgically or treated with radiation. Malignant Lesions may require surgery, chemotherapy, or other specialized therapies, depending on the specific cancer type and stage. Early detection is crucial for effective management."
        elif prediction=="Atopic Dermatitis":
            msg="Atopic Dermatitis, commonly known as eczema, is a chronic skin condition characterized by inflamed, itchy, and red skin. It often begins in childhood and may persist into adulthood, with periods of exacerbation and remission."
            remedy="Management involves moisturizing the skin, avoiding triggers, and using topical corticosteroids or immunomodulators to reduce inflammation. Severe cases may require systemic medications, and ongoing care aims to minimize flare-ups and enhance skin barrier function."
        elif prediction=="Bullous Disease":
            msg="Bullous Disease refers to a group of skin disorders characterized by the formation of fluid-filled blisters on the skin's surface. These blisters can vary in size and may cause itching or pain. Pemphigus and Bullous Pemphigoid are examples of bullous diseases."
            remedy="Treatment involves addressing the underlying immune system dysfunction with corticosteroids, immunosuppressive drugs, or biologics. Additionally, wound care and protection against infection are essential for managing the blisters and promoting skin healing."
        elif prediction=="Cellulitis Impetigo and other Bacterial Infections":
            msg="Cellulitis, Impetigo, and other bacterial skin infections are common conditions caused by bacteria entering the skin through cuts or breaks. Cellulitis involves redness and swelling, often on the legs; Impetigo presents as itchy sores or blisters."
            remedy="Treatment typically includes antibiotics, either topical or oral, depending on the severity of the infection. Keeping the affected area clean, using prescribed medications, and practicing good hygiene are crucial for effective management."
        elif prediction=="Eczema disease":
            msg="Eczema, or atopic dermatitis, is a chronic skin condition characterized by inflamed, itchy, and red patches. It commonly appears in childhood but can affect individuals of any age, leading to dry and sensitive skin."
            remedy="Management involves moisturizing the skin, avoiding triggers like certain soaps or fabrics, and using prescribed topical corticosteroids or immunomodulators to alleviate inflammation. Additionally, antihistamines may help relieve itching, promoting a better quality of life for those with eczema."
        elif prediction=="Exanthems and Drug Eruptions":
            msg="Exanthems and drug eruptions refer to widespread rashes or skin reactions that result from various causes, including infections, medications, or allergic reactions. These conditions often manifest as redness, bumps, or blisters on the skin."
            remedy="Treatment involves identifying and discontinuing the causative agent, whether it be a medication or addressing the underlying infection. Symptomatic relief can be provided through antihistamines or topical corticosteroids. Severe cases may require medical attention, and in drug-induced eruptions, alternative medications may be prescribed."
        elif prediction=="Hair Loss Photos Alopecia and other Hair Diseases":
            msg="Hair loss photos often depict various conditions related to alopecia and other hair diseases. Alopecia refers to hair loss, which can occur in different patterns and may result from factors such as genetics, hormonal changes, autoimmune conditions, or underlying medical issues."
            remedy="Treatment depends on the specific cause of hair loss. Options include medications, topical treatments, and in some cases, procedures like hair transplantation. Consulting with a dermatologist or healthcare professional is essential for an accurate diagnosis and tailored treatment plan."
        elif prediction=="Herpes HPV and other STDs Photos":
            msg="Photos related to herpes, human papillomavirus (HPV), and other sexually transmitted diseases (STDs) showcase skin manifestations associated with these infections. Herpes causes painful sores, while HPV can lead to genital warts or other skin changes."
            remedy="Management involves antiviral medications for herpes, and HPV vaccines are available for prevention. Safe sexual practices and regular screenings are crucial for STD prevention and early detection. Consultation with a healthcare professional is important for proper diagnosis and guidance on treatment and prevention strategies."
        elif prediction=="Light Diseases and Disorders of Pigmentation":
            msg="Light diseases and disorders of pigmentation encompass conditions affecting skin coloration. These may include disorders causing hypo- or hyperpigmentation, such as vitiligo or melasma. External factors like sun exposure can also contribute to pigmentation changes."
            remedy="Management varies based on the specific condition. Treatment may involve topical medications, phototherapy, or laser therapy. Sun protection is essential to prevent exacerbation. Consultation with a dermatologist helps determine an appropriate treatment plan tailored to the individual's condition."
        elif prediction=="Lupus and other Connective Tissue diseases":
            msg="Lupus and other connective tissue diseases are autoimmune disorders affecting various tissues throughout the body. Lupus, specifically, can cause inflammation and damage to the skin, joints, kidneys, heart, lungs, blood cells, and brain."
            remedy="Treatment aims to control symptoms and may include anti-inflammatory medications, immunosuppressants, and lifestyle adjustments. Sun protection is crucial, as sunlight can trigger lupus flares. Management involves collaboration between rheumatologists and dermatologists for a comprehensive approach. Regular follow-ups help monitor the disease and adjust treatment as needed."
        elif prediction=="Melanoma Skin Cancer Nevi and Moles":
            msg="Melanoma is a type of skin cancer that originates from pigment-producing cells (melanocytes). Nevi and moles, which are common skin growths, can sometimes transform into melanoma. Early detection is crucial for successful treatment."
            remedy="Treatment involves surgical removal of the melanoma. In advanced cases, additional therapies like immunotherapy, targeted therapy, or chemotherapy may be recommended. Regular skin checks and sun protection are essential for prevention. Consult a dermatologist promptly for any suspicious changes in nevi or moles."
        elif prediction=="Nail Fungus and other Nail Disease":
            msg="Nail fungus, or onychomycosis, is a fungal infection affecting the nails. It can cause discoloration, thickening, and brittleness of the nails. Other nail diseases may include infections, inflammations, or structural abnormalities affecting the nails."
            remedy="Treatment for nail fungus often involves antifungal medications, topical or oral. Keeping nails clean and trimmed, avoiding moisture, and wearing breathable footwear can aid in prevention. For other nail diseases, proper diagnosis by a dermatologist is essential for determining appropriate remedies, which may include medications or surgical interventions."
        elif prediction=="Poison Ivy Photos and other Contact Dermatitis":
            msg="Contact dermatitis, including poison ivy reactions, is an inflammatory skin condition resulting from exposure to irritants or allergens. Symptoms include redness, itching, and rash, often in the affected area."
            remedy="For poison ivy and contact dermatitis, treatment involves washing the affected area, applying cool compresses, and using over-the-counter or prescription corticosteroid creams to alleviate inflammation. Avoiding the triggering substances is crucial to preventing recurrence. If severe or widespread, consult a healthcare professional for appropriate care."
        elif prediction=="Psoriasis pictures Lichen Planus and related diseases":
            msg="Psoriasis and Lichen Planus are chronic skin conditions characterized by distinct skin lesions. Psoriasis presents as red, scaly plaques, while Lichen Planus exhibits purplish, flat-topped bumps."
            remedy="Treatment for psoriasis and lichen planus involves topical steroids, phototherapy, and systemic medications in severe cases. Management focuses on symptom control, reducing inflammation, and preventing flare-ups. Consultation with a dermatologist is recommended for personalized care."
        elif prediction=="Scabies Lyme Disease and other Infestations and Bites":
            msg="Scabies and Lyme Disease are examples of skin conditions caused by infestations and bites. Scabies is a contagious skin infestation by the itch mite, causing intense itching. Lyme Disease, transmitted by ticks, can result in a characteristic bullseye rash and flu-like symptoms."
            remedy="For scabies, topical medications like permethrin are commonly prescribed. Lyme Disease often requires antibiotics, particularly in the early stages. Avoiding exposure to ticks and maintaining good hygiene are preventive measures. Seek medical advice promptly for proper diagnosis and treatment."
        elif prediction=="Seborrheic Keratoses and other Benign Tumors":
            msg="Seborrheic Keratoses and other Benign Tumors are non-cancerous growths on the skin. Seborrheic Keratoses are typically brown, black, or tan growths with a waxy, scaly, or verrucous surface. Other benign tumors include skin tags, lipomas, and dermatofibromas, which are generally harmless."
            remedy="Treatment for Seborrheic Keratoses and benign tumors is often not necessary unless they become symptomatic or for cosmetic reasons. Surgical removal, cryotherapy, or laser therapy may be considered for certain cases. Consult a dermatologist for proper evaluation and management options."
        elif prediction=="Systemic Disease":
            msg="Systemic diseases are conditions that affect multiple organs or systems throughout the body rather than being confined to a specific organ. Examples include diabetes, lupus, and rheumatoid arthritis. These diseases can have widespread effects on various bodily functions and often require comprehensive medical management."
            remedy="Treatment for systemic diseases varies depending on the specific condition. It may involve medications, lifestyle modifications, and ongoing medical monitoring. Patients with systemic diseases often benefit from a multidisciplinary approach involving various healthcare professionals. Early diagnosis and management are crucial for improving outcomes."
        elif prediction=="Tinea Ringworm Candidiasis and other Fungal Infections":
            msg="Fungal infections, such as tinea (ringworm) and candidiasis, are caused by fungi and can affect the skin, nails, or mucous membranes. Tinea presents as red, itchy, and circular rashes, while candidiasis often involves mucosal areas, causing discomfort and itching."
            remedy="Treatment typically involves antifungal medications, either topical or oral, depending on the severity and location of the infection. Good hygiene practices, keeping the affected area clean and dry, and avoiding sharing personal items can help prevent the spread of fungal infections."
        elif prediction=="Urticaria Hives":
            msg="Urticaria, commonly known as hives, is a skin condition characterized by raised, itchy welts or wheals on the skin. These welts can vary in size and shape and often appear and disappear rapidly. Urticaria is often caused by an allergic reaction but can also result from other triggers."
            remedy="Antihistamines are commonly used to relieve itching and reduce the appearance of hives. Identifying and avoiding triggers, such as certain foods or medications, is crucial in preventing recurrent episodes of urticaria. In severe cases, a doctor may recommend additional medications or therapies to manage symptoms."
        elif prediction=="Vascular Tumors":
            msg="Vascular tumors refer to abnormal growths or masses that involve blood vessels. These tumors can occur in various parts of the body and may be benign (non-cancerous) or malignant (cancerous). Common types include hemangiomas and angiosarcomas."
            remedy="Treatment for vascular tumors depends on factors such as the tumor type, location, and whether it is benign or malignant. Benign tumors may not require treatment unless they cause symptoms or cosmetic concerns. Malignant vascular tumors often involve a combination of surgery, chemotherapy, and radiation therapy, with the specific approach determined by the oncology team based on the individual case."
        elif prediction=="Vasculitis":
            msg="Vasculitis is a group of disorders characterized by inflammation of blood vessels, impacting the flow of blood and potentially causing damage to organs. The symptoms can vary depending on the affected organs and the type of vasculitis."
            remedy="Treatment for vasculitis typically involves medications to reduce inflammation and control the immune system. Corticosteroids, immunosuppressive drugs, and other medications may be prescribed based on the severity and type of vasculitis. Close monitoring and collaboration with healthcare professionals are essential for managing this condition effectively."
        elif prediction=="Warts Molluscum and other Viral Infections":
            msg="Warts are small, non-cancerous growths on the skin caused by the human papillomavirus (HPV). Molluscum contagiosum is a viral skin infection characterized by small, round bumps."
            remedy="Warts: Over-the-counter topical treatments, cryotherapy, or laser therapy may be used to remove warts. Molluscum: Lesions may disappear on their own, but treatments like cryotherapy, topical medications, or minor surgical procedures can be considered.Always consult with a healthcare professional for proper diagnosis and treatment options."
        else:
            msg="No Disease"
            remedy="No Remedies"

        db,cur=data_bace()
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        sql="insert into disease_info(pname,email,age,gender,smoking,days,infection,bmi,image,disease,severity,causes,remedies,date,time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(session['username'],session['useremail'],age,gender,smoking,days,infection,bmi,mypath,prediction,msg1,msg,remedy,date,timeStamp)
        cur.execute(sql,val)
        db.commit()
        sql="select * from doctor"
        cur.execute(sql,db)
        data=cur.fetchall()
        db.commit()
        db.close()
        return render_template("result.html",image_name=fn, text=prediction,msg=msg , msg1=msg1,data=data)
    return render_template('upload.html')

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("static/disease", filename)

@app.route('/expertdash')
def expertdash():
    db,cur=data_bace()
    sql="select * from users where user_Email='"+session['useremail']+"' "
    cur.execute(sql,db)
    data=cur.fetchall()
    return render_template('expertdash.html', data=data)

@app.route('/doctor_info',methods=['GET','POST'])
def doctor_info():
    db,cur=data_bace()
    sql="select * from appointment where pemail='"+session['useremail']+"'"
    cur.execute(sql,db)
    data=cur.fetchall()
    db.commit()
    db.close()
    return render_template('doctor_info.html', data=data)

@app.route('/expertchat/<email>',  methods=['POST', 'GET'])
def expertchat(email=""):
    useremail = session['useremail']   
    if request.method=="POST":
        email=request.form['email']
        messages = request.form['messages']
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        db,cur=data_bace()
        receiver=""
        sql = "INSERT INTO chatting (sender_email,receiver_email,chat_date,chat_time,msg,patient_email,patient_name,doctor_email) VALUES (%s,%s,%s,%s, %s, %s,%s,%s)"
        val = (useremail,email,date,timeStamp,messages,useremail,session['username'],email)
        data = cur.execute(sql, val)
        print(data)
        db.commit()
        db.close()
       
    # Fetch messages from the database
    db,cur=data_bace()
    sql_select = "SELECT * FROM chatting where patient_email='"+session['useremail']+"' ORDER BY chat_date, chat_time"
    cur.execute(sql_select)
    alldata = cur.fetchall()
    print(alldata)
    return render_template('expertchat.html',expert_email=email,farmer_email=useremail, alldata=alldata)

@app.route('/patient_request',methods=['GET','POST'])
def patient_request():
    db,cur=data_bace()
    print(session['useremail'])
    sql="select DISTINCT patient_email, patient_name from chatting where doctor_email='"+session['useremail']+"' "
    cur.execute(sql,db)
    data=cur.fetchall()
    db.commit()
    db.close()
    return render_template('patient_request.html', data=data)
    

@app.route('/patientchat/<email>/<name>',  methods=['POST', 'GET'])
def patientchat(email="",name=""):
    useremail = session['useremail']
    print(useremail) 
    print(email)  
    print(name)  
    if request.method=="POST":
        email=request.form['email']
        print(email)  
        name=request.form['username']
        print(name)  
        messages = request.form['messages']
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        db,cur=data_bace()
        sql = "INSERT INTO chatting (sender_email,receiver_email,chat_date,chat_time,msg,patient_email,patient_name,doctor_email) VALUES (%s,%s,%s,%s, %s, %s,%s,%s)"
        val = (useremail,email,date,timeStamp,messages,email,name,useremail)
        data = cur.execute(sql, val)
        print(data)
        db.commit()
        db.close()
    # Fetch messages from the database
    db,cur=data_bace()
    sql_select = "SELECT * FROM chatting where doctor_email='"+session['useremail']+"' and patient_email='"+email+"' ORDER BY chat_date, chat_time"
    cur.execute(sql_select)
    alldata = cur.fetchall()
    print(alldata[0][2])
    return render_template('patientchat.html',doctor_email=useremail,patient_email=email,patient_name=name, alldata=alldata)

@app.route('/patient')
def patient():
    db,cur=data_bace()
    sql="select * from users"
    cur.execute(sql,db)
    data=cur.fetchall()
    return render_template('patient.html',data=data)

@app.route('/doctor',methods=["POST","GET"])
def doctor():
    if request.method=='POST':
        username=request.form['userName']
        useremail = request.form['userEmail']       
        password = request.form['userPassword']
        mobile = request.form['userPhone']
        address = request.form['addr']
        exp = request.form['exp']
        age = request.form['age']
        gender = request.form['gender']
        hname = request.form['hname']
        db,cur=data_bace()
        sql="select * from doctor where Email='%s' "%(useremail)
        cur.execute(sql)
        data=cur.fetchall()
        db.commit()
        if data==[]:
            sql = "insert into doctor(Name,Email,Password,age,gender,hospital_name,address,exp_type,mobile) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(username,useremail,password,age,gender,hname,address,exp,mobile)
            cur.execute(sql,val)
            db.commit()
            flash("User registered Successfully","success")
            return render_template("doctor.html")
        else:
            flash("Details already Exists","warning")
            return render_template("doctor.html")
        
    return render_template('doctor.html')


@app.route('/doctorin', methods=['POST','GET'])
def sigdoctorinnin():
    if request.method=='POST':
        useremail = request.form['userEmail'] 
        password = request.form['userPassword']

        db,cur=data_bace()
        sql="select * from doctor where Email='"+useremail+"' and Password='"+password+"'"
        cur.execute(sql)
        data=cur.fetchall()
        db.commit()
        if data==[]:
            flash("Invalid data entered","danger")
            return render_template('doctorin.html')
        else:
            session['useremail']=useremail
            session['username']=data[0][1]
            flash("welcome ","success")
            return redirect(url_for('patient_request'))
          
    return render_template('doctorin.html')

@app.route('/appointment/<name>/<email>/<hname>/<addr>')
def appointment(name="",email="",hname="",addr=""):
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    db,cur=data_bace()
    sql="SELECT * FROM disease_info where email='"+session['useremail']+"' ORDER BY id DESC LIMIT 1";
    cur.execute(sql,db)
    data=cur.fetchall()
    db.commit()
    sq="insert into appointment(pname,pemail,age,gender,bmi,infection,smoking,days,image,disease,severity,date,time,hname,address,dname,demail) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(data[0][1],data[0][2],data[0][3],data[0][4],data[0][8],data[0][7],data[0][5],data[0][6],data[0][9],data[0][10],data[0][11],date, timeStamp,hname,addr,name,email)
    cur.execute(sq,val)
    db.commit()
    db.close()
    flash("Appointment Booked successfully","success")
    return render_template('upload.html')

@app.route('/view_appointments')
def view_appointments():
    db,cur=data_bace()
    sql="select * from appointment where demail='"+session['useremail']+"'"
    cur.execute(sql,db)
    data=cur.fetchall()
    return render_template('view_appointments.html',data=data)

@app.route('/appointment_status', methods=['POST','GET'])
def appointment_status(id=0):
    if request.method=='POST':
        id=request.form['id']
        date=request.form['date']
        db,cur=data_bace()
        sql="update appointment set status='Accepted', accepted_date='"+date+"' where id='"+id+"'"
        cur.execute(sql,db)
        db.commit()
        flash("appointment accepted","success")
        return redirect(url_for('view_appointments'))
    return redirect(url_for('view_appointments'))

@app.route('/feedback', methods=['POST','GET'])
def feedback():
    if request.method=='POST':
        id=request.form['id']
        msg=request.form['msg']
        db,cur=data_bace()
        sql="update appointment set status='Accepted', feedback='"+msg+"' where id='"+id+"'"
        cur.execute(sql,db)
        db.commit()
        flash("feedback submitted","success")
        return redirect(url_for('doctor_info'))
     
    return redirect(url_for('doctor_info'))



# Dummy translation function for demonstration
def translate(text, target_language):
    # Implement actual translation logic or integration with a translation service here
    return "Translated Text"

@app.route('/translate/<causes>/<remedy>' , methods=['GET'])
def translate_text(causes="",remedy=""):
    data = request.json
    translated_data = translate(data['text'], data['target_language'])
    return jsonify(translated_data)

from googletrans import Translator
@app.route('/history')
def history():
    db, cur = data_bace()
    sql="select * from disease_info where email='"+session['useremail']+"'"
    cur.execute(sql,db)
    data = cur.fetchall()
    print(data)
    print(type(data))
    return render_template('history.html', data=data)

# @app.route('/history')
# def history():
#     db, cur = data_bace()
#     sql="select * from disease_info where email='"+session['useremail']+"'"
#     # cur.execute(sql, (session['useremail'],))
#     cur.execute(sql,db)
#     data = cur.fetchall()
#     print(data)
#     print(type(data))

#     # Check for language preference in session
#     if 'language' in session and session['language'] == 'telugu':
#         translator = Translator()
#         data = [(translator.translate(text, src='en', dest='te').text if isinstance(text, str) else text) for row in data for text in row]
#         print(data)
#     return render_template('history.html', data=data)

@app.route('/set_language', methods=['POST'])
def set_language():
    session['language'] = request.form['language']
    return redirect(url_for('history'))

@app.route('/feedback_info')
def feedback_info():
    db, cur = data_bace()
    sql="select * from appointment"
    cur.execute(sql,db)
    data = cur.fetchall()
    print(data)
    print(type(data))
    return render_template('feedback_info.html', data=data)
@app.route('/doct_info')
def doct_info():
    db, cur = data_bace()
    sql="select * from doctor"
    cur.execute(sql,db)
    data = cur.fetchall()
    print(data)
    print(type(data))
    return render_template('doct_info.html', data=data)
if __name__=='__main__':
    app.run(debug=True)