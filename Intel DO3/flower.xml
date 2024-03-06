<?xml version="1.0"?>
<net name="TensorFlow_Frontend_IR" version="11">
	<layers>
		<layer id="0" name="resnet50_input" type="Parameter" version="opset1">
			<data shape="1,180,180,3" element_type="f32" />
			<rt_info>
				<attribute name="old_api_map_element_type" version="0" value="f16" />
			</rt_info>
			<output>
				<port id="0" precision="FP32" names="resnet50_input">
					<dim>1</dim>
					<dim>180</dim>
					<dim>180</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="1" name="Constant_7260" type="Const" version="opset1">
			<data element_type="i64" shape="4" offset="0" size="32" />
			<output>
				<port id="0" precision="I64">
					<dim>4</dim>
				</port>
			</output>
		</layer>
		<layer id="2" name="Transpose_7261" type="Transpose" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>180</dim>
					<dim>180</dim>
					<dim>3</dim>
				</port>
				<port id="1" precision="I64">
					<dim>4</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>3</dim>
					<dim>180</dim>
					<dim>180</dim>
				</port>
			</output>
		</layer>
		<layer id="3" name="Multiply_9574_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="64, 3, 7, 7" offset="32" size="18816" />
			<output>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>3</dim>
					<dim>7</dim>
					<dim>7</dim>
				</port>
			</output>
		</layer>
		<layer id="4" name="Multiply_9574" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>3</dim>
					<dim>7</dim>
					<dim>7</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>3</dim>
					<dim>7</dim>
					<dim>7</dim>
				</port>
			</output>
		</layer>
		<layer id="5" name="Multiply_8834" type="Convolution" version="opset1">
			<data strides="2, 2" dilations="1, 1" pads_begin="3, 3" pads_end="3, 3" auto_pad="explicit" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>3</dim>
					<dim>180</dim>
					<dim>180</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>3</dim>
					<dim>7</dim>
					<dim>7</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>90</dim>
					<dim>90</dim>
				</port>
			</output>
		</layer>
		<layer id="6" name="Constant_8842_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 64, 1, 1" offset="18848" size="128" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="7" name="Constant_8842" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="8" name="Transpose_2196" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>90</dim>
					<dim>90</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>90</dim>
					<dim>90</dim>
				</port>
			</output>
		</layer>
		<layer id="9" name="Transpose_2198" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>90</dim>
					<dim>90</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>90</dim>
					<dim>90</dim>
				</port>
			</output>
		</layer>
		<layer id="10" name="Gather_2201" type="Const" version="opset1">
			<data element_type="i64" shape="4" offset="18976" size="32" />
			<rt_info>
				<attribute name="precise" version="0" />
			</rt_info>
			<output>
				<port id="0" precision="I64">
					<dim>4</dim>
				</port>
			</output>
		</layer>
		<layer id="11" name="Gather_2203" type="Const" version="opset1">
			<data element_type="i64" shape="4" offset="18976" size="32" />
			<rt_info>
				<attribute name="precise" version="0" />
			</rt_info>
			<output>
				<port id="0" precision="I64">
					<dim>4</dim>
				</port>
			</output>
		</layer>
		<layer id="12" name="Constant_347_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="" offset="19008" size="2" />
			<output>
				<port id="0" precision="FP16" />
			</output>
		</layer>
		<layer id="13" name="Constant_347" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16" />
			</input>
			<output>
				<port id="1" precision="FP32" />
			</output>
		</layer>
		<layer id="14" name="Transpose_2213" type="Pad" version="opset1">
			<data pad_mode="constant" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>90</dim>
					<dim>90</dim>
				</port>
				<port id="1" precision="I64">
					<dim>4</dim>
				</port>
				<port id="2" precision="I64">
					<dim>4</dim>
				</port>
				<port id="3" precision="FP32" />
			</input>
			<output>
				<port id="4" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>92</dim>
					<dim>92</dim>
				</port>
			</output>
		</layer>
		<layer id="15" name="MaxPool_365" type="MaxPool" version="opset8">
			<data strides="2, 2" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" kernel="3, 3" rounding_type="floor" auto_pad="valid" index_element_type="i64" axis="0" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>92</dim>
					<dim>92</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="2" precision="I64">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="16" name="Multiply_9578_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 64, 1, 1" offset="19010" size="32768" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="17" name="Multiply_9578" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="18" name="Multiply_8848" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="19" name="Constant_8856_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="51778" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="20" name="Constant_8856" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="21" name="Transpose_2271" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="22" name="Multiply_9582_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="64, 64, 1, 1" offset="52290" size="8192" />
			<output>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="23" name="Multiply_9582" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="24" name="Multiply_8862" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="25" name="Constant_8870_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 64, 1, 1" offset="60482" size="128" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="26" name="Constant_8870" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="27" name="Transpose_2329" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="28" name="Transpose_2331" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="29" name="Multiply_9586_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="64, 64, 3, 3" offset="60610" size="73728" />
			<output>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>64</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="30" name="Multiply_9586" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>64</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>64</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="31" name="Multiply_8876" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>64</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="32" name="Constant_8884_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 64, 1, 1" offset="134338" size="128" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="33" name="Constant_8884" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="34" name="Transpose_2389" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="35" name="Transpose_2391" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="36" name="Multiply_9590_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 64, 1, 1" offset="134466" size="32768" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="37" name="Multiply_9590" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="38" name="Multiply_8890" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="39" name="Constant_8898_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="167234" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="40" name="Constant_8898" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="41" name="Transpose_2449" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="42" name="Transpose_2453" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="43" name="Transpose_2455" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="44" name="Multiply_9594_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="64, 256, 1, 1" offset="167746" size="32768" />
			<output>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="45" name="Multiply_9594" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="46" name="Multiply_8904" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="47" name="Constant_8912_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 64, 1, 1" offset="200514" size="128" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="48" name="Constant_8912" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="49" name="Transpose_2513" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="50" name="Transpose_2515" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="51" name="Multiply_9598_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="64, 64, 3, 3" offset="200642" size="73728" />
			<output>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>64</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="52" name="Multiply_9598" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>64</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>64</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="53" name="Multiply_8918" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>64</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="54" name="Constant_8926_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 64, 1, 1" offset="274370" size="128" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="55" name="Constant_8926" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="56" name="Transpose_2573" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="57" name="Transpose_2575" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="58" name="Multiply_9602_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 64, 1, 1" offset="274498" size="32768" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="59" name="Multiply_9602" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="60" name="Multiply_8932" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="61" name="Constant_8940_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="307266" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="62" name="Constant_8940" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="63" name="Transpose_2633" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="64" name="Transpose_2637" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="65" name="Transpose_2639" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="66" name="Multiply_9606_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="64, 256, 1, 1" offset="307778" size="32768" />
			<output>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="67" name="Multiply_9606" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="68" name="Multiply_8946" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="69" name="Constant_8954_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 64, 1, 1" offset="340546" size="128" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="70" name="Constant_8954" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="71" name="Transpose_2697" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="72" name="Transpose_2699" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="73" name="Multiply_9610_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="64, 64, 3, 3" offset="340674" size="73728" />
			<output>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>64</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="74" name="Multiply_9610" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>64</dim>
					<dim>64</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>64</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="75" name="Multiply_8960" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>64</dim>
					<dim>64</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="76" name="Constant_8968_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 64, 1, 1" offset="414402" size="128" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="77" name="Constant_8968" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="78" name="Transpose_2757" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="79" name="Transpose_2759" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="80" name="Multiply_9614_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 64, 1, 1" offset="414530" size="32768" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="81" name="Multiply_9614" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="82" name="Multiply_8974" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>64</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>64</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="83" name="Constant_8982_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="447298" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="84" name="Constant_8982" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="85" name="Transpose_2817" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="86" name="Transpose_2821" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="87" name="Transpose_2823" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
			</output>
		</layer>
		<layer id="88" name="Multiply_9618_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="512, 256, 1, 1" offset="447810" size="262144" />
			<output>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="89" name="Multiply_9618" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="90" name="Multiply_8988" type="Convolution" version="opset1">
			<data strides="2, 2" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="91" name="Constant_8996_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 512, 1, 1" offset="709954" size="1024" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="92" name="Constant_8996" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="93" name="Transpose_2881" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="94" name="Multiply_9622_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="128, 256, 1, 1" offset="710978" size="65536" />
			<output>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="95" name="Multiply_9622" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="96" name="Multiply_9002" type="Convolution" version="opset1">
			<data strides="2, 2" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>45</dim>
					<dim>45</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="97" name="Constant_9010_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 128, 1, 1" offset="776514" size="256" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="98" name="Constant_9010" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="99" name="Transpose_2939" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="100" name="Transpose_2941" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="101" name="Multiply_9626_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="128, 128, 3, 3" offset="776770" size="294912" />
			<output>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="102" name="Multiply_9626" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="103" name="Multiply_9016" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="104" name="Constant_9024_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 128, 1, 1" offset="1071682" size="256" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="105" name="Constant_9024" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="106" name="Transpose_2999" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="107" name="Transpose_3001" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="108" name="Multiply_9630_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="512, 128, 1, 1" offset="1071938" size="131072" />
			<output>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="109" name="Multiply_9630" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="110" name="Multiply_9030" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="111" name="Constant_9038_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 512, 1, 1" offset="1203010" size="1024" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="112" name="Constant_9038" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="113" name="Transpose_3059" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="114" name="Transpose_3063" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="115" name="Transpose_3065" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="116" name="Multiply_9634_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="128, 512, 1, 1" offset="1204034" size="131072" />
			<output>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="117" name="Multiply_9634" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="118" name="Multiply_9044" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="119" name="Constant_9052_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 128, 1, 1" offset="1335106" size="256" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="120" name="Constant_9052" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="121" name="Transpose_3123" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="122" name="Transpose_3125" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="123" name="Multiply_9638_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="128, 128, 3, 3" offset="1335362" size="294912" />
			<output>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="124" name="Multiply_9638" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="125" name="Multiply_9058" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="126" name="Constant_9066_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 128, 1, 1" offset="1630274" size="256" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="127" name="Constant_9066" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="128" name="Transpose_3183" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="129" name="Transpose_3185" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="130" name="Multiply_9642_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="512, 128, 1, 1" offset="1630530" size="131072" />
			<output>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="131" name="Multiply_9642" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="132" name="Multiply_9072" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="133" name="Constant_9080_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 512, 1, 1" offset="1761602" size="1024" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="134" name="Constant_9080" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="135" name="Transpose_3243" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="136" name="Transpose_3247" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="137" name="Transpose_3249" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="138" name="Multiply_9646_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="128, 512, 1, 1" offset="1762626" size="131072" />
			<output>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="139" name="Multiply_9646" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="140" name="Multiply_9086" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="141" name="Constant_9094_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 128, 1, 1" offset="1893698" size="256" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="142" name="Constant_9094" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="143" name="Transpose_3307" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="144" name="Transpose_3309" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="145" name="Multiply_9650_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="128, 128, 3, 3" offset="1893954" size="294912" />
			<output>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="146" name="Multiply_9650" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="147" name="Multiply_9100" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="148" name="Constant_9108_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 128, 1, 1" offset="2188866" size="256" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="149" name="Constant_9108" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="150" name="Transpose_3367" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="151" name="Transpose_3369" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="152" name="Multiply_9654_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="512, 128, 1, 1" offset="2189122" size="131072" />
			<output>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="153" name="Multiply_9654" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="154" name="Multiply_9114" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="155" name="Constant_9122_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 512, 1, 1" offset="2320194" size="1024" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="156" name="Constant_9122" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="157" name="Transpose_3427" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="158" name="Transpose_3431" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="159" name="Transpose_3433" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="160" name="Multiply_9658_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="128, 512, 1, 1" offset="2321218" size="131072" />
			<output>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="161" name="Multiply_9658" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="162" name="Multiply_9128" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="163" name="Constant_9136_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 128, 1, 1" offset="2452290" size="256" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="164" name="Constant_9136" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="165" name="Transpose_3491" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="166" name="Transpose_3493" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="167" name="Multiply_9662_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="128, 128, 3, 3" offset="2452546" size="294912" />
			<output>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="168" name="Multiply_9662" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="169" name="Multiply_9142" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>128</dim>
					<dim>128</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="170" name="Constant_9150_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 128, 1, 1" offset="2747458" size="256" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="171" name="Constant_9150" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="172" name="Transpose_3551" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="173" name="Transpose_3553" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="174" name="Multiply_9666_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="512, 128, 1, 1" offset="2747714" size="131072" />
			<output>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="175" name="Multiply_9666" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="176" name="Multiply_9156" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>128</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>128</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="177" name="Constant_9164_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 512, 1, 1" offset="2878786" size="1024" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="178" name="Constant_9164" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="179" name="Transpose_3611" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="180" name="Transpose_3615" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="181" name="Transpose_3617" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
			</output>
		</layer>
		<layer id="182" name="Multiply_9670_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1024, 512, 1, 1" offset="2879810" size="1048576" />
			<output>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="183" name="Multiply_9670" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="184" name="Multiply_9170" type="Convolution" version="opset1">
			<data strides="2, 2" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="185" name="Constant_9178_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 1024, 1, 1" offset="3928386" size="2048" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="186" name="Constant_9178" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="187" name="Transpose_3675" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="188" name="Multiply_9674_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 512, 1, 1" offset="3930434" size="262144" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="189" name="Multiply_9674" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="190" name="Multiply_9184" type="Convolution" version="opset1">
			<data strides="2, 2" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>23</dim>
					<dim>23</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="191" name="Constant_9192_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="4192578" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="192" name="Constant_9192" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="193" name="Transpose_3733" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="194" name="Transpose_3735" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="195" name="Multiply_9678_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 256, 3, 3" offset="4193090" size="1179648" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="196" name="Multiply_9678" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="197" name="Multiply_9198" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="198" name="Constant_9206_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="5372738" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="199" name="Constant_9206" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="200" name="Transpose_3793" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="201" name="Transpose_3795" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="202" name="Multiply_9682_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1024, 256, 1, 1" offset="5373250" size="524288" />
			<output>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="203" name="Multiply_9682" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="204" name="Multiply_9212" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="205" name="Constant_9220_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 1024, 1, 1" offset="5897538" size="2048" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="206" name="Constant_9220" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="207" name="Transpose_3853" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="208" name="Transpose_3857" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="209" name="Transpose_3859" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="210" name="Multiply_9686_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 1024, 1, 1" offset="5899586" size="524288" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="211" name="Multiply_9686" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="212" name="Multiply_9226" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="213" name="Constant_9234_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="6423874" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="214" name="Constant_9234" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="215" name="Transpose_3917" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="216" name="Transpose_3919" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="217" name="Multiply_9690_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 256, 3, 3" offset="6424386" size="1179648" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="218" name="Multiply_9690" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="219" name="Multiply_9240" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="220" name="Constant_9248_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="7604034" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="221" name="Constant_9248" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="222" name="Transpose_3977" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="223" name="Transpose_3979" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="224" name="Multiply_9694_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1024, 256, 1, 1" offset="7604546" size="524288" />
			<output>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="225" name="Multiply_9694" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="226" name="Multiply_9254" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="227" name="Constant_9262_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 1024, 1, 1" offset="8128834" size="2048" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="228" name="Constant_9262" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="229" name="Transpose_4037" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="230" name="Transpose_4041" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="231" name="Transpose_4043" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="232" name="Multiply_9698_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 1024, 1, 1" offset="8130882" size="524288" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="233" name="Multiply_9698" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="234" name="Multiply_9268" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="235" name="Constant_9276_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="8655170" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="236" name="Constant_9276" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="237" name="Transpose_4101" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="238" name="Transpose_4103" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="239" name="Multiply_9702_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 256, 3, 3" offset="8655682" size="1179648" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="240" name="Multiply_9702" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="241" name="Multiply_9282" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="242" name="Constant_9290_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="9835330" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="243" name="Constant_9290" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="244" name="Transpose_4161" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="245" name="Transpose_4163" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="246" name="Multiply_9706_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1024, 256, 1, 1" offset="9835842" size="524288" />
			<output>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="247" name="Multiply_9706" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="248" name="Multiply_9296" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="249" name="Constant_9304_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 1024, 1, 1" offset="10360130" size="2048" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="250" name="Constant_9304" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="251" name="Transpose_4221" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="252" name="Transpose_4225" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="253" name="Transpose_4227" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="254" name="Multiply_9710_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 1024, 1, 1" offset="10362178" size="524288" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="255" name="Multiply_9710" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="256" name="Multiply_9310" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="257" name="Constant_9318_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="10886466" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="258" name="Constant_9318" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="259" name="Transpose_4285" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="260" name="Transpose_4287" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="261" name="Multiply_9714_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 256, 3, 3" offset="10886978" size="1179648" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="262" name="Multiply_9714" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="263" name="Multiply_9324" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="264" name="Constant_9332_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="12066626" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="265" name="Constant_9332" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="266" name="Transpose_4345" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="267" name="Transpose_4347" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="268" name="Multiply_9718_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1024, 256, 1, 1" offset="12067138" size="524288" />
			<output>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="269" name="Multiply_9718" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="270" name="Multiply_9338" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="271" name="Constant_9346_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 1024, 1, 1" offset="12591426" size="2048" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="272" name="Constant_9346" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="273" name="Transpose_4405" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="274" name="Transpose_4409" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="275" name="Transpose_4411" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="276" name="Multiply_9722_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 1024, 1, 1" offset="12593474" size="524288" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="277" name="Multiply_9722" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="278" name="Multiply_9352" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="279" name="Constant_9360_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="13117762" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="280" name="Constant_9360" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="281" name="Transpose_4469" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="282" name="Transpose_4471" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="283" name="Multiply_9726_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 256, 3, 3" offset="13118274" size="1179648" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="284" name="Multiply_9726" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="285" name="Multiply_9366" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="286" name="Constant_9374_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="14297922" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="287" name="Constant_9374" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="288" name="Transpose_4529" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="289" name="Transpose_4531" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="290" name="Multiply_9730_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1024, 256, 1, 1" offset="14298434" size="524288" />
			<output>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="291" name="Multiply_9730" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="292" name="Multiply_9380" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="293" name="Constant_9388_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 1024, 1, 1" offset="14822722" size="2048" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="294" name="Constant_9388" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="295" name="Transpose_4589" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="296" name="Transpose_4593" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="297" name="Transpose_4595" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="298" name="Multiply_9734_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 1024, 1, 1" offset="14824770" size="524288" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="299" name="Multiply_9734" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="300" name="Multiply_9394" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="301" name="Constant_9402_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="15349058" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="302" name="Constant_9402" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="303" name="Transpose_4653" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="304" name="Transpose_4655" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="305" name="Multiply_9738_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="256, 256, 3, 3" offset="15349570" size="1179648" />
			<output>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="306" name="Multiply_9738" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="307" name="Multiply_9408" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>256</dim>
					<dim>256</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="308" name="Constant_9416_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 256, 1, 1" offset="16529218" size="512" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="309" name="Constant_9416" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="310" name="Transpose_4713" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="311" name="Transpose_4715" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="312" name="Multiply_9742_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1024, 256, 1, 1" offset="16529730" size="524288" />
			<output>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="313" name="Multiply_9742" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="314" name="Multiply_9422" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>256</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1024</dim>
					<dim>256</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="315" name="Constant_9430_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 1024, 1, 1" offset="17054018" size="2048" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="316" name="Constant_9430" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="317" name="Transpose_4773" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="318" name="Transpose_4777" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="319" name="Transpose_4779" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
			</output>
		</layer>
		<layer id="320" name="Multiply_9746_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="2048, 1024, 1, 1" offset="17056066" size="4194304" />
			<output>
				<port id="0" precision="FP16">
					<dim>2048</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="321" name="Multiply_9746" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>2048</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>2048</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="322" name="Multiply_9436" type="Convolution" version="opset1">
			<data strides="2, 2" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>2048</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="323" name="Constant_9444_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 2048, 1, 1" offset="21250370" size="4096" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="324" name="Constant_9444" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="325" name="Transpose_4837" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="326" name="Multiply_9750_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="512, 1024, 1, 1" offset="21254466" size="1048576" />
			<output>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="327" name="Multiply_9750" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="328" name="Multiply_9450" type="Convolution" version="opset1">
			<data strides="2, 2" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>1024</dim>
					<dim>12</dim>
					<dim>12</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>1024</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="329" name="Constant_9458_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 512, 1, 1" offset="22303042" size="1024" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="330" name="Constant_9458" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="331" name="Transpose_4895" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="332" name="Transpose_4897" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="333" name="Multiply_9754_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="512, 512, 3, 3" offset="22304066" size="4718592" />
			<output>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>512</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="334" name="Multiply_9754" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>512</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>512</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="335" name="Multiply_9464" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>512</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="336" name="Constant_9472_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 512, 1, 1" offset="27022658" size="1024" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="337" name="Constant_9472" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="338" name="Transpose_4955" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="339" name="Transpose_4957" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="340" name="Multiply_9758_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="2048, 512, 1, 1" offset="27023682" size="2097152" />
			<output>
				<port id="0" precision="FP16">
					<dim>2048</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="341" name="Multiply_9758" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>2048</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>2048</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="342" name="Multiply_9478" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>2048</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="343" name="Constant_9486_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 2048, 1, 1" offset="29120834" size="4096" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="344" name="Constant_9486" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="345" name="Transpose_5015" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="346" name="Transpose_5019" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="347" name="Transpose_5021" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="348" name="Multiply_9762_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="512, 2048, 1, 1" offset="29124930" size="2097152" />
			<output>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="349" name="Multiply_9762" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="350" name="Multiply_9492" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="351" name="Constant_9500_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 512, 1, 1" offset="31222082" size="1024" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="352" name="Constant_9500" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="353" name="Transpose_5079" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="354" name="Transpose_5081" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="355" name="Multiply_9766_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="512, 512, 3, 3" offset="31223106" size="4718592" />
			<output>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>512</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="356" name="Multiply_9766" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>512</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>512</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="357" name="Multiply_9506" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>512</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="358" name="Constant_9514_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 512, 1, 1" offset="35941698" size="1024" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="359" name="Constant_9514" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="360" name="Transpose_5139" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="361" name="Transpose_5141" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="362" name="Multiply_9770_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="2048, 512, 1, 1" offset="35942722" size="2097152" />
			<output>
				<port id="0" precision="FP16">
					<dim>2048</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="363" name="Multiply_9770" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>2048</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>2048</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="364" name="Multiply_9520" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>2048</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="365" name="Constant_9528_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 2048, 1, 1" offset="38039874" size="4096" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="366" name="Constant_9528" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="367" name="Transpose_5199" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="368" name="Transpose_5203" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="369" name="Transpose_5205" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="370" name="Multiply_9774_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="512, 2048, 1, 1" offset="38043970" size="2097152" />
			<output>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="371" name="Multiply_9774" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="372" name="Multiply_9534" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="373" name="Constant_9542_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 512, 1, 1" offset="40141122" size="1024" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="374" name="Constant_9542" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="375" name="Transpose_5263" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="376" name="Transpose_5265" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="377" name="Multiply_9778_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="512, 512, 3, 3" offset="40142146" size="4718592" />
			<output>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>512</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="378" name="Multiply_9778" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>512</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>512</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</output>
		</layer>
		<layer id="379" name="Multiply_9548" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="same_upper" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>512</dim>
					<dim>3</dim>
					<dim>3</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="380" name="Constant_9556_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 512, 1, 1" offset="44860738" size="1024" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="381" name="Constant_9556" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="382" name="Transpose_5323" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="383" name="Transpose_5325" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="384" name="Multiply_9782_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="2048, 512, 1, 1" offset="44861762" size="2097152" />
			<output>
				<port id="0" precision="FP16">
					<dim>2048</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="385" name="Multiply_9782" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>2048</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>2048</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="386" name="Multiply_9562" type="Convolution" version="opset1">
			<data strides="1, 1" dilations="1, 1" pads_begin="0, 0" pads_end="0, 0" auto_pad="valid" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>2048</dim>
					<dim>512</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="387" name="Constant_9570_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 2048, 1, 1" offset="46958914" size="4096" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="388" name="Constant_9570" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</output>
		</layer>
		<layer id="389" name="Transpose_5383" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>1</dim>
					<dim>1</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="390" name="Transpose_5387" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="391" name="Transpose_5389" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
			</output>
		</layer>
		<layer id="392" name="Constant_5388" type="Const" version="opset1">
			<data element_type="i64" shape="4" offset="46963010" size="32" />
			<output>
				<port id="0" precision="I64">
					<dim>4</dim>
				</port>
			</output>
		</layer>
		<layer id="393" name="sequential/resnet50/conv5_block3_out/Relu" type="Transpose" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>2048</dim>
					<dim>6</dim>
					<dim>6</dim>
				</port>
				<port id="1" precision="I64">
					<dim>4</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32" names="sequential/resnet50/conv5_block3_out/Relu,sequential/resnet50/conv5_block3_out/Relu:0">
					<dim>1</dim>
					<dim>6</dim>
					<dim>6</dim>
					<dim>2048</dim>
				</port>
			</output>
		</layer>
		<layer id="394" name="sequential/flatten/Const" type="Const" version="opset1">
			<data element_type="i64" shape="2" offset="46963042" size="16" />
			<rt_info>
				<attribute name="precise" version="0" />
			</rt_info>
			<output>
				<port id="0" precision="I64" names="sequential/flatten/Const,sequential/flatten/Const:0">
					<dim>2</dim>
				</port>
			</output>
		</layer>
		<layer id="395" name="sequential/flatten/Reshape" type="Reshape" version="opset1">
			<data special_zero="false" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>6</dim>
					<dim>6</dim>
					<dim>2048</dim>
				</port>
				<port id="1" precision="I64">
					<dim>2</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32" names="sequential/flatten/Reshape,sequential/flatten/Reshape:0">
					<dim>1</dim>
					<dim>73728</dim>
				</port>
			</output>
		</layer>
		<layer id="396" name="Transpose_8398_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="512, 73728" offset="46963058" size="75497472" />
			<output>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>73728</dim>
				</port>
			</output>
		</layer>
		<layer id="397" name="Transpose_8398" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>512</dim>
					<dim>73728</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>73728</dim>
				</port>
			</output>
		</layer>
		<layer id="398" name="sequential/dense/MatMul" type="MatMul" version="opset1">
			<data transpose_a="false" transpose_b="true" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>73728</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>512</dim>
					<dim>73728</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32" names="sequential/dense/MatMul,sequential/dense/MatMul:0">
					<dim>1</dim>
					<dim>512</dim>
				</port>
			</output>
		</layer>
		<layer id="399" name="Constant_9956_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 512" offset="122460530" size="1024" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
				</port>
			</output>
		</layer>
		<layer id="400" name="Constant_9956" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>512</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
				</port>
			</output>
		</layer>
		<layer id="401" name="sequential/dense/BiasAdd" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32" names="sequential/dense/BiasAdd,sequential/dense/BiasAdd:0">
					<dim>1</dim>
					<dim>512</dim>
				</port>
			</output>
		</layer>
		<layer id="402" name="sequential/dense/Relu" type="ReLU" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32" names="sequential/dense/Relu,sequential/dense/Relu:0">
					<dim>1</dim>
					<dim>512</dim>
				</port>
			</output>
		</layer>
		<layer id="403" name="Transpose_8401_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="5, 512" offset="122461554" size="5120" />
			<output>
				<port id="0" precision="FP16">
					<dim>5</dim>
					<dim>512</dim>
				</port>
			</output>
		</layer>
		<layer id="404" name="Transpose_8401" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>5</dim>
					<dim>512</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>5</dim>
					<dim>512</dim>
				</port>
			</output>
		</layer>
		<layer id="405" name="sequential/dense_1/MatMul" type="MatMul" version="opset1">
			<data transpose_a="false" transpose_b="true" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>512</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>5</dim>
					<dim>512</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32" names="sequential/dense_1/MatMul,sequential/dense_1/MatMul:0">
					<dim>1</dim>
					<dim>5</dim>
				</port>
			</output>
		</layer>
		<layer id="406" name="Constant_9957_compressed" type="Const" version="opset1">
			<data element_type="f16" shape="1, 5" offset="122466674" size="10" />
			<output>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>5</dim>
				</port>
			</output>
		</layer>
		<layer id="407" name="Constant_9957" type="Convert" version="opset1">
			<data destination_type="f32" />
			<rt_info>
				<attribute name="decompression" version="0" />
			</rt_info>
			<input>
				<port id="0" precision="FP16">
					<dim>1</dim>
					<dim>5</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>5</dim>
				</port>
			</output>
		</layer>
		<layer id="408" name="sequential/dense_1/BiasAdd" type="Add" version="opset1">
			<data auto_broadcast="numpy" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>5</dim>
				</port>
				<port id="1" precision="FP32">
					<dim>1</dim>
					<dim>5</dim>
				</port>
			</input>
			<output>
				<port id="2" precision="FP32" names="sequential/dense_1/BiasAdd,sequential/dense_1/BiasAdd:0">
					<dim>1</dim>
					<dim>5</dim>
				</port>
			</output>
		</layer>
		<layer id="409" name="sequential/dense_1/Softmax" type="SoftMax" version="opset8">
			<data axis="-1" />
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>5</dim>
				</port>
			</input>
			<output>
				<port id="1" precision="FP32" names="dense_1/Softmax:0">
					<dim>1</dim>
					<dim>5</dim>
				</port>
			</output>
		</layer>
		<layer id="410" name="dense_1/Softmax:0" type="Result" version="opset1">
			<input>
				<port id="0" precision="FP32">
					<dim>1</dim>
					<dim>5</dim>
				</port>
			</input>
		</layer>
	</layers>
	<edges>
		<edge from-layer="0" from-port="0" to-layer="2" to-port="0" />
		<edge from-layer="1" from-port="0" to-layer="2" to-port="1" />
		<edge from-layer="2" from-port="2" to-layer="5" to-port="0" />
		<edge from-layer="3" from-port="0" to-layer="4" to-port="0" />
		<edge from-layer="4" from-port="1" to-layer="5" to-port="1" />
		<edge from-layer="5" from-port="2" to-layer="8" to-port="0" />
		<edge from-layer="6" from-port="0" to-layer="7" to-port="0" />
		<edge from-layer="7" from-port="1" to-layer="8" to-port="1" />
		<edge from-layer="8" from-port="2" to-layer="9" to-port="0" />
		<edge from-layer="9" from-port="1" to-layer="14" to-port="0" />
		<edge from-layer="10" from-port="0" to-layer="14" to-port="1" />
		<edge from-layer="11" from-port="0" to-layer="14" to-port="2" />
		<edge from-layer="12" from-port="0" to-layer="13" to-port="0" />
		<edge from-layer="13" from-port="1" to-layer="14" to-port="3" />
		<edge from-layer="14" from-port="4" to-layer="15" to-port="0" />
		<edge from-layer="15" from-port="1" to-layer="18" to-port="0" />
		<edge from-layer="15" from-port="1" to-layer="24" to-port="0" />
		<edge from-layer="16" from-port="0" to-layer="17" to-port="0" />
		<edge from-layer="17" from-port="1" to-layer="18" to-port="1" />
		<edge from-layer="18" from-port="2" to-layer="21" to-port="0" />
		<edge from-layer="19" from-port="0" to-layer="20" to-port="0" />
		<edge from-layer="20" from-port="1" to-layer="21" to-port="1" />
		<edge from-layer="21" from-port="2" to-layer="42" to-port="0" />
		<edge from-layer="22" from-port="0" to-layer="23" to-port="0" />
		<edge from-layer="23" from-port="1" to-layer="24" to-port="1" />
		<edge from-layer="24" from-port="2" to-layer="27" to-port="0" />
		<edge from-layer="25" from-port="0" to-layer="26" to-port="0" />
		<edge from-layer="26" from-port="1" to-layer="27" to-port="1" />
		<edge from-layer="27" from-port="2" to-layer="28" to-port="0" />
		<edge from-layer="28" from-port="1" to-layer="31" to-port="0" />
		<edge from-layer="29" from-port="0" to-layer="30" to-port="0" />
		<edge from-layer="30" from-port="1" to-layer="31" to-port="1" />
		<edge from-layer="31" from-port="2" to-layer="34" to-port="0" />
		<edge from-layer="32" from-port="0" to-layer="33" to-port="0" />
		<edge from-layer="33" from-port="1" to-layer="34" to-port="1" />
		<edge from-layer="34" from-port="2" to-layer="35" to-port="0" />
		<edge from-layer="35" from-port="1" to-layer="38" to-port="0" />
		<edge from-layer="36" from-port="0" to-layer="37" to-port="0" />
		<edge from-layer="37" from-port="1" to-layer="38" to-port="1" />
		<edge from-layer="38" from-port="2" to-layer="41" to-port="0" />
		<edge from-layer="39" from-port="0" to-layer="40" to-port="0" />
		<edge from-layer="40" from-port="1" to-layer="41" to-port="1" />
		<edge from-layer="41" from-port="2" to-layer="42" to-port="1" />
		<edge from-layer="42" from-port="2" to-layer="43" to-port="0" />
		<edge from-layer="43" from-port="1" to-layer="64" to-port="0" />
		<edge from-layer="43" from-port="1" to-layer="46" to-port="0" />
		<edge from-layer="44" from-port="0" to-layer="45" to-port="0" />
		<edge from-layer="45" from-port="1" to-layer="46" to-port="1" />
		<edge from-layer="46" from-port="2" to-layer="49" to-port="0" />
		<edge from-layer="47" from-port="0" to-layer="48" to-port="0" />
		<edge from-layer="48" from-port="1" to-layer="49" to-port="1" />
		<edge from-layer="49" from-port="2" to-layer="50" to-port="0" />
		<edge from-layer="50" from-port="1" to-layer="53" to-port="0" />
		<edge from-layer="51" from-port="0" to-layer="52" to-port="0" />
		<edge from-layer="52" from-port="1" to-layer="53" to-port="1" />
		<edge from-layer="53" from-port="2" to-layer="56" to-port="0" />
		<edge from-layer="54" from-port="0" to-layer="55" to-port="0" />
		<edge from-layer="55" from-port="1" to-layer="56" to-port="1" />
		<edge from-layer="56" from-port="2" to-layer="57" to-port="0" />
		<edge from-layer="57" from-port="1" to-layer="60" to-port="0" />
		<edge from-layer="58" from-port="0" to-layer="59" to-port="0" />
		<edge from-layer="59" from-port="1" to-layer="60" to-port="1" />
		<edge from-layer="60" from-port="2" to-layer="63" to-port="0" />
		<edge from-layer="61" from-port="0" to-layer="62" to-port="0" />
		<edge from-layer="62" from-port="1" to-layer="63" to-port="1" />
		<edge from-layer="63" from-port="2" to-layer="64" to-port="1" />
		<edge from-layer="64" from-port="2" to-layer="65" to-port="0" />
		<edge from-layer="65" from-port="1" to-layer="68" to-port="0" />
		<edge from-layer="65" from-port="1" to-layer="86" to-port="0" />
		<edge from-layer="66" from-port="0" to-layer="67" to-port="0" />
		<edge from-layer="67" from-port="1" to-layer="68" to-port="1" />
		<edge from-layer="68" from-port="2" to-layer="71" to-port="0" />
		<edge from-layer="69" from-port="0" to-layer="70" to-port="0" />
		<edge from-layer="70" from-port="1" to-layer="71" to-port="1" />
		<edge from-layer="71" from-port="2" to-layer="72" to-port="0" />
		<edge from-layer="72" from-port="1" to-layer="75" to-port="0" />
		<edge from-layer="73" from-port="0" to-layer="74" to-port="0" />
		<edge from-layer="74" from-port="1" to-layer="75" to-port="1" />
		<edge from-layer="75" from-port="2" to-layer="78" to-port="0" />
		<edge from-layer="76" from-port="0" to-layer="77" to-port="0" />
		<edge from-layer="77" from-port="1" to-layer="78" to-port="1" />
		<edge from-layer="78" from-port="2" to-layer="79" to-port="0" />
		<edge from-layer="79" from-port="1" to-layer="82" to-port="0" />
		<edge from-layer="80" from-port="0" to-layer="81" to-port="0" />
		<edge from-layer="81" from-port="1" to-layer="82" to-port="1" />
		<edge from-layer="82" from-port="2" to-layer="85" to-port="0" />
		<edge from-layer="83" from-port="0" to-layer="84" to-port="0" />
		<edge from-layer="84" from-port="1" to-layer="85" to-port="1" />
		<edge from-layer="85" from-port="2" to-layer="86" to-port="1" />
		<edge from-layer="86" from-port="2" to-layer="87" to-port="0" />
		<edge from-layer="87" from-port="1" to-layer="90" to-port="0" />
		<edge from-layer="87" from-port="1" to-layer="96" to-port="0" />
		<edge from-layer="88" from-port="0" to-layer="89" to-port="0" />
		<edge from-layer="89" from-port="1" to-layer="90" to-port="1" />
		<edge from-layer="90" from-port="2" to-layer="93" to-port="0" />
		<edge from-layer="91" from-port="0" to-layer="92" to-port="0" />
		<edge from-layer="92" from-port="1" to-layer="93" to-port="1" />
		<edge from-layer="93" from-port="2" to-layer="114" to-port="0" />
		<edge from-layer="94" from-port="0" to-layer="95" to-port="0" />
		<edge from-layer="95" from-port="1" to-layer="96" to-port="1" />
		<edge from-layer="96" from-port="2" to-layer="99" to-port="0" />
		<edge from-layer="97" from-port="0" to-layer="98" to-port="0" />
		<edge from-layer="98" from-port="1" to-layer="99" to-port="1" />
		<edge from-layer="99" from-port="2" to-layer="100" to-port="0" />
		<edge from-layer="100" from-port="1" to-layer="103" to-port="0" />
		<edge from-layer="101" from-port="0" to-layer="102" to-port="0" />
		<edge from-layer="102" from-port="1" to-layer="103" to-port="1" />
		<edge from-layer="103" from-port="2" to-layer="106" to-port="0" />
		<edge from-layer="104" from-port="0" to-layer="105" to-port="0" />
		<edge from-layer="105" from-port="1" to-layer="106" to-port="1" />
		<edge from-layer="106" from-port="2" to-layer="107" to-port="0" />
		<edge from-layer="107" from-port="1" to-layer="110" to-port="0" />
		<edge from-layer="108" from-port="0" to-layer="109" to-port="0" />
		<edge from-layer="109" from-port="1" to-layer="110" to-port="1" />
		<edge from-layer="110" from-port="2" to-layer="113" to-port="0" />
		<edge from-layer="111" from-port="0" to-layer="112" to-port="0" />
		<edge from-layer="112" from-port="1" to-layer="113" to-port="1" />
		<edge from-layer="113" from-port="2" to-layer="114" to-port="1" />
		<edge from-layer="114" from-port="2" to-layer="115" to-port="0" />
		<edge from-layer="115" from-port="1" to-layer="136" to-port="0" />
		<edge from-layer="115" from-port="1" to-layer="118" to-port="0" />
		<edge from-layer="116" from-port="0" to-layer="117" to-port="0" />
		<edge from-layer="117" from-port="1" to-layer="118" to-port="1" />
		<edge from-layer="118" from-port="2" to-layer="121" to-port="0" />
		<edge from-layer="119" from-port="0" to-layer="120" to-port="0" />
		<edge from-layer="120" from-port="1" to-layer="121" to-port="1" />
		<edge from-layer="121" from-port="2" to-layer="122" to-port="0" />
		<edge from-layer="122" from-port="1" to-layer="125" to-port="0" />
		<edge from-layer="123" from-port="0" to-layer="124" to-port="0" />
		<edge from-layer="124" from-port="1" to-layer="125" to-port="1" />
		<edge from-layer="125" from-port="2" to-layer="128" to-port="0" />
		<edge from-layer="126" from-port="0" to-layer="127" to-port="0" />
		<edge from-layer="127" from-port="1" to-layer="128" to-port="1" />
		<edge from-layer="128" from-port="2" to-layer="129" to-port="0" />
		<edge from-layer="129" from-port="1" to-layer="132" to-port="0" />
		<edge from-layer="130" from-port="0" to-layer="131" to-port="0" />
		<edge from-layer="131" from-port="1" to-layer="132" to-port="1" />
		<edge from-layer="132" from-port="2" to-layer="135" to-port="0" />
		<edge from-layer="133" from-port="0" to-layer="134" to-port="0" />
		<edge from-layer="134" from-port="1" to-layer="135" to-port="1" />
		<edge from-layer="135" from-port="2" to-layer="136" to-port="1" />
		<edge from-layer="136" from-port="2" to-layer="137" to-port="0" />
		<edge from-layer="137" from-port="1" to-layer="158" to-port="0" />
		<edge from-layer="137" from-port="1" to-layer="140" to-port="0" />
		<edge from-layer="138" from-port="0" to-layer="139" to-port="0" />
		<edge from-layer="139" from-port="1" to-layer="140" to-port="1" />
		<edge from-layer="140" from-port="2" to-layer="143" to-port="0" />
		<edge from-layer="141" from-port="0" to-layer="142" to-port="0" />
		<edge from-layer="142" from-port="1" to-layer="143" to-port="1" />
		<edge from-layer="143" from-port="2" to-layer="144" to-port="0" />
		<edge from-layer="144" from-port="1" to-layer="147" to-port="0" />
		<edge from-layer="145" from-port="0" to-layer="146" to-port="0" />
		<edge from-layer="146" from-port="1" to-layer="147" to-port="1" />
		<edge from-layer="147" from-port="2" to-layer="150" to-port="0" />
		<edge from-layer="148" from-port="0" to-layer="149" to-port="0" />
		<edge from-layer="149" from-port="1" to-layer="150" to-port="1" />
		<edge from-layer="150" from-port="2" to-layer="151" to-port="0" />
		<edge from-layer="151" from-port="1" to-layer="154" to-port="0" />
		<edge from-layer="152" from-port="0" to-layer="153" to-port="0" />
		<edge from-layer="153" from-port="1" to-layer="154" to-port="1" />
		<edge from-layer="154" from-port="2" to-layer="157" to-port="0" />
		<edge from-layer="155" from-port="0" to-layer="156" to-port="0" />
		<edge from-layer="156" from-port="1" to-layer="157" to-port="1" />
		<edge from-layer="157" from-port="2" to-layer="158" to-port="1" />
		<edge from-layer="158" from-port="2" to-layer="159" to-port="0" />
		<edge from-layer="159" from-port="1" to-layer="162" to-port="0" />
		<edge from-layer="159" from-port="1" to-layer="180" to-port="0" />
		<edge from-layer="160" from-port="0" to-layer="161" to-port="0" />
		<edge from-layer="161" from-port="1" to-layer="162" to-port="1" />
		<edge from-layer="162" from-port="2" to-layer="165" to-port="0" />
		<edge from-layer="163" from-port="0" to-layer="164" to-port="0" />
		<edge from-layer="164" from-port="1" to-layer="165" to-port="1" />
		<edge from-layer="165" from-port="2" to-layer="166" to-port="0" />
		<edge from-layer="166" from-port="1" to-layer="169" to-port="0" />
		<edge from-layer="167" from-port="0" to-layer="168" to-port="0" />
		<edge from-layer="168" from-port="1" to-layer="169" to-port="1" />
		<edge from-layer="169" from-port="2" to-layer="172" to-port="0" />
		<edge from-layer="170" from-port="0" to-layer="171" to-port="0" />
		<edge from-layer="171" from-port="1" to-layer="172" to-port="1" />
		<edge from-layer="172" from-port="2" to-layer="173" to-port="0" />
		<edge from-layer="173" from-port="1" to-layer="176" to-port="0" />
		<edge from-layer="174" from-port="0" to-layer="175" to-port="0" />
		<edge from-layer="175" from-port="1" to-layer="176" to-port="1" />
		<edge from-layer="176" from-port="2" to-layer="179" to-port="0" />
		<edge from-layer="177" from-port="0" to-layer="178" to-port="0" />
		<edge from-layer="178" from-port="1" to-layer="179" to-port="1" />
		<edge from-layer="179" from-port="2" to-layer="180" to-port="1" />
		<edge from-layer="180" from-port="2" to-layer="181" to-port="0" />
		<edge from-layer="181" from-port="1" to-layer="190" to-port="0" />
		<edge from-layer="181" from-port="1" to-layer="184" to-port="0" />
		<edge from-layer="182" from-port="0" to-layer="183" to-port="0" />
		<edge from-layer="183" from-port="1" to-layer="184" to-port="1" />
		<edge from-layer="184" from-port="2" to-layer="187" to-port="0" />
		<edge from-layer="185" from-port="0" to-layer="186" to-port="0" />
		<edge from-layer="186" from-port="1" to-layer="187" to-port="1" />
		<edge from-layer="187" from-port="2" to-layer="208" to-port="0" />
		<edge from-layer="188" from-port="0" to-layer="189" to-port="0" />
		<edge from-layer="189" from-port="1" to-layer="190" to-port="1" />
		<edge from-layer="190" from-port="2" to-layer="193" to-port="0" />
		<edge from-layer="191" from-port="0" to-layer="192" to-port="0" />
		<edge from-layer="192" from-port="1" to-layer="193" to-port="1" />
		<edge from-layer="193" from-port="2" to-layer="194" to-port="0" />
		<edge from-layer="194" from-port="1" to-layer="197" to-port="0" />
		<edge from-layer="195" from-port="0" to-layer="196" to-port="0" />
		<edge from-layer="196" from-port="1" to-layer="197" to-port="1" />
		<edge from-layer="197" from-port="2" to-layer="200" to-port="0" />
		<edge from-layer="198" from-port="0" to-layer="199" to-port="0" />
		<edge from-layer="199" from-port="1" to-layer="200" to-port="1" />
		<edge from-layer="200" from-port="2" to-layer="201" to-port="0" />
		<edge from-layer="201" from-port="1" to-layer="204" to-port="0" />
		<edge from-layer="202" from-port="0" to-layer="203" to-port="0" />
		<edge from-layer="203" from-port="1" to-layer="204" to-port="1" />
		<edge from-layer="204" from-port="2" to-layer="207" to-port="0" />
		<edge from-layer="205" from-port="0" to-layer="206" to-port="0" />
		<edge from-layer="206" from-port="1" to-layer="207" to-port="1" />
		<edge from-layer="207" from-port="2" to-layer="208" to-port="1" />
		<edge from-layer="208" from-port="2" to-layer="209" to-port="0" />
		<edge from-layer="209" from-port="1" to-layer="212" to-port="0" />
		<edge from-layer="209" from-port="1" to-layer="230" to-port="0" />
		<edge from-layer="210" from-port="0" to-layer="211" to-port="0" />
		<edge from-layer="211" from-port="1" to-layer="212" to-port="1" />
		<edge from-layer="212" from-port="2" to-layer="215" to-port="0" />
		<edge from-layer="213" from-port="0" to-layer="214" to-port="0" />
		<edge from-layer="214" from-port="1" to-layer="215" to-port="1" />
		<edge from-layer="215" from-port="2" to-layer="216" to-port="0" />
		<edge from-layer="216" from-port="1" to-layer="219" to-port="0" />
		<edge from-layer="217" from-port="0" to-layer="218" to-port="0" />
		<edge from-layer="218" from-port="1" to-layer="219" to-port="1" />
		<edge from-layer="219" from-port="2" to-layer="222" to-port="0" />
		<edge from-layer="220" from-port="0" to-layer="221" to-port="0" />
		<edge from-layer="221" from-port="1" to-layer="222" to-port="1" />
		<edge from-layer="222" from-port="2" to-layer="223" to-port="0" />
		<edge from-layer="223" from-port="1" to-layer="226" to-port="0" />
		<edge from-layer="224" from-port="0" to-layer="225" to-port="0" />
		<edge from-layer="225" from-port="1" to-layer="226" to-port="1" />
		<edge from-layer="226" from-port="2" to-layer="229" to-port="0" />
		<edge from-layer="227" from-port="0" to-layer="228" to-port="0" />
		<edge from-layer="228" from-port="1" to-layer="229" to-port="1" />
		<edge from-layer="229" from-port="2" to-layer="230" to-port="1" />
		<edge from-layer="230" from-port="2" to-layer="231" to-port="0" />
		<edge from-layer="231" from-port="1" to-layer="234" to-port="0" />
		<edge from-layer="231" from-port="1" to-layer="252" to-port="0" />
		<edge from-layer="232" from-port="0" to-layer="233" to-port="0" />
		<edge from-layer="233" from-port="1" to-layer="234" to-port="1" />
		<edge from-layer="234" from-port="2" to-layer="237" to-port="0" />
		<edge from-layer="235" from-port="0" to-layer="236" to-port="0" />
		<edge from-layer="236" from-port="1" to-layer="237" to-port="1" />
		<edge from-layer="237" from-port="2" to-layer="238" to-port="0" />
		<edge from-layer="238" from-port="1" to-layer="241" to-port="0" />
		<edge from-layer="239" from-port="0" to-layer="240" to-port="0" />
		<edge from-layer="240" from-port="1" to-layer="241" to-port="1" />
		<edge from-layer="241" from-port="2" to-layer="244" to-port="0" />
		<edge from-layer="242" from-port="0" to-layer="243" to-port="0" />
		<edge from-layer="243" from-port="1" to-layer="244" to-port="1" />
		<edge from-layer="244" from-port="2" to-layer="245" to-port="0" />
		<edge from-layer="245" from-port="1" to-layer="248" to-port="0" />
		<edge from-layer="246" from-port="0" to-layer="247" to-port="0" />
		<edge from-layer="247" from-port="1" to-layer="248" to-port="1" />
		<edge from-layer="248" from-port="2" to-layer="251" to-port="0" />
		<edge from-layer="249" from-port="0" to-layer="250" to-port="0" />
		<edge from-layer="250" from-port="1" to-layer="251" to-port="1" />
		<edge from-layer="251" from-port="2" to-layer="252" to-port="1" />
		<edge from-layer="252" from-port="2" to-layer="253" to-port="0" />
		<edge from-layer="253" from-port="1" to-layer="256" to-port="0" />
		<edge from-layer="253" from-port="1" to-layer="274" to-port="0" />
		<edge from-layer="254" from-port="0" to-layer="255" to-port="0" />
		<edge from-layer="255" from-port="1" to-layer="256" to-port="1" />
		<edge from-layer="256" from-port="2" to-layer="259" to-port="0" />
		<edge from-layer="257" from-port="0" to-layer="258" to-port="0" />
		<edge from-layer="258" from-port="1" to-layer="259" to-port="1" />
		<edge from-layer="259" from-port="2" to-layer="260" to-port="0" />
		<edge from-layer="260" from-port="1" to-layer="263" to-port="0" />
		<edge from-layer="261" from-port="0" to-layer="262" to-port="0" />
		<edge from-layer="262" from-port="1" to-layer="263" to-port="1" />
		<edge from-layer="263" from-port="2" to-layer="266" to-port="0" />
		<edge from-layer="264" from-port="0" to-layer="265" to-port="0" />
		<edge from-layer="265" from-port="1" to-layer="266" to-port="1" />
		<edge from-layer="266" from-port="2" to-layer="267" to-port="0" />
		<edge from-layer="267" from-port="1" to-layer="270" to-port="0" />
		<edge from-layer="268" from-port="0" to-layer="269" to-port="0" />
		<edge from-layer="269" from-port="1" to-layer="270" to-port="1" />
		<edge from-layer="270" from-port="2" to-layer="273" to-port="0" />
		<edge from-layer="271" from-port="0" to-layer="272" to-port="0" />
		<edge from-layer="272" from-port="1" to-layer="273" to-port="1" />
		<edge from-layer="273" from-port="2" to-layer="274" to-port="1" />
		<edge from-layer="274" from-port="2" to-layer="275" to-port="0" />
		<edge from-layer="275" from-port="1" to-layer="278" to-port="0" />
		<edge from-layer="275" from-port="1" to-layer="296" to-port="0" />
		<edge from-layer="276" from-port="0" to-layer="277" to-port="0" />
		<edge from-layer="277" from-port="1" to-layer="278" to-port="1" />
		<edge from-layer="278" from-port="2" to-layer="281" to-port="0" />
		<edge from-layer="279" from-port="0" to-layer="280" to-port="0" />
		<edge from-layer="280" from-port="1" to-layer="281" to-port="1" />
		<edge from-layer="281" from-port="2" to-layer="282" to-port="0" />
		<edge from-layer="282" from-port="1" to-layer="285" to-port="0" />
		<edge from-layer="283" from-port="0" to-layer="284" to-port="0" />
		<edge from-layer="284" from-port="1" to-layer="285" to-port="1" />
		<edge from-layer="285" from-port="2" to-layer="288" to-port="0" />
		<edge from-layer="286" from-port="0" to-layer="287" to-port="0" />
		<edge from-layer="287" from-port="1" to-layer="288" to-port="1" />
		<edge from-layer="288" from-port="2" to-layer="289" to-port="0" />
		<edge from-layer="289" from-port="1" to-layer="292" to-port="0" />
		<edge from-layer="290" from-port="0" to-layer="291" to-port="0" />
		<edge from-layer="291" from-port="1" to-layer="292" to-port="1" />
		<edge from-layer="292" from-port="2" to-layer="295" to-port="0" />
		<edge from-layer="293" from-port="0" to-layer="294" to-port="0" />
		<edge from-layer="294" from-port="1" to-layer="295" to-port="1" />
		<edge from-layer="295" from-port="2" to-layer="296" to-port="1" />
		<edge from-layer="296" from-port="2" to-layer="297" to-port="0" />
		<edge from-layer="297" from-port="1" to-layer="300" to-port="0" />
		<edge from-layer="297" from-port="1" to-layer="318" to-port="0" />
		<edge from-layer="298" from-port="0" to-layer="299" to-port="0" />
		<edge from-layer="299" from-port="1" to-layer="300" to-port="1" />
		<edge from-layer="300" from-port="2" to-layer="303" to-port="0" />
		<edge from-layer="301" from-port="0" to-layer="302" to-port="0" />
		<edge from-layer="302" from-port="1" to-layer="303" to-port="1" />
		<edge from-layer="303" from-port="2" to-layer="304" to-port="0" />
		<edge from-layer="304" from-port="1" to-layer="307" to-port="0" />
		<edge from-layer="305" from-port="0" to-layer="306" to-port="0" />
		<edge from-layer="306" from-port="1" to-layer="307" to-port="1" />
		<edge from-layer="307" from-port="2" to-layer="310" to-port="0" />
		<edge from-layer="308" from-port="0" to-layer="309" to-port="0" />
		<edge from-layer="309" from-port="1" to-layer="310" to-port="1" />
		<edge from-layer="310" from-port="2" to-layer="311" to-port="0" />
		<edge from-layer="311" from-port="1" to-layer="314" to-port="0" />
		<edge from-layer="312" from-port="0" to-layer="313" to-port="0" />
		<edge from-layer="313" from-port="1" to-layer="314" to-port="1" />
		<edge from-layer="314" from-port="2" to-layer="317" to-port="0" />
		<edge from-layer="315" from-port="0" to-layer="316" to-port="0" />
		<edge from-layer="316" from-port="1" to-layer="317" to-port="1" />
		<edge from-layer="317" from-port="2" to-layer="318" to-port="1" />
		<edge from-layer="318" from-port="2" to-layer="319" to-port="0" />
		<edge from-layer="319" from-port="1" to-layer="322" to-port="0" />
		<edge from-layer="319" from-port="1" to-layer="328" to-port="0" />
		<edge from-layer="320" from-port="0" to-layer="321" to-port="0" />
		<edge from-layer="321" from-port="1" to-layer="322" to-port="1" />
		<edge from-layer="322" from-port="2" to-layer="325" to-port="0" />
		<edge from-layer="323" from-port="0" to-layer="324" to-port="0" />
		<edge from-layer="324" from-port="1" to-layer="325" to-port="1" />
		<edge from-layer="325" from-port="2" to-layer="346" to-port="0" />
		<edge from-layer="326" from-port="0" to-layer="327" to-port="0" />
		<edge from-layer="327" from-port="1" to-layer="328" to-port="1" />
		<edge from-layer="328" from-port="2" to-layer="331" to-port="0" />
		<edge from-layer="329" from-port="0" to-layer="330" to-port="0" />
		<edge from-layer="330" from-port="1" to-layer="331" to-port="1" />
		<edge from-layer="331" from-port="2" to-layer="332" to-port="0" />
		<edge from-layer="332" from-port="1" to-layer="335" to-port="0" />
		<edge from-layer="333" from-port="0" to-layer="334" to-port="0" />
		<edge from-layer="334" from-port="1" to-layer="335" to-port="1" />
		<edge from-layer="335" from-port="2" to-layer="338" to-port="0" />
		<edge from-layer="336" from-port="0" to-layer="337" to-port="0" />
		<edge from-layer="337" from-port="1" to-layer="338" to-port="1" />
		<edge from-layer="338" from-port="2" to-layer="339" to-port="0" />
		<edge from-layer="339" from-port="1" to-layer="342" to-port="0" />
		<edge from-layer="340" from-port="0" to-layer="341" to-port="0" />
		<edge from-layer="341" from-port="1" to-layer="342" to-port="1" />
		<edge from-layer="342" from-port="2" to-layer="345" to-port="0" />
		<edge from-layer="343" from-port="0" to-layer="344" to-port="0" />
		<edge from-layer="344" from-port="1" to-layer="345" to-port="1" />
		<edge from-layer="345" from-port="2" to-layer="346" to-port="1" />
		<edge from-layer="346" from-port="2" to-layer="347" to-port="0" />
		<edge from-layer="347" from-port="1" to-layer="368" to-port="0" />
		<edge from-layer="347" from-port="1" to-layer="350" to-port="0" />
		<edge from-layer="348" from-port="0" to-layer="349" to-port="0" />
		<edge from-layer="349" from-port="1" to-layer="350" to-port="1" />
		<edge from-layer="350" from-port="2" to-layer="353" to-port="0" />
		<edge from-layer="351" from-port="0" to-layer="352" to-port="0" />
		<edge from-layer="352" from-port="1" to-layer="353" to-port="1" />
		<edge from-layer="353" from-port="2" to-layer="354" to-port="0" />
		<edge from-layer="354" from-port="1" to-layer="357" to-port="0" />
		<edge from-layer="355" from-port="0" to-layer="356" to-port="0" />
		<edge from-layer="356" from-port="1" to-layer="357" to-port="1" />
		<edge from-layer="357" from-port="2" to-layer="360" to-port="0" />
		<edge from-layer="358" from-port="0" to-layer="359" to-port="0" />
		<edge from-layer="359" from-port="1" to-layer="360" to-port="1" />
		<edge from-layer="360" from-port="2" to-layer="361" to-port="0" />
		<edge from-layer="361" from-port="1" to-layer="364" to-port="0" />
		<edge from-layer="362" from-port="0" to-layer="363" to-port="0" />
		<edge from-layer="363" from-port="1" to-layer="364" to-port="1" />
		<edge from-layer="364" from-port="2" to-layer="367" to-port="0" />
		<edge from-layer="365" from-port="0" to-layer="366" to-port="0" />
		<edge from-layer="366" from-port="1" to-layer="367" to-port="1" />
		<edge from-layer="367" from-port="2" to-layer="368" to-port="1" />
		<edge from-layer="368" from-port="2" to-layer="369" to-port="0" />
		<edge from-layer="369" from-port="1" to-layer="390" to-port="0" />
		<edge from-layer="369" from-port="1" to-layer="372" to-port="0" />
		<edge from-layer="370" from-port="0" to-layer="371" to-port="0" />
		<edge from-layer="371" from-port="1" to-layer="372" to-port="1" />
		<edge from-layer="372" from-port="2" to-layer="375" to-port="0" />
		<edge from-layer="373" from-port="0" to-layer="374" to-port="0" />
		<edge from-layer="374" from-port="1" to-layer="375" to-port="1" />
		<edge from-layer="375" from-port="2" to-layer="376" to-port="0" />
		<edge from-layer="376" from-port="1" to-layer="379" to-port="0" />
		<edge from-layer="377" from-port="0" to-layer="378" to-port="0" />
		<edge from-layer="378" from-port="1" to-layer="379" to-port="1" />
		<edge from-layer="379" from-port="2" to-layer="382" to-port="0" />
		<edge from-layer="380" from-port="0" to-layer="381" to-port="0" />
		<edge from-layer="381" from-port="1" to-layer="382" to-port="1" />
		<edge from-layer="382" from-port="2" to-layer="383" to-port="0" />
		<edge from-layer="383" from-port="1" to-layer="386" to-port="0" />
		<edge from-layer="384" from-port="0" to-layer="385" to-port="0" />
		<edge from-layer="385" from-port="1" to-layer="386" to-port="1" />
		<edge from-layer="386" from-port="2" to-layer="389" to-port="0" />
		<edge from-layer="387" from-port="0" to-layer="388" to-port="0" />
		<edge from-layer="388" from-port="1" to-layer="389" to-port="1" />
		<edge from-layer="389" from-port="2" to-layer="390" to-port="1" />
		<edge from-layer="390" from-port="2" to-layer="391" to-port="0" />
		<edge from-layer="391" from-port="1" to-layer="393" to-port="0" />
		<edge from-layer="392" from-port="0" to-layer="393" to-port="1" />
		<edge from-layer="393" from-port="2" to-layer="395" to-port="0" />
		<edge from-layer="394" from-port="0" to-layer="395" to-port="1" />
		<edge from-layer="395" from-port="2" to-layer="398" to-port="0" />
		<edge from-layer="396" from-port="0" to-layer="397" to-port="0" />
		<edge from-layer="397" from-port="1" to-layer="398" to-port="1" />
		<edge from-layer="398" from-port="2" to-layer="401" to-port="0" />
		<edge from-layer="399" from-port="0" to-layer="400" to-port="0" />
		<edge from-layer="400" from-port="1" to-layer="401" to-port="1" />
		<edge from-layer="401" from-port="2" to-layer="402" to-port="0" />
		<edge from-layer="402" from-port="1" to-layer="405" to-port="0" />
		<edge from-layer="403" from-port="0" to-layer="404" to-port="0" />
		<edge from-layer="404" from-port="1" to-layer="405" to-port="1" />
		<edge from-layer="405" from-port="2" to-layer="408" to-port="0" />
		<edge from-layer="406" from-port="0" to-layer="407" to-port="0" />
		<edge from-layer="407" from-port="1" to-layer="408" to-port="1" />
		<edge from-layer="408" from-port="2" to-layer="409" to-port="0" />
		<edge from-layer="409" from-port="1" to-layer="410" to-port="0" />
	</edges>
	<rt_info>
		<Runtime_version value="2023.3.0-13775-ceeafaf64f3-releases/2023/3" />
		<conversion_parameters>
			<framework value="tf" />
			<is_python_object value="True" />
		</conversion_parameters>
	</rt_info>
</net>
