import tkinter as tk
from tkinter import *
from tkinter import messagebox

window=tk.Tk()
window.minsize(800,800)

intro=tk.Label(master=window, text="What is COVID-19?\nCheck out the information below!", foreground="navy", background="lavender")
intro.pack()

def showSymptoms():
    frm2 = tk.Frame(relief=tk.GROOVE, borderwidth=15)
    frm2.place(relx=.5, rely=.5, anchor='c', height=600, width=600)
    symp=tk.Label(master=frm2, justify='left', wraplength=560, text="Here are some symptoms that people infected with COVID-19 experience:\nMost common symptoms:\nfever\ndry cough\ntiredness\nLess common symptoms:\naches and pains\nsore throat\ndiarrhoea\nconjunctivitis\nheadache\nloss of taste or smell\na rash on skin, or discolouration of fingers or toes\nSerious symptoms:\ndifficulty breathing or shortness of breath\nchest pain or pressure\nloss of speech or movement\nSeek immediate medical attention if you have serious symptoms. Always call before visiting your doctor or health facility.\nPeople with mild symptoms who are otherwise healthy should manage their symptoms at home.\nOn average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.\nInformation sourced from who.int")
    symp.pack()

def showTreatment():
    frm2 = tk.Frame(relief=tk.GROOVE, borderwidth=15)
    frm2.place(relx=.5, rely=.5, anchor='c', height=600, width=600)
    treatment=tk.Label(master=frm2, justify='left', wraplength=560, text="Self-care\n\nIf you feel sick you should rest, drink plenty of fluid, and eat nutritious food. Stay in a separate room from other family members, and use a dedicated bathroom if possible. Clean and disinfect frequently touched surfaces.\nEveryone should keep a healthy lifestyle at home. Maintain a healthy diet, sleep, stay active, and make social contact with loved ones through the phone or internet. Children need extra love and attention from adults during difficult times. Keep to regular routines and schedules as much as possible.\nIt is normal to feel sad, stressed, or confused during a crisis. Talking to people you trust, such as friends and family, can help. If you feel overwhelmed, talk to a health worker or counsellor.\nMedical treatments\nIf you have mild symptoms and are otherwise healthy, self-isolate and contact your medical provider or a COVID-19 information line for advice.\nSeek medical care if you have a fever, a cough, and difficulty breathing. Call in advance.\nsourced from who.int")
    treatment.pack()

def showPrevention():
    frm2 = tk.Frame(relief=tk.GROOVE, borderwidth=15)
    frm2.place(relx=.5, rely=.5, anchor='c', height=600, width=600)
    prev=tk.Label(master=frm2, justify='left', wraplength=560, text="To prevent the spread of COVID-19:\nClean your hands often. Use soap and water, or an alcohol-based hand rub.\nMaintain a safe distance from anyone who is coughing or sneezing.\nWear a mask when physical distancing is not possible.\nDon’t touch your eyes, nose or mouth.\nCover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\nStay home if you feel unwell.\nsourced from who.int")
    prev.pack()

def showMentalHealth():
    frm2 = tk.Frame(relief=tk.GROOVE, borderwidth=15)
    frm2.place(relx=.5, rely=.5, anchor='c', height=600, width=600)
    mh=tk.Label(master=frm2, justify='left', wraplength=560, text="Be kind to yourself. Go easy on yourself if you’re experiencing more depression or anxiety than usual. You’re not alone in your struggles.\nMaintain a routine as best you can. Even if you’re stuck at home, try to stick to your regular sleep, school, meal, or work schedule. This can help you maintain a sense of normalcy.\nTake time out for activities you enjoy. Read a good book, watch a comedy, play a fun board or video game, make something—whether it’s a new recipe, a craft, or a piece of art. It doesn’t matter what you do, as long as it takes you out of your worries.\nGet out in nature, if possible. Sunshine and fresh air will do you good. Even a walk around your neighborhood can make you feel better. Just be sure to avoid crowds, keep your distance from people you encounter, and obey restrictions in your area.\nFind ways to exercise. Staying active will help you release anxiety, relieve stress, and manage your mood. While gym and group classes may be out, you can still cycle, hike, or walk. Or if you’re stuck at home, look online for exercise videos you can follow. There are many things you can do even without equipment, such as yoga and exercises that use your own bodyweight.\nAvoid self-medicating. Be careful that you’re not using alcohol or other substances to deal with anxiety or depression. If you tend to overdo it in the best of times, it may be a good idea to avoid for now.\nTake up a relaxation practice. When stressors throw your nervous system out of balance, relaxation techniques such as deep breathing, meditation, and yoga can bring you back into a state of equilibrium. Regular practice delivers the greatest benefits, so see if you can set aside even a little time every day.\n sourced from helpguide.org")
    mh.pack()

frm1 = tk.Frame()
frm1.pack()

btnSymptoms = tk.Button(frm1, text ="Symptoms", command = showSymptoms, foreground="VioletRed4", background="PaleVioletRed1").grid(column=1, row=1)

btnTreatment = tk.Button(frm1, text ="Treatment", command = showTreatment, foreground="VioletRed4", background="PaleVioletRed1").grid(column=2, row=1)

btnPrevention = tk.Button(frm1, text ="Prevention", command = showPrevention, foreground="VioletRed4", background="PaleVioletRed1").grid(column=3, row=1)

btnMentalHealth = tk.Button(frm1, text ="Mental Health", command = showMentalHealth, foreground="VioletRed4", background="PaleVioletRed1").grid(column=4, row=1)

for child in frm1.winfo_children(): 
    child.grid_configure(padx=5, pady=25)

window.mainloop()