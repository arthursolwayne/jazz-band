
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Drums only (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=kick, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=snare, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=snare, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=hihat, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=hihat, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Bass, Piano, Sax enter
# Bass: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.1875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.1875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.1875),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.1875),  # C#
    # D7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875),  # C#
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Introduce the motif
# Start with a short phrase that ends on a rest
# D (62), F# (67), B (71) — ascending minor 3rd to major 7th
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # F#
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # B
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3 and 4: Continue with variation
# Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # C#
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),   # F#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Continue comping with 7th chords
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.6875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.6875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.6875),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.6875),  # C#
    # D7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.6875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.6875),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.6875),  # C#
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=kick, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=kick, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=snare, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=snare, start=4.875, end=5.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=hihat, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=hihat, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=hihat, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=hihat, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=hihat, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=hihat, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=hihat, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=hihat, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=hihat, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=hihat, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=hihat, start=4.875, end=5.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Sax: Return with variation of the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),   # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.0, end=4.25),   # E
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),   # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),   # F#
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),   # D
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
