import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  public endpoint = 'http://127.0.0.1:5000';
  // API_KEY
  constructor(private httpClient: HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  }

  public getTodosClientes(): Observable<any>{
    return this.httpClient.get(this.endpoint + '/clientes/clientes');
  }

  public getClienteId(id_cliente:number): Observable<any>{
    let url = this.endpoint + `/clientes/clientes/${id_cliente}`
    console.log(url)
    return this.httpClient.get(url)
  }

  public postClientes(cliente:any){
    return this.httpClient.post(this.endpoint + '/clientes/clientes', cliente);
  }

  public deleteCliente(id_cliente:number) {
    return this.httpClient.delete(this.endpoint + `/clientes/clientes/` + id_cliente)
  }


}

