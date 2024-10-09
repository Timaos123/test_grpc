import grpc

# 导入生成的代码
import qa_service_pb2
import qa_service_pb2_grpc

def run():
    # 创建与服务器的通道
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = qa_service_pb2_grpc.QAServiceStub(channel)

        # 输入问题
        question_text = input("请输入您的问题：")

        # 创建请求
        request = qa_service_pb2.Question(text=question_text)

        # 调用服务的 GetAnswer 方法
        response = stub.GetAnswer(request)

        # 输出答案
        print(f"回答：{response.text}")

if __name__ == '__main__':
    run()
