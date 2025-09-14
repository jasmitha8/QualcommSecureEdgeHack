✨ Features
	•	Suspicious Motion (YOLOv8 + CV): flags edge-to-center motion, extra faces, proximity spikes, and “phone-up” gestures.
	•	Screenshot Interceptor: if a protected window/region is visible, screenshots are auto-blurred/redacted (clipboard & file flows).
	•	PasteGuard (LLM): on Ctrl/⌘+V, secrets (API keys / JWTs / credit cards / passwords) are masked before reaching any app.

⸻

✅ Requirements
	•	Windows 11 on Snapdragon (ARM64) (dev also works on macOS CPU)
	•	Python 3.12 (ARM64 on Snapdragon)
	•	Models:
	•	LLM from Qualcomm AI Hub exported as ONNX Runtime GenAI bundle
(must include genai_config.json, a tokenizer, and weight_sharing_model_*.serialized.bin shards)
	•	YOLOv8 exported to ONNX (e.g., yolov8n.onnx)
