import streamlit as st
from scraper import search_amazon

st.title("🛒 Product Search Engine")

query = st.text_input("Search product")

min_price, max_price = st.slider(
    "Select Budget",
    0, 100000, (100, 2000)
)

if st.button("Search"):

    results = search_amazon(query)

    if len(results) == 0:
        st.write("No products found")

    for p in results:

        if min_price <= p["price"] <= max_price:

            st.image(p["image"], width=200)

            st.subheader(p["name"])

            st.write("Price: ₹", p["price"])

            st.write("Website:", p["website"])

            st.markdown(f"[Buy Now]({p['url']})")

            st.write("---")
