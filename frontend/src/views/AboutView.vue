<template>
    <div class="about">
        <div class="pdf">
            <!-- <vue-pdf-embed :source="pdfSrc" ></vue-pdf-embed> -->
        </div>
    </div>
</template>

<script>
import VuePdfEmbed from "vue-pdf-embed"
export default {
    components: {
        VuePdfEmbed
    },
    data() {
        return {
            pdfSrc: "http://storage.xuetangx.com/public_assets/xuetangx/PDF/PlayerAPI_v1.0.6.pdf",
            //pdfSrc: require("@/assets/Meow.pdf")
        }
    }
}
</script>

<style scoped>
.about {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    /* background-color: black; */
}

.pdf {
    width: 1000px;
}
</style>