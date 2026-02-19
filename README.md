# the_snake
Description
A classic Snake game implemented in Python using the pygame library. The player controls a snake to collect apples while avoiding self-collision.

Classes and Methods
GameObject: Base class for game entities.

__init__(): Initializes position and color.

draw(): Placeholder method for rendering.

Apple(GameObject): Represents the food object.

randomize_position(snake_position): Sets a random position not occupied by the snake.

draw(): Renders the apple on the surface.

Snake(GameObject): Represents the player-controlled snake.

get_head_position(): Returns the coordinates of the snake's head.

move(): Updates positions, including screen-wrap logic.

reset(): Restores the snake to its initial state upon collision.

update_direction(): Updates the current movement vector.

Testing and Standards
Tests: Quality assurance is handled via pytest.

PEP 8: The codebase strictly adheres to PEP 8 style guidelines.
_________________________________________________________________

Beschreibung
Ein klassisches „Snake“-Spiel, implementiert in Python unter Verwendung der pygame-Bibliothek. Der Spieler steuert eine Schlange, um Äpfel zu sammeln und Kollisionen mit dem eigenen Körper zu vermeiden.

Implementierte Klassen und Methoden
GameObject: Basisklasse für Spielobjekte.

__init__(): Initialisiert Position und Farbe.

draw(): Abstrakte Methode zum Zeichnen.

Apple(GameObject): Klasse für das Apfel-Objekt.

randomize_position(snake_position): Bestimmt eine zufällige Position außerhalb des Schlangenkörpers.

draw(): Zeichnet den Apfel auf dem Spielfeld.

Snake(GameObject): Klasse für die Schlange.

get_head_position(): Gibt die Koordinaten des Kopfes zurück.

move(): Aktualisiert die Position der Schlange (inkl. Spielfeldrand-Logik).

reset(): Setzt die Schlange nach einer Kollision zurück.

update_direction(): Aktualisiert die Bewegungsrichtung.

Tests und Standards
Tests: Die Überprüfung erfolgt mittels pytest.

PEP 8: Der Quellcode entspricht den PEP 8-Richtlinien für Python-Code.
