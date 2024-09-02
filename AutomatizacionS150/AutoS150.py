from docxtpl import DocxTemplate
doc = DocxTemplate("S-140_S.docx")
week1 = "24 Octubre"
week2 = "31 Octubre"
cap1 = "Genesis 1-3"
cap2 = "Genesis 4,5"
bibleTreasures_week1 = "Como ser fiel a pesar de las pruebas"
bibleTreasures_week2 = "La lucha del siervo fiel complace a Jehova"
bestMaster1_week1 = "primera conversacion"
bestMaster2_week1 = "revisita"
bestMaster3_week1 = "curso biblico"
bestMaster1_week2 = "primera conversacion video"
bestMaster2_week2 = "primera conversacion"
bestMaster3_week2 = "Discurso"
my_context = {'week1' : week1, 'week2' : week2,'cap1' : cap1,'cap2' : cap2,'bibleTreasures_week1' : bibleTreasures_week1,
'bibleTreasures_week2' : bibleTreasures_week2, 'bestMaster1_week1' : bestMaster1_week1,'bestMaster2_week1' : bestMaster2_week1,
'bestMaster3_week1' : bestMaster3_week1,'bestMaster1_week2' : bestMaster1_week2,'bestMaster2_week2' : bestMaster2_week2,
'bestMaster3_week2' : bestMaster3_week2}

doc.render(my_context)
doc.save("generated_doc.docx")