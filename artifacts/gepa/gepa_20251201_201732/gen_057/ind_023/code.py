
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Upright Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
drums = pretty_midi.Instrument(program=drums_program)

sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [bass, piano, drums, sax]

# Time variables
note_length = 0.375  # 1/8 note at 160 BPM
bar_length = 1.5  # 4/4 bar at 160 BPM

# ----------------------------- DRUMS -----------------------------
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Bar 2-4: Same pattern but with fills

# Bar 1 (0.0 to 1.5)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5))

# Bar 2 (1.5 to 3.0)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.625))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0))

# Bar 3 (3.0 to 4.5)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5))

# Bar 4 (4.5 to 6.0)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0))

# ----------------------------- BASS -----------------------------
# Bass line: Roots and fifths with chromatic approaches, over F7

# Bar 1 (0.0 to 1.5): F (C3) -> B (C3) -> E (D3) -> A (D3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=0.0, end=0.375))  # F (C3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=0.375, end=0.75)) # B (C3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=0.75, end=1.125)) # E (D3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=1.125, end=1.5))  # A (D3)

# Bar 2 (1.5 to 3.0): B (C3) -> E (D3) -> A (D3) -> D (D3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875))  # B (C3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25)) # E (D3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625)) # A (D3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0))  # D (D3)

# Bar 3 (3.0 to 4.5): C (C3) -> F (C3) -> B (C3) -> E (D3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375))  # C (C3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75)) # F (C3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.125)) # B (C3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5))  # E (D3)

# Bar 4 (4.5 to 6.0): A (D3) -> D (D3) -> G (D3) -> C (C3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875))  # A (D3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25)) # D (D3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=80, start=5.25, end=5.625)) # G (D3)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0))  # C (C3)

# ----------------------------- PIANO -----------------------------
# Open voicings, different chord each bar, resolve on the last
# Bar 1: F7 (F, A, C, E, Bb)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=0.0, end=1.5))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=0.0, end=1.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=0.0, end=1.5))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=0.0, end=1.5))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=0.0, end=1.5))  # Bb

# Bar 2: Gm7 (G, Bb, D, F)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=3.0))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=3.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=3.0))  # F

# Bar 3: Am7 (A, C, E, G)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=4.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=4.5))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=3.0, end=4.5))  # G

# Bar 4: C7 (C, E, G, Bb)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=6.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=6.0))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=4.5, end=6.0))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0))  # Bb

# ----------------------------- SAX (You) -----------------------------
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 1 (0.0 to 1.5): F (G4) -> A (A4) -> F (G4) -> rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=0.0, end=0.375)) # F (G4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=0.375, end=0.75)) # A (A4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=0.75, end=1.125)) # F (G4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=1.125, end=1.5))  # Rest

# Bar 2 (1.5 to 3.0): C (C5) -> B (B4) -> C (C5) -> rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=78, start=1.5, end=1.875)) # C (C5)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=79, start=1.875, end=2.25)) # B (B4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=78, start=2.25, end=2.625)) # C (C5)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=78, start=2.625, end=3.0))  # Rest

# Bar 3 (3.0 to 4.5): G (G4) -> E (E4) -> rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375)) # G (G4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75)) # E (E4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.5))  # Rest

# Bar 4 (4.5 to 6.0): F (G4) -> A (A4) -> C (C5) -> F (G4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875)) # F (G4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25)) # A (A4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=78, start=5.25, end=5.625)) # C (C5)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0))  # F (G4)

# Write the MIDI file
# midi.write disabled

print("MIDI file 'dante_intro.mid' has been created.")
