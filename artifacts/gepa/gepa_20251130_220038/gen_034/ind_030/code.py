
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

# Drums continue
for i in range(2, 4):
    bar_start = i * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat = [
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.0, end=bar_start + 1.5),
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 1.5),
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.5),
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
    ]
    for n in hihat:
        drums.notes.append(n)
    drums.notes.append(kick)
    drums.notes.append(snare)

# Bass line: Marcus
# Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25),  
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625),   # Chromatic approach
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  

    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),   # Chromatic approach
    pretty_midi.Note(velocity=90, pitch=54, start=4.125, end=4.5),  

    pretty_midi.Note(velocity=90, pitch=54, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625),   # Chromatic approach
    pretty_midi.Note(velocity=90, pitch=56, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane
# 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=2.25),    # D7
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=2.25),

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.75),    # D7
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.75),
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.75),

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=5.25),    # D7
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=5.25),
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=5.25),
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=5.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante
# Motif: Whisper -> cry
# D, F#, A, D (melodic minor)
sax_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),   # Whisper
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # Build
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Cry
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),   # Return

    pretty_midi.Note(velocity=70, pitch=64, start=3.0, end=3.375),   # Whisper again
    pretty_midi.Note(velocity=85, pitch=67, start=3.375, end=3.75),  # Build
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # Cry
    pretty_midi.Note(velocity=70, pitch=64, start=4.125, end=4.5),   # Return

    pretty_midi.Note(velocity=60, pitch=62, start=4.5, end=4.875),   # Whisper
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # Build
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # Cry
    pretty_midi.Note(velocity=60, pitch=62, start=5.625, end=6.0),   # Return
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
