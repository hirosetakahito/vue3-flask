<script lang="ts" setup>
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router'
import DataApiService from "../service/DataApiService";

const router = useRouter()
const formValid = ref(false)

const form = reactive({
  name: '',
  price: 0,
})

const cancel = () => {
  router.push({name: 'list'})
}

const add = () => {
  const confirmResult = window.confirm("本当に追加しますか？");
  if (confirmResult) {
    DataApiService.create(form.name, form.price)
      .then(() => {
        router.push({name: 'list'})
        alert("追加が完了しました");
      })
      .catch((error) => {
        console.log('error_%s', error);
        alert("追加に失敗しました");
      });
  } else {
    alert("中止しました");
  }
}
</script>

<template>
  <v-form v-model="formValid" ref="formRef">
    <v-row>
      <v-col cols="9" sm="6">
        <v-text-field
          label="ID"
          :model-value="'自動採番'"
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
          label="価格"
          autocomplete="off"
          type="number"
        ></v-text-field>
      </v-col>
    </v-row>

    <v-row class="mt-4 justify-end">
      <v-btn variant="text" @click="cancel">Cancel</v-btn>
      <v-btn color="primary" class="ml-2" @click="add">Confirm</v-btn>
    </v-row>
  </v-form>
</template>

