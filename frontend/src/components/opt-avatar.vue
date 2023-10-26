<template>
    <a-avatar v-if="msg === 'Boolean'" class="boolean-avatar">01</a-avatar>
    <a-avatar v-if="msg === 'Integer'" class="integer-avatar">Z</a-avatar>
    <a-avatar v-if="msg === 'Float'" class="float-avatar">R</a-avatar>
    <a-avatar v-if="msg === 'Category'" class="category-avatar">C</a-avatar>
</template>

<script>
export default {
    name: "optAvatar",
    components: {
        
    },
    props: {
        msg: String
    }
}
</script>

<style scoped>
.boolean-avatar {
    background-color: #ACB1D6;
    color: white;
    font-weight: 400;
}

.integer-avatar {
    background-color: #8294C4;
    color: white;
    font-weight: 600;
}

.float-avatar {
    background-color: #8294C4;
    color: white;
    font-weight: 600;
}

.category-avatar {
    background-color: #ACB1D6;
    color: white;
    font-weight: 600;
}
</style>