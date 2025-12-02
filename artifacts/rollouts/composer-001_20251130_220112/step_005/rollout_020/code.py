
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=100, pitch=54, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0),   # F#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),   # Db
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # Db
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),    # G (start motif)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),    # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),    # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),    # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),    # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),    # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),    # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),    # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),    # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),    # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),    # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),    # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),    # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),    # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),    # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),    # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),    # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),    # G
]

for note in sax_notes:
    sax.notes.append(note)

# Drums continue through bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + (i * 0.375), end=bar_start + 1.5)
        drums.notes.append(hihat)
    drums.notes.append(kick)
    drums.notes.append(snare)

# Add kicks and snares on 1 and 3
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    drums.notes.append(kick_3)

# Add snare on 4
for bar in range(2, 5):
    bar_start = bar * 1.5
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    drums.notes.append(snare_4)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.save('dante_intro.mid')
