
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
drum_notes = []
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax - motif starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # E5
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0625), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.4375),  # E5
    pretty_midi.Note(velocity=100, pitch=60, start=2.4375, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.8125), # D5
    pretty_midi.Note(velocity=100, pitch=64, start=2.8125, end=3.0),   # E5
]

for note in sax_notes:
    sax.notes.append(note)

# Bass - walking line in D (D2-G2, MIDI 38-43)
bass_notes = []
bass_chords = [
    [38, 43],  # D2, A2
    [40, 43],  # F2, A2
    [43, 38],  # A2, D2
    [40, 43],  # F2, A2
]
for i, chord in enumerate(bass_chords):
    for pitch in chord:
        start = 1.5 + i * 0.375
        end = start + 0.375
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

for note in bass_notes:
    bass.notes.append(note)

# Piano - open voicings, resolve on the last bar
piano_notes = []
chords = [
    [62, 67, 72],  # D5, A5, D6
    [64, 67, 72],  # E5, A5, D6
    [62, 64, 67],  # D5, E5, A5
    [62, 67, 72],  # D5, A5, D6
]
for i, chord in enumerate(chords):
    for pitch in chord:
        start = 1.5 + (i % 2) * 0.75
        end = start + 0.75
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax - repeat motif but end with a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # E5
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5625), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.9375),  # E5
    pretty_midi.Note(velocity=100, pitch=60, start=3.9375, end=4.125), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.3125), # D5
    pretty_midi.Note(velocity=100, pitch=64, start=4.3125, end=4.5),   # E5
]

for note in sax_notes:
    sax.notes.append(note)

# Bass - walking line in D
bass_notes = []
for i, chord in enumerate(bass_chords):
    for pitch in chord:
        start = 3.0 + i * 0.375
        end = start + 0.375
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

for note in bass_notes:
    bass.notes.append(note)

# Piano - open voicings, resolve on the last bar
piano_notes = []
for i, chord in enumerate(chords):
    for pitch in chord:
        start = 3.0 + (i % 2) * 0.75
        end = start + 0.75
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax - complete the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # E5
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0625), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.4375),  # E5
    pretty_midi.Note(velocity=100, pitch=60, start=5.4375, end=5.625), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.8125), # D5
    pretty_midi.Note(velocity=100, pitch=64, start=5.8125, end=6.0),   # E5
]

for note in sax_notes:
    sax.notes.append(note)

# Bass - walking line in D
bass_notes = []
for i, chord in enumerate(bass_chords):
    for pitch in chord:
        start = 4.5 + i * 0.375
        end = start + 0.375
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

for note in bass_notes:
    bass.notes.append(note)

# Piano - open voicings, resolve on the last bar
piano_notes = []
for i, chord in enumerate(chords):
    for pitch in chord:
        start = 4.5 + (i % 2) * 0.75
        end = start + 0.75
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
