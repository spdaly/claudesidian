#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { 
  ListToolsRequestSchema, 
  CallToolRequestSchema 
} from "@modelcontextprotocol/sdk/types.js";
import { GoogleGenerativeAI } from "@google/generative-ai";
import { GoogleAIFileManager } from "@google/generative-ai/server";
import fs from "fs/promises";
import path from "path";
import os from "os";

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
  console.error("❌ GEMINI_API_KEY environment variable is required");
  console.error("");
  console.error("To fix this:");
  console.error("");
  console.error("1. Get your API key from: https://aistudio.google.com/apikey");
  console.error("");
  console.error("2. Add to your shell profile:");
  console.error("   For macOS/Linux (add to ~/.zshrc or ~/.bashrc):");
  console.error("   export GEMINI_API_KEY='your-actual-api-key-here'");
  console.error("");
  console.error("   For Windows PowerShell:");
  console.error("   [System.Environment]::SetEnvironmentVariable('GEMINI_API_KEY', 'your-key', 'User')");
  console.error("");
  console.error("3. Reload your terminal:");
  console.error("   source ~/.zshrc  (or source ~/.bashrc)");
  console.error("");
  console.error("4. Restart Claude Code");
  console.error("");
  console.error("For detailed instructions, see GEMINI_VISION_SETUP.md");
  process.exit(1);
}

const genAI = new GoogleGenerativeAI(apiKey);
const fileManager = new GoogleAIFileManager(apiKey);
const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });

// Expand home directory in paths
function expandPath(filepath) {
  if (filepath.startsWith("~/")) {
    return path.join(os.homedir(), filepath.slice(2));
  }
  return filepath;
}

// Upload file to Gemini
async function uploadFile(filePath) {
  const expandedPath = expandPath(filePath);
  
  try {
    await fs.access(expandedPath);
  } catch {
    throw new Error(`File not found: ${filePath}`);
  }
  
  const ext = path.extname(expandedPath).toLowerCase();
  const mimeTypes = {
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.gif': 'image/gif',
    '.bmp': 'image/bmp',
    '.webp': 'image/webp',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.doc': 'application/msword',
    '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    '.odt': 'application/vnd.oasis.opendocument.text',
    '.rtf': 'application/rtf',
  };
  
  const uploadResult = await fileManager.uploadFile(expandedPath, {
    mimeType: mimeTypes[ext] || 'application/octet-stream',
  });
  
  return uploadResult.file;
}

// Tool handlers
async function analyzeImage(args) {
  const imagePath = args.image_path;
  const prompt = args.prompt || "Describe this image in detail";
  
  const file = await uploadFile(imagePath);
  const result = await model.generateContent([
    prompt,
    { fileData: { fileUri: file.uri, mimeType: file.mimeType }}
  ]);
  
  return result.response.text();
}

async function analyzeMultiple(args) {
  const imagePaths = args.image_paths;
  const prompt = args.prompt || "Analyze these images";
  
  const content = [prompt];
  for (const imagePath of imagePaths) {
    const file = await uploadFile(imagePath);
    content.push({ fileData: { fileUri: file.uri, mimeType: file.mimeType }});
  }
  
  const result = await model.generateContent(content);
  return result.response.text();
}

async function extractText(args) {
  const imagePath = args.image_path;
  const format = args.format || "plain";
  
  const prompts = {
    plain: "Extract and transcribe all text from this image. Return only the text, nothing else.",
    markdown: "Extract all text from this image and format it in markdown, preserving structure.",
    structured: "Extract all text from this image and organize it with clear sections and structure."
  };
  
  const file = await uploadFile(imagePath);
  const result = await model.generateContent([
    prompts[format] || prompts.plain,
    { fileData: { fileUri: file.uri, mimeType: file.mimeType }}
  ]);
  
  return result.response.text();
}

async function compareImages(args) {
  const image1Path = args.image1_path;
  const image2Path = args.image2_path;
  const focus = args.focus || "differences";
  
  const prompts = {
    differences: "Compare these two images and describe all the differences you can find.",
    similarities: "Compare these two images and describe what they have in common.",
    changes: "Describe what has changed between the first and second image."
  };
  
  const [file1, file2] = await Promise.all([
    uploadFile(image1Path),
    uploadFile(image2Path)
  ]);
  
  const result = await model.generateContent([
    prompts[focus] || prompts.differences,
    { fileData: { fileUri: file1.uri, mimeType: file1.mimeType }},
    { fileData: { fileUri: file2.uri, mimeType: file2.mimeType }}
  ]);
  
  return result.response.text();
}

