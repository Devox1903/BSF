import tkinter as tk
from tkinter import ttk

#window and grid
cs = tk.Tk()
cs.title("Blacksmithfraction")
cs.geometry("1060x720")
for i in range(0,25):
    cs.columnconfigure(i,weight = 1)
    cs.rowconfigure(i,weight = 1)

#widgets
cst = ttk.Label(cs,text= "Charackter Sheet",)
cn = ttk.Label(cs, text = "Name:")
sc =ttk.Label(cs, text = "Rasse:")
cl = ttk.Label(cs, text = "Klasse")
lv = ttk.Label(cs, text = "Level")
atr = ttk.Label(cs, text ="Attribute")
avl = ttk.Label(cs, text ="Werte")
mod = ttk.Label(cs, text ="Modifikator")
sth = ttk.Label(cs, text ="Resttungswurf")
stre = ttk.Label(cs, text ="Stärke")
ges = ttk.Label(cs, text ="Geschicklichkeit")
con = ttk.Label(cs, text ="Konstitution")
vit = ttk.Label(cs, text ="Vitalität")
inte = ttk.Label(cs, text ="Intelligenz")
wis = ttk.Label(cs, text ="Weisheit")
cha = ttk.Label(cs, text ="Charisma")
emp = ttk.Label(cs, text ="Empathie")
end = ttk.Label(cs, text ="Ausdauer")
tp = ttk.Label(cs, text ="Trefferpunkte")
bl = ttk.Label(cs, text ="Blut")
mo = ttk.Label(cs, text ="Moral")
maxi = ttk.Label(cs, text ="Maximum")
dmg = ttk.Label(cs, text ="Schäden")
act = ttk.Label(cs, text ="Aktuell")
stat = ttk.Label(cs, text ="Status")
l_cn = ttk.Label(text="Name")
l_sc =ttk.Label(text="Rasse")
l_cl = ttk.Label(text="Klasse")
e_lv = ttk.Entry()
e_atr = ttk.Entry()
e_avl = ttk.Entry()
e_mod = ttk.Entry()
e_sth = ttk.Entry()
e_str = ttk.Entry()
e_ges = ttk.Entry()
e_con = ttk.Entry()
e_vit = ttk.Entry()
e_int = ttk.Entry()
e_wis = ttk.Entry()
e_cha = ttk.Entry()
e_emp = ttk.Entry()
e_end = ttk.Entry()
e_enddmg = ttk.Entry()
end_act = ttk.Label(text="")
end_stat = ttk.Label(text="")
e_tp = ttk.Entry()
e_tpdmg = ttk.Entry()
tp_act = ttk.Label(text="")
tp_stat = ttk.Label(text="")
e_bl = ttk.Entry()
e_bldmg = ttk.Entry()
bl_act = ttk.Label(text="")
bl_stat = ttk.Label(text="")
e_mo = ttk.Entry()
e_modmg = ttk.Entry()
mo_act = ttk.Label(text="")
mo_stat = ttk.Label(text="")
e_max = ttk.Entry()
e_dmg = ttk.Entry()
e_act = ttk.Entry()
e_stat = ttk.Entry()

#widgets placing
cst.grid(column = 14 , row = 0, columnspan = 2,)
cn.grid(column = 1, row = 2)
sc.grid(column = 3, row = 2)
cl.grid(column = 5, row = 2)
lv.grid(column = 7, row = 2)
atr.grid(column = 1, row = 4)
avl.grid(column = 2, row = 4)
mod.grid(column = 3, row = 4)
sth.grid(column = 4, row = 4)
stre.grid(column = 1, row = 5)
ges.grid(column = 1, row = 6)
con.grid(column = 1, row = 7)
vit.grid(column = 1, row = 8)
inte.grid(column = 1, row = 9)
wis.grid(column = 1, row = 10)
cha.grid(column = 1, row = 11)
emp.grid(column = 1, row = 12)
end.grid(column = 11, row = 2)
tp.grid(column = 11, row = 3)
bl.grid(column = 11, row = 4)
mo.grid(column = 11, row = 5)
maxi.grid(column = 12, row = 1)
dmg.grid(column = 13, row = 1)
act.grid(column = 14, row = 1)
stat.grid(column = 15, row = 1)
l_cn.grid(column = 2, row = 2, sticky="w" )
l_sc.grid(column = 4, row = 2, sticky="w")
l_cl.grid(column = 6, row = 2, sticky="w")
e_lv.grid(column = 8, row = 2)
e_str.grid(column = 2, row = 5)
e_ges.grid(column = 2, row = 6)
e_con.grid(column = 2, row = 7)
e_vit.grid(column = 2, row = 8)
e_int.grid(column = 2, row = 9)
e_wis.grid(column = 2, row = 10)
e_cha.grid(column = 2, row = 11)
e_emp.grid(column = 2, row = 12)
e_end.grid(column = 12, row = 2)
e_enddmg.grid(column = 13, row = 2)
end_act.grid(column = 14, row = 2)
end_stat.grid(column = 15, row = 2)
e_tp.grid(column = 12, row = 3)
e_tpdmg.grid(column = 13, row = 3)
tp_act.grid(column = 14, row = 3)
tp_stat.grid(column = 15, row = 3)
e_bl.grid(column = 12, row = 4)
e_bldmg.grid(column = 13, row = 4)
bl_act.grid(column = 14, row = 4)
bl_stat.grid(column = 15, row = 4)
e_mo.grid(column = 12, row = 5)
e_modmg.grid(column = 13, row = 5 )
mo_act.grid(column = 14, row = 5)
mo_stat.grid(column = 15, row = 5)

#Statusfenster
def status_update():
    end_val=None
    if e_end.get() != "" and e_enddmg.get() != "":
        end_val = int(e_end.get()) - int(e_enddmg.get())
        end_act.config(text=str(end_val))
    else:
        end_act.config(text=e_end.get())
    if end_val is not None and end_val<= 0:
        end_stat.config(text="Erschöpft",background="red")
    else:
        end_stat.config(text="Ausgeruht", background="green")

    tp_val = None
    if e_tp.get() != "" and e_tpdmg.get() != "":
        tp_val = int(e_tp.get()) - int(e_tpdmg.get())
        tp_act.config(text=str(tp_val))
    else:
        tp_act.config(text=e_tp.get())
    if tp_val is not None and tp_val<= 0:
        tp_stat.config(text="Bewusstlos",background="red")
    else:
        tp_stat.config(text="Bei Bewusst sein", background="green")

    bl_val = None
    if e_bl.get() != "" and e_bldmg.get() != "":
        bl_val = int(e_bl.get()) - int(e_bldmg.get())
        bl_act.config(text=str(bl_val))
    else:
        bl_act.config(text=e_bl.get())
    if bl_val is not None and bl_val<= 0:
        bl_stat.config(text="Tod",background="red")
    else:
        bl_stat.config(text="Lebend", background="green")

    mo_val = None
    if e_mo.get() != "" and e_modmg.get() != "":
        mo_val = int(e_mo.get()) - int(e_modmg.get())
        mo_act.config(text=str(mo_val))
    else:
        mo_act.config(text=e_mo.get()) 
    if mo_val is not None and mo_val <= 0:
        mo_stat.config(text="Panisch",background="red")
    else:
        mo_stat.config(text="Gelassen", background="green")
    cs.after(50, status_update)

status_update()
cs.mainloop()

#find ich super