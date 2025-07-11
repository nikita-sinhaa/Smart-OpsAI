
import numpy as np
import onnx
import onnx.helper as helper
import onnx.numpy_helper as numpy_helper
from onnx import TensorProto

# Define input and output
input_tensor = helper.make_tensor_value_info("input", TensorProto.FLOAT, [None, 1])
output_tensor = helper.make_tensor_value_info("output", TensorProto.FLOAT, [None, 2])

# Simple weights and biases
W = np.array([[1.0, -1.0]], dtype=np.float32).T  # Shape: (2, 1)
B = np.array([0.0, 0.0], dtype=np.float32)       # Shape: (2,)

# Convert to ONNX tensors
W_initializer = numpy_helper.from_array(W, name="W")
B_initializer = numpy_helper.from_array(B, name="B")

# Nodes
linear_node = helper.make_node("Gemm", inputs=["input", "W", "B"], outputs=["linear_out"])
softmax_node = helper.make_node("Softmax", inputs=["linear_out"], outputs=["output"])

# Create graph
graph_def = helper.make_graph(
    [linear_node, softmax_node],
    "DummyModel",
    inputs=[input_tensor],
    outputs=[output_tensor],
    initializer=[W_initializer, B_initializer]
)

# Create and save model
model_def = helper.make_model(graph_def, producer_name="onnx-dummy")
onnx.save(model_def, "model.onnx")
print("✅ model.onnx generated successfully.")
