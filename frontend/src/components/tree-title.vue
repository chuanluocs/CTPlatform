<template>
    <a-popover>
        <template #content>
            {{ expression }}
        </template>
        <div v-if="msg === 'OR'">
            <a-avatar class="or-avatar" size="small"> || </a-avatar>
            <span class="title-font">
                {...} OR {...} OR {...}
            </span>
        </div>

        <div v-else-if="msg === 'AND'">
            <a-avatar class="and-avatar" size="small"> && </a-avatar>
            <span class="title-font">
                {...} AND {...} AND {...}
            </span>
        </div>

        <div v-else-if="msg === 'not'">
            <a-avatar class="not-avatar" size="small"> ! </a-avatar>
            <span class="title-font">
                not {...}
            </span>
        </div>

        <div v-else-if="msg === '=>'">
            <a-avatar class="implies-avatar" size="small"> => </a-avatar>
            <span class="title-font">
                {...} => {...}
            </span>
        </div>

        <div v-else-if="msg === '<=>'">
            <a-avatar class="same-avatar" size="small"> {{ "<=>" }} </a-avatar>
            <span class="title-font">
                {{ "{...} <=> {...}" }}
            </span>
        </div>
        
        <div v-else>
            <a-avatar size="small"> ~ </a-avatar>
            <span class="title-font">
                {{ expression }}
            </span>
        </div>
    </a-popover>
</template>

<script>
export default {
    name: "tree-title",
    components: {
        
    },
    props: {
        msg: String,
        expression: String,
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

.or-avatar {
    background-color: #BFACE2;
    color: white;
    font-weight: 400;
}

.and-avatar {
    background-color: #BFACE2;
    color: white;
    font-weight: 400;
}

.implies-avatar {
    background-color: #BFACE2;
    color: white;
    font-weight: 400;
}

.same-avatar {
    background-color: #BFACE2;
    color: white;
    font-weight: 400;
}

.not-avatar {
    background-color: #BFACE2;
    color: white;
    font-weight: 400;
}

.title-font {
    padding-left: 10px;
    font-weight: 300;
    font-size: 16px;
    padding-top: 10px;
}
</style>