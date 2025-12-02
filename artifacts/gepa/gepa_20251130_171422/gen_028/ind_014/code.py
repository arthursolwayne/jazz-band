
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
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

# Add to drums
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # Dm7 - D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.4375), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.4375, end=2.625), # D
]

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=80, pitch=52, start=2.0625, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.4375), # Ab
    pretty_midi.Note(velocity=80, pitch=55, start=2.4375, end=2.625), # Bb
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0625), # D
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.0625), # Bb
    # 4th beat
    pretty_midi.Note(velocity=90, pitch=62, start=2.4375, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.4375, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=71, start=2.4375, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.4375, end=2.625), # Bb
]

# Add to instruments
for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.9375), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.9375, end=4.125), # D
]

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.1875), # Bb
    pretty_midi.Note(velocity=80, pitch=57, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.5625), # C#
    pretty_midi.Note(velocity=80, pitch=60, start=3.5625, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=3.9375), # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=3.9375, end=4.125), # F
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5625), # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.5625), # Bb
    # 4th beat
    pretty_midi.Note(velocity=90, pitch=62, start=3.9375, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.9375, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.9375, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.9375, end=4.125), # Bb
]

# Add to instruments
for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.4375), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.4375, end=5.625), # D
]

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.6875), # F
    pretty_midi.Note(velocity=80, pitch=65, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.0625, end=5.25), # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.4375), # C
    pretty_midi.Note(velocity=80, pitch=72, start=5.4375, end=5.625), # Db
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0625), # D
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.0625), # Bb
    # 4th beat
    pretty_midi.Note(velocity=90, pitch=62, start=5.4375, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=69, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=71, start=5.4375, end=5.625), # A
    pretty_midi.Note(velocity=90, pitch=72, start=5.4375, end=5.625), # Bb
]

# Add to instruments
for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# Add drum fills for bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]

# Add to drums
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
