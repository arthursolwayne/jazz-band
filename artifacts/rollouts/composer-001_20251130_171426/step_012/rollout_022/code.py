
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 70),  # F
    (1.875, 69),  # E
    (2.25, 71),  # F#
    (2.625, 72),  # G
    (3.0, 74),  # A
    (3.375, 73),  # Ab
    (3.75, 75),  # Bb
    (4.125, 76),  # B
    (4.5, 77),  # C
    (4.875, 76),  # B
    (5.25, 74),  # A
    (5.625, 73),  # Ab
    (6.0, 72),  # G
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# F7 on beat 2, Bb7 on beat 4
piano_notes = [
    (1.875, 65), (1.875, 69), (1.875, 72), (1.875, 76),  # F7
    (2.25, 65), (2.25, 69), (2.25, 72), (2.25, 76),
    (3.375, 60), (3.375, 64), (3.375, 67), (3.375, 71),  # Bb7
    (3.75, 60), (3.75, 64), (3.75, 67), (3.75, 71),
    (4.875, 65), (4.875, 69), (4.875, 72), (4.875, 76),  # F7
    (5.25, 65), (5.25, 69), (5.25, 72), (5.25, 76),
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing
# Start with F (65), then Ab (68), then Bb (71), then rest on beat 1
sax_notes = [
    (1.5, 65),  # F
    (1.875, 68),  # Ab
    (2.25, 71),  # Bb
    (2.625, 65),  # F
    (3.0, 69),  # A
    (3.375, 71),  # Bb
    (3.75, 65),  # F
    (4.125, 68),  # Ab
    (4.5, 71),  # Bb
    (4.875, 76),  # C
    (5.25, 69),  # A
    (5.625, 71),  # Bb
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Drums continue in bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
