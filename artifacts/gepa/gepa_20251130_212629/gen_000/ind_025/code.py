
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
for bar in [0]:
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, Dm7 -> G7 -> Cm7 -> F7
# Bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D (chromatic approach to Dm7)
# Then G -> Ab -> Bb -> B -> C -> D -> Eb -> F (chromatic approach to G7)
# Then C -> Db -> Eb -> F -> G -> Ab -> A -> Bb (chromatic approach to Cm7)
# Then F -> Gb -> G -> A -> Bb -> B -> C -> Db (chromatic approach to F7)

bass_notes = [
    (1.5, 50, 100), (1.75, 51, 100), (2.0, 52, 100), (2.25, 53, 100),
    (2.5, 55, 100), (2.75, 56, 100), (3.0, 57, 100), (3.25, 58, 100),
    (3.5, 59, 100), (3.75, 60, 100), (4.0, 61, 100), (4.25, 62, 100),
    (4.5, 64, 100), (4.75, 65, 100), (5.0, 66, 100), (5.25, 67, 100)
]

for start, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Diane on piano: 7th chords on 2 and 4, Dm7 on 2, G7 on 4, Cm7 on 2, F7 on 4
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb

piano_notes = [
    # Bar 2
    (2.0, 62, 100), (2.0, 65, 100), (2.0, 67, 100), (2.0, 69, 100),  # Dm7
    # Bar 3
    (3.5, 67, 100), (3.5, 71, 100), (3.5, 69, 100), (3.5, 65, 100),  # G7
    # Bar 4
    (5.0, 60, 100), (5.0, 63, 100), (5.0, 67, 100), (5.0, 71, 100),  # Cm7
    # Bar 4
    (6.5, 65, 100), (6.5, 68, 100), (6.5, 72, 100), (6.5, 67, 100)   # F7
]

for start, pitch, vel in piano_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.5)
    piano.notes.append(note)

# Dante on sax: your motif. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# D - Eb - F - G (Dm scale), but played with space and tension
# Bar 2: Start with D
# Bar 3: Leave it hanging
# Bar 4: Finish it with G

sax_notes = [
    (2.0, 62, 100), (2.25, 63, 100), (2.5, 64, 100), (2.75, 65, 100),  # D, Eb, F, G
    (3.0, 62, 100), (3.25, 63, 100), (3.5, 64, 100), (3.75, 65, 100),  # D, Eb, F, G (second pass)
    (4.0, 62, 100), (4.25, 63, 100), (4.5, 64, 100), (4.75, 65, 100)   # D, Eb, F, G (final)
]

for start, pitch, vel in sax_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Little Ray on drums: same pattern as bar 1, but for bars 2-4
for bar in [1, 2]:
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.05)
        drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
