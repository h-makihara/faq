import * as grpcWeb from 'grpc-web';

import {
  FaqShowRequest,
  FaqShowResponse} from './faq_pb';

export class FaqGatewayClient {
  constructor (hostname: string,
               credentials?: null | { [index: string]: string; },
               options?: null | { [index: string]: string; });

  faqShow(
    request: FaqShowRequest,
    metadata: grpcWeb.Metadata | undefined,
    callback: (err: grpcWeb.Error,
               response: FaqShowResponse) => void
  ): grpcWeb.ClientReadableStream<FaqShowResponse>;

}

export class FaqGatewayPromiseClient {
  constructor (hostname: string,
               credentials?: null | { [index: string]: string; },
               options?: null | { [index: string]: string; });

  faqShow(
    request: FaqShowRequest,
    metadata?: grpcWeb.Metadata
  ): Promise<FaqShowResponse>;

}

