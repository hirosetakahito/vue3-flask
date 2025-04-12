<script lang="ts" setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import DataApiService from "../service/DataApiService";

const router = useRouter()
const formValid = ref(false)
const form = reactive({
  id: 0,
  name: '',
  price: 0,
})

const cancel = () => {
  router.push({name: 'list'})
}

const edit = () => {
  const confirmResult = window.confirm("本当に更新しますか？");
  if (confirmResult) {
    DataApiService.update(form.id, form.name, form.price)
      .then(() => {
        router.push({name: 'list'})
        alert("更新が完了しました");
      })
      .catch((error: unknown) => {
        console.log('error_%s', error);
        alert("更新に失敗しました");
      });
    
  } else {
    alert("中止しました");
  }
}


const props = defineProps({
  id: Number,
  name: String,
  price: Number
})


const initilize = () => {
  if(props.id === undefined) {
    router.push({name: 'list'})
    alert("更新に失敗しました");
  } else {
    form.id = props.id;
    form.name = props.name == undefined ? '' : props.name;
    form.price = props.price == undefined ? 0 : props.price;
  }
}

initilize();
</script>


<template>
  <v-form v-model="formValid" ref="formRef">
    <v-row>
      <v-col cols="9" sm="6">
        <v-text-field
          label="ID"
          :model-value="form.id"
          disabled
        ></v-text-field>
      </v-col>

      <v-col cols="9" sm="6">
        <v-text-field
          v-model="form.name"
          label="名称"
          autocomplete="off"
        ></v-text-field>
      </v-col>

      <v-col cols="9" sm="6">
        <v-text-field
          v-model="form.price"
          label="名称"
          autocomplete="off"
          type="number"
        ></v-text-field>
      </v-col>
    </v-row>

    <v-row class="mt-4 justify-end">
      <v-btn variant="text" @click="cancel">Cancel</v-btn>
      <v-btn type="primary" class="ml-2" @click="edit">Confirm</v-btn>
    </v-row>
  </v-form>
</template>
