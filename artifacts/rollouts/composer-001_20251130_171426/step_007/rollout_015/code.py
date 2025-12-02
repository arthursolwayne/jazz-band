
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

kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125, 3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125, 4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    if t < 1.5:
        note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
        drums.notes.append(note)

for t in snare_times:
    if t < 1.5:
        note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125)
        drums.notes.append(note)

for t in hihat_times:
    if t < 1.5:
        note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.0625)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking in Dm, chromatic approaches
bass_notes = [
    (1.5, 48),   # D
    (1.75, 49),  # Eb
    (2.0, 47),   # C
    (2.25, 50),  # F
    (2.5, 52),   # G
    (2.75, 51),  # Gb
    (3.0, 50),   # F
    (3.25, 48),  # D
    (3.5, 49),   # Eb
    (3.75, 47),  # C
    (4.0, 50),   # F
    (4.25, 52),  # G
    (4.5, 51),   # Gb
    (4.75, 50),  # F
    (5.0, 48),   # D
    (5.25, 49),  # Eb
    (5.5, 47),   # C
    (5.75, 50),  # F
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62),  # D7
    (1.5, 67),
    (1.5, 71),
    (1.5, 74),
    (2.0, 62),  # D7
    (2.0, 67),
    (2.0, 71),
    (2.0, 74),
    (2.5, 62),  # D7
    (2.5, 67),
    (2.5, 71),
    (2.5, 74),
    (3.0, 62),  # D7
    (3.0, 67),
    (3.0, 71),
    (3.0, 74),
    (3.5, 62),  # D7
    (3.5, 67),
    (3.5, 71),
    (3.5, 74),
    (4.0, 62),  # D7
    (4.0, 67),
    (4.0, 71),
    (4.0, 74),
    (4.5, 62),  # D7
    (4.5, 67),
    (4.5, 71),
    (4.5, 74),
    (5.0, 62),  # D7
    (5.0, 67),
    (5.0, 71),
    (5.0, 74),
    (5.5, 62),  # D7
    (5.5, 67),
    (5.5, 71),
    (5.5, 74),
]

for t, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0)
sax.notes.append(note)

# Bar 3: Leave it hanging
note = pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75)
sax.notes.append(note)

# Bar 4: Come back and finish it
note = pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
