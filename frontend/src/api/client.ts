import { HttpClientProvider } from "./provider";

export class HttpClient {
  protected readonly provider: HttpClientProvider;

  public constructor(provider: HttpClientProvider) {
    this.provider = provider;
    this.provider.initializeResponseInterceptor();
  }

  get baseUrl() {
    return this.provider.baseUrl;
  }
}
