from fpdf import FPDF

def main():

    name = input("Name: ")
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 75, txt="CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", x=0, y=60, w=210)
    pdf.set_font("helvetica", "B", 26)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(-190,250,f"{name}", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()