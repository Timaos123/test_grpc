import grpc
from concurrent import futures
import time

# 导入生成的代码
import qa_service_pb2
import qa_service_pb2_grpc

# 实现服务类
class QAServiceServicer(qa_service_pb2_grpc.QAServiceServicer):
    def GetAnswer(self, request, context):
        # 简单的问答逻辑：返回固定答案或回显问题
        question_text = request.text
        print(f"Received question: {question_text}")

        # 这里可以实现复杂的问答逻辑，例如调用模型或 API
        # 为了简单起见，我们返回一个固定的答案
        answer_text = "这是一个示例回答。"

        # 构建并返回响应
        return qa_service_pb2.Answer(text=answer_text)

def serve():
    # 创建 gRPC 服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    qa_service_pb2_grpc.add_QAServiceServicer_to_server(QAServiceServicer(), server)

    # 监听端口 50051
    server.add_insecure_port('[::]:50051')
    server.start()
    print("QAService server started on port 50051.")

    try:
        while True:
            time.sleep(86400)  # 一直运行，单位为秒
    except KeyboardInterrupt:
        server.stop(0)
        print("QAService server stopped.")

if __name__ == '__main__':
    serve()
