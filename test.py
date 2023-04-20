import torchvision
from torchinfo.torchinfo import summary
from torchinfo.write_table import write_table

def main():
  model_stat = summary(
      torchvision.models.segmentation.fcn_resnet101(),
      (1, 3, 224, 224),
      depth=10,
      verbose=1,
      col_names=["kernel_size","input_size", "output_size", "num_params", "mult_adds"],
      row_settings=["depth"],
    )
  
  model_layers_table = model_stat.layers_table
  write_table(model_layers_table, 'test-param.xlsx', 'fcn_resnet101')

if __name__ == "__main__":
    main()
