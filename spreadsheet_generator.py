import pandas as pd

# Data for the first pair of columns (key-value pair)
data = {
    'name': ['Method', 'Ref', 'Epoch', 'Encoder', 'Dataset', 'Base LR', 'Warm Up', 'Epochs', 'Filters', 
             'Framework', 'Methods', 'Backbone', 'Batch Size', 'Data', 'Token', 'Image Size', 'Pre-training Dataset', 
             'Model', 'Pre-training Epochs', 'Methodology', 'α', 'Loss Function', 'Method (Local-only)', 'BASE', 
             'Metric', 'Baseline', 'LLFI', 'Filter', 'PPG', 'Num', 'Params(K)', 'FLOPs(M)', 'Technique', 'Modality', 
             'Version', 'Prompt', 'Type', 'Prompts', 'Network', 'Network Architecture', 'Augmentation Method', 'Class', 
             'Specimen', 'IoU_input', 'Parameters', 'Model Variant', '#Params', 'GFLOPs', 'GMACs', 'Memory (GB)', 'Task', 
             'Grid Size', 'Prompt Strategy', 'Prompt Type', 'Box Type', 'Detector', 'Imp.surf.', 'Building', 'Lowveg.', 
             'Tree', 'Car', 'CVSSBlock', 'MFMSBlock', 'SS2D', 'CS2D', 'Params(Mb)', 'FLOPs(Gbps)', 'Local Branch', 
             'Residual Block', 'Multi-Scale', 'Multi-Frequency', 'Adaptive 1D Conv', 'FC', 'shiftfraction', 'channels', 
             'matching', 'Preprocessing', 'Input size', 'Optimizer', 'Batch size', 'Training epochs or iterations', 
             'Learning rate', 'Dimension of z', 'β', 'γ', 'N', 'T', 'Execution manner'],
    'occurrences': [1191, 21, 21, 21, 1177, 30, 30, 15, 4, 4, 18, 15, 12, 13, 13, 13, 13, 835, 2, 6, 9, 6, 60, 176, 352, 6, 
                    6, 6, 6, 7, 7, 7, 142, 234, 28, 48, 56, 56, 105, 105, 105, 122, 80, 80, 3, 3, 15, 15, 15, 54, 54, 54, 18, 
                    90, 60, 224, 50, 50, 50, 50, 12, 12, 2, 2, 16, 16, 4, 4, 9, 9, 9, 9, 52, 52, 52, 3, 3, 3, 3, 3, 3, 3, 3, 
                    3, 3, 3, 3, 3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to a spreadsheet
file_path = "data_stats/key_name_pair.xlsx"
df.to_excel(file_path, index=False)

file_path