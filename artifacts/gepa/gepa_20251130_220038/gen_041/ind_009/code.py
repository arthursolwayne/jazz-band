
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

# Bass line: Fm walking line with chromatic approaches
bass_notes = [
    # Bar 2: F, Eb, D, C
    (1.5, 53, 100, 0.25), (1.75, 51, 100, 0.25), (2.0, 50, 100, 0.25), (2.25, 48, 100, 0.25),
    # Bar 3: Bb, A, G, F
    (2.5, 57, 100, 0.25), (2.75, 55, 100, 0.25), (3.0, 53, 100, 0.25), (3.25, 53, 100, 0.25),
    # Bar 4: F, Eb, D, C
    (3.5, 53, 100, 0.25), (3.75, 51, 100, 0.25), (4.0, 50, 100, 0.25), (4.25, 48, 100, 0.25)
]
for start, pitch, velocity, duration in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2, Cm7 on 4
    (2.0, 53, 100, 0.25), (2.0, 50, 100, 0.25), (2.0, 48, 100, 0.25), (2.0, 55, 100, 0.25),
    (2.5, 53, 100, 0.25), (2.5, 50, 100, 0.25), (2.5, 48, 100, 0.25), (2.5, 55, 100, 0.25),
    # Bar 3: F7 on 2, Cm7 on 4
    (3.0, 53, 100, 0.25), (3.0, 50, 100, 0.25), (3.0, 48, 100, 0.25), (3.0, 55, 100, 0.25),
    (3.5, 53, 100, 0.25), (3.5, 50, 100, 0.25), (3.5, 48, 100, 0.25), (3.5, 55, 100, 0.25),
    # Bar 4: F7 on 2, Cm7 on 4
    (4.0, 53, 100, 0.25), (4.0, 50, 100, 0.25), (4.0, 48, 100, 0.25), (4.0, 55, 100, 0.25),
    (4.5, 53, 100, 0.25), (4.5, 50, 100, 0.25), (4.5, 48, 100, 0.25), (4.5, 55, 100, 0.25)
]
for start, pitch, velocity, duration in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [1, 2, 3]:
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.05)
        drums.notes.append(note)

# Saxophone: short motif, make it sing
# Motif: F - Eb - D - C (start on bar 2, beat 1)
sax_notes = [
    (2.0, 53, 100, 0.25), # F
    (2.25, 51, 100, 0.25), # Eb
    (2.5, 50, 100, 0.25), # D
    (2.75, 48, 100, 0.25)  # C
]
for start, pitch, velocity, duration in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Repeat the motif on bar 4, beat 1
sax_notes = [
    (3.5, 53, 100, 0.25), # F
    (3.75, 51, 100, 0.25), # Eb
    (4.0, 50, 100, 0.25), # D
    (4.25, 48, 100, 0.25)  # C
]
for start, pitch, velocity, duration in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
