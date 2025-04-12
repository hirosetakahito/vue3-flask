<script lang='ts' setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import DataApiService from "../service/DataApiService";

const router = useRouter()
const isLoading = ref(false)
const data = ref([])
const totalItems = ref(0)

const initilize = async() => {
  return new Promise(async (resolve, reject) => {
    isLoading.value = true;
    await DataApiService.getAll()
      .then((response) => {
        data.value = response
        resolve(200)
      })
      .catch((error: unknown) => {
        console.log(error)
        data.value = [];
        reject(500);
      })
      .finally(() => {
        isLoading.value = false
      })
  });
}

const deleteData = (index: number) => {
  const confirmResult = window.confirm("本当に削除しますか？");
  if (confirmResult) {
    DataApiService.delete(data.value[index]["id"])
      .then(() => {
        initilize();
        alert("削除完了しました");
      })
      .catch((error: unknown) => {
        console.error("error:", error);
        alert("削除に失敗しました");
      });
  } else {
    alert("中止しました");
  }
}

const editData = (index: number) => {
  router.push({
    name:'edit', 
    query: {
      id: data.value[index]["id"],
      name: data.value[index]["name"],
      price: data.value[index]["price"]
    }
  })
}

const addData = () => {
  router.push({name: 'add'})
}


const headers = [
  { title: 'ID', value: 'id', width: 50 },
  { title: '名称', value: 'name', width: 100 },
  { title: '価格', value: 'price', width: 100 },
  { title: '作成日時', value: 'created_at', width: 200 },
  { title: '更新日時', value: 'updated_at', width: 200 },
  { title: '操作1', value: 'actions', width: 120, sortable: false },
]


initilize()
</script>


<template>
  <v-icon icon="mdi-home" />
  <v-data-table-server
    :items="data"
    :headers="headers"
    :items-length="totalItems"
    :loading="isLoading"
    fixed-header
    hide-default-footer
    height="500"
    class="elevation-1"
  >
    <template icon #item.actions="{ index }">
      <v-btn color="primary" @click.prevent="editData(index)">
        EDIT
      </v-btn>
      <v-btn color="error" @click.prevent="deleteData(index)">
        DEL
      </v-btn>
    </template>
  </v-data-table-server>
  <v-btn color="primary" @click='addData'>Add Item</v-btn>
</template>
