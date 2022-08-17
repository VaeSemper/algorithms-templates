"""
Id:69676003

Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет
жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков.
Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого
участка. Если участок пустой, эта величина будет равна нулю — расстояние до
самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта
улицы. Дома в городе Тимофея нумеровались в том порядке, в котором
строились, поэтому их номера на карте никак не упорядочены. Пустые участки
обозначены нулями.
"""
from typing import List, Tuple


def nearest_zero(street_length: int, houses: Tuple[str]) -> List[int]:
    # zero_index - a tuple that lists the indices of zeros in the houses tuple
    zero_index = tuple(index for index, el in enumerate(houses) if el == '0')

    def intermediate_distances(index: int, index_value: int) -> List[int]:
        """
        :param index: current index of zero to zero_index tuple
        :param index_value: current value (real index) of zero to houses tuple
        :return: list of distances to the nearest zero in both directions.

        The function counts the distances to the nearest closest zero to the
        left and to the right of the location of the current object.
        """
        # calculate the distance between two zeros
        dist_bt_zero = index_value - zero_index[index + 1]
        # calculate the first (left) half of the distance
        dist_to_zero = list(range(abs(dist_bt_zero) // 2 + 1))
        # calculate the second (right) half of the distance
        if dist_bt_zero % 2 == 0:
            dist_to_zero += dist_to_zero[-2:0:-1]
        else:
            dist_to_zero += dist_to_zero[:0:-1]
        return dist_to_zero

    result_list = []
    # if there is only one zero in the houses, then in time O(n) we find
    # all distances
    if len(zero_index) == 1:
        dist_to_zero = list(map(
            lambda house_index, zero_index=zero_index[0]:
            abs(house_index[0] - zero_index), enumerate(houses)
        ))
        result_list += dist_to_zero
    # otherwise, we first find the left border, intermediate results and the
    # right border of the entire tuple
    else:
        for index, value in enumerate(zero_index):
            # find all distances to the left of the first zero and the
            # distances to the next one
            if index == 0:
                left_border = list(reversed(range(1, abs(0 - value) + 1)))
                result_list += left_border
                result_list += intermediate_distances(index, value)
            # find all distances to the right of the last zero
            elif index == len(zero_index) - 1:
                right_border = list(range(abs(street_length - value)))
                result_list += right_border
            # find all intermediate distances
            else:
                result_list += intermediate_distances(index, value)
    return result_list


def read_input() -> Tuple[int, Tuple[str]]:
    street_length = int(input())
    houses = tuple(input().strip().split())
    return street_length, houses


if __name__ == '__main__':
    street_length, houses = read_input()
    print(*nearest_zero(street_length, houses))
