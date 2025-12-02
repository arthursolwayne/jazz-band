
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - chromatic approach, walking line, searching
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=54, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=56, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4, emotional
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=58, start=1.5, end=1.875),

    # Bar 3
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=58, start=2.25, end=2.625),

    # Bar 4
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.375),
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - concise, memorable motif, emotionally resonant
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=68, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=105, pitch=70, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=95, pitch=68, start=2.625, end=3.0),    # D
    pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=105, pitch=70, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=95, pitch=68, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),   # Bb
    pretty_midi.Note(velocity=85, pitch=67, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=75, pitch=68, start=5.625, end=6.0),   # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 1.5)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('jazz_intro.mid')
