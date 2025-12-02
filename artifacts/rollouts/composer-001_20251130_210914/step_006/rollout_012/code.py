
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=51, start=4.125, end=4.5),   # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=5.625, end=6.0),   # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),   # D7 (F#)
    # Bar 3 (2.25 - 3.0)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=3.0),   # D7 (F#)
    # Bar 4 (3.0 - 3.75)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75),   # D7 (F#)
    # Bar 4 (4.5 - 5.25)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25),   # D7 (F#)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),   # E (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),   # E (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),   # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),   # G (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),   # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),   # E (Dm7)
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),   # D (Dm7)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # C (Dm7)
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # D (Dm7)
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),   # E (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),   # G (Dm7)
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),   # A (Dm7)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2 (1.5 - 3.0), Bar 3 (3.0 - 4.5), Bar 4 (4.5 - 6.0)
for bar_start in [1.5, 3.0, 4.5]:
    drum_notes = [
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
        # Hi-hat on every eighth
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 2.625, end=bar_start + 3.0),
    ]
    for note in drum_notes:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
