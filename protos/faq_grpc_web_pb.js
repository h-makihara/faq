/**
 * @fileoverview gRPC-Web generated client stub for faq
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */

const grpc = {};
grpc.web = require('grpc-web');

const proto = {};
proto.faq = require('./faq_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.faq.FaqGatewayClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.faq.FaqGatewayPromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.faq.FaqShowRequest,
 *   !proto.faq.FaqShowResponse>}
 */
const methodDescriptor_FaqGateway_FaqShow = new grpc.web.MethodDescriptor(
  '/faq.FaqGateway/FaqShow',
  grpc.web.MethodType.UNARY,
  proto.faq.FaqShowRequest,
  proto.faq.FaqShowResponse,
  /**
   * @param {!proto.faq.FaqShowRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.faq.FaqShowResponse.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.faq.FaqShowRequest,
 *   !proto.faq.FaqShowResponse>}
 */

const methodInfo_FaqGateway_FaqShow = new grpc.web.AbstractClientBase.MethodInfo(
  proto.faq.FaqShowResponse,
  /**
   * @param {!proto.faq.FaqShowRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.faq.FaqShowResponse.deserializeBinary
);

/**
 * @param {!proto.faq.FaqShowRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.faq.FaqShowResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.faq.FaqShowResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.faq.FaqGatewayClient.prototype.faqShow =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/faq.FaqGateway/FaqShow',
      request,
      metadata || {},
      methodDescriptor_FaqGateway_FaqShow,
      callback);
};


/**
 * @param {!proto.faq.FaqShowRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.faq.FaqShowResponse>}
 *     A native promise that resolves to the response
 */
proto.faq.FaqGatewayPromiseClient.prototype.faqShow =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/faq.FaqGateway/FaqShow',
      request,
      metadata || {},
      methodDescriptor_FaqGateway_FaqShow);
};


module.exports = proto.faq;

