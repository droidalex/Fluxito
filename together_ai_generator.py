import base64
import streamlit as st
from together import Together 
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv('TOGETHER_API_KEY')


def main():
	# Interface gráfica com botão gerar e mostrar imagem
	with st.form("gerador"):
		st.write("Gerador de imagens:")
		prompt = st.text_input("Prompt", "")
		width = st.number_input("Width (pixels)", 1536, 2000)
		height = st.number_input("Height (pixels)", 768, 800)
		n=1
		tkey = KEY
		

		# Botão gerar
		def gerar():
			try:
				os.environ["TOGETHER_API_KEY"] = tkey
				model = "black-forest-labs/FLUX.1-schnell-Free"
				client = Together()
				response = client.images.generate(
					prompt=prompt,
					model=model,
					width=width,
					height=height,
					steps=4,
					n=n,
					response_format="b64_json"
				)

				# Converte o código em base64 para imagem
				image_data = base64.b64decode(response.data[0].b64_json)
				with open(f"imagens_{width}_x{height}.png", "wb") as f:
					f.write(image_data)
				st.image(f"imagens_{width}_x{height}.png", 
						caption=f"Igualdade de pixels: {width} x {height}")
				with open(f"imagens_{width}_x{height}.png", "wb") as f:
					f.write(image_data)
			except Exception as e:
				st.error(str(e))

		# Botão de envio
		submit_button = st.form_submit_button("Gerar")

		if submit_button:
			gerar()

if __name__ == "__main__":
	main()
