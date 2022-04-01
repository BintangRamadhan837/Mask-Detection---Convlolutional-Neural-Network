import streamlit as st
from PIL import Image

def main():
    with st.container():
        # st.write('Muhammad Bintang Ramadhan')
        # st.write('FTDS hactiv8 batch 8')
        st.markdown("<h6 style='text-align: center; color: black;'> Muhammad Bintang Ramadhan </h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; color: black;'> FTDS hacktiv8 Batch 8 </h6>", unsafe_allow_html=True)


        st.markdown("<h3 style='text-align: center; color: Orange;'> Problem Statement </h3>", unsafe_allow_html=True)
        st.write('Dalam Projek Milestone 2 Phase 2 ini, saya ingin membuat projek pendeteksi penggunaan masker. Membagi menjadi 3 kelas yaitu orang yang menggunakan masker, tidak menggunakan masker dan tidak menggunakan masker dengan benar.')
        st.write('Pada saat ini telah banyak kabar bahwa sekolah dan kampus akan melakukan pendidikan secara tatap muka, tetapi penyakit COVID-19 ini tetap ada dan tetap bisa menyebar walaupun masyarakat telah melakukan vaksinasi, maka ketika penyelenggaraan pendidikan tatap muka masih harus mematuhi protokol kesehatan salah satunya menggunakan masker. Akan tetapi pada faktanya banyak sekali masyarakat yang mengabaikan penggunaan masker ini, sehingga dikhawatirkan dengan adanya pendidikan tatap muka ini menyebabkan cluster penyebaranvirus, jika para masyarakat (siswa/mahasiswa) tidak taat pada protokol kesehetan. Oleh karena itu, saya ingin membuat projek pendeteksi penggunaan masker menggunakan kamera, jika ada siswa/mahasiswa yang tidak menggunakan masker atau tidak menggunakan maskerdengan baik maka akan terdeteksi kamera dan akan dilakukan teguran oleh pengawas protokol kesehatan.')

        st.markdown("<h6 style='text-align: center; color: black;'> Objective </h6>", unsafe_allow_html=True)
        st.write('Membuat model deep learning CNN (convolutional neural network) untuk melakukan pendeteksian penggunaan masker.')
    with st.container():
        st.markdown("<h3 style='text-align: center; color: Orange;'> Dataset </h3>", unsafe_allow_html=True)
        with st.expander('Dataset Image Class'):
            col1, col2, col3 = st.columns(3)
            with col1:
                img_data1 = Image.open('datawithmask.jpg')
                st.image(img_data1, caption='Image With Mask', width=200)

            with col2:
                img_data2 = Image.open('datawithoutmask.jpg')
                st.image(img_data2, caption='Image Without Mask', width=200)

            with col3:
                img_data3 = Image.open('dataincorrectmask.jpg')
                st.image(img_data3, caption='Image Incorrect Mask', width=200)
           
    with st.container():
        st.markdown("<h3 style='text-align: center; color: Orange;'>Model Architecture & Evaluation Model</h3>", unsafe_allow_html=True)
        with st.expander('Base Model'):
            st.markdown("<h4 style='text-align: center; color: green;'>Model Architecture</h4>", unsafe_allow_html=True)
            img_basemodel = Image.open('basemodel_arch.jpg')
            st.image(img_basemodel, caption='Base Model Architecture', width=500)
            st.markdown("<h4 style='text-align: center; color: green;'>Model Evaluation</h4>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                img_basemodel = Image.open('basemodel_acc.jpg')
                st.image(img_basemodel, caption='Base Model Architecture', width=300)

            with col2:
                img_basemodel_plot = Image.open('basemodel_eval_plot.jpg')
                st.image(img_basemodel_plot, caption='Base Model Evaluation', width=300)

        with st.expander('ResNet50V2'):
            st.markdown("<h4 style='text-align: center; color: green;'>Model Architecture</h4>", unsafe_allow_html=True)
            img_loadresnet = Image.open('loadresnet50v2.jpg')
            st.image(img_loadresnet, width=500)
            img_resnet = Image.open('resnet50v2_arch.jpg')
            st.image(img_resnet, caption='Resnet Model Architecture', width=500)
            st.markdown("<h4 style='text-align: center; color: green;'>Model Evaluation</h4>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                img_resnet_accuracy = Image.open('resnet50v2_acc.jpg')
                st.image(img_resnet_accuracy, caption='ResNet50V2 Model Accuracy', width=300)

            with col2:
                img_resnet_plot = Image.open('resnet50v2_eval_plot.jpg')
                st.image(img_resnet_plot, caption='ResNet50V2 Model Evaluation', width=300)
        
        with st.expander('Model Improvement'):
            st.markdown("<h4 style='text-align: center; color: green;'>Model Architecture</h4>", unsafe_allow_html=True)
            img_improve_arch = Image.open('modelimprove_arch.jpg')
            st.image(img_improve_arch, caption='Resnet Model Architecture', width=500)
            st.markdown("<h4 style='text-align: center; color: green;'>Model Evaluation</h4>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                img_improve = Image.open('modelimprove_acc.jpg')
                st.image(img_improve, caption='Model Improvement Model Accuracy', width=300)

            with col2:
                img_improve_plot = Image.open('modelimprove_eval_plot.jpg')
                st.image(img_improve_plot, caption='Model Improvement Model Evaluation', width=300)