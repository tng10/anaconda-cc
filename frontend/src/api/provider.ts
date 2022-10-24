import axios from "axios";
import type { AxiosInstance, AxiosResponse } from "axios";

export abstract class HttpClientProvider {
  protected abstract instance: any;
  public abstract initializeResponseInterceptor(): void;
  protected abstract handleResponse({ data }: any): any;
  protected abstract handleError(error: any): Promise<never>;
  public abstract get baseUrl(): string;
}

export class AxiosHttpClientProvider extends HttpClientProvider {
  protected readonly instance: AxiosInstance;

  public constructor(baseURL: string) {
    super();
    this.instance = axios.create({ baseURL });
  }

  public initializeResponseInterceptor() {
    this.instance.interceptors.response.use(
      this.handleResponse,
      this.handleError
    );
  }

  protected handleResponse({ data }: AxiosResponse) {
    return data;
  }

  protected handleError(error: any) {
    return Promise.reject(error);
  }

  public get baseUrl(): string {
    return this.instance.defaults.baseURL || "not-defined";
  }
}
