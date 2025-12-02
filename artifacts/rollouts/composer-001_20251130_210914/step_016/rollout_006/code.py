
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Dm7 = D F A C
# Walking bass line: D, F, Eb, G, A, Bb, B, C, D...

marcus_notes = [
    (1.5, 62, 100, 0.25),  # D
    (1.75, 64, 100, 0.25), # F
    (2.0, 63, 100, 0.25),  # Eb
    (2.25, 67, 100, 0.25), # G
    (2.5, 69, 100, 0.25),  # A
    (2.75, 67, 100, 0.25), # Bb
    (3.0, 71, 100, 0.25),  # B
    (3.25, 69, 100, 0.25), # C
    (3.5, 67, 100, 0.25),  # D
    (3.75, 69, 100, 0.25), # F
    (4.0, 68, 100, 0.25),  # Eb
    (4.25, 72, 100, 0.25), # G
    (4.5, 74, 100, 0.25),  # A
    (4.75, 72, 100, 0.25), # Bb
    (5.0, 76, 100, 0.25),  # B
    (5.25, 74, 100, 0.25), # C
    (5.5, 72, 100, 0.25),  # D
    (5.75, 74, 100, 0.25)  # F
]

for time, pitch, vel, dur in marcus_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + dur)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Rootless: F A C D
# Dm7 on 2 and 4

diane_notes = [
    (2.0, 64, 100, 0.25),  # F
    (2.0, 69, 100, 0.25),  # A
    (2.0, 72, 100, 0.25),  # C
    (2.0, 62, 100, 0.25),  # D
    (4.0, 64, 100, 0.25),  # F
    (4.0, 69, 100, 0.25),  # A
    (4.0, 72, 100, 0.25),  # C
    (4.0, 62, 100, 0.25)   # D
]

for time, pitch, vel, dur in diane_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + dur)
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth (bars 2-4)
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Dante: Tenor sax (bars 2-4)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Motif: D (62) -> Eb (63) -> F (64) -> D (62)
# Bar 2: D, Eb, F, D (starts on 2.0)
# Bar 3: Leave it hanging (rest)
# Bar 4: Come back and finish it

# Bar 2
sax_notes = [
    (2.0, 62, 100, 0.25),
    (2.25, 63, 100, 0.25),
    (2.5, 64, 100, 0.25),
    (2.75, 62, 100, 0.25)
]

# Bar 4
sax_notes.extend([
    (4.0, 62, 100, 0.25),
    (4.25, 63, 100, 0.25),
    (4.5, 64, 100, 0.25),
    (4.75, 62, 100, 0.25)
])

for time, pitch, vel, dur in sax_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + dur)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
