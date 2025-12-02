
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    start = bar * 1.5
    # Kick
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hihat
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62, 100),  # C
    (1.875, 63, 100), # C#
    (2.25, 64, 100),  # D
    (2.625, 65, 100), # D#
    (3.0, 67, 100),   # E
    (3.375, 69, 100), # F#
    (3.75, 71, 100),  # G#
    (4.125, 72, 100), # A
    (4.5, 74, 100),   # Bb
    (4.875, 76, 100), # B
    (5.25, 77, 100),  # B#
    (5.625, 79, 100), # C
]

for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 60, 100),  # C
    (1.875, 64, 100),  # E
    (1.875, 67, 100),  # G
    (1.875, 71, 100),  # Bb
    (3.375, 60, 100),  # C
    (3.375, 64, 100),  # E
    (3.375, 67, 100),  # G
    (3.375, 71, 100),  # Bb
    (4.875, 60, 100),  # C
    (4.875, 64, 100),  # E
    (4.875, 67, 100),  # G
    (4.875, 71, 100),  # Bb
]

for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Drums - continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hihat
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Saxophone - your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66, 100),  # D
    (1.875, 69, 100),  # F#
    (2.25, 71, 100),  # G#
    (2.625, 72, 100),  # A
    (3.0, 69, 100),  # F#
    (3.375, 66, 100),  # D
    (3.75, 64, 100),  # E
    (4.125, 62, 100),  # C
    (4.5, 66, 100),  # D
    (4.875, 69, 100),  # F#
    (5.25, 71, 100),  # G#
    (5.625, 72, 100),  # A
]

for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
