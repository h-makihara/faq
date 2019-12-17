import * as grpcWeb from 'grpc-web';

import {
  FaqCreateRequest,
  FaqCreateResponse,
  FaqShowRequest,
  FaqShowResponse,
  FaqUpdateRequest,
  FaqUpdateResponse} from './faq_pb';

export class FaqGatewayClient {
  constructor (hostname: string,
               credentials?: null | { [index: string]: string; },
               options?: null | { [index: string]: string; });

  faqCreate(
    request: FaqCreateRequest,
    metadata: grpcWeb.Metadata | undefined,
    callback: (err: grpcWeb.Error,
               response: FaqCreateResponse) => void
  ): grpcWeb.ClientReadableStream<FaqCreateResponse>;

  faqShow(
    request: FaqShowRequest,
    metadata: grpcWeb.Metadata | undefined,
    callback: (err: grpcWeb.Error,
               response: FaqShowResponse) => void
  ): grpcWeb.ClientReadableStream<FaqShowResponse>;

  faqUpdate(
    request: FaqUpdateRequest,
    metadata: grpcWeb.Metadata | undefined,
    callback: (err: grpcWeb.Error,
               response: FaqUpdateResponse) => void
  ): grpcWeb.ClientReadableStream<FaqUpdateResponse>;

}

export class FaqGatewayPromiseClient {
  constructor (hostname: string,
               credentials?: null | { [index: string]: string; },
               options?: null | { [index: string]: string; });

  faqCreate(
    request: FaqCreateRequest,
    metadata?: grpcWeb.Metadata
  ): Promise<FaqCreateResponse>;

  faqShow(
    request: FaqShowRequest,
    metadata?: grpcWeb.Metadata
  ): Promise<FaqShowResponse>;

  faqUpdate(
    request: FaqUpdateRequest,
    metadata?: grpcWeb.Metadata
  ): Promise<FaqUpdateResponse>;

}