async function suggestFilename(args) {
  const imagePath = args.image_path;
  const maxLength = args.max_length || 60;
  const includeDate = args.include_date || false;
  
  const prompt = `Analyze this image and suggest a descriptive filename for it. 
  Requirements:
  - Maximum ${maxLength} characters (not including extension)
  - Use title case with spaces (will be converted to hyphens)
  - Be specific and descriptive about the content
  - ${includeDate ? 'Include YYYY-MM-DD prefix if a date is visible in the image' : 'Do not include date prefix'}
  - Focus on the main subject or purpose of the image
  - For screenshots: include the application or website name
  - For diagrams: include the type and subject
  - For photos: include the subject and context
  - Return ONLY the filename suggestion, no explanation or extension`;
  
  const file = await uploadFile(imagePath);
  const result = await model.generateContent([
    prompt,
    { fileData: { fileUri: file.uri, mimeType: file.mimeType }}
  ]);
  
  // Clean up the suggestion and format it
  let suggestion = result.response.text().trim();
  // Remove any file extension if accidentally included
  suggestion = suggestion.replace(/\.(png|jpg|jpeg|gif|webp|pdf)$/i, '');
  // Replace spaces with hyphens
  suggestion = suggestion.replace(/\s+/g, ' ').replace(/ /g, ' - ');
  // Ensure it doesn't exceed max length
  if (suggestion.length > maxLength) {
    suggestion = suggestion.substring(0, maxLength).replace(/ - $/, '');
  }
  
  return suggestion;
}

async function analyzeDocument(args) {
  const documentPath = args.document_path;
  const prompt = args.prompt || "Analyze this document and provide a comprehensive summary";
  
  const file = await uploadFile(documentPath);
  const result = await model.generateContent([
    prompt,
    { fileData: { fileUri: file.uri, mimeType: file.mimeType }}
  ]);
  
  return result.response.text();
}

// Create MCP server
const server = new Server(
  { name: "gemini-vision", version: "1.0.0" },
  { capabilities: { tools: {} }}
);

// List available tools
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "analyze_image",
      description: "Analyze an image - transcribe text, describe content, or answer questions",
      inputSchema: {
        type: "object",
        properties: {
          image_path: { type: "string", description: "Path to the image file" },
          prompt: { type: "string", description: "What to do with the image", default: "Describe this image" }
        },
        required: ["image_path"]
      }
    },
    {
      name: "analyze_multiple",
      description: "Analyze multiple images at once",
      inputSchema: {
        type: "object",
        properties: {
          image_paths: { type: "array", items: { type: "string" }, description: "List of image paths" },
          prompt: { type: "string", description: "What to do with the images", default: "Analyze these images" }
        },
        required: ["image_paths"]
      }
    },
    {
      name: "extract_text",
      description: "Extract and transcribe all text from an image (OCR)",
      inputSchema: {
        type: "object",
        properties: {
          image_path: { type: "string", description: "Path to the image file" },
          format: { type: "string", enum: ["plain", "markdown", "structured"], default: "plain" }
        },
        required: ["image_path"]
      }
    },
    {
      name: "compare_images",
      description: "Compare two images and describe differences or similarities",
      inputSchema: {
        type: "object",
        properties: {
          image1_path: { type: "string", description: "Path to first image" },
          image2_path: { type: "string", description: "Path to second image" },
          focus: { type: "string", enum: ["differences", "similarities", "changes"], default: "differences" }
        },
        required: ["image1_path", "image2_path"]
      }
    },
    {
      name: "suggest_image_filename",
      description: "Analyze an image and suggest a descriptive filename (without extension)",
      inputSchema: {
        type: "object",
        properties: {
          image_path: { type: "string", description: "Path to the image file" },
          max_length: { type: "number", description: "Maximum filename length", default: 60 },
          include_date: { type: "boolean", description: "Include date prefix in suggestion", default: false }
        },
        required: ["image_path"]
      }
    },
    {
      name: "analyze_document",
      description: "Analyze a PDF or document with custom prompts - extract specific information, find mentions of topics, summarize sections, etc.",
      inputSchema: {
        type: "object",
        properties: {
          document_path: { type: "string", description: "Path to the document file (PDF, DOC, DOCX, ODT, RTF, TXT)" },
          prompt: { type: "string", description: "What to analyze or extract from the document", default: "Analyze this document and provide a comprehensive summary" }
        },
        required: ["document_path"]
      }
    }
  ]
}));

// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  
  try {
    let result;
    switch (name) {
      case "analyze_image":
        result = await analyzeImage(args);
        break;
      case "analyze_multiple":
        result = await analyzeMultiple(args);
        break;
      case "extract_text":
        result = await extractText(args);
        break;
      case "compare_images":
        result = await compareImages(args);
        break;
      case "suggest_image_filename":
        result = await suggestFilename(args);
        break;
      case "analyze_document":
        result = await analyzeDocument(args);
        break;
      default:
        throw new Error(`Unknown tool: ${name}`);
    }
    
    return {
      content: [{ type: "text", text: result }]
    };
  } catch (error) {
    throw new Error(`Tool execution failed: ${error.message}`);
  }
});

// Start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("🚀 Gemini Vision MCP Server running");
}

main().catch(console.error);