import Graphics.rectangle
import Graphics.circle
import Graphics.graphics_3d.cuboid as cuboid
import Graphics.graphics_3d.sphere as sphere

print("Rectangle Area:", Graphics.rectangle.area(10, 5))
print("Rectangle Perimeter:", graphics.rectangle.perimeter(10, 5))

print("Circle Area:", Graphics.circle.area(7))
print("Circle Perimeter:", Graphics.circle.perimeter(7))

print("Cuboid Surface Area:", cuboid.surface_area(10, 5, 3))
print("Cuboid Perimeter:", cuboid.perimeter(10, 5, 3))

print("Sphere Surface Area:", sphere.surface_area(7))
print("Sphere Volume:", sphere.volume(7))
