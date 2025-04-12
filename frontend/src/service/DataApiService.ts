import httpClient from "../service/httpclient";


class DataApiService {
  async getAll(): Promise<any> {
    return httpClient("/api/item", { method: "GET" });
  }

  async create(name: string, price: number): Promise<any> {
    const res =  httpClient(
      "/api/item",
      {
        method: "POST",
        body: JSON.stringify({name: name, price: price})
    });
    console.log(res)
    return res
  }

  async update(id: number, name: string, price: number): Promise<any> {
    return httpClient(
      `/api/item/${id}`,
      {
        method: "PUT",
        body: JSON.stringify({name, price})
    });
  }

  async delete(id: number): Promise<any> {
    return httpClient(`/api/item/${id}`, { method: "DELETE" });
  }
}

export default new DataApiService();
