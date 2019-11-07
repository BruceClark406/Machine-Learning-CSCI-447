from Data_Processing_Lists import Data_Processing_Lists
from Data_Processing_Pd import Data_Processing_Pd
from MLP2 import MLP2
from Loss_Functions import Loss_Functions
import numpy as np
import copy


def run2():
    #in order to process the data, run the data processing file

    df_list = ["abalone", "car", "segmentation", "machine", "forestfires", "wine"]
    # df_list = ["machine", "forestfires", "wine"]
    df_class_num = [3, 4, 7, 1, 1, 1]
    # df_class_num = [1, 1, 1]

    #data = []
    #classes = []

    results_file = open("./results/results.txt", "a+")
    for i in range(len(df_list)):

        data_array = Data_Processing_Lists("./processed", df_list[i]+"_processed")
        data_array.file_array = data_array.file_array[:]
        class_list = []
        for j in range(df_class_num[i]):  #makes an array of integers the same lenght as the number of classes each data set has
            class_list.append(j)
        #data.append(data_array)
        #classes.append(class_list)

        data_array.slicer(5)
        
        # layer_num = 2
        

        for k in range(1):
            
            toy = copy.deepcopy(data_array)

            test_data = toy.file_array.pop(k)
            toy.join_array()
            training_data = toy.file_array
            x = int(len(training_data[0])*1.5)
            layer_nodes_2 = [x,x]
            layer_nodes_1 = [x]
            print(class_list)
            # print(d)
            mlp2 = MLP2(training_data, class_list, 2, layer_nodes_2, True)
            mlp2.train()

            #mlp = MLP(training_data, class_list, 1, [12], True)
            guesses = mlp2.classify(test_data)
            losses = Loss_Functions(guesses)

            if (len(class_list)==1):#regression
                print_str = "MSE for "+str(df_list[i])+" fold: "+str(k)+ " \nNetwork layer dimensions "+str(layer_nodes_2)
                print(print_str)
                print(losses.mse())

                results_file.write("\n"+print_str)
                results_file.write("\nMSE: "+str(losses.mse())+"\n")
                
                results_file.close()
                results_file = open("./results/results.txt", "a+")
            
            else:#classification
                losses.confusion_matrix_generator()
                print_str = "Fscore for "+str(df_list[i])+" fold: "+str(k)+ "\nNetwork layer dimensions "+str(layer_nodes_2)
                print(print_str)
                print(losses.f_score())

                results_file.write("\n"+print_str)
                results_file.write("\nF-score: "+str(losses.f_score())+"\n")

                results_file.close()
                results_file = open("./results/results.txt", "a+")

            mlp2 = MLP2(training_data, class_list, 1, layer_nodes_1, True)
            mlp2.train()
            #mlp = MLP(training_data, class_list, 1, [12], True)
            guesses = mlp2.classify(test_data)
            losses = Loss_Functions(guesses)

            if (len(class_list)==1):#regression
                print_str = "MSE for "+str(df_list[i])+" fold: "+str(k)+ " \nNetwork layer dimensions "+str(layer_nodes_1)
                print(print_str)
                print(losses.mse())

                results_file.write("\n"+print_str)
                results_file.write("\nMSE: "+str(losses.mse())+"\n")

                results_file.close()
                results_file = open("./results/results.txt", "a+")
            
            else:#classification
                losses.confusion_matrix_generator()
                print_str = "Fscore for "+str(df_list[i])+" fold: "+str(k)+ "\nNetwork layer dimensions "+str(layer_nodes_1)
                print(print_str)
                print(losses.f_score())

                results_file.write("\n"+print_str)
                results_file.write("\nF-score: "+str(losses.f_score())+"\n")

                results_file.close()
                results_file = open("./results/results.txt", "a+")


    results_file.close()
     
run2()
# if __name__ == "__main__":
#     main()
