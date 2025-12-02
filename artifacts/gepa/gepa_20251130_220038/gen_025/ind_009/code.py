
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Snare on 2 and 4
    note = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.375, end=start + 1.375 + 0.125)
    drums.notes.append(note)
    # Hihat on every eighth
    for i in range(8):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1, 55), (1, 57), (1, 59), (1, 60),  # bar 2
    (1, 62), (1, 60), (1, 58), (1, 57),  # bar 3
    (1, 55), (1, 57), (1, 59), (1, 60)   # bar 4
]
for i, (pitch, duration) in enumerate(bass_notes):
    start = 1.5 + (i // 4) * 1.5 + (i % 4) * 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2 and 4
    (1, 62, 0.75), (1, 67, 0.75), (1, 69, 0.75), (1, 64, 0.75),  # D7
    # Bar 3: G7 on 2 and 4
    (1, 67, 0.75), (1, 72, 0.75), (1, 74, 0.75), (1, 69, 0.75),  # G7
    # Bar 4: C7 on 2 and 4
    (1, 60, 0.75), (1, 65, 0.75), (1, 67, 0.75), (1, 62, 0.75)   # C7
]
for i, (velocity, pitch, duration) in enumerate(piano_notes):
    start = 1.5 + (i // 4) * 1.5 + (i % 4) * 0.375
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3):
    start = 1.5 + bar * 1.5
    # Kick on 1 and 3
    note = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.75 + 0.125)
    drums.notes.append(note)
    # Snare on 2 and 4
    note = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.375, end=start + 1.375 + 0.125)
    drums.notes.append(note)
    # Hihat on every eighth
    for i in range(8):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(note)

# Sax: motif, start it, leave it hanging, come back and finish it
# Dorian mode: D, E, F#, G, A, B, C
sax_notes = [
    # Bar 2: motif starts
    (1, 62, 0.375), (1, 67, 0.375), (1, 66, 0.375), (1, 69, 0.375),  # D E F# G
    # Bar 3: leave it hanging
    (1, 69, 0.375), (1, 62, 0.375), (1, 67, 0.375), (1, 66, 0.375),  # G D E F#
    # Bar 4: come back and finish it
    (1, 69, 0.375), (1, 71, 0.375), (1, 72, 0.375), (1, 69, 0.375)   # G A B G
]
for i, (velocity, pitch, duration) in enumerate(sax_notes):
    start = 1.5 + (i // 4) * 1.5 + (i % 4) * 0.375
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
