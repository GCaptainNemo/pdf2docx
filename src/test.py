from src.img2str2 import *


if __name__ == "__main__":
    NUM = 170
    with open("../result/p4/{}_4.pkl".format(NUM), "rb+") as f:
        res = pickle.load(f)
    row_content_lst, delta_y_lst, delta_x_lst = Dealer.deal_result(result=res)
    par_lst = Dealer.row_deltay2par(row_content_lst, delta_y_lst, delta_x_lst)
    IoOBJ.img2docx(par_lst, "../test.docx")
    Utils.show_detect_img(result=res, img_address="../linshi/p4/{}_4.png".format(NUM))


