
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in Dm
# Dm7 = D F A C
# Chromatic approach to each note
bass_notes = [
    (4, 0.125, 1.5),     # D
    (5, 0.125, 1.625),   # F (approach from E)
    (9, 0.125, 1.75),    # A
    (12, 0.125, 1.875),  # C
    (4, 0.125, 2.0),     # D
    (5, 0.125, 2.125),   # F
    (9, 0.125, 2.25),    # A
    (12, 0.125, 2.375),  # C
    (4, 0.125, 2.5),     # D
    (5, 0.125, 2.625),   # F
    (9, 0.125, 2.75),    # A
    (12, 0.125, 2.875),  # C
    (4, 0.125, 3.0),     # D
    (5, 0.125, 3.125),   # F
    (9, 0.125, 3.25),    # A
    (12, 0.125, 3.375),  # C
    (4, 0.125, 3.5),     # D
    (5, 0.125, 3.625),   # F
    (9, 0.125, 3.75),    # A
    (12, 0.125, 3.875),  # C
    (4, 0.125, 4.0),     # D
    (5, 0.125, 4.125),   # F
    (9, 0.125, 4.25),    # A
    (12, 0.125, 4.375),  # C
    (4, 0.125, 4.5),     # D
    (5, 0.125, 4.625),   # F
    (9, 0.125, 4.75),    # A
    (12, 0.125, 4.875),  # C
    (4, 0.125, 5.0),     # D
    (5, 0.125, 5.125),   # F
    (9, 0.125, 5.25),    # A
    (12, 0.125, 5.375),  # C
]

for pitch, duration, start_time in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time, end=start_time + duration)
    bass.notes.append(note)

# Diane - 7th chords, comp on 2 and 4
# Dm7: D F A C
# Dm7 = D (root), F (minor 3rd), A (5th), C (diminished 7th)
# Comp on 2 and 4
for bar in range(3):
    start_time = 1.5 + bar * 1.5
    # Bar 2: Dm7 on 2 and 4
    # 2: D, F, A, C
    for note in [4, 5, 9, 12]:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time + 0.75, end=start_time + 0.875))
    # 4: Dm7 again
    for note in [4, 5, 9, 12]:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time + 1.125, end=start_time + 1.25))

# Dante - Tenor sax. Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F - A - C (Dm7) with a space between the first and second note
# Start on 1.5s, first note D (4), then silence, then F (5), then A (9), then C (12)
# Delay the second note to create tension
sax_notes = [
    (4, 0.125, 1.5),     # D
    (5, 0.125, 1.75),    # F (delayed)
    (9, 0.125, 1.875),   # A
    (12, 0.125, 2.0),    # C
]

for pitch, duration, start_time in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start_time, end=start_time + duration)
    sax.notes.append(note)

# Add the rest of the sax motif later in the bar
# Motif repeats with small variations
sax_notes = [
    (4, 0.125, 2.5),     # D (repeat)
    (5, 0.125, 2.75),    # F
    (9, 0.125, 2.875),   # A
    (12, 0.125, 3.0),    # C
    (4, 0.125, 3.5),     # D
    (5, 0.125, 3.75),    # F
    (9, 0.125, 3.875),   # A
    (12, 0.125, 4.0),    # C
    (4, 0.125, 4.5),     # D
    (5, 0.125, 4.75),    # F
    (9, 0.125, 4.875),   # A
    (12, 0.125, 5.0),    # C
]

for pitch, duration, start_time in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start_time, end=start_time + duration)
    sax.notes.append(note)

# Add the full quartet
midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
