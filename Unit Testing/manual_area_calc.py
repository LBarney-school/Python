import area_calc

# Perform 3 Tests for Circle Area Function
circle_known1 = 31.4
circle_calc1 = area_calc.area_circle(5)
if circle_known1 == circle_calc1:
    print("Test passed")
else:
    print("Test failed")
    print(f"Known area: {circle_known1}, calculated area: {circle_calc1}")

circle_known2 = 62.8
circle_calc2 = area_calc.area_circle(10)
if circle_known2 == circle_calc2:
    print("Test passed")
else:
    print("Test failed")
    print(f"Known area: {circle_known2}, calculated area: {circle_calc2}")

circle_known3 = 15.7
circle_calc3 = area_calc.area_circle(2.5)
if circle_known3 == circle_calc3:
    print("Test passed")
else:
    print("Test failed")
    print(f"Known area: {circle_known3}, calculated area: {circle_calc3}")

# Perform 3 Tests for Rectangle Area Function
rectangle_known1 = 10
rectangle_calc1 = area_calc.area_rectangle(2, 5)
if rectangle_known1 == rectangle_calc1:
    print("Test passed")
else:
    print("Test failed")
    print(f"Known area: {rectangle_known1}, calculated area: {rectangle_calc1}")

rectangle_known2 = 36
rectangle_calc2 = area_calc.area_rectangle(6, 6)
if rectangle_known2 == rectangle_calc2:
    print("Test passed")
else:
    print("Test failed")
    print(f"Known area: {rectangle_known2}, calculated area: {rectangle_calc2}")

rectangle_known3 = 15
rectangle_calc3 = area_calc.area_rectangle(5, 3)
if rectangle_known3 == rectangle_calc3:
    print("Test passed")
else:
    print("Test failed")
    print(f"Known area: {rectangle_known3}, calculated area: {rectangle_calc3}")

# Perform 3 Tests for Triange Area Function
triangle_known1 = 10
triangle_calc1 = area_calc.area_triangle(2, 10)
if triangle_known1 == triangle_calc1:
    print("Test passed")
else:
    print("Test failed")
    print(f"Known area: {triangle_known1}, calculated area: {triangle_calc1}")

triangle_known2 = 40
triangle_calc2 = area_calc.area_triangle(5, 16)
if triangle_known2 == triangle_calc2:
    print("Test passed")
else:
    print("Test failed")
    print(f"Known area: {triangle_known2}, calculated area: {triangle_calc2}")

triangle_known3 = 20
triangle_calc3 = area_calc.area_triangle(10, 4)
if triangle_known3 == triangle_calc3:
    print("Test passed")
else:
    print("Test failed")
    print(f"Known area: {triangle_known3}, calculated area: {triangle_calc3}")
