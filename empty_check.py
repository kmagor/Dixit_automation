import cv2
import numpy as np
font = cv2.FONT_HERSHEY_COMPLEX
hanyadik_negyzet = 0
hanyadik_karika = 1
pos_Rec_X = [0] * 12
pos_Rec_Y = [0] * 12
pos_Cir_X = [0] * 6
pos_Cir_Y = [0] * 6
RECT_num_and_content = [[0]*13,[0]*13]
hanyadik = 0

img = cv2.imread("sablon_pottyok_sok.jpg", cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (166), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    #print(hanyadik)
    hanyadik = hanyadik +1
    if len(approx) == 3: ## TRIANGLE
        cv2.putText(img, "Triangle", (x, y), font, 1, (0))

    elif len(approx) == 4: ## RECTANGLE!!!
        hanyadik_negyzet = hanyadik_negyzet+1
        cv2.putText(img,str(hanyadik_negyzet-1) + ".Rect.", (x, y-15), font, 1, (0))
        print(hanyadik_negyzet-1, ". negyzet pozicioja:", x,y)
        cv2.line(img, (x, y-80), (x, y + 700), (55, 0, 0), 2)
        cv2.line(img, (x - 80, y), (x +80, y), (55, 0, 0), 2)
        if hanyadik_negyzet < 14:
            (RECT_num_and_content[0][hanyadik_negyzet-1])=hanyadik_negyzet-1
            (RECT_num_and_content[1][hanyadik_negyzet - 1]) = hanyadik-1
            pos_Rec_X[hanyadik_negyzet-2] = x
            pos_Rec_Y[hanyadik_negyzet - 2] = y
    # elif len(approx) == 5:
    #     cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
    # elif 6 < len(approx) < 15:
    #     cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
    else: ## CIRCLE
        cv2.putText(img, str(hanyadik_karika) + "circle", (x, y+30), font, 1, (0))
        if hanyadik_karika < 7:
            pos_Cir_X[hanyadik_karika-1] = x
            pos_Cir_Y[hanyadik_karika - 1] = y
            for x in range(18):
                if cv2.pointPolygonTest(contours[x], (pos_Cir_X[hanyadik_karika-1], pos_Cir_Y[hanyadik_karika-1]), False) == 1:
                    #print(hanyadik_karika, ". kör benne van az a " + str(x) + ". kontúrban")
                    for d in range(1,hanyadik_negyzet):
                        if RECT_num_and_content[1][d] == x:
                            print(hanyadik_karika, ". kör benne van az a " + str(RECT_num_and_content[0][d]) + ". négyzetben")

        print("KARIKA:",hanyadik_karika, ". karika pozicioja:", x, y)
        hanyadik_karika = hanyadik_karika + 1


print("Körpoziciok:")
print(pos_Cir_X)
print(pos_Cir_Y)
print("Négyzet_pozik:")
print(pos_Rec_X)
print(pos_Rec_Y)
print("--------------")

print(RECT_num_and_content)
cv2.imshow("shapes", img)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()