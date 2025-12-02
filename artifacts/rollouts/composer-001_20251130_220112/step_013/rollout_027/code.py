
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75), # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25), # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=6.0),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Your moment. One short motif, make it sing.
# D (62), F# (66), B (71), D (62) - with a slight delay on the B
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),   # B
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    kick_start = bar_start
    snare_start = bar_start + 0.375
    hihat_start = bar_start
    kick_end = kick_start + 0.375
    snare_end = snare_start + 0.375
    hihat_end = hihat_start + 1.5

    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    # Hihat on every eighth (8 notes per bar)
    for i in range(8):
        hihat_start = bar_start + (i * 0.375)
        hihat_end = hihat_start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
