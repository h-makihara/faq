import * as jspb from "google-protobuf"

export class FaqComponent extends jspb.Message {
  getQid(): number;
  setQid(value: number): void;

  getScope(): string;
  setScope(value: string): void;

  getServiceName(): string;
  setServiceName(value: string): void;

  getCategory(): string;
  setCategory(value: string): void;

  getQuestion(): string;
  setQuestion(value: string): void;

  getAnswer(): string;
  setAnswer(value: string): void;

  getTagList(): Array<string>;
  setTagList(value: Array<string>): void;
  clearTagList(): void;
  addTag(value: string, index?: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FaqComponent.AsObject;
  static toObject(includeInstance: boolean, msg: FaqComponent): FaqComponent.AsObject;
  static serializeBinaryToWriter(message: FaqComponent, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FaqComponent;
  static deserializeBinaryFromReader(message: FaqComponent, reader: jspb.BinaryReader): FaqComponent;
}

export namespace FaqComponent {
  export type AsObject = {
    qid: number,
    scope: string,
    serviceName: string,
    category: string,
    question: string,
    answer: string,
    tagList: Array<string>,
  }
}

export class ServerResponseComponent extends jspb.Message {
  getIsSuccess(): boolean;
  setIsSuccess(value: boolean): void;

  getMessage(): string;
  setMessage(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ServerResponseComponent.AsObject;
  static toObject(includeInstance: boolean, msg: ServerResponseComponent): ServerResponseComponent.AsObject;
  static serializeBinaryToWriter(message: ServerResponseComponent, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ServerResponseComponent;
  static deserializeBinaryFromReader(message: ServerResponseComponent, reader: jspb.BinaryReader): ServerResponseComponent;
}

export namespace ServerResponseComponent {
  export type AsObject = {
    isSuccess: boolean,
    message: string,
  }
}

export class FaqShowRequest extends jspb.Message {
  getTimestamp(): string;
  setTimestamp(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FaqShowRequest.AsObject;
  static toObject(includeInstance: boolean, msg: FaqShowRequest): FaqShowRequest.AsObject;
  static serializeBinaryToWriter(message: FaqShowRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FaqShowRequest;
  static deserializeBinaryFromReader(message: FaqShowRequest, reader: jspb.BinaryReader): FaqShowRequest;
}

export namespace FaqShowRequest {
  export type AsObject = {
    timestamp: string,
  }
}

export class FaqShowResponse extends jspb.Message {
  getFaqList(): Array<FaqComponent>;
  setFaqList(value: Array<FaqComponent>): void;
  clearFaqList(): void;
  addFaq(value?: FaqComponent, index?: number): FaqComponent;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FaqShowResponse.AsObject;
  static toObject(includeInstance: boolean, msg: FaqShowResponse): FaqShowResponse.AsObject;
  static serializeBinaryToWriter(message: FaqShowResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FaqShowResponse;
  static deserializeBinaryFromReader(message: FaqShowResponse, reader: jspb.BinaryReader): FaqShowResponse;
}

export namespace FaqShowResponse {
  export type AsObject = {
    faqList: Array<FaqComponent.AsObject>,
  }
}

