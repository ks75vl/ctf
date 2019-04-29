import base64

data = 'iVBORw0KGgoAAAANSUhEUgAAAzcAAADiCAIAAAD8qK6MAA..AAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZ..cwAADsMAAA7DAcdvqGQAABkXSURBVHhe7d1bYtu6rgDQO6..4OqOPpaPZkMphz/ZQpiYRAm06YZK2vc3YhPkBQRtuk+b//..AQAwH10aAMCMdGkAADPSpQEAzEiXBgAwI10aAMCMdGkAAD..PSpQEAzEiXBgAwI10aAMCMdGkAADPSpQEAzEiXBgAwI10a..AMCMdGkAADPSpQEAzEiXBgAwI10aAMCMdGkAADPSpQEAzE..iXBgAwI10aAMCMdGkAADPSpQEAzEiXBgAwI10aAMCMdGkA..ADPSpQEAzEiXBgAwI10aAMCMdGkAADPSpQEAzEiXBgAwI1..0aAMCMdGkAADPSpQEAzEiXBgAwI10aAMCMdGkAADPSpQEA..zEiXBgAwI10aAMCMdGkAADPSpQEAzEiXBgAwI10aAMCMdG..kAADPSpQEAzEiXBgAwI10aAMCMdGkAADPSpQEAzEiXBgAw..I10aAMCMdGkAADPSpQEAzEiXBgAwI10aAMCMdGkAADPSpQ..EAzEiXBgAwI10aAMCMdGkAADPSpQEAzEiXBgAwI10aAMCM..dGkAADPSpQEAzEiXBgAwI10aAMCMdGkAADPSpQEAzEiXBg..AwI10aAMCMdGkAADPSpQEAzEiXBkkfH//9+/v3z58//1c6../f+///7993ELgqtTtfw7V8u6XE7O/+3v31PJqJlv7wvfCX..O+jrwkx9Ol8YWqN/riz7/4Rt+fLB/9+9/tF4c7z1ZZ5Mbp..TfSb3kP//b3tO/S+Q5nXR6Zark4fXm/+LH/6iu3Ot3ggPP..vfceRf+E6Y83X08qreVVSrcc+fGd+tYdSl8UX+C6908BHy..8a/x4Hs+HT7ihe4cffj9FLkm7fd1acm8lN6Vo6evWP2S6d..LuvvCdMOfraMiqPqVLK5z6xVvE5HRpfIVmp3XXerlEN/kd..l+6Jz9zPejN+rWxifv5H9spT9fKWinn6ijU/cosHwm3+9C..P/wnfCnK+jQat6V1FF436LWtWlDRBVwdtvyCy6knD4CdLI..W/w6GH/j4vkiPqlufnoiVo7rumn0i+LJKxb9oUjxQHj8P/..vIB74ToqFqpzPn62jYqt5VVPECv0G16tIG6L1sP1JXEo4v..djVvB4+Nvm8vfOb+9IM/PsC7b/ASHGamgum/Yod/a1U8EI..7+k4986BFHWdyXw5yvo4GreldRHVyF+ctVlzZA32X7oXqS..0LrZB1/uenDbRl+36P1z29Hpg+32H/Z+8skfnUThN3VpiT..vwX7uohhZMxxW7fNV35qO2WGBYAD/4yMe+ExL18jDn62jk..qt5VVOG4b8vMQLq0Abou20/Vk4TW1T64ibUp/v77eNM/aJ..B4/5wE2/65R3/w2lv5RV1aqmKCoJGpSl2xnnM8KQo6fPLn..Hvngd0KUxe3bY87X0dBVvb2oPup/XDx9vc7UpUWHtCRy/R..u/8zfV7v/4ZfObw3rQzump82Pb31Uu37nbHqHnsm01/3mZ..vm8X/vivNswT33b89D9305OE1EfITuWpxP16OjOpckxGjf..eVlyWae2edhPDRW+jlXRotqf3RsJqsHfaWD6xowvJM2kG3..ZTUiir21sliEtKZZZajrIFdpy5zjO+Tm3dd05fUdDbUb6f..YfUs8ko06iwG2NDp5649nX/tBVRWFLXBi0s7/plYvxptfB..ON+qS2u+4Io017vlk1O9tc6i+czGbojgjbuzuyOXz6LbLw..YOPjUvr5FbaOhgnOxI+78x6UrCv2xw5ebsJwqv16uZyb1a..ot2/8/Z/2WXpfU+u6z589hQaXMVi3c1RVhlvH83uLo4R1c..JjynYK7quvRzz21prnGhGtYuXP6Xelt/+ZkzmBszel9+x4..3nbdb5YVDXUNLWrx9uzxM2fRCXSe0cngqbeefe1fDV3V8e..EeBe1U9rwfoJ6YiXyfLu2gsK+ZPjjCR90seu7LRXmkT1y2..q2xfeLd9w9z0L74+Tu96VmXdlYTP6tJez0w4wiM4Cmsv73..VfclkuKm+56Hcb62GiOY+7hvtY7e2VszXnete5RFl/LCxI..wT2oHrIM0Rjhtq2Ds3/4gV3awWtsdfDBUOe49S9ftxSm9r..HrKOy6hPQZnQyeuvTKa/9i7KpSRRUG7eyXXBmgEjSXb9Kl..hZ8DN5mXzuY8ei5LYSm/nucfNdtZaHfFAFfPDdN51Voew3..Ql4XO6tBGZCbfV/QIa7vMvy81+4j9/o3f9umyfO5nFfUnN..rJdrbs61u0mDRLXwmLOdgmXx9YGONn+bIlrFyvp8PxpftF..MoHgjP8V35PYnmzdR9sbRgqP3tuD4XpvYxdBR2zWH6jE4G..T73oWcOiZ4zuVaWKKgza2az3bL+YStBcvsufpY1SHshTZX..p1K5meEZaafX6bj7I/e3qcdVE+nYX7MF1JGNulrROyGJKZ..cFuPiZNhw332Zbnbz/vnX/B9i8OK9ua+pOY4xXSZmKGiWl..jmDIIe+a4H3cZo7Os+Q1iRpdzxFooHwrh35fcknDfjsbZg..qH2/d30sedmPw9JndDJ46pueFaysqmbsqlJF1VcBlRrfL6..Z2Eaby27q0bOkcuQ7TM8RzVbZWltML45TDvJKFJ5LwGV3a..mMyE20pWUX19Q3zyZbnbT3tKWUcOXl72bbjmlI8TTIR8hS..ADRaqqi78uvLGvZVfhaZRqeQgfLh4Iz3Hmsn/soWuo65bC..7Dx2fRyWPqOTwVNf9SxgKztM96pSRdVXAZUaryym2NGUvk..2Xdv3qxYPiSgQtB9KOun2JUjjM6vSjhW/LJIq9LT8IeYwW..rO54mEdVHuTqMlA003WUs54kHMx6i9raz1ANHZSZaD9F2H..Nbed3B8g4O7iwRtFt/ZdZTTMcY4bJvZZLKfCsocUPeeCoH..zn+peFtExWpd1cBLRH2IMVcsTn4xRxT2zgSH897WF279sY..dwqK3rlpK7Tuc+meyzsVMfhJ1nDkIe44xdVXK0neC57bU4..qSwmGHsK3+e7B45jlqCoKJYDaY+UGWZ1+tGiNmWSGTM1bz..soscPHol7Lebm5jiSEO3ysf2s3w3bYq0/ITLHG57byumh5..xwd3cg+KNrBdf2XAc0hHDjJLCoe7H1AzaJmvOdV2V+8V7q..awXVVt+efNN8bbPt5xJivRARX3LXOO75CaN7eHcKit69DJ..Xadzn1voxdipo9HuUe2YZA6HrqoI2+iu9P00zbEn8V2+e+..BeF6kjiYKWA2nPlghZH2wU13HZuuZt7zExzLB0FlnoSEJu..2q39BNthr8ZkJtxPscantjJAsLxhp7tdf2XOy1wdOYiyuq..w7FdSa9HCUJeBzhMm5qX3rdfW5U1x9W7sBOs5kJZX7OCwa../lWp5eX2EG5h67ql5K7Tuc8t9GLo1KmoIGgZaGxCkqOtRW..PXr/p+mnrcPH5dl7aM1J4tVYNl0URx6wLIlWtm3vZIiR0O..S2exu3wSsmlYqzxTjxyTmXA/xczPbGWEYHnDTndzbpUprw..EdOUhVSSqoGXWbsLmoNx5KTZick+Y/TVd7sPWdGuuDOus4..k5Vc7sOwd2b4E+qn6rql5K7Tuc8t9GLo1KmoICiV6f6EJE..dbiYbepPCu9khj9En8pC6tKyiISZTp+ljzly03ZGq8dtA9..5Dgit54gqNhdPgkdmV3UntiOejckM+F+ijX2b2WMYHnLHq..K19QWd1Wa8brAjB1FWl9lSQc1ZbxEHv/xpwuTc/bl+LdBa..NeF/a7mp7KnjTFZyuQ/DvqjsH8vL7SHcwtZ1S8ldp3OfW+..jF0KlTUUFQKtP9CUmOVopG3mTwoTZPM3gGurS9Wz2EpbU6..1ai61qcfj5mR2mT9rV8RDtJzXXuSkJz25vKzS2rh20EXQz..KTfWX0bGWkT70sZ7UJMzdlnYNUlSRLqRV2nbG1qHJPnyFM..TmlfLFEeVip11nEmKy/m/iIY/lWp5eX2cJjdy88kWf1kqe..Su07nPLfRi6NSpqCAolen+hCRHK0RPVB+4qq/net63kKn8..2i4tkvmhGeU4Ua2s5wvLNeUx3uFYjZ98VArHCMq8Ip+E7L..TxBrsvYSGRmewrY2AGu3z2ZanNd//ljhykqiRZSq1pryGt..Qd54JlVhctZ2S4sSUShysug4k5Vk7sOVfU3Z99ZPnNxaTr..O7Tuc+t9CLoVM/Wxw7YxOSHO0heiDeRjhV9ey/ki6tlP7R..j+txoiNfzxeWa0o5Xmq0y48avj2wk7w+GfkkZKcNosJTPH..k9M/E9fqRmYAa7fPJlqU2XGmKTg1SVZEupMe81pDFI+fyn..+kj84/7begkTu6huqeNMVpK5j8K+qOwfy8vt4YktJB9J5z..630IuhUz9bHDtjE9J7IlH84S6CNVUv1FfSpZ1d3p9BIVWU..40TVsp4vLNeUzfrTA9Y7kvDxnuvak4TstI2o5N9ZvpiZ7C..tjYAa7fO5lqc32ONSOHKSqJF1KjcDzlK01vfFIUqK9rTd3..Fmb2rrqljjNZSeY+3MYbc5xaXm4PT2wh+Ug697mFXgyd+t..ni2BmbkL4TiQbdXaSq1u+ack9/ol/fpR3+/rahHCd/2cJy..Tdmu/+Qj/weA24YkeX0y8knITtuI+nP8t5V3L2Rm8AtouE..+9LNXJnspBqkrSpdSskOY/K/bOIwnzsMyb3txZFLyobqnj..TFaSywsX9sYcp5aX20Nyp6XkrtO571jC0KmfLY6dsQlJjn..YVjdk4vq2Pxo+2Sz7+eX51lxYWz+mDO/qIL8fJX7ZkuT4h..3W2e+pHbIycD15NPQnbaICr3x2lXz2Vm8AtouM+8LNW5ir..115CBVJflSakSe5mysaf34YFEeljR0JCuOfdg8ddEzTSmZ..+ygsGv5VA+snudNSctfp3HcsYejUzxbHztiEJEe7iIZsnN..5Ge7bc85/oF3dpYdSlDYiqpjzJbFy6XJ+V/Lq6XA4y16fY..XT4J2WnDqO2QB7ozE+6nSM2bT7QpWN6yiWhtHUHVqcr8d+..QgVSUdpVQPPQU1xnjjicR5yFX1enlhaGGTk4uOaVaSuY/C..3pnk1PJye0jutJTcdTr3HUsYOnVygc05U5nuT0hytLOOzF..WFK8oM8Kl+b5cWBN1jsqWQL5lkuSbWFkh0JPepkutpbrBY..Tc+9SU570fyXODZxGR2ZCfdTzN2zlZGC5S3ZjtaWDwp3mH..fNRapKOkqpsbi//zXGeOOJxJlaJg7TuV5eWIKlTVLOOqZZ..SeY+XNobk5xaXm4PyZ2WkrtO575jCUOnTi6wOWcq0/0JSY..52EkWuAhuqz1++m6x67l/t93Zp7dlSNbgEnWTj0uUahK3H..a4sbkvsor16fYjX5JKSnLdRGz6ZiI5eZAUeVe2E8KUh3ag..v5oHCHeddcpKqkp5Tqsa2vVtg+PVaUqaUU8gXTkfj9vvLT..rCVzH4V9Udn31k9yp6VkUtO571jC0KmTgzWXt6xtbEKidB..RhcWAZ11J5vnHic9Cl7S3nHBVDearZuBFV3bP+YJhbTHI9..zbmK3eWTkJ52pTJ+PvKmIzPZNUZh222PFKR7mTa1tsOgMB..F515SlquT1Ump1aY2KGSTKVKb01uurBtZ/9kBlY+lpNpK5..j8LemeWB9dNTZTfJpEZhq5E7ljB06uRgzeUtI41NSJSOsq..iiuCKsqfJ85rGv82u7tCBmObGoGoriSsed5AosWNwyXnuk..xzjtmNswUaYy4xTF3ZGE7LRr+wm2w94MyUx2jVFYY31DBO..lepk2t7TAoTETeNWWpKkkF3dWD/1T/YZ3dw2NFmVoqJkxn..Wfu1jf3596+Rm/LJs/Q0G8ncR2HR8K9KLS+3h+ROS8mkRm..GrkTuWMHTq5GDN5S0hYxMSpSM3Z+Pc1ioDPJY6JV3a3nJk..2UvUcdmi0FRVJxb3GKcdc19Wbj3NqEdIONImCeEBlWOu7W..eoh7ZX0pOZ5BoztfYOQbqXaVNrOwwKE5F3TVmqSlJBiyh6..Y//wUFGmlooJ01kUdHVbf/9rPl48epadZiuZ+zDpwfCvSi..0vt4fkTkvJpEZhq5E7ljB26mjix2DNqCXk81a1jJZObtN+..hNxzX0eXtrdUV/YSZeNOcjUWDJhYXGacrppvBj2ZhHDW4n..Jv7Geoh47JTLihx8S5qPGCeY/P7SQfFB5W3jUZUbqWJaWC..Fh3re+eBnAULX6ZOHUoj7PzrrTk2iQmzEuQhmfso7J1pTs..2b20NypyvRM49d56JOepYwdOpUETaDknXQvaoo7B6XvD6R../TTFGqbk69Iqrv8aV+ub+a/KiogCt5UTxf69xn60/lbj5D..FcsMn7OOEWL4PE67kmov3vja321pOE6IDaV2Y/Qz10UGai..RT4mDkba7nqozLype5AKinUcZ6pKUkEPUfhKcjvPCxKR2t..wjV/WRzr/enGO9u44zWUnmPsx5MPyrwnlv6wu3/thDcqcr..0dCPXQcjrwfuWcLYqcM8drz2h67qYFFHIdmy24+RffKr6N..KelK+uIvDspXnLcnploGL1zw9TpqAvCdEBta/M/qn1ChaD..MhO/gS5hz21khGCPyxZS9yAVFOvIQnQ0y2ypoIdw+tL7X8..bByhO/9Sv2Vg27/npzhNX2nq3MV9Z398Y8h/NmPNaW3Ola..lNb+d0Kcxc0aPnHq0Do3I1eVKKreZdcOcjdG87Rn8Xu7tL..B2jpUnmxvqXo/PT7yppkEX7dlh1re+Kwlh7Gbch/1Tm4Qs..BmXm+ZM6a+5jiM+9LLGO44xOZpktFVRIHndyNy95vvJW66..sPc3R5ylR3nMlKMvfhPt9Y+a/k9yy5hXaphHk9tMlMbrD7..Q0OnfjqT23EGripRVL2rrh3kboz2aU/i93ZpL5bX6mRTtf..MoyOdm3tfSszsYcGH3i+lJQrjw7eoW+6cqq7j6wszcNHcx..yCdfllDHcUYJXWZLBZVyx/TuI7l4vmKKndUTeg9oT1HssO..NMVpK5D7f5xkSHy6t+X+9asbTkTnfCrYf2eUmN9Xhs5NRP..jfbC7avZrCoc6BrbO1dlwfubEZ32FH5xlxa/yM6RjR/Ger..E+2UzxrEryYO6d9c+YfOgdZ7vwm75hGovJJyGcrrHT2lPV..vdwMykzva+GquYdhPvuyRDqOM0rnMlsqqJQ66+RmXpb9sb..Frq9XVE7BkspmfYpCOM1lJ5j4Ke2f1HyzvoBASSb5aBe6E..m2+qZiUzVPngwKlPUvdm0foMGraqcJhrdO9MlYPcbzo+7Q..n85i7tpBl5+UGe+XEyBb8ryvbXZ65d1hLIjnMa6F97pMRP..TzoLF5NNQhjXfBdUnmrGXg3JTHqQu0+59F9wWZo6jjN6yy..6zpYIK4fyLg1oZ6cWKqe//EdTebybmJEhFMvdR2Dszfby8..5sa3TUZvlZUGvhOOi3e97sGvoxGv/ZMhq0oUVRhSUZlmn/..Cj0/5yv7xLO/s4V1jxh+WPT+y+cU7x54o/u8WsNd5dl59T..eXnsFnd1/g9//wVd1dZ5nOv0txFu+gZqr+Zv1OIVMkkI30..yNPFWfSt2vAZnJvoRO46UP7DVfdFmqOo4z9dGYCup9YzfL..6j0u1+A2deTxtlk00llsoL3z1LFGuRiR+zemOre86zvo9p..9P9/yc402S0zttGvhOyLwzS8NfR6+/9k9eXlWiqMKQiv1B..Vi5G5rS/1ExdGoRqV/T8m7zP+hG5jXdZ58uMQbre2G/sHA..LtT79rxSiZTq+2VsN94TthztfRxC/J0wdF9YuYvubd0EGX..xrcR/vnAF72l+TIdXdr072FypuvSmN/Bi2L+utGl8X3E18..1b+ndJdmlHX1LDN6JLo9vBi2L+38Lp0vhGwj9N85b+XcJP..7PtfsCiJH0WXRrewS/sOVaNL41sJ+rQ579vBb+Se4NPoZQ..7l3WSYWQS1+D2KSpfGd/PR+O45XRpJDuXdZJhZNGox/R2w..X06Xxrf0sf/XNbzGAVhZdWmXr4Xo+SeuJqBLAwCYkS4NAG..BGujQAgBnp0gAAZqRLAwCYkS4NAGBGujQAgBnp0gAAZqRL..AwCYkS4NAGBGujQAgBnp0gAAZqRLAwCYkS4NAGBGujQAgB..np0gAAZqRLAwCYkS4NAGBGujQAgBnp0gAAZqRLAwCYkS4N..AGBGujQAgBnp0gAAZqRLAwCYkS4NAGBGujQAgBnp0gAAZq..RLAwCYkS4NAGBGujQAgBnp0gAAZqRLAwCYkS4NAGBGujQA..gBnp0gAAZqRLAwCYkS4NAGBGujQAgBnp0gAAZqRLAwCYkS..4NAGBGujQAgBnp0gAAZqRLAwCYkS4NAGBGujQAgBnp0gAA..ZqRLAwCYkS4NAGBGujQAgBnp0gAAZqRLAwCYkS4NAGBGuj..QAgBnp0gAAZqRLAwCYkS4NAGBGujQAgBnp0gAAZqRLAwCY..kS4NAGBGujQAgBnp0gAAZqRLAwCYkS4NAGBGujQAgBnp0g..AAZqRLAwCYkS4NAGBGujQAgBnp0gAAZqRLAwCYkS4NAGBG..ujQAgBnp0gAAZqRLAwCYkS4NAGBGujQAgBnp0gAAZqRLAw..CYkS4NAGBGujQAgBnp0gAAZqRLAwCYkS4NAGBGujQAgBnp..0gAAZqRLAwCYkS4NAGBGujQAgBnp0gAAZqRLAwCYkS4NAG..BGujQAgBnp0gAAZqRLAwCYkS4NAGBGujQAgBnp0gAAZqRL..AwCYkS4NAGBGujQAgBnp0gAA5vO///0/YNYX3hx7AaUAAA..AASUVORK5CYII='
data = data.replace('..', '')
data = base64.b64decode(data)

f = open('flag.png', 'wb')
f.write(data)
f.close()